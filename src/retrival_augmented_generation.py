from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from gemini_manager import GeminiManager
from knowledge_uploader import DBManager
from knowledge_uploader import EmbedderManager
from config import Config


class RetrievalAugmentedGeneration:
    """
    This class manages the rag process, composed of these steps:
        1 Embedding as a vector of the user request
        2 Semantic search on the user query
        3 Retrival of most useful parts 
        4 generation of model response trought prompt engegnering 
    """

    def __init__(self):
        """Initialize all components required for the RAG pipeline."""

        # Getting the config
        config = Config()

        # Embedder
        embedder_mgr = EmbedderManager(config)

        # db manager
        db_managerr = DBManager(config, embedder_mgr)
        self.retriever = db_managerr.get_retriever()

        # LLM 
        self.gemini_mgr = GeminiManager(config)
        self.llm = self.gemini_mgr.get_llm()

        # Build the RAG pipeline
        self.rag_chain = self._build_chain()

    def _build_chain(self):
        """
        Construct the RAG pipeline using LangChain runnables. The chain performs: 
        - Parallel retrieval of context and passthrough of the user question. 
        - Prompt construction using a system + human template. 
        - LLM invocation to generate the final answer.
        """
        system_prompt = (
            "You are an expert assistant based on the provided documents. "
            "Use the following pieces of context to answer the user's question. "
            "if the question is gibberish or without meaning ask the user to repeat politely"
            "If the answer is not in the context, clearly say that you don't know. "
            "Be concise and professional.\n\n"
            "--- CONTEXT ---\n{context}\n----------------"
        )


        prompt = ChatPromptTemplate.from_messages([("system", system_prompt),("human", "{question}")])


        rag_chain = (RunnableParallel(context=self.retriever, question=RunnablePassthrough())  | prompt   | self.llm)

        return rag_chain

    def ask(self, query: str):
        """
        Query the RAG system with a user question.
        """
        if not query:
            return "Please type a question"

        try:
            response = self.rag_chain.invoke(query)
            return response.content
        except Exception as e:
            return f"❌ Error During Text Generation  {e}"
