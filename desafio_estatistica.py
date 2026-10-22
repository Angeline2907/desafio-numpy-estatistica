import numpy as np
import matplotlib.pyplot as plt

# Dados fornecidos no desafio
dados = [5, 6, 6, 7, 7, 7, 8, 8, 9, 10]

# 1. Utilizando NumPy para calcular a média e o desvio padrão amostral
media = np.mean(dados)
desvio_padrao_amostral = np.std(dados, ddof=1) # ddof=1 define como amostral

# 2. Definindo o intervalo (média - desvio padrão) e (média + desvio padrão)
limite_inferior = media - desvio_padrao_amostral
limite_superior = media + desvio_padrao_amostral

# 3. Exibindo os valores mínimo e máximo desse intervalo no terminal
print("--- RESULTADOS DO DESAFIO ---")
print(f"Média dos dados: {media:.2f}")
print(f"Desvio Padrão Amostral: {desvio_padrao_amostral:.2f}")
print(f"Intervalo Solicitado: [{limite_inferior:.2f}, {limite_superior:.2f}]")
print("-----------------------------\n")

# Construindo o Histograma com a faixa destacada
plt.figure(figsize=(8, 5))

# Plot do histograma
plt.hist(dados, bins=np.arange(4.5, 11.5, 1), rwidth=0.8, color='skyblue', edgecolor='black', alpha=0.7)

# Adicionando a faixa amarela destacando o intervalo solicitado
plt.axvspan(limite_inferior, limite_superior, color='gold', alpha=0.3, label='Média ± 1 Desvio Padrão')

# Adicionando linha tracejada para indicar graficamente a média
plt.axvline(media, color='red', linestyle='dashed', linewidth=1.5, label=f'Média ({media:.1f})')

# Configurações estéticas do gráfico
plt.title('Distribuição dos Dados com Intervalo de Desvio Padrão', fontsize=14, pad=15)
plt.xlabel('Valores do Conjunto', fontsize=12)
plt.ylabel('Frequência', fontsize=12)
plt.xticks(range(4, 12))
plt.legend(loc='upper right')
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Exibe o gráfico na tela
plt.tight_layout()
plt.show()
