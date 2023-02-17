"""
Deze ADT geeft een gebruiker weer

data:
self.id: integer (id dat overeenkomt met de gebruiker)
self.voornaam: string (bewaard de voornaam van de gebruiker)
self.achternaam: string (bewaard de achternaam van de gebruiker)
self.mail: string (bewaard de emailvan de gebruiker)
"""


class Gebruiker:
    def __init__(self, id, voornaam, achternaam, mail):
        """
        Het object gebruiker wordt geïnitialiseerd.

        precondities: Er worden 4 parameters gegeven.
        id is een integer en voornaam, achternaam, mail zijn strings.
        postcondities: het object Gebruiker wordt geïnitialiseerd.

        :param id: integer
        :param voornaam: string
        :param achternaam: string
        :param mail: string
        """
        pass

    def get_gegevens(self):
        """
        Deze functie geeft de voornaam, achternaam en e-mail van de gebruiker
        precondities: Er worden geen parameters gegeven
        postcondities: de gebruikers gegevens worden in een tuple teruggegeven (voornaam, achternaam, mail)
        :return: de gebruikersgegevens volgens volgend format (voornaam, achternaam, mail)
        """
        pass
