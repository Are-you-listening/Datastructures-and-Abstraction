"""
Deze ADT geeft een gebruiker weer

Data:
self.id: positive unsigned integer (id dat overeenkomt met de gebruiker)
self.voornaam: string (bewaard de voornaam van de gebruiker)
self.achternaam: string (bewaard de achternaam van de gebruiker)
self.mail: string (bewaard de email van de gebruiker)
"""


class Gebruiker:
    def __init__(self, id, voornaam, achternaam, mail):
        """
        Het object gebruiker wordt geïnitialiseerd.

        Precondities: Er worden 4 parameters gegeven.
        id is een unsigned positive integer en voornaam, achternaam, mail zijn strings.
        Postcondities: Het object Gebruiker wordt geïnitialiseerd.

        :param id: unsigned positive integer
        :param voornaam: string
        :param achternaam: string
        :param mail: string
        """
        self.id = id
        self.vnaam = voornaam
        self.anaam = achternaam
        self.mail = mail

    def get_id(self):
        return self.id