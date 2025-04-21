from praisonaiagents import Agent, MCP, PraisonAIAgents


web_agent = Agent(
    instructions="""ocê tem acesso a uma ferramenta MCP chamada 'somar'.
                  Use a ferramenta 'somar' para calcular a soma de dois números quando solicitado.
                  Você também pode acessar o recurso 'info://saudacao' para obter uma mensagem do servidor.""",
    llm="ollama/qwen2.5:0.5b", 
    tools=MCP('/bin/python /home/alanb/mcp/mcps-servers/server-api.py')
)
tarefa = 'Quanto é 15 mais 27?'
web_agent.start(tarefa)