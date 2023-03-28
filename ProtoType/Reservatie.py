"""
Deze ADT geeft een reservatie weer

data:
self.vertoning_id: integer (id dat overeenkomt met de vertoning waarvoor er gereserveerd wordt)
self.aantal_plaatsen: integer (geeft weer voor hoeveel plaatsen een reservatie gemaakt wordt)
self.tijdstip: integer (bewaard op welk tijdstip er een reservatie gemaakt is)
self.gebruiker-id: integer (het id van de gebruiker dat de reservatie gemaakt heeft)
"""

class Reservatie:
    def __init__(self,vertoning_id, aantal_plaatsen, tijdstip, gebruiker_id):
        """
        Initialiseer de reservatie

        Precondities: Er worden 4 parameters gegeven, ze zijn allemaal positieve integers
                      Er wordt een geldige vertoning_id gegeven en een geldig gebruiker_id (gebruiker en vertoning bestaan).
        Postcondities: Er wordt een nieuw reservatie object aangemaakt

        :param vertoning_id: integer
        :param aantal_plaatsen: unsigned integer
        :param tijdstip: integer
        :param gebruiker_id: integer
        """
        self.vertoning_id = vertoning_id
        self.aantal_plaatsen = aantal_plaatsen
        self.tijdstip = tijdstip
        self.gebruiker_id = gebruiker_id