from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
import re
from dotenv import load_dotenv

load_dotenv()


def extract_video_id(url: str) -> str | None:
    """Extract YouTube video ID from URL."""
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11})"
    match = re.search(pattern, url)
    return match.group(1) if match else None


def get_transcript(video_id: str) -> str | None:
    """Fetch transcript using YouTubeTranscriptApi."""
    try:
        fetched = YouTubeTranscriptApi().fetch(video_id, languages=["en"])
        return " ".join(snippet.text for snippet in fetched)
    except TranscriptsDisabled:
        return None
    except NoTranscriptFound:
        return None


def build_vectorstore(transcript: str):
    """Split transcript and build FAISS vectorstore."""
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.create_documents([transcript])
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vectorstore = FAISS.from_documents(chunks, embeddings)
    return vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 4})


def create_chain(retriever):
    """Create RAG chain using LangChain."""
    llm = ChatOpenAI(model="gpt-5-nano")

    prompt = PromptTemplate(
        template="""
        You are a helpful assistant.
        Answer ONLY from the provided transcript context.
        If the context is insufficient, just say you don't know.

        {context}
        Question: {question}
        """,
        input_variables=['context', 'question']
    )

    def format_docs(retrieved_docs):
        return "\n\n".join(doc.page_content for doc in retrieved_docs)

    parallel_chain = RunnableParallel({
        'context': retriever | RunnableLambda(format_docs),
        'question': RunnablePassthrough()
    })

    parser = StrOutputParser()

    main_chain = parallel_chain | prompt | llm | parser
    return main_chain
