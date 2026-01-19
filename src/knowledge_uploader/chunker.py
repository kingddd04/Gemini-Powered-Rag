from langchain_text_splitters import RecursiveCharacterTextSplitter

class Chunker:
    """Wrapper class for langchain RecursiveCharacterTextSplitter"""

    def __init__(self, config):

        """Initialize a langchain object following config class attributes"""
        
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=config.CHUNK_SIZE,
            chunk_overlap=config.CHUNK_OVERLAP,
            separators=["\n\n", "\n", " ", ""]
        )

    def split_documents(self, documents):

        """Split the documents in smaller pieces as issued by the config class"""

        chunks = self.splitter.split_documents(documents)
        print(f"✂️  Documents divided in {len(chunks)} chunks.")
        return chunks