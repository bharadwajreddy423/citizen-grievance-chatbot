import streamlit as st

# Azure OpenAI
AZURE_OPENAI_API_KEY = st.secrets["AZURE_OPENAI_API_KEY"]
AZURE_OPENAI_ENDPOINT = st.secrets["AZURE_OPENAI_ENDPOINT"]
AZURE_OPENAI_DEPLOYMENT_NAME = st.secrets["AZURE_OPENAI_DEPLOYMENT_NAME"]
AZURE_OPENAI_API_VERSION = st.secrets.get("AZURE_OPENAI_API_VERSION", "2024-05-01-preview")

# Azure AI Search
AZURE_AI_SEARCH_API_KEY = st.secrets["AZURE_AI_SEARCH_API_KEY"]
AZURE_AI_SEARCH_ENDPOINT = st.secrets["AZURE_AI_SEARCH_ENDPOINT"]
AZURE_AI_SEARCH_INDEX_NAME = st.secrets.get("AZURE_AI_SEARCH_INDEX_NAME", "grievanceindex")

# Logging Level
LOG_LEVEL = st.secrets.get("LOG_LEVEL", "INFO")

'''
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

    # Azure OpenAI
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION", "2024-05-01-preview")

    # Azure AI Search
AZURE_AI_SEARCH_API_KEY = os.getenv("AZURE_AI_SEARCH_API_KEY")
AZURE_AI_SEARCH_ENDPOINT = os.getenv("AZURE_AI_SEARCH_ENDPOINT")
AZURE_AI_SEARCH_INDEX_NAME = os.getenv("AZURE_AI_SEARCH_INDEX_NAME", "grievanceindex")

    # Logging Level
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

'''

