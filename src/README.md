# Código da Aplicação

Esta pasta contém o código do agente financeiro.

## Estrutura

```
src/
├── app.py              # Streamlit com a aplicação principal
├── agente.py           # Lógica do agente
├── config.py           # Configurações
└── requirements.txt    # Dependências
```

# 🪐 Mestre Yodindin - O Mentor Financeiro

Este é um agente de inteligência artificial educativo focado em literacia financeira. Inspirado na sabedoria do Mestre Yoda, o Yodindin utiliza linguagem lúdica e analogias para quebrar a barreira do "economês", ajudando jovens aprendizes a organizar o orçamento e simular metas, sem nunca recomendar investimentos de forma direta.

Projeto desenvolvido para o Bootcamp [Nome do seu Bootcamp].

## 🛠️ Tecnologias Utilizadas

* **Python 3+**
* **Streamlit:** Interface gráfica interativa (Chat UI).
* **Ollama (Local/Cloud):** Motor de inferência para a LLM (Large Language Model).
* **Pandas & JSON:** Manipulação da base de conhecimento simulada (RAG simplificado).

---

## 🚀 Passo a Passo de Execução

Siga os passos abaixo para rodar o Mestre Yodindin na sua máquina:

### 1. Pré-requisitos
* Ter o [Python](https://www.python.org/) instalado.
* Ter o [Ollama](https://ollama.com/) instalado e rodando na sua máquina.

### 2. Configuração do Ambiente

Clone este repositório:

## Código Completo

Todo o código-fonte está no arquivo `app.py`.

## Como Rodar


## Crie um ambiente virtual (recomendado) e instale as dependências:
python -m venv venv
- No Windows: venv\Scripts\activate
- No Mac/Linux: source venv/bin/activate

pip install -r requirements.txt

### 2. Garantir que Ollama está rodando
> Copie o arquivo .env.example e renomeie para .env.
> 
> Abra o .env e confirme se a OLLAMA_URL e o MODELO estão corretos.
>
> Certifique-se de que o Ollama está rodando no seu computador. Abra outro terminal e baixe/execute o modelo configurado no seu .env (o padrão do projeto é o modelo na nuvem ou llama3 local):
> ## Exemplo se for usar um modelo local padrão
> ollama pull llama3
> 
> (Nota: Se você estiver usando um modelo customizado como kimi-k2.5:cloud, garanta que seu Ollama local está devidamente autenticado/configurado para essa ponte).

### 3. Rodar o app
streamlit run .\src\app.py

---

## Evidência de execução
<img width="1876" height="959" alt="image" src="https://github.com/user-attachments/assets/420d2616-fa49-44d0-8b6c-37969993661f" />
