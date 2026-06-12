from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def load_pdf(pdf_path):
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()
    return docs


def split_documents(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(docs)

    return chunks


def create_vector_store(chunks):
    db = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model
    )

    return db


def load_rag(pdf_path):
    docs = load_pdf(pdf_path)

    chunks = split_documents(docs)

    db = create_vector_store(chunks)

    return db

