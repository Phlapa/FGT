import pandas as pd

# Supondo que o arquivo esteja no mesmo diretório que seu script Python
def read_excel_file('FGT.xlsx'):
    try:
        data = pd.read_excel('FGT.xlsx')
        print("Arquivo lido com sucesso!")
        return data
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")

# Nome do arquivo
file_name = 'FGT.xlsx'

# Chamada da função
df = read_excel_file('FGT.xlsx')

# Caso queira visualizar as primeiras linhas do DataFrame
if df is not None:
    print(df.head())
import pandas as pd
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
