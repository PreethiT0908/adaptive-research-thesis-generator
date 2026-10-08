from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from app.config.settings import EMBEDDING_MODEL, VECTOR_DIR

def build_vector_store(chunks: list):
    embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)
    vector_db = FAISS.from_texts(chunks, embeddings)
    vector_db.save_local(VECTOR_DIR)
    return vector_db
