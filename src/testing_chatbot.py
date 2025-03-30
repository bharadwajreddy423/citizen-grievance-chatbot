import os
from dotenv import load_dotenv
from chatbot import Chatbot

# Load environment variables
load_dotenv()

# Initialize Chatbot
chatbot = Chatbot()

# User input for testing
while True:
    user_input = input("👤 You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting chatbot. Goodbye!")
        break

    response = chatbot.chatbot_response(user_input)
    print(f"Chatbot: {response}\n")
