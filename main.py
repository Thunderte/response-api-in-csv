from utils.request import Request
import pandas as pd
from utils.average_comments_user import averageCommentsUser
from utils.plot_graphic_average import plotGraphicAverage
import time


def main():
    try:
        ##iniciando contagem tempo de execucao
        inicio = time.time()

        ##pegando dados da api
        url = "https://jsonplaceholder.typicode.com/comments"
        request = Request()
        data = request.getData(url)

        ##transformando dados em dataframe
        dataframe = pd.DataFrame(data)

        ##Média de comentários por usuário
        averageCommentsUserDf = averageCommentsUser(dataframe)

        ##Gráfico da média de comentários por usuário
        plotGraphicAverage(averageCommentsUserDf)

        dataframe.to_csv("comments.csv", index=False)
        
        #finalizando contagem tempo de execucao
        fim = time.time()

        #printando resultados
        print(f"\nMédia de comentários por usuário: {averageCommentsUserDf}")
        print(f"\nTempo de execução: {(fim - inicio):.2f} segundos")

        return True
    except Exception as e:
        print(f"Ops... Ocorreu um erro inesperado: {e}")
        raise Exception("Ops... Ocorreu um erro inesperado")

if __name__ == "__main__":
    main()