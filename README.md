# 🛡️ Nexus Global | Sentiment Intelligence & Recovery Command

Nexus Global is an enterprise-grade customer retention dashboard designed to bridge the gap between negative customer sentiment and formal resolution. Built with **Streamlit** and powered by the **Gemini 2.0 Flash** large language model, this system automates the analysis of client feedback and generates high-impact, professional outreach packages.

---

### 🚀 Core Capabilities

* **Sentiment Intelligence Feed**: Aggregates customer review data into a centralized obsidian-themed interface for rapid assessment.
* **Dynamic Priority Engine**: Automatically categorizes clients as "Critical" or "High" priority based on purchase history and tier status.
* **AI Outreach Generation**: Utilizes generative AI to draft concise, empathetic 3-sentence apologies coupled with strategic recovery offers (e.g., `RESET20` discount codes).
* **Enterprise Dispatch Integration**: Features a direct `mailto` integration that formats drafts into ready-to-send enterprise emails.

---

### 🛠️ Technical Architecture

The application is architected for security and performance:
* **Frontend**: Streamlit (Python-based reactive web framework)
* **Intelligence**: Google Gemini 2.0 Flash API
* **Data Layer**: Pandas for structured CSV processing
* **Security**: Professional environment variable management using `python-dotenv` to ensure API credentials remain abstracted from source control.

---

### 📦 Installation & Deployment

#### 1. Clone the Repository
```bash
git clone https://github.com/IshaniArora1024/nexus-recovery-suite.git
cd nexus-recovery-suite
2. Environment Configuration
Create a .env file in the root directory and define your API key:

Plaintext

GEMINI_API_KEY=your_secured_api_key_here
3. System Launch
Bash

pip install -r requirements.txt
streamlit run app.py
📊 Operational Constraints & Quota Management
As this project utilizes the Google AI Studio Free Tier, it operates within the following parameters to ensure stability:

RPM: 5 Requests Per Minute

RPD: 20 Requests Per Day
