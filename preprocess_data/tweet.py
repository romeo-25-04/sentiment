class Tweet:
    def __init__(self, line):
        id1, id2, polarity, text = line.strip().split('\t')
        self.id1 = id1
        self.id2 = id2
        self.polarity = polarity
        self.text = text

    def __repr__(self):
        return str(self.__dict__)

    def __str__(self):
        return "{}\t{}\t{}\t{}".format(
            self.id1,
            self.id2,
            self.polarity,
            self.text
        )
