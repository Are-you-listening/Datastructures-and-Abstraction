"""
Deze ADT geeft een zaal weer

data:
self.zaalnummer: integer (nummer van de overeenkomstige zaal)
self.plaatsen: integer (aantal plaatsen in de zaal)
"""

class Zaal:
    def __init__(self, nummer, plaatsen):
        """
        Initialiseer een zaal met een nummer en een aantal plaatsen.

        Precondities: Er worden 2 parameters gegeven, die beide positieve integers zijn.
                      De parameters zijn ook niet None.
        Postcondities: Er wordt een nieuwe zaal aangemaakt

        :param nummer: unsigned integer
        :param plaatsen: unsigned integer
        """

        self.zaalnummer = nummer
        self.plaatsen = plaatsen

    def get_id(self):
        """
        Er wordt een zaalnummer terug gegeven.

        Precondities: Er worden geen parameters gegeven.
        Postcondities: Er wordt een positieve integer terug gegeven die het zaalnummer van de zaal weergeeft.

        :return: zaalnummer
        """
        return self.zaalnummer