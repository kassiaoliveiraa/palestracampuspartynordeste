import pandas as pd
import numpy as np
import random

# Função para gerar dados fictícios
def generate_data(num_rows):
    # Listas de exemplo de cidades, estados e países
    cities = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Porto Alegre', 'Brasília']
    states = ['SP', 'RJ', 'MG', 'PR', 'RS', 'DF']
    countries = ['Brasil']

    # Gerar dados fictícios
    data = {
        'Cidade': [random.choice(cities) for _ in range(num_rows)],
        'Estado': [random.choice(states) for _ in range(num_rows)],
        'País': [random.choice(countries) for _ in range(num_rows)]
    }
    
    return pd.DataFrame(data)

# Definir o tamanho do arquivo CSV em bytes
target_size = 1 * 1024**3  # 1 GB

# Estimar o número de linhas necessárias
# Vamos usar uma média de 100 bytes por linha como exemplo
average_line_size = 100
num_rows = target_size // average_line_size

# Gerar os dados
df = generate_data(num_rows)

# Salvar em um arquivo CSV
df.to_csv('dados_cidades.csv', index=False)
