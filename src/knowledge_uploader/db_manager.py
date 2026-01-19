from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams


class DBManager:
    """Manager class for handling Qdrant vector database operations.

    This class abstracts the logic for:
    - Connecting to Qdrant (Cloud or local mode)
    - Creating a collection if it does not exist
    - Indexing documents (chunks)
    - Exposing a LangChain retriever for similarity search
    """

    def __init__(self, config, embedder_manager):
        """Initialize the Qdrant client, collection, and vector store.
        If QDRANT_URL and QDRANT_API_KEY are provided, the system connects
        to Qdrant Cloud. Else it fails.
        """
        self.embeddings = embedder_manager.get_embeddings()

        # --- CONNECTION LOGIC (Cloud vs Local) ---
        if config.QDRANT_URL and config.QDRANT_API_KEY:
            print(f"☁️  Connecting to Qdrant Cloud... ({config.QDRANT_URL[:20]}...)")
            self.client = QdrantClient(
                url=config.QDRANT_URL,
                api_key=config.QDRANT_API_KEY
            )
        else:
            raise RuntimeError("💾 No Cloud credentials found.")

            

        # --- COLLECTION CREATION ---
        if not self.client.collection_exists(config.COLLECTION_NAME):
            print(f"🆕 Creating new collection: {config.COLLECTION_NAME}")
            self.client.create_collection(
                collection_name=config.COLLECTION_NAME,
                vectors_config=VectorParams(
                    size=config.EMBEDDING_DIMENSIONS,
                    distance=Distance.COSINE
                )
            )

        # --- LANGCHAIN VECTOR STORE WRAPPER ---
        self.vector_store = QdrantVectorStore(
            client=self.client,
            collection_name=config.COLLECTION_NAME,
            embedding=self.embeddings
        )

    def index_documents(self, chunks):
        """
        Insert document chunks into the Qdrant collection.
        """
        if chunks:
            print(f"⬆️  Uploading {len(chunks)} chunks to Qdrant...")
            self.vector_store.add_documents(chunks)
            print("✅ Upload completed!")

    def get_retriever(self):
        """
        Return a retriever for performing similarity search.
        """
        return self.vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 5})
