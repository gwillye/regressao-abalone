# Análise de Regressão para Predição da Idade do Abalone

## Introdução

Este documento detalha o processo de desenvolvimento de um modelo de regressão linear múltipla para prever a idade do abalone a partir de medições físicas. A idade do abalone é tradicionalmente determinada por um método manual e demorado de contagem de anéis na casca. O objetivo deste projeto é explorar a viabilidade de utilizar outras medições mais fáceis de obter para automatizar e agilizar essa predição.

## Configuração e Exploração Inicial dos Dados

O conjunto de dados utilizado foi fornecido e contém diversas medições físicas de abalones. As colunas foram renomeadas para maior clareza e uma nova coluna 'Age' (Idade) foi criada a partir da coluna 'Rings' (Anéis), adicionando 1.5 conforme a especificação do problema, para representar a idade em anos. A coluna 'Rings' original foi então removida.

### Informações Gerais

Após o carregamento e pré-processamento inicial, o conjunto de dados apresenta as seguintes características:

- **Número de Instâncias:** 4177
- **Número de Variáveis:** 9 (incluindo a variável alvo 'Age')

Não foram encontrados valores ausentes no conjunto de dados, o que simplifica a etapa de pré-processamento. Os tipos de dados são apropriados para cada variável, com a maioria sendo `float64` para as medições contínuas e `object` para a variável categórica 'Sex'.

### Análise Descritiva

A análise descritiva das variáveis numéricas revela as seguintes estatísticas:




```
            Length     Diameter       Height  Whole weight  Shucked weight  Viscera weight  Shell weight          Age
count  4177.000000  4177.000000  4177.000000   4177.000000     4177.000000     4177.000000   4177.000000  4177.000000
mean      0.523992     0.407881     0.139516      0.828742        0.359367        0.180594      0.238831    11.433684
std       0.120093     0.099240     0.041827      0.490389        0.221963        0.109614      0.139203     3.224169
min       0.075000     0.055000     0.000000      0.002000        0.001000        0.000500      0.001500     2.500000
25%       0.450000     0.350000     0.115000      0.441500        0.186000        0.093500      0.130000     9.500000
50%       0.545000     0.425000     0.140000      0.799500        0.336000        0.171000      0.234000    10.500000
75%       0.615000     0.480000     0.165000      1.153000        0.502000        0.253000      0.329000    12.500000
max       0.815000     0.650000     1.130000      2.825500        1.488000        0.760000      1.005000    30.500000
```

## Análise Exploratória com Visualizações

Para uma compreensão mais aprofundada dos dados, foram gerados os seguintes gráficos:

### Distribuição das Variáveis Numéricas

Os histogramas das variáveis numéricas (Figura 1) mostram a distribuição de cada característica. Observa-se que a maioria das variáveis possui uma distribuição aproximadamente normal, com algumas assimetrias. A variável `Height` (Altura) apresenta um valor mínimo de 0, o que pode indicar a presença de outliers ou erros de medição, que podem impactar o desempenho do modelo.

![Histogramas das Variáveis Numéricas](histograms.png)
*Figura 1: Histogramas das Variáveis Numéricas*

### Distribuição da Idade por Sexo

O box plot da idade por sexo (Figura 2) revela que, em média, abalones machos (M) e fêmeas (F) tendem a ter idades semelhantes, enquanto abalones infantis (I) são, como esperado, significativamente mais jovens. Há uma presença notável de outliers em todas as categorias de sexo, indicando abalones com idades atípicas para seus respectivos grupos.

![Box Plot da Idade por Sexo](age_by_sex_boxplot.png)
*Figura 2: Box Plot da Idade por Sexo*

### Mapa de Calor da Correlação

O mapa de calor da correlação (Figura 3) exibe a relação linear entre as variáveis numéricas. Observa-se uma alta correlação entre as variáveis de dimensão (`Length`, `Diameter`, `Height`) e as variáveis de peso (`Whole weight`, `Shucked weight`, `Viscera weight`, `Shell weight`). A variável alvo `Age` (Idade) apresenta uma correlação moderada com a maioria das variáveis preditoras, sendo a mais forte com `Shell weight` (0.63) e `Diameter` (0.57). Isso sugere que essas características são as mais influentes na determinação da idade do abalone.

![Mapa de Calor da Correlação](correlation_heatmap.png)
*Figura 3: Mapa de Calor da Correlação entre Variáveis Numéricas*

