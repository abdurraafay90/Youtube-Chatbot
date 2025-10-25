# 🎥 YouTube Q&A Chatbot

A conversational **YouTube video assistant** built using **LangChain**, **OpenAI**, and **Chainlit**.  
Simply paste a YouTube link, and the chatbot will fetch the transcript and let you **ask questions** about the video content — just like ChatGPT for YouTube!

---

## 🚀 Features

- 🔗 Accepts any YouTube video link or video ID  
- 🧠 Fetches and processes the transcript using `youtube-transcript-api`  
- 🧩 Splits transcript into chunks using `LangChain Text Splitters`  
- 🧮 Embeds and stores chunks in a local FAISS vectorstore  
- 💬 Creates a Retrieval-Augmented Generation (RAG) chain using `ChatOpenAI`  
- 🤖 Lets users ask natural language questions about the video content  
- 🌐 Built on top of **Chainlit** for an interactive chat interface  

---

## 🧰 Tech Stack

| Component | Library |
|------------|----------|
| Framework | [Chainlit](https://docs.chainlit.io/) |
| LLM | [OpenAI GPT (via LangChain)](https://python.langchain.com/docs/integrations/llms/openai) |
| Embeddings | `text-embedding-3-small` |
| Vector Store | [FAISS](https://github.com/facebookresearch/faiss) |
| Transcript Fetching | [youtube-transcript-api](https://pypi.org/project/youtube-transcript-api/) |
| Environment | `.env` for API keys |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/youtube-chatbot.git
cd youtube-chatbot
