"""ADT Zaal"""

class Zaal:
    """
    Creeërt een Zaal object
    :parameter in ; 'nummer': int, 'aantal_plaatsen': int
    :parameter out ;
    Preconditie:
    Postconditie: Er is een Zaal-Object geconstrueeerd.
    """
    def __init__(self,nummer,aantal_plaatsen):
        self.nummer=nummer
        self.aantal_plaatsen=aantal_plaatsen
        print("Zaal is geconstrueerd met nummer: ", self.nummer)