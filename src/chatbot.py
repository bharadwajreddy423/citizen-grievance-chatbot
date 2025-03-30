import os
from dotenv import load_dotenv
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from openai import AzureOpenAI

# Load environment variables
load_dotenv()

class Chatbot:
    def __init__(self):
        """Initialize Azure OpenAI & Azure AI Search Clients using .env variables"""
        self.client = AzureOpenAI(
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION")
        )

        self.deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

        # Azure AI Search Client
        self.search_client = SearchClient(
            endpoint=os.getenv("AZURE_AI_SEARCH_ENDPOINT"),
            index_name=os.getenv("AZURE_AI_SEARCH_INDEX_NAME"),
            credential=AzureKeyCredential(os.getenv("AZURE_AI_SEARCH_API_KEY"))
        )

    def search_grievances(self, user_query):
        """Search relevant grievances from Azure AI Search"""
        search_results = self.search_client.search(search_text=user_query, top=3)
        formatted_results = [
            f"- {res.get('description', 'N/A')} (Category: {res.get('category', 'N/A')})"
            for res in search_results
        ]
        return "\n".join(formatted_results) if formatted_results else "No relevant past grievances found."

    def chatbot_response(self, user_query):
        """Generate response using GPT-4o, incorporating relevant grievance data"""
        search_context = self.search_grievances(user_query)

        messages = [
            {"role": "system", "content": "You are a helpful assistant for citizen grievance redressal."},
            {"role": "user", "content": f"The user reported: '{user_query}'.\n\nRelevant past grievances:\n{search_context}"}
        ]

        response = self.client.chat.completions.create(
            model=self.deployment_name,
            messages=messages,
            temperature=0.7,
            max_tokens=800
        )

        return response.choices[0].message.content
