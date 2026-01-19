from langchain_google_genai import ChatGoogleGenerativeAI

class GeminiManager:
    """
    This class manages the gemini llm trought langchain library
    """

    def __init__(self, config):
        self.llm = ChatGoogleGenerativeAI(
            model=config.CHAT_MODEL,
            temperature=config.TEMPERATURE,
            api_key=config.GOOGLE_API_KEY
        )
        print(config.CHAT_MODEL)

    def get_llm(self):
        """
        returns the llm ready to be used
        """
        return self.llm
    