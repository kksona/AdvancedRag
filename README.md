# 📚 PDF & Firestore RAG Chatbot

Hi everyone! 👋 This is a Retrieval Augmented Generation (RAG) project I built. Originally it was just for chatting with PDFs, but I've upgraded it to also fetch data directly from a **Firestore Database**! 🚀

It takes your documents (books or interview questions), converts them into vectors, and lets you ask questions about all of them using an LLM.

## 🚀 Features
- **PDF Loading**: Reads PDF files from the data folder.
- **🔥 Firestore Integration**: Connects to Google Firestore to fetch live data (like interview questions).
- **Smart Deduplication**: Prevents duplicate documents from cluttering the database using content hashing.
- **Chunking**: Splits large documents into smaller pieces.
- **Embeddings**: Uses `sentence-transformers` (HuggingFace) to convert text into numbers.
- **Vector DB**: Stores everything in ChromaDB for fast searching.

## 🛠️ Tech Stack
- Python 🐍
- LangChain
- **Firebase Admin SDK** (New!)
- ChromaDB
- Sentence Transformers
- Groq (for the LLM part)

## 💻 How to Run

1. **Clone the repo**
2. **Install requirements**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Setup Environment**:
   - Create a `.env` file and add your `GROQ_API_KEY`.
   - **Firestore Setup**: Download your `serviceAccountKey.json` from Firebase Console and place it in the root folder.
   
4. **Run the Notebook**:
   Open `notebook/document.ipynb` in Jupyter/VS Code. It will load both your PDFs and your Firestore data automatically!

## 📂 Project Structure
- `data/` -> Put your PDF files here
- `notebook/` -> Contains the main logic (`document.ipynb`)
- `firestore_loader.py` -> Custom script to fetch data from Firestore
- `serviceAccountKey.json` -> Your Firebase credentials (keep this secret! 🤫)

---
*Note: This is a learning project where I honestly learned a lot about Vector DBs and Data Pipelines!* 😊
