# 🐚 Regressão Linear para Predição da Idade do Abalone

Projeto de **Machine Learning** (regressão linear múltipla) que prevê a idade de abalones a partir de medições físicas, evitando o método manual e demorado de contagem de anéis na casca. Inclui análise exploratória, visualizações e avaliação de modelo com `scikit-learn`.

> Trabalho acadêmico (UFMS) — Ciência de Dados / Aprendizado de Máquina.

## 🎯 Objetivo
Determinar a idade do abalone (`Age = Rings + 1.5`) usando 8 medições físicas fáceis de obter, em vez de contar anéis ao microscópio. Avaliar a viabilidade de um modelo linear para automatizar a predição.

## 📊 Dataset
[Abalone Data Set — UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/1/abalone) (incluído: `abalone.data`, descrição em `abalone.names`).
- **4.177 instâncias**, sem valores ausentes.
- **Features:** `Sex` (M/F/I — categórica), `Length`, `Diameter`, `Height`, `Whole weight`, `Shucked weight`, `Viscera weight`, `Shell weight`.
- **Alvo:** `Age` (anos), derivado de `Rings + 1.5`.

## 🧪 Metodologia
1. **Exploração inicial** (`initial_exploration.py`): carga, renomeação de colunas, estatísticas descritivas, checagem de tipos/ausentes.
2. **Visualização** (`data_visualization.py`): histogramas, box plot de idade por sexo, mapa de calor de correlação.
3. **Modelagem** (`train_and_evaluate_model.py`): `Pipeline` do scikit-learn com `OneHotEncoder` para `Sex` + `LinearRegression`; split treino/teste 80/20 (`random_state=42`).

## 📈 Resultados
| Métrica | Valor |
|---|---|
| **R²** (coef. de determinação) | **0,5482** |
| **RMSE** (erro médio) | **2,21 anos** |

O modelo explica ~55% da variância da idade; o erro médio (~2,2 anos) é razoável dado o intervalo de 2,5–30,5 anos. As variáveis mais influentes são `Shell weight` (r=0,63) e `Diameter` (r=0,57).

### Principais limitações (ver relatório completo)
- Relação possivelmente **não-linear** entre medidas e idade.
- **Variáveis omitidas** (clima, localização/alimento) não estão no dataset.
- **Outliers** (ex.: `Height = 0`) afetam a regressão linear.
- **Próximos passos:** tratar outliers + testar modelos não-lineares (Random Forest, Gradient Boosting).

📄 Relatório detalhado: [`abalone_analysis_report.md`](abalone_analysis_report.md) (também em PDF).

## 🗂️ Estrutura
```
.
├── initial_exploration.py        # EDA: carga + estatísticas descritivas
├── data_visualization.py         # gera os 3 gráficos (.png)
├── train_and_evaluate_model.py   # pipeline de regressão + métricas
├── abalone.data / abalone.names  # dataset UCI + descrição
├── histograms.png                # distribuições das variáveis
├── age_by_sex_boxplot.png        # idade por sexo
├── correlation_heatmap.png       # correlação entre variáveis
├── abalone_analysis_report.md/.pdf
├── model_evaluation_results.txt  # R² e RMSE salvos pela execução
├── requirements.txt
└── .gitignore
```

## ▶️ Como executar
```bash
# 1) ambiente
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 2) pipeline (os scripts leem abalone.data por caminho relativo)
python initial_exploration.py
python data_visualization.py        # gera os .png
python train_and_evaluate_model.py  # imprime e salva R²/RMSE
```

## 🛠️ Stack
Python · pandas · scikit-learn · numpy · matplotlib · seaborn

## 📜 Licença / Crédito
Dataset: UCI ML Repository (Nash et al., 1994). Código de uso acadêmico — sinta-se livre para estudar e adaptar.
