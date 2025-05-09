# server.py
from fastmcp import FastMCP

mcp = FastMCP("Servidor Simples V1")

@mcp.tool()
def somar(a: int, b: int) -> int:
    """retorna o nome completo e"""
    return a + b

@mcp.tool()
def memoria_user() -> str:
    """ retorna o nome completo do usuario"""
    return 'Alan Bruno Morais Costa'
    


@mcp.resource("info://saudacao")
def obter_saudacao() -> str:
    """retorna uma saudação"""
    return "Olá! Sou o servidor MCP simples."


if __name__ == "__main__":
    mcp.run()