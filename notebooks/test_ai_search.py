import os
import sys
import json
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential

# Add project root to system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import Azure AI Search credentials from config.py
from config import AZURE_AI_SEARCH_ENDPOINT, AZURE_AI_SEARCH_API_KEY, AZURE_AI_SEARCH_INDEX_NAME

# Ensure credentials are set
if not AZURE_AI_SEARCH_ENDPOINT or not AZURE_AI_SEARCH_API_KEY or not AZURE_AI_SEARCH_INDEX_NAME:
    raise ValueError("Missing Azure AI Search credentials. Check config.py file.")

# Initialize AI Search Client
search_client = SearchClient(endpoint=AZURE_AI_SEARCH_ENDPOINT, 
                             index_name=AZURE_AI_SEARCH_INDEX_NAME, 
                             credential=AzureKeyCredential(AZURE_AI_SEARCH_API_KEY))

def test_ai_search(query_text):
    """Test function to check AI Search query response."""
    search_results = search_client.search(search_text="*", top=5)

    print("\n🔹 Raw AI Search Response:")
    for result in search_results:
        print(json.dumps(result, indent=2))  # Print full result to inspect keys

        # Extract only available fields
        complaint_text = result.get("complaint_text", "N/A")
        category = result.get("category", "N/A")
        department = result.get("department", "N/A")
        status = result.get("status", "N/A")
        priority = result.get("priority", "N/A")
        submitted_date = result.get("submitted_date", "N/A")
        resolution_text = result.get("resolution_text", "N/A")

        print(f"- Complaint: {complaint_text}")
        print(f"  ↳ Category: {category}")
        print(f"  ↳ Department: {department}")
        print(f"  ↳ Status: {status}")
        print(f"  ↳ Priority: {priority}")
        print(f"  ↳ Submitted Date: {submitted_date}")
        print(f"  ↳ Resolution: {resolution_text}\n")

# Run test query
if __name__ == "__main__":
    sample_query = "Power cut in my area for 5 hours"
    test_ai_search(sample_query)
