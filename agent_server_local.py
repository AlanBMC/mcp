from praisonaiagents import Agent, MCP


web_agent = Agent(
    instructions="""ocê tem acesso a uma ferramenta MCP chamada 'somar'.
                  Use a ferramenta 'somar' para calcular a soma de dois números quando solicitado.
                  Você também pode acessar o recurso 'info://saudacao' para obter uma mensagem do servidor.""",
    llm="ollama/qwen2.5:0.5b", 
    tools=MCP('C:/Users/8761817/AppData/Local/Microsoft/WindowsApps/python3.11.exe C:/Users/8761817/Downloads/mcp/mcps-servers/server-api.py')
)

web_agent.start("quanto é 5 mais 5?")