"""
Deze ADT geeft een vertoning weer

Data:
self.id: positive unsigned integer (id van de vertoning)
self.zaalnummer: positive unsigned integer (nummer van de overeenkomstige zaal)
self.slot: positive unsigned integer (tijdslot value waarbij (uur*100)+minuten)
self.filmid: positive unsigned integer (id van de overeenkomstige film)
self.vrije_plaatsen: positive unsigned integer (geeft weer hoeveel vrije plaatsen er beschikbaar zijn voor de vertoning)
self.afspelend: boolean (geeft weer dat de film al dan niet gestart is)
"""

class Vertoning:
    def __init__(self, id, zaalnummer, slot, datum, filmid, vrije_plaatsen): # contract moet herbekeken worden
        """
        Een vertoning object wordt geinitialiseerd/geconstrueerd.

        Precondities: Er worden 6 parameters gegeven, die allemaal positive unsigned integers en niet None zijn.
                      Er bestaat een film die overeenkomt met het gegeven filmid
                      Er bestaat een zaal die overeenkomt met een gegeven zaalnummer
                      Er wordt een geldige slotwaarde gegeven waarvoor geldt dat:
                      er maximum 4 en minium 3 cijfers zijn.
                      De laatste 2 cijfers hebben als getal samen de volgende range [0, 59] en
                      de andere cijfers hun samengevoegd getal hebben als range [0, 23]
                      vb. 23u30 -> 2330
        Postcondities: Er wordt een nieuwe vertoning aangemaakt/geconstrueerd

        :param id: positive unsigned integer
        :param zaalnummer: positive unsigned integer
        :param slot: positive unsigned integer (geeft de slot in seconden weer)
        :param datum: positive unsigned integer
        :param filmid: positive unsigned integer
        :param vrije_plaatsen: positive unsigned integer

        :data afspelend: bool
        :data vrije_plaatsenFysiek
        :data vrije_plaatsenVirtueel
        """
        self.id = id
        self.zaalnummer = zaalnummer
        self.slot = slot
        self.datum = datum
        self.filmid = filmid
        self.afspelend = False #Initaliseer op False
        self.vrije_plaatsen = vrije_plaatsen
        self.vrije_plaatsenVirtueel = vrije_plaatsen
        self.vrije_plaatsenFysiek = 0  # Ingenomen aantal plaatsen

    def verminder_plaatsenVirtueel(self, hoeveelheid):
        """
        Deze functie verminderd het aantal beschikbare plaatsen voor de vertoning

        preconditie: Er moeten meer plaatsen beschikbaar zijn dan dat er verdwijnen.
        postconditie: Het aantal plaatsen worden verminderd.
        :param hoeveelheid: integer (geeft weer hoeveel plaatsen minder er beschikbaar zijn)
        """
        if (self.vrije_plaatsenVirtueel - hoeveelheid >= 0):
            self.vrije_plaatsenVirtueel = self.vrije_plaatsenVirtueel - hoeveelheid
            return True
        return False

    def verhoog_plaatsenFysiek(self, hoeveelheid):
        """
        Deze functie verminderd het aantal beschikbare plaatsen voor de vertoning

        preconditie: Er moeten meer plaatsen beschikbaar zijn dan dat er verdwijnen.
        postconditie: Het aantal plaatsen worden verminderd.
        :param hoeveelheid: integer (geeft weer hoeveel plaatsen minder er beschikbaar zijn)
        """
        if self.vrije_plaatsenFysiek + hoeveelheid < self.vrije_plaatsen:
            self.vrije_plaatsenFysiek = self.vrije_plaatsenFysiek + hoeveelheid
            return True #Operatie geslaagd
        return False #Operatie niet geslaagd

    def check_vol(self):
        """valideert of alle plaatsen vol is, geeft een bool terug"""
        if self.vrije_plaatsenFysiek == self.vrije_plaatsenVirtueel:
            return True
        return False

    def start(self):  # Public
        """
        Start de vertoning
        preconditie: De vertoning start op het juiste tijdstip en er mag geen andere vertoning bezig zijn in deze zaal
        postconditie: De vertoning wordt gestart (gestart = true)
        """
        self.afspelend = True

    def get_id(self):
        return self.id

    def status(self,current_time):
        """
        Geeft de status van een Vertoning in string mee

        :param current_time: positive integer (Time van reservatie systeem)
        :return:
        """
        datetime = int( str(self.datum) + str(self.slot) ) #Date time in seconden volgens format
        if(self.afspelend):
            return "F:"+str(self.vrije_plaatsenFysiek)
        elif ( current_time > datetime ): #Wanneer de film eig al had moeten starten
            return "W:" + str(self.vrije_plaatsen - self.vrije_plaatsenVirtueel - self.vrije_plaatsenFysiek)
        else:
            return "G:"+str(self.vrije_plaatsen - self.vrije_plaatsenVirtueel)