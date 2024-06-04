import pandas as pd
import matplotlib.pyplot as plt

# Função para ler um arquivo Excel e retornar um DataFrame
def read_excel_file(file_name):
    """Função para ler um arquivo Excel e retornar um DataFrame."""
    try:
        data = pd.read_excel(file_name)  # Lendo o arquivo com o nome fornecido
        print("Arquivo lido com sucesso!")
        return data
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return None

# Nome do arquivo Excel
file_name = 'FGT.xlsx'

# Chamada da função com o nome do arquivo como argumento
df = read_excel_file(file_name)

# Verificar se o DataFrame foi carregado corretamente
if df is not None:
    print(df.head())

    # Suponha que as colunas 'AUD' e 'PROF' existam em seu DataFrame
    # Certifique-se de substituir 'AUD' e 'PROF' pelos nomes corretos das colunas após verificar df.head()
    aud_data = df['AUD'].dropna()
    prof_data = df['PROF'].dropna()

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
