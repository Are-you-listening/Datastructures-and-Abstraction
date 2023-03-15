"""
Deze ADT geeft een zaal weer

data:
self.zaalnummer: integer (nummer van de overeenkomstige zaal)
self.plaatsen: integer (aantal plaatsen in de zaal)
"""


class Zaal:
    def __init__(self, nummer, plaatsen):
        """
        Initialiseer een zaal met een nummer en een aantal plaatsen

        precondities: Er worden 2 parameters gegeven, die beide integers zijn.
                      De parameters zijn ook niet None.
        postcondities: Er wordt een nieuwe zaal aangemaakt

        :param nummer: integer
        :param plaatsen: integer
        """
        self.zaalnummer = nummer
        self.plaatsen = plaatsen

    def get_id(self):
        return self.zaalnummer
