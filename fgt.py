import pandas as pd

# Supondo que o arquivo esteja no mesmo diretório que seu script Python
def read_excel_file(file_name):
    """Função para ler um arquivo Excel e retornar um DataFrame."""
    try:
        data = pd.read_excel(file_name)
        print("Arquivo lido com sucesso!")
        return data
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")

# Nome do arquivo
file_name = 'FGT.xlsx'

# Chamada da função
df = read_excel_file(file_name)

# Caso queira visualizar as primeiras linhas do DataFrame
if df is not None:
    print(df.head())
