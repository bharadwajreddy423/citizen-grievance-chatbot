import os
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Azure Search Credentials (Loaded from .env)
SERVICE_ENDPOINT = os.getenv("AZURE_AI_SEARCH_ENDPOINT")
INDEX_NAME = os.getenv("AZURE_AI_SEARCH_INDEX_NAME", "grievanceindex")
API_KEY = os.getenv("AZURE_AI_SEARCH_API_KEY")

# Ensure variables are set
if not SERVICE_ENDPOINT or not API_KEY:
    raise ValueError("Missing Azure AI Search credentials. Please check your .env file.")

# Initialize Search Client
search_client = SearchClient(endpoint=SERVICE_ENDPOINT, index_name=INDEX_NAME, credential=AzureKeyCredential(API_KEY))

# Test Search Query
results = search_client.search(search_text="potholes", top=3)  # Searching for "potholes" in complaints

for result in results:
    print(f"📌 Complaint ID: {result.get('complaint_id', 'N/A')}")
    print(f"🔹 Category: {result.get('category', 'Unknown')}")
    print(f"🔹 Description: {result.get('description', 'No details available')}")
    print(f"🔹 Previous Resolutions: {result.get('previous_resolutions', 'N/A')}")
    print("-" * 50)
