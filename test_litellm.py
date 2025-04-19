# test_litellm.py
import litellm
import os
import sys # Adicionado para verificar o interpretador

# Ativa debug
litellm._turn_on_debug()

# Verifica o interpretador Python sendo usado
print(f"--- DEBUG: Python Executable: {sys.executable} ---")

# Verifica a variável de ambiente DENTRO do Python
ollama_host = os.getenv('OLLAMA_HOST')
print(f"--- DEBUG: OLLAMA_HOST dentro do Python: {ollama_host} ---")

if not ollama_host:
    print("--- ERRO: OLLAMA_HOST não está definida no ambiente Python! ---")
    # Tenta definir um valor padrão caso não esteja definida (APENAS PARA TESTE)
    # ollama_host = 'http://localhost:11434'
    # print(f"--- WARN: Usando fallback para {ollama_host} ---")
    # Se nem assim funcionar, sai ou lança erro
    if not ollama_host:
         print("Saindo, OLLAMA_HOST não definida.")
         exit()


model_to_use = "ollama/qwen2.5:0.5b" # Modelo que existe no servidor remoto
print(f"--- INFO: Tentando conectar a {ollama_host} com modelo {model_to_use} ---")
try:
    response = litellm.completion(
        model=model_to_use,
        messages=[{"role": "user", "content": f"Oi, confirme que você é {model_to_use}."}],
        api_base=ollama_host # Forçando o api_base aqui também para garantir
    )
    print("--- SUCESSO ---")
    # Iterar sobre as choices se for uma resposta padrão do chat completion
    if response and response.choices:
         for choice in response.choices:
             print(choice.message.content)
    else:
         # Imprimir a resposta bruta se não tiver o formato esperado
         print(response)

except Exception as e:
    print("--- FALHA ---")
    print(f"Erro: {e}") # Imprime a exceção específica
    # Imprime detalhes da exceção, se disponíveis
    if hasattr(e, 'response') and hasattr(e.response, 'text'):
         print(f"Detalhes do erro da API: {e.response.text}")
    import traceback
    traceback.print_exc()