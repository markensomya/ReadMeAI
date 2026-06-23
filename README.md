# 📚 ReadMeAI

**Your AI-Powered Reading Companion** - Upload PDFs and get instant, intelligent answers from your documents.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)
![LangChain](https://img.shields.io/badge/LangChain-Latest-green.svg)

## ✨ Features

- 📄 **PDF Upload** - Upload any PDF document
- 🧠 **AI-Powered Q&A** - Ask questions and get accurate answers from your documents
- 🎨 **Beautiful UI** - Modern gradient design with smooth interactions
- ⚡ **Fast Retrieval** - Uses ChromaDB for efficient vector search
- 🔍 **Smart Search** - MMR (Maximal Marginal Relevance) for diverse results
- 🤖 **Mistral AI** - Powered by Mistral's advanced language models

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- Mistral API key

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/ReadMeAI.git
cd ReadMeAI
```

2. **Create virtual environment (optional but recommended):**
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables:**
Create a `.env` file in the root directory:
```env
MISTRAL_API_KEY=your_mistral_api_key_here
```

### Running the Application

#### Web Interface (Streamlit)
```bash
streamlit run app.py
```
Then open http://localhost:8501 in your browser.

#### Command Line Interface
```bash
python main.py
```

## 📁 Project Structure

```
ReadMeAI/
├── app.py                  # Streamlit web application
├── main.py                 # CLI version
├── create_database.py      # Database creation script
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not in repo)
├── .gitignore             # Git ignore rules
├── document_loaders/      # PDF documents folder
│   └── GRU.pdf           # Sample document
└── chroma_db/            # Vector database (auto-generated)
```

## 🛠️ How It Works

1. **Document Loading**: PDFs are loaded using PyPDFLoader
2. **Text Splitting**: Documents are split into chunks (1000 chars, 200 overlap)
3. **Embeddings**: Mistral-embed model creates vector embeddings
4. **Vector Store**: ChromaDB stores and indexes the embeddings
5. **Retrieval**: MMR retrieves the most relevant diverse chunks
6. **Answer Generation**: Mistral-small generates answers based on context

## 🔧 Technologies Used

- **LangChain** - Framework for LLM applications
- **ChromaDB** - Vector database for embeddings
- **Mistral AI** - LLM and embedding models
- **Streamlit** - Web interface
- **PyPDF** - PDF processing

## 📝 Usage

### Web Interface
1. Open the app in your browser
2. Upload a PDF document
3. Click "Create Vector Database"
4. Ask questions in the text input
5. Get AI-powered answers instantly

### CLI
1. Run `python create_database.py` to create the database from your PDF
2. Run `python main.py` to start the interactive CLI
3. Type your questions and press Enter
4. Type `0` to exit

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Mistral AI for their powerful language models
- LangChain for the RAG framework
- Streamlit for the amazing web framework

---

Made with ❤️ by [Your Name]
