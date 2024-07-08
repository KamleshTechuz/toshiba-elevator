# README.md

## TOSHIBA Standard Type Elevator: Q&A

This is a Streamlit application that answers questions regarding the TOSHIBA Standard Type Elevator by processing and retrieving relevant information from a provided PDF document.

### Features

- Load a PDF document and process it for text-based Q&A.
- Split the document into manageable chunks for better processing.
- Use OpenAI's embedding model to create a vector store of the document.
- Perform similarity search to retrieve relevant information based on the user's query.
- Answer questions using a language model based on the retrieved document chunks.

### Requirements

- Python 3.8 or later
- `pip` for installing Python packages

### Installation

1. Clone the repository to your local machine:

   ```sh
   git clone https://github.com/KamleshTechuz/toshiba-elevator.git
   cd toshiba-elevator
   ```
2. Create a virtual environment:

   ```sh
   python -m venv venv
   ```
3. Activate the virtual environment:

   - On Windows:

     ```sh
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:

     ```sh
     source venv/bin/activate
     ```
4. Install the required packages:

   ```sh
   pip install -r requirements.txt
   ```

### Configuration

1. Create a `.env` file in the root directory of your project and add your environment variables. For example:

   ```env
   OPENAI_API_KEY=your_openai_api_key
   ORG_API_KEY=your_org_key

   LANGCHAIN_TRACING_V2=true
   LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
   LANGCHAIN_API_KEY=your_langchain_api_key
   LANGCHAIN_PROJECT=your_langchain_project_name

   GROQ_API_KEY=your_groq_api_key
   ```

### Usage

1. Run the Streamlit application:

   ```sh
   streamlit run app.py
   ```
2. Open the provided URL in your web browser (usually http://localhost:8501).
3. Use the text input to ask questions regarding the TOSHIBA Standard Type Elevator and click on "Document Embeddings" to load the vector store before querying.

### File Structure

- `app.py`: The main application file.
- `requirements.txt`: The file containing all the necessary Python packages.
- `elevator.pdf`: The PDF document containing the information on the TOSHIBA Standard Type Elevator.

### Dependencies

This project uses the following dependencies:

- `streamlit`: For creating the web application.
- `python-dotenv`: For loading environment variables.
- `langchain_groq`: For the language model.
- `langchain_community.embeddings`: For creating text embeddings.
- `langchain.text_splitter`: For splitting the document text.
- `langchain.chains`: For creating chains for document retrieval.
- `langchain_community.vectorstores`: For creating a vector store.
- `langchain_community.document_loaders`: For loading the PDF document.
- `faiss`: For vector similarity search.
