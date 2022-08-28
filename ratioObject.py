class ratObj:
    def __init__(self, game, win, loss, ratio, date):
        self.game = game
        self.win = win
        self.loss = loss
        self.ratio = ratio
        self.date = date
    def __str__(self):
        return "%f win-loss ratio for %s game: %d wins %d losses, registered on %s" % (self.ratio, self.game, self.win, self.loss, self.date)
    def getGame(self):
        return self.game
    def getRatio(self):
        return float(self.ratio)