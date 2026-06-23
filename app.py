import streamlit as st
from dotenv import load_dotenv
import tempfile
import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_mistralai import MistralAIEmbeddings
from langchain_chroma import Chroma
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()

st.set_page_config(
    page_title="ReadMeAI",
    page_icon="📚",
    layout="wide"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
    }
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    h1 {
        color: white;
        text-align: center;
        font-size: 3rem;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    h3 {
        color: white !important;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
    }
    .subtitle {
        color: white;
        text-align: center;
        font-size: 1.2rem;
        margin-bottom: 2rem;
        opacity: 0.9;
    }
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.5rem 2rem;
        border-radius: 10px;
        font-weight: bold;
        transition: transform 0.2s;
    }
    .stButton>button:hover {
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>📚 ReadMeAI</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Your AI-Powered Reading Companion - Upload PDFs and Get Instant Answers</p>", unsafe_allow_html=True)


# Upload Section
uploaded_file = st.file_uploader("📄 Upload a PDF book", type="pdf")


if uploaded_file:

    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        file_path = tmp_file.name

    st.success("✅ PDF uploaded successfully!")

    if st.button("🚀 Create Vector Database"):

        with st.spinner("🔄 Processing document..."):

            loader = PyPDFLoader(file_path)
            docs = loader.load()

            splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200
            )

            chunks = splitter.split_documents(docs)

            embeddings = MistralAIEmbeddings(model="mistral-embed")

            vectorstore = Chroma.from_documents(
                documents=chunks,
                embedding=embeddings,
                persist_directory="chroma_db"
            )

        st.success(f"✨ Vector database created! Processed {len(docs)} pages into {len(chunks)} chunks.")

# Question Section
if os.path.exists("chroma_db"):
    
    embeddings = MistralAIEmbeddings(model="mistral-embed")

    vectorstore = Chroma(
        persist_directory="chroma_db",
        embedding_function=embeddings
    )

    retriever = vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k":4,
            "fetch_k":10,
            "lambda_mult":0.5
        }
    )

    llm = ChatMistralAI(model="mistral-small-2506")

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """You are a helpful AI assistant.

Use ONLY the provided context to answer the question.

If the answer is not present in the context,
say: "I could not find the answer in the document."
"""
            ),
            (
                "human",
                """Context:
{context}

Question:
{question}
"""
            )
        ]
    )

    st.markdown("### 💬 Ask Questions From Your Book")
    st.markdown("<br>", unsafe_allow_html=True)

    query = st.text_input("🔍 Enter your question:", placeholder="What is this document about?", label_visibility="collapsed")

    if query:

        with st.spinner("🤔 Thinking..."):
            docs = retriever.invoke(query)

            context = "\n\n".join(
                [doc.page_content for doc in docs]
            )

            final_prompt = prompt.invoke({
                "context": context,
                "question": query
            })

            response = llm.invoke(final_prompt)

        st.markdown("---")
        st.markdown("### 🤖 AI Answer")
        st.markdown(f"<div style='background: rgba(255, 255, 255, 0.15); padding: 1.5rem; border-radius: 10px; border-left: 4px solid #fff; color: white; font-size: 1.1rem; backdrop-filter: blur(10px);'>{response.content}</div>", unsafe_allow_html=True)
else:
    st.info("📌 Please upload a PDF and create the vector database first to start asking questions.")