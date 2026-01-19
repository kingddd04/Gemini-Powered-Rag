from knowledge_uploader import PDFLoaderManager
from knowledge_uploader import Chunker
from knowledge_uploader import EmbedderManager
from knowledge_uploader import DBManager
from config import Config

class KnowledgeUploaderManager:
    """
    This class handles the uploading process
    of the pdfs for the Rag on the database following these steps:
        1 pdf loading
        2 chunking
        3 embedding
        4 uploading
    """
    def __init__(self):
        """
        Initialize the objects that we need for the upload process from their classes
        """

        self.config = Config()
        self.pdf_loader = PDFLoaderManager(self.config)
        self.chunker = Chunker(self.config)
        self.embedder_manager = EmbedderManager(self.config)
        self.db_manager = DBManager(self.config, self.embedder_mgr)

    def run_ingestion(self):
        """
        Executes the uploading pipeline -loading-chunking-embedding-uploading on the db
        """
        print(f"\n- Loading pdfs from : {self.config.RESOURCES_PATH}")

        # Phase 1: loading
        try:
            raw_docs = self.pdf_loader.load_documents()

        except Exception as e:
            print(f"❌ Error while loading: {e}")
            return

        if not raw_docs:
            print("⚠️ Nothing was loaded from the folder.")
            return
        
        # Phase 2: Splitting (Chunking)
        chunks = self.chunker.split_documents(raw_docs)

        # Phase 3: Indexing (Embedding + Uploading on db)
        self.db_manager.index_documents(chunks) # the class uploader manager calls the embedder