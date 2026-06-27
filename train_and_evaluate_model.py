
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import numpy as np

# Carregar o conjunto de dados
df = pd.read_csv("abalone.data", header=None)
df.columns = ["Sex", "Length", "Diameter", "Height", "Whole weight", "Shucked weight", "Viscera weight", "Shell weight", "Rings"]
df["Age"] = df["Rings"] + 1.5
df = df.drop("Rings", axis=1)

# Separar features (X) e target (y)
X = df.drop("Age", axis=1)
y = df["Age"]

# Identificar colunas categóricas e numéricas
categorical_features = ["Sex"]
numerical_features = X.select_dtypes(include=np.number).columns.tolist()

# Criar um pré-processador para aplicar OneHotEncoder à coluna 'Sex'
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
    ], remainder="passthrough"
)

# Criar o pipeline do modelo
model_pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", LinearRegression())
])

# Dividir os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar o modelo
model_pipeline.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
y_pred = model_pipeline.predict(X_test)

# Avaliar o modelo
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"R-squared (R²): {r2:.4f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")

# Salvar os resultados da avaliação em um arquivo de texto
with open("model_evaluation_results.txt", "w") as f:
    f.write(f"R-squared (R²): {r2:.4f}\n")
    f.write(f"Root Mean Squared Error (RMSE): {rmse:.4f}\n")

print("\nAvaliação do modelo concluída e salva em model_evaluation_results.txt")


