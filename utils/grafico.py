import matplotlib.pyplot as plt
import random

def gerar_grafico():
    valores = [random.uniform(0.8, 1.2) for _ in range(10)]
    plt.plot(valores)
    plt.title("Variação do token SAHARA")
    plt.savefig("grafico.png")
