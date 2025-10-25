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
```


3️⃣ Install dependencies
🧩 Option 1 — Using pip
```
pip install -r requirements.txt
```

⚡ Option 2 — Using uv (faster)

If you have uv
 installed:
 
```
uv pip install -r requirements.txt
```

4️⃣ Set up your environment variables

Create a .env file in your project root directory and add your OpenAI API key:

OPENAI_API_KEY=your_openai_api_key_here

5️⃣ Run the chatbot
Using uv (recommended)

```
uv run chainlit run app.py
```

Or using Python directly

```
chainlit run app.py
```

Once the server starts, open the provided local URL in your browser — your YouTube Q&A Chatbot will be live! 🎉

🧠 How It Works

The app extracts the video ID from any YouTube link.

It fetches the transcript using youtube-transcript-api.

LangChain splits the transcript into smaller chunks for embedding.

The chunks are stored locally in a FAISS vectorstore.

When a question is asked, the app retrieves relevant chunks and uses OpenAI GPT to generate an answer.

📜 License

This project is licensed under the MIT License — feel free to use, modify, and distribute it with attribution.

💡 Author

Abdur Raafay
