from langchain_google_genai import GoogleGenerativeAIEmbeddings

class EmbedderManager:
    """
    Wrapper class for Google Generative AI embedding models.

    This class initializes a LangChain-compatible embedding model using
    configuration parameters from the class config. It exposes a simple
    accessor method to retrieve the embedding instance.
    """

    def __init__(self, config):
        """
        Initialize the embedding model using the provided configuration.
        """
        if not config.GOOGLE_API_KEY:
            raise ValueError("❌ GOOGLE_API_KEY not provided")

        self.embeddings = GoogleGenerativeAIEmbeddings(
            model=config.EMBEDDING_MODEL,
            google_api_key=config.GOOGLE_API_KEY
        )

    def get_embeddings(self):
        """
        Return the initialized embedding model 
        """
        return self.embeddings
