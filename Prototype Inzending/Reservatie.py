"""ADT Reservatie"""

class Reservatie:
    def __init__(self, userid,timestamp,vertoningid,aantal_plaatsen):
        """
        Creeërt een Reservatie-object
        :parameter in ; 'userid': int, 'timestamp': int, 'vertoningid': int, 'aantal_plaatsen':int
        :parameter out ;
        Preconditie:
        Postconditie: Er is een Reservatie geconstrueerd
        """
        ##Data
        self.id = None
        self.userid=userid
        self.timestamp=timestamp
        self.vertoningid=vertoningid
        self.aantal_plaatsen=aantal_plaatsen
        print("Reservatie is geconstrueerd met nummer: ", self.id)

    def print(self):
        """
        Print de reservatie-data in een leesbaar format
        :parameter
        :parameter out ;
        Preconditie:
        Postconditie:
        """
        return str("De reservatie met ID: ",self.id, "op userID: " , self.userid, "voor " , self.aantal_plaatsen , "personen om: " , self.timestamp, "is uitgelezen. VertoningID: " , self.vertoningid)

