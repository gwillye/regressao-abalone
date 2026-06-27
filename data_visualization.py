
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o conjunto de dados
df = pd.read_csv("abalone.data", header=None)
df.columns = ["Sex", "Length", "Diameter", "Height", "Whole weight", "Shucked weight", "Viscera weight", "Shell weight", "Rings"]
df["Age"] = df["Rings"] + 1.5
df = df.drop("Rings", axis=1)

# Configurar o estilo dos gráficos
sns.set_style("whitegrid")

# 1. Histograma das variáveis numéricas
plt.figure(figsize=(15, 10))
for i, col in enumerate(df.select_dtypes(include=["float64", "int64"]).columns):
    plt.subplot(3, 3, i + 1)
    sns.histplot(df[col], kde=True)
    plt.title(f"Distribuição de {col}")
plt.tight_layout()
plt.savefig("histograms.png")
plt.close()

# 2. Box plot da Idade por Sexo
plt.figure(figsize=(8, 6))
sns.boxplot(x="Sex", y="Age", data=df)
plt.title("Distribuição da Idade por Sexo")
plt.savefig("age_by_sex_boxplot.png")
plt.close()

# 3. Mapa de calor da correlação
plt.figure(figsize=(10, 8))
sns.heatmap(df.select_dtypes(include=["float64", "int64"]).corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Mapa de Calor da Correlação entre Variáveis Numéricas")
plt.savefig("correlation_heatmap.png")
plt.close()

print("Gráficos gerados e salvos como histograms.png, age_by_sex_boxplot.png e correlation_heatmap.png")


