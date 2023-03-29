"""
Deze ADT geeft een film (met haar data) weer

data:
self.id: (integer) id die overeenkomt met de film
self.titel: (string) de titel van de overeenkomende film
self.rating: (float) de score van de desbetreffende film
"""


class Film:
    def __init__(self, id, titel, rating):
        """
        Construeert een film object.

        Precondities: Er worden 3 parameters ingegeven.
                      Het id is een positieve unsigned integer
                      De rating is een positieve float tussen 0 en 100
                      De titel is een string en komt overeen met de film
        Postcondities: Er wordt een nieuw film-object aangemaakt

        :param id: positive unsigned integer
        :param titel: string
        :param rating: positive float ([0-100])
        """
        if not isinstance(id, int) or id < 0:
            raise Exception(f"Preconditie Film gefaald: id {id} wordt niet geaccepteerd")
        if not isinstance(titel, str):
            raise Exception(f"Preconditie Film gefaald: titel {titel} wordt niet geaccepteerd")
        if not (isinstance(rating, float) and 0 <= rating <= 100):
            raise Exception(f"Preconditie Film gefaald: rating {rating} wordt niet geaccepteerd")

        self.id = id
        self.titel = titel
        self.rating = rating

    def get_id(self):
        """
        Er wordt een film id terug gegeven

        Precondities: Er worden geen parameters gegeven.
        Postcondities: Er wordt een positieve integer terug gegeven die het id van de film weergeeft.

        :return: id
        """
        return self.id
