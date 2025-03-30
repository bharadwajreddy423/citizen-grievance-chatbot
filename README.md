# 🆘 Citizen Grievance Chatbot  

### **An AI-powered chatbot for citizen complaint redressal using Azure AI & OpenAI services.**  

## 🚀 **Overview**  

The **Citizen Grievance Chatbot** is an AI-powered virtual assistant designed to help citizens **file complaints, track past grievances, and get AI-generated resolutions**. It uses **Azure OpenAI (GPT-4o)** to generate responses and **Azure AI Search** to fetch similar past grievances, making the redressal process **faster and more efficient**.  

### **👨‍💼 Who is this for?**  
- **Citizens** who want to file complaints and check previous grievances.  
- **Government officials** who need an AI-assisted way to manage public grievances.  
- **Developers & AI enthusiasts** exploring how Azure OpenAI can be used in real-world applications. 

🔗 **Live App:** [Citizen Grievance Chatbot](https://ewmwu4gykjccurcsvkyko2.streamlit.app/) 

---

## 🏗 **Project Features**  

📝 File Complaints: Users can describe their grievances in natural language.
🆔 Complaint ID Generation & Tracking: Each complaint gets a unique Complaint ID for tracking.
🔍 AI Search for Similar Complaints: The chatbot retrieves relevant past grievances from Azure AI Search.
🤖 AI-Powered Responses: The chatbot generates possible solutions using Azure OpenAI (GPT-4o).
🎨 User-Friendly Interface: A sleek Streamlit UI for easy interaction.
⚡ Scalable & Secure: Built with Azure services, ensuring security & performance.  

---

## 🛠 **Tech Stack & Architecture**  

| Technology | Purpose |
|------------|---------|
| **Python** | Core language for backend processing |
| **Streamlit** | Interactive UI for the chatbot |
| **Azure OpenAI (GPT-4o)** | AI-generated responses to citizen grievances |
| **Azure AI Search** | Fetches past grievances to improve response accuracy |
| **Azure Document Intelligence** | Extracts structured data from uploaded grievance forms (optional) |
| **Azure Blob Storage** | Stores grievance data and logs |
| **GitHub & Streamlit Cloud** | Deployment and hosting |

---

## 🔧 **Setup & Installation**  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/bharadwajreddy423/citizen-grievance-chatbot.git
cd citizen-grievance-chatbot
```

### **2️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **3️⃣ Set Up Environment Variables**  
Create a **.env** file in the root folder and add your API keys:  

```env
AZURE_OPENAI_API_KEY=your-openai-api-key
AZURE_OPENAI_ENDPOINT=your-openai-endpoint
AZURE_OPENAI_DEPLOYMENT_NAME=your-deployment-name
AZURE_AI_SEARCH_API_KEY=your-ai-search-api-key
AZURE_AI_SEARCH_ENDPOINT=your-ai-search-endpoint
AZURE_AI_SEARCH_INDEX_NAME=grievanceindex
```

Alternatively, if deploying to **Streamlit Cloud**, add these to **secrets.toml**:  
```toml
[secrets]
AZURE_OPENAI_API_KEY = "your-openai-api-key"
AZURE_OPENAI_ENDPOINT = "your-openai-endpoint"
AZURE_OPENAI_DEPLOYMENT_NAME = "your-deployment-name"
AZURE_AI_SEARCH_API_KEY = "your-ai-search-api-key"
AZURE_AI_SEARCH_ENDPOINT = "your-ai-search-endpoint"
AZURE_AI_SEARCH_INDEX_NAME = "grievanceindex"
```

### **4️⃣ Run the Application Locally**  
```bash
streamlit run app.py
```

---

## 🚀 **Deployment on Streamlit Cloud**  

1️⃣ Push your latest code to GitHub:  
```bash
git add .
git commit -m "Updated chatbot logic"
git push origin main
```

2️⃣ Go to **Streamlit Cloud** → **New App** → Select your repository.  

3️⃣ Add **secrets** in the settings and deploy! 🎉  

---

## 🧩 **How It Works**  

1️⃣ User enters a complaint into the chatbot.
2️⃣ The chatbot generates a unique Complaint ID and saves the complaint.
3️⃣ The chatbot searches past grievances using Azure AI Search.
4️⃣ If similar cases exist, they are retrieved & displayed.
5️⃣ The chatbot generates a response using Azure OpenAI GPT-4o.
6️⃣ The user receives both past references & AI-generated solutions.
7️⃣ User can later check their Complaint ID to track grievance status.  

---

📌 Use Case Example
🔹 User Complaint: "The streetlights in my area have been broken for weeks. No action has been taken."

🔍 AI Search Results:

"Streetlights were repaired in XYZ area after a complaint to the municipal office."

"Civic authorities resolved a similar issue in ABC colony within 7 days."

🆔 Complaint ID: "GRV-20250331-123456"

🤖 AI Response:
"Based on past grievances, you can report this issue to the municipal office under the streetlight maintenance department. Your complaint will be addressed within 7 days."

🔎 Later, when the user checks their complaint status:
🆔 User Enters Complaint ID: "GRV-20250331-123456"
✅ Status Retrieved: "Your complaint has been assigned to the municipal office and is currently being reviewed."
---

##  **Future Enhancements**  

🔹 **Multilingual Support:** Enable grievance filing in **regional languages**.  
🔹 **Integration with Government APIs:** Automate complaint registration in **official portals**.  
🔹 **Complaint Tracking System:** Allow users to track **real-time status** of complaints.  
🔹 **Speech-to-Text:** Users can **speak** their complaints instead of typing.  

---

## 🤝 **Contributing**  

We welcome contributions! Feel free to **fork** this repository, submit **pull requests**, or report **issues**.  
---

📜 License
This project is licensed under the  Apache License.
