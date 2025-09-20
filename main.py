from utils.request import Request
import pandas as pd
from utils.average_comments_user import averageCommentsUser
from utils.plot_graphic_average import plotGraphicAverage


def main():
    ##pegando dados da api
    url = "https://jsonplaceholder.typicode.com/comments"
    request = Request()
    data = request.getData(url)
    print(data[0])

    ##transformando dados em dataframe
    dataframe = pd.DataFrame(data)

    ##Média de comentários por usuário
    averageCommentsUserDf = averageCommentsUser(dataframe)

    ##Gráfico da média de comentários por usuário
    plotGraphicAverage(averageCommentsUserDf)

    dataframe.to_csv("comments.csv", index=False)

if __name__ == "__main__":
    main()