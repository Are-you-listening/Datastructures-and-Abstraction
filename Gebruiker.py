"""ADT Gebruiker"""

class Gebruiker:
    """
    Creeërt een Gebruiker object.
    :parameter in ; 'voornaam': string ,'achternaam': string ,'email': string
    :parameter out ; 'voornaam': string ,'achternaam': string ,'email': string, 'id': int
    Preconditie:
    Postconditie: De input paramaters zijn gedefinieerd. Het ID is geïnitaliseerd op None.
    """
    def __init__(self, voornaam,achternaam,email):
        ##Data
        self.id=None
        self.voornaam=voornaam
        self.achternaam=achternaam
        self.email=email
        print("Gebruiker", email, "is aangemaakt - Constructor Aangeroepen")