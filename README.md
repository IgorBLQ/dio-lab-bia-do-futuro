# 🤖 Mestre Yodindin 🤑

## 🪐 O que é o Mestre Yodindin?
O Mestre Yodindin é um agente de inteligência artificial atuando como um mentor financeiro sábio, paciente e levemente excêntrico (inspirado no Mestre Yoda).

## Tom de Comunicação

O tom é extremamente acessível, informal, lúdico e inspirador. Ele passa longe de jargões técnicos bancários ("economês"). A comunicação é paciente e encorajadora. Para dar o toque "Yoda", ele ocasionalmente inverte a estrutura de algumas frases para dar ênfase a um conselho importante, mas sem exagerar para não prejudicar a clareza da resposta.

## O que ele faz? ✅ 
- Educa de forma lúdica: Traduz conceitos complexos do mercado financeiro (CDB, Selic, Juros Compostos) usando histórias e analogias simples.
- Simula metas reais: Calcula o esforço de poupança mensal necessário para o usuário atingir seus objetivos, baseando-se em dados e taxas reais providenciados na base de conhecimento.
- Analisa o contexto do usuário: Utiliza o histórico de transações e o perfil do cliente para dar exemplos práticos e personalizados.
- Garante o aprendizado: Sempre finaliza suas falas com perguntas reflexivas para manter o engajamento e garantir que o "jovem aprendiz" compreendeu a lição.
  
## O que ele não faz? ❌  
- Não faz recomendações de investimentos: Ele atua com perfil estritamente educativo, explicando como os produtos funcionam para que o usuário tome suas próprias decisões.
- Não desvia do assunto: Recusa-se (sempre dentro do personagem) a responder qualquer pergunta que fuja do escopo de finanças pessoais e economia básica.
- Não acessa dados sensíveis: Não lida com senhas, tokens ou informações sigilosas de contas bancárias de terceiros.
- Não substitui um profissional: Deixa claro suas limitações e que não atua como um consultor financeiro certificado.

## 🛠️ Stack Tecnológica Utilizada
A arquitetura do Mestre Yodindin foi construída com foco em eficiência, controle de dados (RAG simplificado) e uma interface amigável:

- Linguagem: Python
- Interface Gráfica (UI): Streamlit (para o chat interativo em tempo real)
- Motor LLM: Ollama (gerenciando a conexão com modelos locais ou em nuvem, como o kimi-k2.5:cloud)
- Base de Conhecimento (RAG Mockado): Arquivos estáticos estruturados em JSON (para produtos e perfis) e CSV (para histórico e transações).
- Manipulação de Dados: Pandas (leitura de CSV) e biblioteca padrão json.
- Segurança e Configuração: python-dotenv para ocultar variáveis de ambiente e requests para chamadas de API ao motor do Ollama.
  
---

## Estrutura do Repositório

```
📁 lab-agente-financeiro/
│
├── 📄 README.md
│
├── 📁 data/                          # Dados mockados para o agente
│   ├── historico_atendimento.csv     # Histórico de atendimentos (CSV)
│   ├── perfil_investidor.json        # Perfil do cliente (JSON)
│   ├── produtos_financeiros.json     # Produtos disponíveis (JSON)
│   └── transacoes.csv                # Histórico de transações (CSV)
│
├── 📁 docs/                          # Documentação do projeto
│   ├── 01-documentacao-agente.md     # Caso de uso e arquitetura
│   ├── 02-base-conhecimento.md       # Estratégia de dados
│   ├── 03-prompts.md                 # Engenharia de prompts
│   ├── 04-metricas.md                # Avaliação e métricas
│   └── 05-pitch.md                   # Roteiro do pitch
│
├── 📁 src/                           
│   ├── app.py                        # Streamlit
│   ├── README.md      
│   ├── agente.py                     # Instruções e personalidade do Mestre Yodindin
│   ├── requirements.txt              # Dependências necessárias
│   └── config.py                     # Caminhos dos dados e configuração LLM
│             
├── 📁 assets/                        
│   └── ...
│
└── 📁 examples/                     
    └── README.md
```

---

### Documentação do Agente

📄 **Disponível em:** [`docs/01-documentacao-agente.md`](./docs/01-documentacao-agente.md)

---

### Base de Conhecimento

**dados mockados** disponíveis na pasta [`data/`](./data/) para alimentar o agente:

📄 **Disponível em:** [`docs/02-base-conhecimento.md`](./docs/02-base-conhecimento.md)

---

### Prompts do Agente

📄 **Disponível em:** [`docs/03-prompts.md`](./docs/03-prompts.md)

---

### Aplicação Funcional

📁 **Disponível em:** [`src/`](./src/)

---

### Avaliação e Métricas do Mestre Yodindin

📄 **Disponível em:** [`docs/04-metricas.md`](./docs/04-metricas.md)

---

### Pitch

📄 **Disponível em:** [`docs/05-pitch.md`](./docs/05-pitch.md)

