
import pandas as pd

# Carregar o conjunto de dados
df = pd.read_csv('abalone.data', header=None)

# Definir os nomes das colunas com base em abalone.names
df.columns = ['Sex', 'Length', 'Diameter', 'Height', 'Whole weight', 'Shucked weight', 'Viscera weight', 'Shell weight', 'Rings']

# Adicionar a coluna 'Age' (Rings + 1.5)
df['Age'] = df['Rings'] + 1.5

# Remover a coluna 'Rings' original, pois 'Age' é o alvo
df = df.drop('Rings', axis=1)

# Exibir informações iniciais
print('Número de instâncias:', df.shape[0])
print('Número de variáveis:', df.shape[1])
print('\nTipos de dados:\n', df.dtypes)
print('\nValores ausentes:\n', df.isnull().sum())
print('\nAnálise descritiva:\n', df.describe())

# Salvar as informações iniciais em um arquivo de texto
with open('abalone_initial_exploration.txt', 'w') as f:
    f.write(f'Número de instâncias: {df.shape[0]}\n')
    f.write(f'Número de variáveis: {df.shape[1]}\n')
    f.write('\nTipos de dados:\n')
    f.write(df.dtypes.to_string())
    f.write('\n\nValores ausentes:\n')
    f.write(df.isnull().sum().to_string())
    f.write('\n\nAnálise descritiva:\n')
    f.write(df.describe().to_string())

print('\nExploração inicial concluída e salva em abalone_initial_exploration.txt')


