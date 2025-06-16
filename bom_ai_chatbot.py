import pandas as pd
import openai
from langchain_openai import ChatOpenAI

from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain.agents.agent_types import AgentType
import os

# 🔐 Set your OpenAI API key here (replace with your actual key)
#openai.api_key = "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"

# 📄 Load BOM data
df = pd.read_csv("bom.csv")

# 🤖 Create LangChain Agent
#llm = OpenAI(temperature=0, openai_api_key="your-key")
llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    openai_api_key="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",
    model="mistralai/mistral-7b-instruct:free",
    temperature=0
)


agent = create_pandas_dataframe_agent(
    llm,
    df,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    allow_dangerous_code=True
)

# 💬 Chat loop
print("🤖 BOM AI Assistant (Type 'exit' to quit)")
while True:
    query = input("You: ")
    if query.lower() in ["exit", "quit"]:
        break
    try:
        response = agent.run(query)
        print(f"AI: {response}\n")
    except Exception as e:
        print("Error:", e)
