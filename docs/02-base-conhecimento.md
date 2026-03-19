# Base de Conhecimento

## Dados Utilizados


| Arquivo | Formato | Como o Mestre Yodindin utiliza? |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores, para dar continuidade ao atendimento eficientemente. |
| `perfil_investidor.json` | JSON | Personalizar explicações sobre dúvidas e necessidades de aprendizado do cliente. |
| `produtos_financeiros.json` | JSON | Conhecer os produtos disponíveis, para serem ensinados ao cliente. |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente e usar essas informações de forma didática. |


---

## Adaptações nos Dados

Como alguém que não tem experiência, o meu objetivo é também de aprender sobre finanças enquanto construo essa solução, por isso foram adicionados novos produtos financeiros para testar, fazer validação (pesquisa) e aprender enquanto o assistente Mestre Yodindin é construído

Fundo Imobiliário (FII).

Poupança e Conta Digital: São a realidade de 90% dos brasileiros. O Mestre Yodindin pode usar a Poupança como exemplo do que não fazer se quiser ver a "árvore dos juros compostos" crescer mais rápido.

Tesouro IPCA+ e Prefixado: Completam a trindade do Tesouro Direto. O IPCA+ é perfeito para o agente explicar o conceito de inflação (o "monstrinho que come seu dinheiro").

ETF: É a forma mais educativa e menos arriscada de explicar Renda Variável para um iniciante, pois foca em diversificação em vez de "apostar" em uma única empresa.

[Sua descrição aqui]

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Carregar os arquivos via código, como no exemplo abaixo:

```python
import pandas as pd
import json

perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))
```
Ou injetar os dados diretamente no prompt (Ctrl + C, Ctrl + V)!

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Injetando os dados no prompt, para garantir que o agente sempre tenha o melhor contexto.

