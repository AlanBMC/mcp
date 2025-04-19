from praisonaiagents import Agent, MCP
import os 

playwright_mcp_command = "npx @playwright/mcp@latest --headless"

playwright_agent = Agent(
    # Instruções atualizadas para refletir o fluxo de snapshot
    instructions="""Você é um assistente que automatiza o navegador usando Playwright. Você deve primeiro usar a ferramenta 'browser_snapshot' para obter a estrutura acessível da página atual. Depois, analise o snapshot para encontrar a referência exata ('ref') do elemento desejado e use as ferramentas de interação (como 'browser_click', 'browser_type') passando essa 'ref'.""",
    llm="ollama/qwen2.5:0.5b", 
    tools=MCP(playwright_mcp_command)
)

tarefa = """
1. Use a ferramenta 'browser_navigate' para ir até 'https://github.com/login'.
2. Use a ferramenta 'browser_snapshot' para obter a estrutura da página de login.
3. Analise o snapshot, encontre a referência ('ref') do campo de input para 'Username or email address'.
4. Use a ferramenta 'browser_type' com a 'ref' encontrada para digitar 'teste@exemplo.com' nesse campo.
"""


print(f"Iniciando agente com a tarefa: {tarefa}")
playwright_agent.start(tarefa)

print("Agente concluiu a tarefa.")