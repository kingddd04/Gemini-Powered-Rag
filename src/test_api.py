from langchain_qdrant import Qdrant
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from qdrant_client import QdrantClient
from dotenv import load_dotenv
import os

load_dotenv()  # loads .env from the current directory

print(os.getenv("GOOGLE_API_KEY"))


# --- Load env variables ---
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
QDRANT_COLLECTION = os.getenv("QDRANT_COLLECTION")

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
EMBED_MODEL = os.getenv("GEMINI_EMBEDDINGS_MODEL", "models/text-embedding-004")

# --- Initialize embeddings ---
embeddings = GoogleGenerativeAIEmbeddings(
    model=EMBED_MODEL,
    google_api_key=GOOGLE_API_KEY
)

# --- Initialize Qdrant client ---
client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY
)

# --- Wrap Qdrant with LangChain ---
vectorstore = Qdrant(
    client=client,
    collection_name=QDRANT_COLLECTION,
    embeddings=embeddings
)

# --- Test document ---
docs = ["Davide is building a powerful RAG system using Qdrant and Gemini."]

# --- Upload to Qdrant ---
ids = vectorstore.add_texts(docs)

print("Uploaded vector IDs:", ids)
print("Success! Your vector is now in Qdrant.")
