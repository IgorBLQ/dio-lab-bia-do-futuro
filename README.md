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

### 1. Documentação do Agente

Definindo **o que** o agente faz e **como** ele funciona:

- **Caso de Uso:** Qual problema financeiro ele resolve? (ex: consultoria de investimentos, planejamento de metas, alertas de gastos)
- **Persona e Tom de Voz:** Como o agente se comporta e se comunica?
- **Arquitetura:** Fluxo de dados e integração com a base de conhecimento
- **Segurança:** Como evitar alucinações e garantir respostas confiáveis?

📄 **Template:** [`docs/01-documentacao-agente.md`](./docs/01-documentacao-agente.md)

---

### 2. Base de Conhecimento

**dados mockados** disponíveis na pasta [`data/`](./data/) para alimentar o agente:

| Arquivo | Formato | Descrição |
|---------|---------|-----------|
| `transacoes.csv` | CSV | Histórico de transações do cliente |
| `historico_atendimento.csv` | CSV | Histórico de atendimentos anteriores |
| `perfil_investidor.json` | JSON | Perfil e preferências do cliente |
| `produtos_financeiros.json` | JSON | Produtos e serviços disponíveis |

Pode-se adaptar ou expandir esses dados conforme seu caso de uso.

📄 **Template:** [`docs/02-base-conhecimento.md`](./docs/02-base-conhecimento.md)

---

### 3. Prompts do Agente

Documentados os prompts que definem o comportamento do agente:

- **System Prompt:** Instruções gerais de comportamento e restrições
- **Exemplos de Interação:** Cenários de uso com entrada e saída esperada
- **Tratamento de Edge Cases:** Como o agente lida com situações limite

📄 **Template:** [`docs/03-prompts.md`](./docs/03-prompts.md)

---

### 4. Aplicação Funcional

Desenvolva um **protótipo funcional** do agente:

- Chatbot interativo 
- Integração com LLM (via API ou modelo local)
- Conexão com a base de conhecimento

📁 **Pasta:** [`src/`](./src/)

---

### 5. Avaliação e Métricas

Descreva como está a avaliação da qualidade do agente:

**Métricas Sugeridas:**
- Precisão/assertividade das respostas
- Taxa de respostas seguras (sem alucinações)
- Coerência com o perfil do cliente

📄 **Template:** [`docs/04-metricas.md`](./docs/04-metricas.md)

---

### 6. Pitch

Um **pitch de 3 minutos** (estilo elevador) apresentando:

- Qual problema seu agente resolve?
- Como ele funciona na prática?
- Por que essa solução é inovadora?

📄 **Template:** [`docs/05-pitch.md`](./docs/05-pitch.md)

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
│   ├── app.py
│   ├── README.md      
│   ├── app.py
│   ├── requirements.txt         
│   └── config.py
│             
├── 📁 assets/                        
│   └── ...
│
└── 📁 examples/                     
    └── README.md
```

---
