import os
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient

# Load environment variables
SERVICE_ENDPOINT = os.getenv("AZURE_AI_SEARCH_ENDPOINT")
API_KEY = os.getenv("AZURE_AI_SEARCH_API_KEY")  # Replace with your API Key
INDEX_NAME = "grievanceindex"

# Initialize Azure AI Search client
search_client = SearchClient(endpoint=SERVICE_ENDPOINT, index_name=INDEX_NAME, credential=AzureKeyCredential(API_KEY))

def search_grievances(query, top_n=3):
    """
    Searches Azure AI Search for relevant grievances based on the user's query.
    """
    results = search_client.search(search_text=query, top=top_n)
    
    response = []
    for result in results:
        complaint_id = result.get("complaint_id", "N/A")
        category = result.get("category", "Unknown")
        description = result.get("description", "No details available")
        previous_resolutions = result.get("previous_resolutions", ["No past resolutions found."])

        response.append({
            "complaint_id": complaint_id,
            "category": category,
            "description": description,
            "previous_resolutions": previous_resolutions
        })
    
    return response