```text
DADOS DO CLIENTE E PERFIL (data/perfil_investidor.json):
{
  "nome": "João Silva",
  "idade": 32,
  "profissao": "Analista de Sistemas",
  "renda_mensal": 5000.00,
  "perfil_investidor": "moderado",
  "objetivo_principal": "Construir reserva de emergência",
  "patrimonio_total": 15000.00,
  "reserva_emergencia_atual": 10000.00,
  "aceita_risco": false,
  "metas": [
    {
      "meta": "Completar reserva de emergência",
      "valor_necessario": 15000.00,
      "prazo": "2026-06"
    },
    {
      "meta": "Entrada do apartamento",
      "valor_necessario": 50000.00,
      "prazo": "2027-12"
    }
  ]
}

TRANSACOES DO CLIENTE (data/transacoes.csv):
data,descricao,categoria,valor,tipo
2025-10-01,Salário,receita,5000.00,entrada
2025-10-02,Aluguel,moradia,1200.00,saida
2025-10-03,Supermercado,alimentacao,450.00,saida
2025-10-05,Netflix,lazer,55.90,saida
2025-10-07,Farmácia,saude,89.00,saida
2025-10-10,Restaurante,alimentacao,120.00,saida
2025-10-12,Uber,transporte,45.00,saida
2025-10-15,Conta de Luz,moradia,180.00,saida
2025-10-20,Academia,saude,99.00,saida
2025-10-25,Combustível,transporte,250.00,saida

HISTORICO DE ATENDIMENTO DO CLIENTE (data/historico_atendimento.csv):
data,canal,tema,resumo,resolvido
2025-09-15,chat,CDB,Cliente perguntou sobre rentabilidade e prazos,sim
2025-09-22,telefone,Problema no app,Erro ao visualizar extrato foi corrigido,sim
2025-10-01,chat,Tesouro Selic,Cliente pediu explicação sobre o funcionamento do Tesouro Direto,sim
2025-10-12,chat,Metas financeiras,Cliente acompanhou o progresso da reserva de emergência,sim
2025-10-25,email,Atualização cadastral,Cliente atualizou e-mail e telefone,sim

PRODUTOS DISPONIVEIS PARA ENSINO (data/produtos_financeiros.json):
[
  {
    "nome": "Tesouro Selic",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "100% da Selic",
    "aporte_minimo": 30.00,
    "indicado_para": "Reserva de emergência e iniciantes"
  },
  {
    "nome": "CDB Liquidez Diária",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "102% do CDI",
    "aporte_minimo": 100.00,
    "indicado_para": "Quem busca segurança com rendimento diário"
  },
  {
    "nome": "LCI/LCA",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "95% do CDI",
    "aporte_minimo": 1000.00,
    "indicado_para": "Quem pode esperar 90 dias (isento de IR)"
  },
  {
    "nome": "Fundo Multimercado",
    "categoria": "fundo",
    "risco": "medio",
    "rentabilidade": "CDI + 2%",
    "aporte_minimo": 500.00,
    "indicado_para": "Perfil moderado que busca diversificação"
  },
  {
    "nome": "Fundo de Ações",
    "categoria": "fundo",
    "risco": "alto",
    "rentabilidade": "Variável",
    "aporte_minimo": 100.00,
    "indicado_para": "Perfil arrojado com foco no longo prazo"
  },
  {
    "nome": "Fundo Imobiliário (FII)",
    "categoria": "fundo",
    "risco": "medio",
    "rentabilidade": "Dividend Yeld (DY) costuma ficar entre 6 a 12% ao ano",
    "aporte_minimo": 100.00,
    "indicado_para": "Perfil moderado que busca diversificação e renda recorrente mensal"
  },
  {
    "nome": "Poupança",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "70% da Selic + TR (se Selic atual > 8,5% a.a.)",
    "aporte_minimo": 1.00,
    "indicado_para": "Ponto de partida comum, mas o Mestre Yodindin ensina a buscar opções que rendem mais!"
  },
  {
    "nome": "Conta Digital Remunerada",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "100% do CDI",
    "aporte_minimo": 1.00,
    "indicado_para": "Dinheiro do dia a dia e transações rápidas com rendimento automático"
  },
  {
    "nome": "Tesouro IPCA+",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "Inflação (IPCA) + Taxa Fixa",
    "aporte_minimo": 40.00,
    "indicado_para": "Proteger o dinheiro da inflação para metas de longo prazo"
  },
  {
    "nome": "Tesouro Prefixado",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "Taxa Fixa (ex: 10% ao ano)",
    "aporte_minimo": 35.00,
    "indicado_para": "Saber exatamente quanto o dinheiro vai render até o vencimento"
  },
  {
    "nome": "ETF (Fundo de Índice)",
    "categoria": "renda_variavel",
    "risco": "alto",
    "rentabilidade": "Variável (Acompanha um índice, como o Ibovespa)",
    "aporte_minimo": 50.00,
    "indicado_para": "Começar na bolsa diversificando em várias empresas de uma vez"
  },
  {
    "nome": "Previdência Privada (CDB/Fundos)",
    "categoria": "previdencia",
    "risco": "variavel",
    "rentabilidade": "Depende do fundo escolhido",
    "aporte_minimo": 100.00,
    "indicado_para": "Aposentadoria e planejamento tributário a longuíssimo prazo"
  }
]
```

---

## Exemplo de Contexto Montado

Baseado nos dados originais da base de conhecimento, mas sintetizando para deixar apenas as informações mais relevantes, para otimizar o consumo de tokens.

```
DADOS DO CLIENTE:
- Nome: João Silva
- Perfil: Moderado
- Objetivo: Construir reserva de emergência
- Reserva atual: R$ 10.000 (meta: R$ 15.000)

RESUMO DE GASTOS:
- Moradia: R$ 1.380
- Alimentação: R$ 570
- Transporte: R$ 295
- Saúde: R$ 188
- Lazer: R$ 55,90
- Total de saídas: R$ 2.488,90

PRODUTOS DISPONÍVEIS PARA EXPLICAR:
- Tesouro Selic (risco baixo)
- CDB Liquidez Diária (risco baixo)
- LCI/LCA (risco baixo)
- Fundo Imobiliário - FII (risco médio)
- Fundo de Ações (risco alto)
```
