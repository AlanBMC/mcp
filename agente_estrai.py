from praisonaiagents import Agent, MCP


web_browser_mcp_command = "uv tool run web-browser-mcp-server"

# Crie o agente
web_agent = Agent(
    instructions="""Você é um assistente que usa a ferramenta 'browse_webpage' para acessar URLs e extrair conteúdo web usando seletores CSS, se fornecidos.""",
    llm="ollama/qwen2.5:0.5b", 
    tools=MCP(web_browser_mcp_command)
)

tarefa = "Use a ferramenta browse_webpage para acessar a URL 'https://docs.praison.ai/' e extrair o conteúdo dos elementos h1 e p (parágrafos)."


print(f"Iniciando agente com a tarefa: {tarefa}")
web_agent.start(tarefa)

print("Agente concluiu a tarefa.")