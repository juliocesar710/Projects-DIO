#  Cálculo das Métricas
def calcular_metricas(vp, fn, fp, vn):
    acuracia = (vp + vn) / (vp + fn + fp + vn)
    sensibilidade = vp / (vp + fn)
    precisao = vp / (vp + fp)
    especificidade = vn / (vn + fp)
    fscore = 2 * (precisao * sensibilidade) / (precisao + sensibilidade)
    
    return acuracia, sensibilidade, precisao, especificidade, fscore

# ------ # # ------ # # ------ # # ------ # # ------ # # ------ # # ------ # # ------ # # ------ # # ------ # # ------ #

# Cálculo da Matriz de Confusão
from sklearn.metrics import confusion_matrix

def calcular_matriz_confusao(y_true, y_pred):
    return confusion_matrix(y_true, y_pred)

# ------ # # ------ # # ------ # # ------ # # ------ # # ------ # # ------ # # ------ # # ------ # # ------ # # ------ #

# Função para Plotar a Matriz de Confusão
import seaborn as sns
import matplotlib.pyplot as plt

def plotar_matriz_confusao(matrix):
    plt.figure(figsize=(6, 5))
    sns.heatmap(matrix, annot=True, fmt="d", cmap="Blues", xticklabels=["Previsto Positivo", "Previsto Negativo"], 
                yticklabels=["Real Positivo", "Real Negativo"])
    plt.title("Matriz de Confusão")
    plt.xlabel("Classe Prevista")
    plt.ylabel("Classe Real")
    plt.show()

# ------ # # ------ # # ------ # # ------ # # ------ # # ------ # # ------ # # ------ # # ------ # # ------ # # ------ #

# Função para Plotar as Métricas
import matplotlib.pyplot as plt

def plotar_metricas(metricas, valores):
    plt.figure(figsize=(8, 5))
    plt.bar(metricas, valores, color=['blue', 'green', 'orange', 'red', 'purple'])
    plt.ylim(0, 1)  # As métricas estão em proporção de 0 a 1
    plt.title("Métricas de Avaliação de Classificação")
    plt.ylabel("Valor")
    plt.show()

