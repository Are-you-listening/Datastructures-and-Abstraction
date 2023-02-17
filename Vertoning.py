"""ADT Vertoning"""

class Vertoning:
    """
    Creeërt een Film object
    :parameter in ; 'zaalnummer': int, tijdslot: "int", 'datum': date, 'filmID': int, 'vrije_plaatsen': int
    :parameter out ;
    Preconditie:
    Postconditie: Er is een Film-Object geconstrueeerd.
    """
    def __init__(self,zaalnummer,tijdslot,datum,filmID,vrije_plaatsen):
        ##Data
        self.id=None
        self.zaalnummer=zaalnummer
        self.tijdslot=tijdslot
        self.datum=datum
        self.filmID=filmID
        self.vrije_plaatsen=vrije_plaatsen
        self.ingenomen_plaatsen=0
        print("Vertoning is aangemaakt met ID: " , self.id )