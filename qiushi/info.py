class Info():
    def __init__(self, author, article):
        self.author = author
        self.article = article

    def __str__(self):
        return 'author:{}', 'article:{}'.format(self.author, self.article)

