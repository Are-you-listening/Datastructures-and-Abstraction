"""ADT Film"""

class Film:
    def __init__(self,titel,rating):
        """
        Creeërt een Film object
        :parameter in ; 'titel': string, 'rating': int (0-10)
        :parameter out ;
        Preconditie:
        Postconditie: Er is een Film-Object geconstrueeerd.
        """
        ##Data
        self.id=None
        self.titel=titel
        self.rating=rating
        print("Film is aangemaakt met titel: " , titel)