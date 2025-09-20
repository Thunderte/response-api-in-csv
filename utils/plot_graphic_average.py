import matplotlib.pyplot as plt

def plotGraphicAverage(average):
    plt.bar(['Average Comments per User'], [average], color='skyblue')
    plt.ylabel('Average Number of Comments')
    plt.title('Average Comments per User')

    # Adiciona o valor numérico acima da barra
    plt.text(0, average + 0.05, f"{average:.2f}", ha='center', fontsize=10)

    plt.show()
