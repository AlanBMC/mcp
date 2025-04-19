# MCP - Projeto de Orquestração de Agentes e Servidores

## Descrição


O projeto MCP (Model Context Protocol) é visando o aprendizado desta nova tecnologia utilizando bibliotecas atuais em python, ferramentas que usam servers de serviços que são gerenciados por agentes-llm's. Atualmente irei integrar pelo menos 2 serves (a proposta é escalar)

## Arquitetura geral (Planejamento)

Arquivo central de agentes que usam tools mcps que que vão estar depender de node- ou do proprio servidor configurado na pasta servers_mcp, agentes tambem serão alimentados por bancos dados(RAG) via api( Talvez podemos usar um GraphQL ).


##  Ferramentas

MCP's servers que podem ser encontrados de diversas formas como no github buscando por `MCP SERVER`.
`praisonaiagents` que integra muito bem com ferramentas mcp e ollama.
Confira as dependencias em `requirements.txt`.



## Integrando IA

Voce pode conferir a documentação do `praison` em https://docs.praison.ai/mcp/airbnb

## Adendo Importante (Configuração de Ollama Remoto):

Com base em testes recentes (Abril de 2025), ao integrar com um servidor Ollama remoto (em outra máquina na sua rede, como um Umbrel), pode ser necessário configurar duas variáveis de ambiente no terminal onde você executará o script praison antes de iniciá-lo.

Isso ocorre porque a biblioteca subjacente (litellm) pode precisar de ambas as variáveis para direcionar corretamente todas as suas chamadas internas para o servidor remoto:
Bash

# Defina ANTES de rodar seu script Python
export OLLAMA_HOST='http://<IP_DO_SEU_SERVIDOR_OLLAMA>:<PORTA>'
export OLLAMA_API_BASE='http://<IP_DO_SEU_SERVIDOR_OLLAMA>:<PORTA>'

Substitua <IP_DO_SEU_SERVIDOR_OLLAMA>:<PORTA> pelo endereço correto do seu servidor Ollama (ex: http://192.168.1.7:11434). Definir apenas OLLAMA_HOST pode resultar em erros de "model not found" devido a chamadas internas que falham em localizar o servidor correto sem OLLAMA_API_BASE.

## Como Iniciar o Projeto

1.  **Clonar o Repositório:**
    ```bash
    git clone https://github.com/AlanBMC/mcp.git
    cd mcp
    python -m venv venv
    pip install -r requirements.txt
    
    ```
     * No Windows (PowerShell): `.\venv\Scripts\Activate.ps1`
    * No Windows (CMD): `.\venv\Scripts\activate.bat`
    * No Linux / macOS: `source venv/bin/activate`
