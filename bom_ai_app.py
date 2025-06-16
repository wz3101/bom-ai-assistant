import streamlit as st
import pandas as pd
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain.agents.agent_types import AgentType
from langchain_openai import ChatOpenAI

# Set up your model (using OpenRouter)
llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    openai_api_key="your_key",
    model="mistralai/mistral-7b-instruct:free",
    temperature=0
)

# Load the CSV
df = pd.read_csv("bom.csv")

# Create the LangChain agent
agent = create_pandas_dataframe_agent(
    llm,
    df,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    allow_dangerous_code=True
)

# Streamlit UI
st.set_page_config(page_title="BOM AI Assistant", page_icon="🤖")
st.title("🤖 BOM AI Assistant")
st.write("Ask me anything about your Bill of Materials!")

query = st.text_input("Your question:")

if query:
    with st.spinner("Thinking..."):
        try:
            response = agent.run(query)
            st.success(response)
        except Exception as e:
            st.error(f"Error: {str(e)}")
