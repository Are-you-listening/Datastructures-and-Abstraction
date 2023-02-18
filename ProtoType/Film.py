"""
Deze ADT geeft filmdata weer

data:
self.id: integer (id dat overeenkomt met de film)
self.titel: string (de titel dat overeenkomt met de film)
self.rating: float (de score dat de film krijgt)
"""


class Film:
    def __init__(self, id, titel, rating):
        """
        Initialiseer een film object.

        precondities: Er worden 3parameters gegeven.
                      Het id is een positieve integer
                      De rating is een positieve float
                      De titel is een string
        postcondities: Er wordt een nieuwe film object aangemaakt

        :param id: integer
        :param titel: string
        :param rating: float
        """

        self.id = id
        self.titel = titel
        self.rating = rating
