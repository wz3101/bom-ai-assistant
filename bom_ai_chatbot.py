import pandas as pd
import openai
from langchain_openai import ChatOpenAI

from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain.agents.agent_types import AgentType
import os


# 📄 Load BOM data
df = pd.read_csv("bom.csv")

# 🤖 Create LangChain Agent
#llm = OpenAI(temperature=0, openai_api_key="your-key")
llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    openai_api_key="key",
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
