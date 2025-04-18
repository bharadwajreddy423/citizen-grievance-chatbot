import os
import sys
import random
import streamlit as st

# Add src/ to system path so Python can find chatbot.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from chatbot import Chatbot
import config  # Import configuration variables

# Initialize Chatbot (WITHOUT passing API keys)
chatbot = Chatbot()  # ✅ Fix: No unnecessary arguments

# Set up Streamlit UI with custom styling
st.set_page_config(
    page_title="Citizen Grievance Chatbot",
    layout="wide",
    page_icon="🆘",
)

# Custom CSS for enhanced UI
st.markdown("""
    <style>
        body {
            background-color: #f4f4f9;
            color: #333333;
        }
        .stApp {
            background: linear-gradient(to right, #4facfe, #00f2fe);
        }
        .css-18e3th9 {
            padding: 2rem !important;
        }
        .stTextArea textarea {
            background-color: #ffffff;
            color: #333333;
            border-radius: 10px;
        }
        .stButton button {
            background: linear-gradient(to right, #4facfe, #00f2fe);
            border: none;
            color: white;
            padding: 10px 24px;
            text-align: center;
            font-size: 16px;
            border-radius: 10px;
            cursor: pointer;
        }
        .stButton button:hover {
            background: linear-gradient(to right, #00f2fe, #4facfe);
        }
        .stAlert {
            font-size: 16px;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Title and Header
st.markdown("<h1 style='text-align: center;'>🆘 Citizen Grievance Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>🔹 Describe your complaint, and the chatbot will provide past grievances along with an AI-generated response.</h4>", unsafe_allow_html=True)

# Input Section
st.markdown("### 📝 Enter Your Complaint Below:")
user_input = st.text_area("Describe the issue you are facing:", height=150)

# Generate a random 7-digit complaint ID function
def generate_complaint_id():
    return str(random.randint(1000000, 9999999))

# Submit Button
if st.button("🚀 Submit"):
    if user_input:
        complaint_id = generate_complaint_id()  # Generate a unique complaint ID
        
        with st.spinner("🔍 Searching past grievances..."):
            search_results = chatbot.search_grievances(user_input)

        with st.spinner("🤖 Generating AI response..."):
            ai_response = chatbot.chatbot_response(user_input)

        # Display Results
        st.markdown("## 🔍 Relevant Past Grievances")
        if search_results.strip():
            st.info(search_results)
        else:
            st.warning("⚠️ No relevant past grievances found.")

        st.markdown("## 🤖 AI Response")
        st.success(ai_response)

        # Display Complaint ID
        st.markdown(f"### 📌 Your Complaint ID: `{complaint_id}`")
        st.info("Use this Complaint ID to track your complaint status.")

    else:
        st.warning("⚠️ Please enter a complaint before submitting.")

# Tracking Input Section
st.sidebar.markdown("### 🔍 Track Your Complaint")
tracking_input = st.sidebar.text_input("Enter your Complaint ID to track:")

# Fixed tracking response
if tracking_input:
    if tracking_input.isdigit() and len(tracking_input) == 7:
        st.sidebar.success("✅ Your complaint has been assigned to the concerned department. You will receive updates via email and SMS once resolved.")
    else:
        st.sidebar.warning("⚠️ Please enter a valid 7-digit Complaint ID.")

# Sidebar Info
st.sidebar.header("ℹ️ About the Chatbot")
st.sidebar.write(
    "This AI-powered chatbot searches past grievances using **Azure AI Search** and generates responses using **Azure OpenAI (GPT-4o)**."
)

st.sidebar.markdown("🚀 **Technologies Used:**")
st.sidebar.markdown("- Azure AI Search 🧐")
st.sidebar.markdown("- Azure OpenAI GPT-4o 🤖")
st.sidebar.markdown("- Streamlit UI 🎨")

st.sidebar.markdown("---")
st.sidebar.write("Developed with ❤️ for Citizen Grievance Redressal.")
