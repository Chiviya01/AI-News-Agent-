# News Agent Project

The **News Agent Project** is an agentic system designed to efficiently process user queries and provide relevant news information. This system utilizes three key tools to handle queries:

1. **Query Processing Tool**: The agent first determines if the user's query is searchable or not.
2. **DuckDuckGo Search Tool**: If the query is searchable, DuckDuckGo is used to retrieve relevant search results.
3. **Summarization Tool**: This tool either gets the user query if not searchable or the search results from our search engine, 
the agent then uses a **Groq-powered LLM (Large Language Model)** to summarize the query or the search results and provide a concise response.

The entire system is exposed through **FastAPI** and interacts with a **React frontend**, providing a clean and intuitive user interface for easy query input and response display.

## Tools Used
- **FastAPI**: To expose the backend as an API.
- **DuckDuckGo Search**: For privacy-focused search results.
- **Groq LLM**: For query summarization and response generation.
- **React**: For the user interface.

## Setup and Installation

Follow these steps to get the project up and running locally:

### 1. Install Dependencies

First, install the required Python dependencies by running:

```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables
Create a .env file in the root directory of the project and add your Groq API Key:
```bash
GROQ_API_KEY=your_groq_api_key_here
```

### 3. Run the Application
Now, you can run the FastAPI backend by executing:
```bash
fastapi dev app.py
```

