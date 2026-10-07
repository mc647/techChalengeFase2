# Tech Challenge — Fase 2 | POSTECH Data Analytics

---

## 1. Identificação

| Campo | Valor |
|---|---|
| Turma | POSTECH - BB |
| Grupo | 35 |
| Data de entrega | 10/10/2026 |

### Integrantes

| Nome completo | RM | E-mail |
|---|---|---|
| Alexandre dos Anjos de Jesus  | RM377732 | dosanjosdejesus@gmail.com |
| Didan Junqueira Ribeiro ALEXANDRE DOS ANJOS DE JESUS | RM377825 | didanunb@gmail.com |
| Fernanda Arruda Pimenta da Silva | RM377753 | arruda.fernanda@gmail.com |
| Nathalia Fernanda dos Santos Gelais |  | nathaliafersantos@gmail.com |
| Guilherme Caetano Peron | RM377756 | caetano.peron@bb.com.br |

---

## 2. Links da entrega

| Item | Link |
|---|---|
| Repositório | https://github.com/mc647/techChalengeFase2 |
| Vídeo executivo (≤ 5 min) | <!-- PREENCHER: YouTube não listado / Drive com acesso liberado --> |
| Apresentação | <!-- PREENCHER: link do arquivo em `docs/` ou Drive --> |

---

## 3. O problema

O objetivo deste projeto é desenvolver uma solução de **Machine Learning supervisionado** capaz de identificar perfis de **bons e maus pagadores**, utilizando informações pessoais, financeiras e cadastrais dos solicitantes.

### Variável alvo

<!-- PREENCHER: qual é a variável alvo, como foi definida e — se houve binarização —
     qual limiar foi adotado e por quê. Justifique com base na distribuição das classes. -->

### Dataset

| Campo | Valor |
|---|---|
| Fonte | https://www.kaggle.com/datasets/rikdifos/credit-card-approval-prediction/data |
| Linhas × colunas | <!-- PREENCHER --> |
| Período / versão | <!-- PREENCHER --> |
| Licença de uso | CC0: Public Domain |

Descrição das variáveis:

### Dicionário de dados application_record original
___
| Variável | Tipo (Dtype) | Descrição | Exemplo de Valores |
| :--- | :--- | :--- | :--- |
| `ID` | `int64` | Identificador único do cliente. | 5008804, 5008805, 5008806, ... |
| `CODE_GENDER` | `str` | Gênero do cliente. | F, M |
| `FLAG_OWN_CAR` | `str` | Flag indicando se o cliente possui carro. | N (Não), Y (Sim) |
| `FLAG_OWN_REALTY` | `str` | Flag indicando se o cliente possui propriedades imobiliárias. | N (Não), Y (Sim) |
| `CNT_CHILDREN` | `int64` | Quantidade de filhos. | 0, 1, ..., 19 |
| `AMT_INCOME_TOTAL` | `float64` | Renda anual. | 26100.0, 427500.0, ... |
| `NAME_INCOME_TYPE` | `str` | Nome do tipo de renda. | Working, Commercial associate, Pensioner, State servant, Student |
| `NAME_EDUCATION_TYPE` | `str` | Nome escolaridade. | Secondary / secondary special, Higher education, Incomplete higher, Lower secondary, Academic degree |
| `NAME_FAMILY_STATUS` | `str` | Nome da situação matrimonial. | Married, Single / not married, Civil marriage, Separated, Widow |
| `NAME_HOUSING_TYPE` | `str` | Nome do tipo de residência. | House / apartment, With parents, Municipal apartment, Rented apartment, Office apartment, Co-op apartment |
| `DAYS_BIRTH` | `int64` | Quantidade de dias de nascido. Na data de referência (0), -1 é o dia anterior ao da data de referência. | -7849, -32765, ... |
| `DAYS_EMPLOYED` | `int64` | Quantidade de dias empregado (Negativo). Positivo significa dias desempregado. | -2610.0, 4275.0, ... |
| `FLAG_MOBIL` | `int64` | Tem celular. | 0 (Não), 1 (Sim) |
| `FLAG_WORK_PHONE` | `int64` | Tem telefone do trabalho. | 0 (Não), 1 (Sim) |
| `FLAG_PHONE` | `int64` | Tem telefone fixo. | 0 (Não), 1 (Sim) |
| `FLAG_EMAIL` | `int64` | Tem e-mail. | 0 (Não), 1 (Sim) |
| `OCCUPATION_TYPE` | `str` | Ocupação. | Managers, Drivers, ... |
| `CNT_FAM_MEMBERS` | `int64` | Tamanho da família. | 0, 1, ..., 20 |

---

## 4. Como reproduzir

```bash
git clone https://github.com/mc647/techChalengeFase2
cd <NOME_DO_REPOSITORIO>

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

pip install -r requirements.txt
jupyter notebook
```

Baixe o dataset e coloque o arquivo bruto em `data/raw/` (os dados **não** são versionados —
veja `data/README.md`).

Depois execute os notebooks nesta ordem:

| # | Notebook | O que faz |
|---|---|---|
| 1 | `notebooks/01_eda.ipynb` | Análise exploratória |
| 2 | `notebooks/02_preprocessamento.ipynb` | Limpeza, escala e feature engineering |
| 3 | `notebooks/03_modelagem.ipynb` | Treino e comparação dos modelos |
| 4 | `notebooks/04_avaliacao.ipynb` | Métricas, importância de variáveis e conclusões |

**Semente fixa:** `RANDOM_STATE = 42`, declarada na primeira célula de cada notebook.
Rodar os notebooks na ordem acima, a partir de um ambiente limpo, deve reproduzir
exatamente os números da seção 5.

---

## 5. Resultados

| Modelo | Acurácia | Precisão | Recall | F1 | AUC-ROC |
|---|---|---|---|---|---|
| <!-- PREENCHER --> | | | | | |
| | | | | | |

**Modelo escolhido:** <!-- PREENCHER --> — <!-- PREENCHER: por quê. -->

**Métricas priorizadas:** <!-- PREENCHER: justifique a escolha considerando o
     desbalanceamento de classes e o custo de cada tipo de erro no contexto do negócio. -->

---

## 6. Principais conclusões

<!-- PREENCHER: 3 a 5 conclusões em linguagem de negócio.
     Inclua quais variáveis mais influenciam o resultado e o que isso significa
     na prática para quem vai usar o modelo. -->

1.
2.
3.

### Limitações e próximos passos

<!-- PREENCHER -->

---

## 7. Estrutura do repositório

```
.
├── data/          dados brutos (raw) e tratados (processed) — não versionados
├── notebooks/     análise em ordem numerada
└── docs/          apresentação executiva
```

Detalhes e convenções em [`ESTRUTURA.md`](ESTRUTURA.md).
Antes de enviar, percorra o [`CHECKLIST.md`](CHECKLIST.md).

---

## 8. Tecnologias

<!-- PREENCHER: Python 3.11, pandas, scikit-learn, ... -->
# techChalengeFase2
