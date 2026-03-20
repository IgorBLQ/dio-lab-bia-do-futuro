import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# ============ CONFIGURAÇÕES DA LLM ============
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
MODELO = os.getenv("MODELO", "llama3") # Coloquei llama3 como um fallback padrão

# ============ CAMINHOS DOS DADOS ============
DATA_DIR = "./data"
PERFIL_PATH = f"{DATA_DIR}/perfil_investidor.json"
TRANSACOES_PATH = f"{DATA_DIR}/transacoes.csv"
HISTORICO_PATH = f"{DATA_DIR}/historico_atendimento.csv"
PRODUTOS_PATH = f"{DATA_DIR}/produtos_financeiros.json"