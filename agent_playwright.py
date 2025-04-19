from praisonaiagents import Agent, MCP


playwright_agent = Agent(
    instructions="""Você é um assistente que pode navegar na web e 
    interagir com páginas usando o Playwright para realizar tarefas.""",    
    llm="ollama/gemma3:1b",
    tools=MCP("npx -y @blazickjp/web-browser-mcp-server")
)
tarefa = "Primeiro, navegue para 'https://www.google.com/search?q=google.com'. " \
"Depois, digite 'PraisonAI' na barra de busca. Finalmente, clique no botão de pesquisa."
playwright_agent.start(tarefa)