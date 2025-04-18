from praisonaiagents import Agent, MCP
import os
from langchain_community.llms import Ollama
OLLAMA_BASE_URL = os.getenv("http://192.168.1.7:11434/", "http://localhost:11434")
LOCAL_MODEL_NAME = "qwen2.5:0.5b"

local_llm = Ollama(
        model=LOCAL_MODEL_NAME,
        base_url=OLLAMA_BASE_URL
        # Add other parameters if needed, e.g., temperature, top_k, etc.
        # temperature=0.7
    )
search_agent = Agent(
    instructions="""Voce deve me ajudar a encontrar uma casa para alugar no Airbnb""",
    llm="ollama/gemma3:1b",
    tools=MCP("npx -y @openbnb/mcp-server-airbnb --ignore-robots-txt")
)

search_agent.start("Eu quero uma casa com 2 quartos e 2 banheiros em São Paulo, Brasil, 3 dias 15-04-2025 ate 18-04-2025")
