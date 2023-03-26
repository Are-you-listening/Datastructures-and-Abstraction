"""
Deze ADT geeft filmdata weer

data:
self.id: integer (id dat overeenkomt met de film)
self.titel: string (de titel dat overeenkomt met de film)
self.rating: float (de score dat de film krijgt)
"""


class Film:
    def __init__(self, id, titel, rating):
        if not isinstance(id, int) or id < 0:
            raise Exception(f"Preconditie Film gefaald: id {id} wordt niet geaccepteerd")
        if not isinstance(titel, str):
            raise Exception(f"Preconditie Film gefaald: titel {titel} wordt niet geaccepteerd")
        if not (isinstance(rating, float) and 0 <= rating <= 100):
            raise Exception(f"Preconditie Film gefaald: rating {rating} wordt niet geaccepteerd")
        """
        Initialiseer een film object.

        precondities: Er worden 3parameters gegeven.
                      Het id is een positieve integer
                      De rating is een positieve float tussen 0 en 100
                      De titel is een string
        postcondities: Er wordt een nieuwe film object aangemaakt

        :param id: integer
        :param titel: string
        :param rating: float
        """

        self.id = id
        self.titel = titel
        self.rating = rating

    def get_id(self):
        """
        Er wordt een film id terug gegeven
        precondities: er worden geen parameters gegeven.
        postcondities: Er wordt een positieve integer terug gegeven die het id van de film weergeeft.
        :return: id
        """
        return self.id
