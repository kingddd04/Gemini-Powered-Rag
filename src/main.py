from knowledge_uploader_manager import KnowledgeUploaderManager
from retrival_augmented_generation import RetrievalAugmentedGeneration
from config import Config

def main():
    print("\n---Gemini Powered Rag---\n")
    reload_rag_choice = input("- Do you want to upload current pdf folder content with cloud?(y/n)")
    
    if reload_rag_choice.lower() == 'y':
        print("\nUploading your files...")
        builder = KnowledgeUploaderManager()
        builder.run_ingestion()

    print("\n💬Booting the chatbot...")

    rag = RetrievalAugmentedGeneration()
    conf = Config()
    
    while True:
        user_input = input("\nYou: ")
        answer = rag.ask(user_input)
        print(f"Gemini {conf.CHAT_MODEL} : {answer}")

if __name__ == "__main__":
    main()
    print("n")