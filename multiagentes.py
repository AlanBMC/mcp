from praisonaiagents import Agent, MCP, PraisonAIAgents

mcp_tool_connector = MCP('/bin/python /home/alanb/mcp/mcps-servers/server-api.py')


agente_somador = Agent(
    role='Calculador Matemático',
    goal='Calcular a soma de dois números fornecidos usando a ferramenta `somar`.',
    backstory="""Você é um especialista em aritmética. Sua única função é receber dois números
                 e usar a ferramenta 'somar' para calcular o resultado.
                 Não realize outras tarefas.""",
    llm="ollama/gemma3:1b", # Ou o LLM de sua preferência
    tools=mcp_tool_connector, # Permite que este agente acesse as ferramentas do servidor MCP
    allow_delegation=False, # Este agente executa a tarefa, não delega
     # Útil para depuração
)
agente_memoria = Agent(
    role='Assistente de Memória do Usuário',
    goal='Recuperar o nome completo do usuário usando a ferramenta `memoria_user`.',
    backstory="""Você tem acesso a informações do usuário. Sua única função é usar
                 a ferramenta 'memoria_user' quando solicitado a fornecer o nome do usuário.
                 Não realize outras tarefas.""",
    llm="ollama/gemma3:1b", # Ou o LLM de sua preferência
    tools=mcp_tool_connector, # Permite que este agente acesse as ferramentas do servidor MCP
    allow_delegation=False, # Este agente executa a tarefa, não delega
    
)


agente_dispatcher = Agent(
    role='Gerente de Tarefas',
    goal='Analisar a solicitação do usuário e delegar a tarefa para o agente especialista apropriado.',
    backstory=f"""Você é o gerente de uma equipe de dois agentes:
                 1. Calculador Matemático (role: {agente_somador.role}): Especialista em somar números usando a ferramenta 'somar'.
                 2. Assistente de Memória do Usuário (role: {agente_memoria.role}): Especialista em buscar o nome do usuário usando a ferramenta 'memoria_user'.

                 Sua responsabilidade é:
                 - Receber a solicitação do usuário.
                 - Entender a intenção (é uma soma ou um pedido de nome?).
                 - Delegar a tarefa para o agente correto ('Calculador Matemático' para somas, 'Assistente de Memória do Usuário' para nomes).
                 - Fornecer ao agente delegado toda a informação necessária da solicitação original.
                 - Retornar a resposta final do agente delegado para o usuário.""",
    llm="ollama/gemma3:1b", 
    tools=mcp_tool_connector,
    allow_delegation=True, 
    
)
grupo_de_agentes = PraisonAIAgents(
    agents=[agente_dispatcher, agente_somador, agente_memoria],
    
)
grupo_de_agentes.start("quanto é 15 mais 27?")