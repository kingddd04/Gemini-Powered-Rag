# Gemini Powered RAG

A Retrieval-Augmented Generation (RAG) system powered by Google Gemini and Qdrant vector database. This project enables you to build an intelligent chatbot that can answer questions based on your PDF documents using state-of-the-art AI technology.

## Features

### 📄 PDF Ingestion
- **Loading**: Automatically loads PDF documents from a designated folder
- **Chunking**: Splits documents into manageable chunks for efficient processing
- **Embedding**: Converts text chunks into vector embeddings using Google's `text-embedding-004` model

### 🗄️ Vector Storage
- **Qdrant Integration**: Stores and manages document embeddings in Qdrant vector database
- **Semantic Search**: Performs similarity search to retrieve relevant context for user queries

### 🤖 AI Chat
- **Gemini-Powered**: Uses Google's Gemini models (default: `gemini-2.5-flash-lite` or configurable) for intelligent responses
- **Context-Aware**: Generates answers based on retrieved document content
- **Interactive CLI**: Provides a simple command-line interface for real-time conversations

## Project Structure

```
Gemini-Powered-Rag/
├── src/                              # Source code directory
│   ├── main.py                       # Entry point for the application
│   ├── config.py                     # Configuration management (API keys, settings)
│   ├── knowledge_uploader_manager.py # Orchestrates the PDF ingestion pipeline
│   ├── retrival_augmented_generation.py # RAG pipeline implementation
│   ├── gemini_manager.py             # Manages Gemini LLM integration
│   └── knowledge_uploader/           # PDF processing modules
│       ├── pdf_loader_manager.py     # PDF loading functionality
│       ├── chunker.py                # Document chunking logic
│       ├── embedder_manager.py       # Embedding generation
│       └── db_manager.py             # Qdrant database operations
├── rag_knowledge_pdfs/               # Place your PDF files here
├── requirements.txt                  # Python dependencies
├── empty.env                         # Environment variables template
└── README.md                         # This file
```

## Prerequisites

Before you begin, ensure you have the following:

- **Python 3.8+**: Make sure Python is installed on your system
- **Google API Key**: Obtain a free API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
- **Qdrant Database**: Set up a Qdrant instance
  - Cloud option: Sign up for free at [Qdrant Cloud](https://cloud.qdrant.io/)
  - Self-hosted option: Run Qdrant locally using Docker
- **Qdrant API Key & URL**: Credentials for your Qdrant instance

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/kingddd04/Gemini-Powered-Rag.git
   cd Gemini-Powered-Rag
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **Create a `.env` file** based on the `empty.env` template:
   ```bash
   cp empty.env .env
   ```

2. **Edit the `.env` file** with your credentials:
   ```env
   # --- QDRANT ---
   QDRANT_URL=https://your-qdrant-instance.cloud.qdrant.io
   QDRANT_API_KEY=your_qdrant_api_key_here
   QDRANT_COLLECTION=your_collection_name

   # --- GOOGLE ---
   GOOGLE_API_KEY=your_google_api_key_here
   GEMINI_MODEL=gemini-2.5-flash-lite
   GEMINI_EMBEDDINGS_MODEL=models/text-embedding-004
   ```

   **Configuration Options**:
   - `QDRANT_URL`: Your Qdrant instance URL
   - `QDRANT_API_KEY`: Authentication key for Qdrant
   - `QDRANT_COLLECTION`: Name of the collection to store embeddings
   - `GOOGLE_API_KEY`: Your Google AI API key
   - `GEMINI_MODEL`: Gemini model to use for chat (e.g., `gemini-2.5-flash-lite`, `gemini-1.5-flash`)
   - `GEMINI_EMBEDDINGS_MODEL`: Embedding model (default: `models/text-embedding-004`)

## Usage

### Step 1: Add Your PDF Documents

Place the PDF files you want to query into the `rag_knowledge_pdfs/` directory:

```bash
cp /path/to/your/documents/*.pdf rag_knowledge_pdfs/
```

### Step 2: Run the Application

Start the application by running:

```bash
python src/main.py
```

### Step 3: Upload PDFs to Vector Database

When prompted, choose whether to upload your PDFs:

```
---Gemini Powered Rag---

- Do you want to upload current pdf folder content with cloud?(y/n)
```

- Type `y` to process and upload your PDFs to Qdrant (required on first run or when adding new documents)
- Type `n` to skip uploading and use existing vector data

### Step 4: Chat with Your Documents

Once the chatbot boots up, you can start asking questions:

```
💬Booting the chatbot...

You: What is the main topic of the document?
Gemini gemini-2.5-flash-lite: The document discusses...

You: Can you summarize the key points?
Gemini gemini-2.5-flash-lite: Here are the key points...
```

**Tips**:
- Ask specific questions related to your PDF content
- The chatbot will only answer based on the documents you've uploaded
- If the answer isn't in the documents, the chatbot will let you know

## How It Works

### Technical Architecture

This project uses the **LangChain** framework to build a Retrieval-Augmented Generation system:

1. **Document Loading**: PDFs are loaded using `PyMuPDF` through LangChain's document loaders

2. **Text Chunking**: Documents are split into chunks of 1000 characters with 200 character overlap to maintain context

3. **Embedding Generation**: Text chunks are converted to 768-dimensional vectors using Google's `text-embedding-004` embedding model

4. **Vector Storage**: Embeddings are stored in Qdrant vector database for efficient similarity search

5. **Query Processing**:
   - User query is embedded using the same embedding model
   - Semantic search finds the most relevant document chunks
   - Retrieved context is passed to the Gemini LLM

6. **Response Generation**: Gemini model (default: `gemini-2.5-flash-lite` or as configured) generates a contextual answer using:
   - Retrieved document chunks as context
   - A carefully crafted prompt template
   - Temperature setting of 0.9 for creative responses

### Key Technologies

- **LangChain**: Orchestrates the RAG pipeline
- **Google Gemini**: Powers the chat responses with advanced AI
- **Qdrant**: Provides fast vector similarity search
- **PyMuPDF**: Handles PDF document parsing
- **text-embedding-004**: Google's embedding model for semantic understanding

### RAG Pipeline Flow

```
User Query → Embedding → Vector Search → Context Retrieval → LLM Prompt → Gemini Response
```

This architecture ensures that responses are grounded in your document content while leveraging the power of large language models for natural, coherent answers.

## License

This project is open-source and available under the MIT License.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## Support

For questions or issues, please open an issue on the [GitHub repository](https://github.com/kingddd04/Gemini-Powered-Rag/issues).