## Desenvolvimento e Treinamento do Modelo de Regressão

Para prever a idade do abalone, foi implementado um modelo de Regressão Linear Múltipla utilizando a biblioteca `scikit-learn`. Antes do treinamento, a variável categórica `Sex` foi transformada em representação numérica usando One-Hot Encoding para que pudesse ser utilizada pelo modelo. Os dados foram divididos em conjuntos de treinamento (80%) e teste (20%) para avaliar a capacidade de generalização do modelo.

O pipeline do modelo incluiu o pré-processamento (One-Hot Encoding) e o regressor (Regressão Linear).

## Avaliação do Modelo e Análise dos Resultados

Após o treinamento, o modelo foi avaliado no conjunto de teste utilizando as métricas R-squared (R²) e Root Mean Squared Error (RMSE).




Os resultados obtidos no conjunto de teste foram:

- **R-squared (R²):** 0.5482
- **Root Mean Squared Error (RMSE):** 2.2116

### Discussão dos Resultados

O valor de R-squared (R²) de aproximadamente 0.5482 indica que cerca de 54.82% da variância na idade do abalone pode ser explicada pelas variáveis preditoras no modelo. Embora este valor sugira que o modelo consegue capturar uma parte significativa da variabilidade, ele também indica que uma parcela considerável (aproximadamente 45.18%) da variância não é explicada pelo modelo. Isso significa que há outros fatores não incluídos neste conjunto de dados que influenciam a idade do abalone, ou que a relação entre as variáveis não é puramente linear.

O Root Mean Squared Error (RMSE) de 2.2116 representa o desvio padrão dos resíduos (erros de previsão). Em termos práticos, isso significa que, em média, as previsões de idade do modelo se desviam em aproximadamente 2.21 anos da idade real do abalone. Considerando que a idade do abalone varia de 2.5 a 30.5 anos, um RMSE de 2.21 anos pode ser considerado razoável para algumas aplicações, mas pode ser alto para outras que exigem maior precisão.

### Potenciais Problemas e Limitações do Modelo

1.  **Linearidade:** O modelo de regressão linear assume uma relação linear entre as variáveis preditoras e a variável alvo. No entanto, a relação entre as medições físicas e a idade do abalone pode ser não linear. A presença de outliers, como observado na variável `Height`, também pode afetar a linearidade e o desempenho do modelo.

2.  **Variáveis Omitidas:** Conforme mencionado na descrição original do conjunto de dados, fatores como padrões climáticos e localização (e, consequentemente, disponibilidade de alimento) podem ser cruciais para prever a idade do abalone. Essas informações não estão presentes no conjunto de dados atual, o que limita a capacidade do modelo de explicar toda a variância na idade.

3.  **Outliers:** A presença de outliers, especialmente na variável `Height` (altura zero), pode distorcer os resultados do modelo de regressão linear, que é sensível a valores extremos. Embora o pré-processamento inicial tenha removido valores ausentes, a análise de outliers e o tratamento adequado (como remoção ou transformação) poderiam melhorar o desempenho.

4.  **Variável Categórica `Sex`:** Embora o One-Hot Encoding tenha sido aplicado, a variável `Sex` (Sexo) pode ter interações complexas com outras variáveis que um modelo linear simples pode não capturar adequadamente.

5.  **Complexidade da Relação:** A idade do abalone é um fenômeno biológico complexo. Um modelo de regressão linear, por sua simplicidade, pode não ser capaz de capturar todas as nuances e interações entre as diversas características físicas que determinam a idade. Modelos mais complexos, como redes neurais ou modelos baseados em árvores (e.g., Random Forest, Gradient Boosting), poderiam potencialmente alcançar um desempenho superior.

Em resumo, o modelo de regressão linear múltipla forneceu um ponto de partida razoável para a predição da idade do abalone, mas suas limitações destacam a necessidade de explorar modelos mais avançados, incorporar variáveis adicionais e realizar um tratamento mais robusto de outliers para melhorar a precisão das previsões.

## Documentação e Submissão

Todo o processo, incluindo o código utilizado, as saídas relevantes (gráficos e textos) e comentários explicativos de cada etapa, foi documentado neste relatório. Os gráficos gerados estão anexados como `histograms.png`, `age_by_sex_boxplot.png` e `correlation_heatmap.png`.



