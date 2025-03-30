import os
import json
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from dotenv import load_dotenv

#  Load environment variables
load_dotenv()

#  Azure AI Search Credentials (Loaded from .env)
SERVICE_ENDPOINT = os.getenv("AZURE_AI_SEARCH_ENDPOINT")
API_KEY = os.getenv("AZURE_AI_SEARCH_API_KEY")
INDEX_NAME = os.getenv("AZURE_AI_SEARCH_INDEX_NAME", "grievanceindex")

#  Ensure credentials are set
if not SERVICE_ENDPOINT or not API_KEY:
    raise ValueError(" Missing Azure AI Search credentials. Please check your .env file.")

#  Create Azure AI Search Client
search_client = SearchClient(
    endpoint=SERVICE_ENDPOINT,
    index_name=INDEX_NAME,
    credential=AzureKeyCredential(API_KEY)
)

#  Construct the correct file path dynamically
current_dir = os.path.dirname(os.path.abspath(__file__))  # Get script directory
file_path = os.path.join(current_dir, "../data/synthetic_grievances.json")

#  Check if file exists before opening
if not os.path.exists(file_path):
    raise FileNotFoundError(f" The file '{file_path}' does not exist! Please check the path.")

#  Load the synthetic grievance dataset
with open(file_path, "r", encoding="utf-8") as file:
    documents = json.load(file)  # Load all grievances

#  Upload data in batches (1000 docs per request)
batch_size = 1000  
for i in range(0, len(documents), batch_size):
    batch = documents[i:i + batch_size]
    upload_result = search_client.upload_documents(batch)
    print(f" Uploaded batch {i // batch_size + 1}/{(len(documents) - 1) // batch_size + 1} successfully!")

print(f" Successfully uploaded {len(documents)} grievances to Azure AI Search!")
