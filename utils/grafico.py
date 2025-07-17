import matplotlib.pyplot as plt

def gerar_grafico(preco):
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [preco, preco + 0.001, preco - 0.001])
    ax.set_title("Variação do Token SAHARA")
    file_path = "grafico.png"
    plt.savefig(file_path)
    return file_path
