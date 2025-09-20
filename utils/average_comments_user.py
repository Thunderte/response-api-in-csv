def averageCommentsUser(df):
    commentsUser = df.groupby("email")["id"].count()

    averageComments = commentsUser.mean()
    return averageComments