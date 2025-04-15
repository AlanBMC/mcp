from praisonaiagents import Agent, MCP

search_agent = Agent(
    instructions="""Voce deve me ajudar a encontrar uma casa para alugar no Airbnb""",
    llm="ollama/gemma3:1b",
    tools=MCP("npx -y @openbnb/mcp-server-airbnb --ignore-robots-txt")
)

search_agent.start("Eu quero uma casa com 2 quartos e 2 banheiros em São Paulo, Brasil, 3 dias 15-04-2025 ate 18-04-2025")
