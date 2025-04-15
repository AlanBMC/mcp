from praisonaiagents import Agent, MCP
ferramenta_duckduckgo = "@nickclyde/duckduckgo-mcp-server"
# funciona: npx -y @modelcontextprotocol/server-puppeteer 
# Use MCP("npx -y @modelcontextprotocol/server-puppeteer") para o puppeteer
puppeteer_agent = Agent(
    instructions="""Você é um assistente útil que pode automatizar as interações do navegador da web.
    Use as ferramentas disponíveis quando relevante para realizar tarefas de automação web
""",
    llm="ollama/gemma3:1b",
    tools=[ferramenta_duckduckgo]
)

puppeteer_agent.start("Liste para mim os melhores site de compras")
