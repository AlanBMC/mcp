# MCP - Projeto de Orquestração de Agentes e Servidores

## Descrição

O projeto MCP (Model Context Protocol) é visando o aprendizado desta nova tecnologia utilizando bibliotecas atuais em python, ferramentas que usam servers de serviços que são gerenciados por agentes-llm's. Atualmente irei integrar pelo menos 2 serves


## Arquitetura geral (Planejamento)

arquivo central de agentes que usam tools mcps que que vão estar depender de node- ou do proprio servidor configurado na pasta servers_mcp, agentes tambem serão alimentados por bancos dados(RAG) via api( Talvez podemos usar um GraphQL ). 


##  Ferramentas

MCP's servers que podem ser encontrados de diversas formas como no github buscando por `MCP SERVER`,
praisonaiagents que integra  muito bem com ferramentas mcp e ollama.
confira as dependencias em `requirements.txt`


# Integrando IA

Voce pode conferir a documentação do `praison` em https://docs.praison.ai/mcp/airbnb
