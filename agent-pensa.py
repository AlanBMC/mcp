from praisonaiagents import Agent, MCP
import os

# Use a single string command with Sequential Thinking configuration
sequential_agent = Agent(
    instructions="""Você é um assistente útil que pode resolver problemas complexos.
    Use as ferramentas disponíveis quando relevante para realizar análises passo a passo.""",
    llm="ollama/qwen2.5:0.5b",
    tools=MCP("npx -y @modelcontextprotocol/server-sequential-thinking")
)

sequential_agent.start("Divida o processo de fazer uma xícara de chá")
