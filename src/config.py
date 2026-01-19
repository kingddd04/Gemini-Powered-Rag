import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

class Config:
    """
    This class is tasked with handling all api keys of the project and some additional settings for chunking and generation
    """


    # Gemini llm Config
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    CHAT_MODEL = os.getenv("GEMINI_MODEL")
    TEMPERATURE = 0.9

    # embedding config
    EMBEDDING_MODEL = "models/text-embedding-004"
    EMBEDDING_DIMENSIONS = 768 

    # Knowledge config
    RESOURCES_PATH = Path(__file__).resolve().parents[1] / "rag_knowledge_pdfs"

    # chunking config
    CHUNK_SIZE = 1000
    CHUNK_OVERLAP = 200

    # qdrant config
    QDRANT_URL = os.getenv("QDRANT_URL")
    QDRANT_API_KEY= os.getenv("QDRANT_API_KEY")
    COLLECTION_NAME = os.getenv("QDRANT_COLLECTION")
