from praisonaiagents import Agent, MCP


search_agent = Agent(
    instructions="""Você é um assistente especializado em busca web que:
    1. Deve usar puppeteer_navigate para acessar o Google
    2. Deve usar puppeteer_type para digitar a busca
    3. Deve usar puppeteer_click para clicar em elementos
    4. Deve usar puppeteer_evaluate para extrair informações
    5. Deve organizar e apresentar os resultados de forma clara
    """,
    llm="ollama/qwen2.5:0.5b",
    tools=MCP("npx -y @modelcontextprotocol/server-puppeteer")
)

search_agent.start("me mostre os principais sites de notícias do Brasil")