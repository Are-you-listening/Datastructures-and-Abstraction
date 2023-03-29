"""
Deze ADT geeft een reservatie weer

Data:
self.vertoning_id: (integer) id dat overeenkomt met de vertoning waarvoor er gereserveerd wordt
self.aantal_plaatsen: (positive unsigned integer) geeft weer voor hoeveel plaatsen een reservatie gemaakt wordt
self.tijdstip: (positive unsigned integer) bewaard op welk tijdstip er een reservatie gemaakt is, in seconden
self.gebruiker-id: (positive unsigned integer) het id van de gebruiker die de reservatie gemaakt heeft
"""

class Reservatie:
    def __init__(self,vertoning_id, aantal_plaatsen, tijdstip, gebruiker_id):
        """
        Constructor

        Precondities: Er worden 4 parameters gegeven, ze zijn allemaal positieve integers.
                      Het resp. gekoppelde vertoning_id & gebruiker_id komen overeen met een bestaande vertoning & gebruiker.
        Postcondities: Er wordt een nieuw reservatie object aangemaakt.

        :param vertoning_id: integer
        :param aantal_plaatsen: unsigned integer
        :param tijdstip: integer
        :param gebruiker_id: integer
        """
        self.vertoning_id = vertoning_id
        self.aantal_plaatsen = aantal_plaatsen
        self.tijdstip = tijdstip
        self.gebruiker_id = gebruiker_id