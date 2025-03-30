import os
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    SearchIndex, SimpleField, SearchableField, SearchField, SearchFieldDataType
)

#  Load environment variables
load_dotenv()

#  Azure AI Search Credentials (Loaded from .env)
SERVICE_ENDPOINT = os.getenv("AZURE_AI_SEARCH_ENDPOINT")
API_KEY = os.getenv("AZURE_AI_SEARCH_API_KEY")
INDEX_NAME = os.getenv("AZURE_AI_SEARCH_INDEX_NAME", "grievanceindex")

#  Ensure credentials are set
if not SERVICE_ENDPOINT or not API_KEY:
    raise ValueError("❌ Missing Azure AI Search credentials. Please check your .env file.")

#  Create Azure Search Client
search_index_client = SearchIndexClient(
    endpoint=SERVICE_ENDPOINT,
    credential=AzureKeyCredential(API_KEY)  #  Must be AzureKeyCredential, not a string
)

#  Delete existing index (if it exists)
try:
    search_index_client.delete_index(INDEX_NAME)
    print(f" Deleted existing index: {INDEX_NAME}")
except Exception:
    print(" No existing index found. Creating new index.")

#  Define new index schema
index_schema = SearchIndex(
    name=INDEX_NAME,
    fields=[
        SimpleField(name="complaint_id", type="Edm.String", key=True),  # Primary Key
        SearchableField(name="category", type="Edm.String", filterable=True, facetable=True),
        SearchableField(name="subcategory", type="Edm.String", filterable=True),
        SearchableField(name="description", type="Edm.String"),  # Complaint details
        SearchableField(name="citizen_name", type="Edm.String"),
        SimpleField(name="pincode", type="Edm.String", filterable=True),
        SearchableField(name="city", type="Edm.String", filterable=True),
        SimpleField(name="priority", type="Edm.String", filterable=True),
        SearchableField(name="department", type="Edm.String", filterable=True),
        SearchField(name="previous_resolutions", type=SearchFieldDataType.Collection(SearchFieldDataType.String))  # ✅ Corrected Collection type
    ]
)

#  Create the index
search_index_client.create_index(index_schema)
print(f" Created new index: {INDEX_NAME}")
