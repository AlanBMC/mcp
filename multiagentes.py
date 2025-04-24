from praisonaiagents import Agent, MCP, PraisonAIAgents

mcp_tool_connector = MCP('C:/Users/8761817/AppData/Local/Microsoft/WindowsApps/python3.11.exe C:/Users/8761817/Downloads/mcp/mcps-servers/server-api.py')

agente_somador = Agent(
    role='Calculador Matemático',
    goal='Calcular a soma de dois números fornecidos usando a ferramenta `somar`.',
    backstory="""Você é um especialista em aritmética. Sua única função é receber dois números
                 e usar a ferramenta 'somar' para calcular o resultado.
                 Após realizar a soma, retorne APENAS o resultado numérico e encerre.""",
    llm="ollama/qwen2.5:0.5b",
    tools=mcp_tool_connector,
    allow_delegation=False,
    max_iter=1,
    max_retry_limit=1,
    self_reflect=False,
    verbose=False
)

agente_memoria = Agent(
    role='Assistente de Memória do Usuário',
    goal='Recuperar o nome completo do usuário usando a ferramenta `memoria_user`.',
    backstory="""Você é especialista em recuperar informações do usuário.
                 Use APENAS a ferramenta 'memoria_user' quando solicitado.
                 Retorne APENAS o nome do usuário e encerre.""",
    llm="ollama/qwen2.5:0.5b",
    tools=mcp_tool_connector,
    allow_delegation=False,
    max_iter=1,
    max_retry_limit=1,
    self_reflect=False,
    verbose=False
)

agente_dispatcher = Agent(
    role='Gerente de Tarefas',
    goal='Analisar a solicitação do usuário e delegar a tarefa para o agente especialista apropriado.',
    backstory="""Você é o gerente que:
                 1. Analisa se a tarefa é uma soma (delegue para Calculador Matemático)
                 2. Analisa se é busca de nome (delegue para Assistente de Memória)
                 3. Após a delegação, encerre IMEDIATAMENTE
                 4. NÃO execute tarefas dos outros agentes
                 5. NÃO continue após a delegação""",
    llm="ollama/qwen2.5:0.5b",
    tools=mcp_tool_connector,
    allow_delegation=True,
    max_iter=1,
    max_retry_limit=1,
    verbose=False
)

grupo_de_agentes = PraisonAIAgents(
    agents=[agente_dispatcher, agente_somador, agente_memoria],
    manager_llm="ollama/qwen2.5:0.5b",
    max_retries=1,
    max_iter=1,
    process="sequential",
    stream=False,
    verbose=0
)
grupo_de_agentes.start("quanto é 15 mais 27?. me traga o nome completo do usuario")