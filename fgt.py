import pandas as pd

# Nome do arquivo
file_name = 'FGT.xlsx'

import matplotlib.pyplot as plt

# Caminho do arquivo
file_path = 'FGT.xlsx'

# Carregar o DataFrame
df = pd.read_excel(file_path)

# Extraindo informações (adaptar isso com os nomes corretos das colunas após ver o df.head())
aud_data = df['AUD'].dropna()  # Substitua 'AUD' pelo nome correto da coluna
prof_data = df['PROF'].dropna()  # Substitua 'PROF' pelo nome correto da coluna

# Gráfico para AUD
plt.figure(figsize=(10, 5))
plt.plot(aud_data, label='Audiência')
plt.title('Audiência ao Longo do Tempo')
plt.xlabel('Tempo')
plt.ylabel('Audiência')
plt.legend()
plt.show()

# Gráfico para PROF
plt.figure(figsize=(10, 5))
plt.plot(prof_data, label='Professores')
plt.title('Atividade dos Professores ao Longo do Tempo')
plt.xlabel('Tempo')
plt.ylabel('Número de Professores')
plt.legend()
plt.show()
