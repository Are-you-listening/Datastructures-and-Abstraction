"""
Deze ADT geeft een reservatie weer

data:
self.vertoning_id: integer (id dat overeenkomt met de vertoning waarvoor er gereserveerd wordt)
self.aantal_plaatsen: integer (geeft weer voor hoeveel plaatsen een reservatie gemaakt wordt)
self.timestamp: integer (bewaard op welk tijdstip er een reservatie gemaakt is)
self.userid: integer (het id van de gebruiker dat de reservatie gemaakt heeft)
"""


class Reservatie:
    def __init__(self, vertoning_id, aantal_plaatsen, tijdstip, gebruiker_id):
        """
        Initialiseer de reservatie

        precondities: Er worden 4 parameters gegeven, ze zijn allemaal positieve integers
                      Er wordt een geldige vertoning_id gegeven en een geldig gebruiker_id
        postcondities: Er wordt een nieuw reservatie object aangemaakt

        :param vertoning_id: integer
        :param aantal_plaatsen: integer
        :param tijdstip: integer
        :param gebruiker_id: integer
        """
        pass

    def get_vertoning_id(self):
        """
        Geeft het vertonings-id terug dat overeenkomt met de reservatie
        precondities: Het vertoning-id is een positieve integer
        postcondities: Er wordt een vertongings-id teruggeven.
        :return: geeft de integer self.vertoning_id terug.
        """
        pass

    def get_plaatsen(self):
        """
        Geeft terug voor hoeveel plaatsen de reservatie geldt.
        precondities: Het aantal plaatsen is een integer groter dan 0
        postcondities: Er wordt teruggeven voor hoeveel plaatsen de reservatie geldt.
        :return: geeft de integer self.aantal_plaatsen terug.
        """
        pass

