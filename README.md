# Desafio NumPy e Estatística Frequencial

Repositório criado para solucionar o desafio de análise de dispersão de dados utilizando Python, NumPy e Matplotlib.

## 📋 Respostas do Desafio

### 1. Código NumPy para Desvio Padrão Amostral
Utilizado o parâmetro `ddof=1` na função `np.std()` para garantir o cálculo amostral:
```python
desvio_padrao_amostral = np.std(dados, ddof=1)
```

### 3. Valores Mínimo e Máximo do Intervalo
* **Valor Mínimo (Média - Desvio Padrão):** ~5.75
* **Valor Máximo (Média + Desvio Padrão):** ~8.85

### 4. O que essa faixa representa?
A faixa amarela destacada no histograma representa a região de **variabilidade central** dos dados coletados ao redor da média aritmética. 

Matematicamente, em distribuições simétricas ou aproximadamente normais, esse intervalo ($\mu \pm 1\sigma$) engloba cerca de **68% das ocorrências totais**. No contexto deste conjunto de dados, ele demonstra visualmente que os valores 6, 7 e 8 concentram a esmagadora maioria das observações da equipe.
