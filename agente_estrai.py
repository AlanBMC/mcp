from praisonaiagents import Agent, MCP
import os # Para variáveis de ambiente do Ollama, se necessário

# Comando CORRETO para iniciar o servidor MCP usando 'uv'
# Pré-requisitos: 'uv' instalado e 'uv tool install web-browser-mcp-server' executado com sucesso
web_browser_mcp_command = "uv tool run web-browser-mcp-server"

# Crie o agente
web_agent = Agent(
    instructions="""Você é um assistente que usa a ferramenta 'browse_webpage' para acessar URLs e extrair conteúdo web usando seletores CSS, se fornecidos.""",
    llm="ollama/qwen2.5:0.5b", # Ou outro LLM
                                 # Lembre-se do OLLAMA_HOST/OLLAMA_API_BASE se usar Ollama remoto!
    tools=MCP(web_browser_mcp_command)
    # Nota: A documentação menciona uma variável de ambiente REQUEST_TIMEOUT=30.
    # Não está claro se o MCP() do praisonaiagents passa env vars, mas pode ser algo a investigar se houver timeouts.
)

# Exemplo de tarefa focada na ferramenta 'browse_webpage'
# (Esta MCP parece oferecer principalmente essa ferramenta)
tarefa = "Use a ferramenta browse_webpage para acessar a URL 'https://docs.praison.ai/' e extrair o conteúdo dos elementos h1 e p (parágrafos)."
# Ou um exemplo mais específico com seletores:
# tarefa = 'Use browse_webpage para acessar "https://github.com/blazickjp/web-browser-mcp-server" e extrair o texto com o seletor "h1" e também com o seletor ".markdown-body p"'


print(f"Iniciando agente com a tarefa: {tarefa}")
web_agent.start(tarefa)

print("Agente concluiu a tarefa.")