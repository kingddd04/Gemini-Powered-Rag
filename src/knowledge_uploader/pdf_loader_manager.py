import os
from langchain_community.document_loaders import PyMuPDFLoader

class PDFLoaderManager:
    """
    Manager class for loading PDF documents from a directory.
    This class scans a configured folder, loads all `.pdf` files using
    LangChain's `PyMuPDFLoader`, and returns them as LangChain Document objects.
    """

    def __init__(self, config):
        """
        Initialize the loader with the directory path from the config.
        """
        self.directory_path = config.RESOURCES_PATH

    def load_documents(self):
        """
        Load all PDF documents found in the configured directory.
        """
        all_documents = []

        if not os.path.isdir(self.directory_path):
            raise FileNotFoundError(f"Directory not found: {self.directory_path}")

        print(f"📂 Scanning Folder: {self.directory_path}...")

        for filename in os.listdir(self.directory_path):
            if filename.endswith(".pdf"):
                file_path = os.path.join(self.directory_path, filename)
                print(f"   📄 Loading: {filename}...", end=" ")

                try:
                    loader = PyMuPDFLoader(file_path)
                    loaded_pdf = loader.load()
                    all_documents.extend(loaded_pdf)
                    print("OK")
                except Exception as e:
                    print(f"\n❌ An error occurred while loading {filename}: {e}")

        return all_documents
