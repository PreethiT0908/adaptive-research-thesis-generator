import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

BASE_DIR = "app/storage"
DOC_DIR = f"{BASE_DIR}/documents"
VECTOR_DIR = f"{BASE_DIR}/vectors"
OUTPUT_DIR = f"{BASE_DIR}/outputs"

EMBEDDING_MODEL = "text-embedding-3-large"
LLM_MODEL = "gpt-4"
