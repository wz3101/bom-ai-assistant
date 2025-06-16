# 🤖 BOM AI Assistant

An interactive AI-powered assistant that answers natural language questions about a Bill of Materials (BOM) using **LangChain**, **OpenRouter GPT**, **Pandas**, and **Streamlit**. This chatbot allows users to explore and analyze structured product data without writing code.

---

## 🔧 Tech Stack

- **LangChain** – Agent and prompt orchestration
- **OpenRouter** – Free GPT-4-style model provider (Mistral 7B used)
- **Pandas** – Data analysis and manipulation
- **Streamlit** – Web-based user interface
- **Python** – Core programming language

---

## 🚀 Features

- Ask natural-language questions like:
  - “What is the total cost of all parts?”
  - “Which parts are mechanical?”
  - “Which part has the highest quantity?”
- Powered by GPT-like models via OpenRouter
- Automatically interprets BOM data from CSV
- User-friendly browser interface built with Streamlit

---

## 📁 Project Structure

bom-ai-assistant/
├── bom.csv # Sample BOM data
├── bom_ai_chatbot.py # Terminal-based chatbot version
├── bom_ai_app.py # Streamlit web app version
├── requirements.txt # (Optional) Package list
├── .gitignore # Git exclusions
└── README.md # You're here!
---

## ▶️ How to Run

### 1. Install Requirements

```bash
pip install -r requirements.txt
pip install pandas langchain streamlit langchain-openai langchain-experimental openrouter tabulate
##Run the web app:
streamlit run bom_ai_app.py
