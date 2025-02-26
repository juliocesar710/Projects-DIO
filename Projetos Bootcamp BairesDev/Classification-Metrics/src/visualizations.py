# Função para Plotar as Métricas
import matplotlib.pyplot as plt

def plotar_metricas(metricas, valores, salvar=False, arquivo="metricas.jpeg"):
    plt.figure(figsize=(8, 5))
    plt.bar(metricas, valores, color=['blue', 'green', 'orange', 'red', 'purple'])
    plt.ylim(0, 1)
    plt.title("Métricas de Avaliação de Classificação")
    plt.ylabel("Valor")
    
    if salvar:
        plt.savefig(arquivo, format='jpeg')
        print(f'Gráfico salvo como {arquivo}')
    else:
        plt.show()

# ------ # # ------ # # ------ # # ------ # # ------ # # ------ # # ------ # # ------ # # ------ # # ------ # # ------ #

# Função para Plotar o Heatmap das Métricas
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def plotar_heatmap(metricas, valores, salvar=False, arquivo="heatmap.jpeg"):
    data = pd.DataFrame({"Métrica": metricas, "Valor": valores})
    data = data.set_index("Métrica")

    plt.figure(figsize=(8, 5))
    sns.heatmap(data, annot=True, cmap="coolwarm", cbar=True, fmt=".2f")
    plt.title("Heatmap das Métricas de Avaliação")

    if salvar:
        plt.savefig(arquivo, format='jpeg')
        print(f'Heatmap salvo como {arquivo}')
    else:
        plt.show()

# ------ # # ------ # # ------ # # ------ # # ------ # # ------ # # ------ # # ------ # # ------ # # ------ # # ------ #

# Função para Plotar a Matriz de Confusão
import seaborn as sns
import matplotlib.pyplot as plt

def plotar_matriz_confusao(matrix, salvar=False, arquivo="matriz_confusao.jpeg"):
    plt.figure(figsize=(6, 5))
    sns.heatmap(matrix, annot=True, fmt="d", cmap="Blues", 
                xticklabels=["Previsto Positivo", "Previsto Negativo"], 
                yticklabels=["Real Positivo", "Real Negativo"])
    plt.title("Matriz de Confusão")
    plt.xlabel("Classe Prevista")
    plt.ylabel("Classe Real")
    
    if salvar:
        plt.savefig(arquivo, format='jpeg')
        print(f'Matriz de confusão salva como {arquivo}')
    else:
        plt.show()

