"""
Deze ADT geeft een zaal weer

data:
self.zaalnummer: integer (nummer van de overeenkomstige zaal)
self.plaatsen: integer (aantal plaatsen in de zaal)
"""


class Zaal:
    def __init__(self, nummer, plaatsen):
        if not isinstance(nummer, int) or nummer < 0:
            raise Exception(f"Preconditie Zaal gefaald: nummer {nummer} wordt niet geaccepteerd")
        if not isinstance(plaatsen, int) or plaatsen < 0:
            raise Exception(f"Preconditie Zaal gefaald: plaatsen {plaatsen} wordt niet geaccepteerd")
        """
        Initialiseer een zaal met een nummer en een aantal plaatsen

        precondities: Er worden 2 parameters gegeven, die beide positieve integers zijn.
                      De parameters zijn ook niet None.
        postcondities: Er wordt een nieuwe zaal aangemaakt

        :param nummer: integer
        :param plaatsen: integer
        """
        self.zaalnummer = nummer
        self.plaatsen = plaatsen

    def get_id(self):
        """
        Er wordt een zaalnummer terug gegeven
        precondities: er worden geen parameters gegeven.
        postcondities: Er wordt een positieve integer terug gegeven die het zaalnummer van de zaal weergeeft.
        :return: zaalnummer
        """
        return self.zaalnummer
