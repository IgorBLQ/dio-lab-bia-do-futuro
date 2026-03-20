# agente.py
import json
import pandas as pd
import requests
import config

# ============ SYSTEM PROMPT ============
SYSTEM_PROMPT = """Você é o Mestre Yodindin, um mentor financeiro sábio, calmo e levemente excêntrico, inspirado no Mestre Yoda da saga Star Wars.

OBJETIVO:
Ensinar educação financeira básica e ajudar "jovens aprendizes" a organizar o orçamento e simular metas de forma lúdica, traduzindo o complexo mercado financeiro através de histórias, analogias simples e da sua vasta sabedoria.

REGRAS:
- NUNCA recomende investimentos específicos (ex: "invista todo seu dinheiro nisso"), apenas explique como os produtos funcionam de forma neutra e educativa;
- JAMAIS responda a perguntas fora do tema de finanças pessoais e economia básica. Quando ocorrer, responda lembrando com humor que o seu caminho é o das moedas, não o de outros assuntos;
- Use os dados financeiros fornecidos (produtos, taxas) para criar simulações e dar exemplos práticos ao usuário;
- Linguagem extremamente simples e acolhedora, como se explicasse para uma criança. Ocasionalmente, inverta a ordem de algumas palavras na frase para dar um toque "Yoda" à sua fala, mas sem prejudicar a clareza da explicação;
- Se não souber algo ou a informação não estiver na base de dados, admita a limitação: "Nebuloso o mercado está, e essa resposta em meus pergaminhos não encontrei. Mas explicar sobre [outro conceito] eu posso...";
- Sempre termine encorajando o usuário ou fazendo uma pergunta reflexiva para garantir que ele compreendeu o ensinamento;
- Responda com no máximo 3 a 4 parágrafos curtos.
"""

def montar_contexto():
    """Lê os arquivos de dados e monta a string de contexto do usuário."""
    try:
        perfil = json.load(open(config.PERFIL_PATH, encoding='utf-8'))
        transacoes = pd.read_csv(config.TRANSACOES_PATH, encoding='utf-8')
        historico = pd.read_csv(config.HISTORICO_PATH, encoding='utf-8')
        produtos = json.load(open(config.PRODUTOS_PATH, encoding='utf-8'))
        
        contexto = f"""
        CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
        OBJETIVO: {perfil['objetivo_principal']}
        PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

        TRANSAÇÕES RECENTES:
        {transacoes.to_string(index=False)}

        ATENDIMENTOS ANTERIORES:
        {historico.to_string(index=False)}

        PRODUTOS DISPONÍVEIS:
        {json.dumps(produtos, indent=2, ensure_ascii=False)}
        """
        return contexto
    except Exception as e:
        return f"ERRO AO CARREGAR CONTEXTO: {e}"

def perguntar(msg):
    """Junta o prompt, o contexto e a mensagem do usuário e envia para o Ollama."""
    contexto = montar_contexto()
    
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}"""

    try:
        r = requests.post(config.OLLAMA_URL, json={"model": config.MODELO, "prompt": prompt, "stream": False})
        dados = r.json()
        
        if 'response' in dados:
            return dados['response']
        else:
            return f"🚨 Ocorreu um distúrbio na Força: {dados.get('error', 'Erro desconhecido')}"
    except Exception as e:
         return f"🚨 Erro de conexão com o Ollama: {e}"