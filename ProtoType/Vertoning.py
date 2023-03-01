"""
Deze ADT geeft een veretoning weer

data:
self.id: integer (id van de vertoning)
self.filmid: integer (id van de overeenkomstige film)
self.zaalnummer: integer (nummer van de overeenkomstige zaal)
self.slot: integer (tijdslot value waarbij (uur*100)+minuten)
self.vrije_plaatsen: integer (geeft wee hoeveel vrije plaatsen er beschikbaar zijn voor de vertoning)
self.gestart: boolean (geeft weer dat de film al dan niet gestart is)
"""


class Vertoning:
    def __init__(self, id, zaalnummer, slot, datum, filmid, vrije_plaatsen): # contract moet herbekeken worden
        """
        Een vertoning object wordt geinitialiseerd.
        Een vertoning heeft een id, zaalnummer, tijdslot, datum, filmid, aantal vrije plaatsen, afspelend

        precondities: Er worden 5 parameters gegeven, die allemaal integers en niet None zijn.
                      Er bestaat een film die overeenkomt met het gegeven filmid
                      Er bestaat een zaal die overeenkomt met een gegeven zaalnummer
                      Waasrbij het zaalnummer zelfs een positief integer is.
                      Er wordt een geldige slotwaarde gegeven waarvoor geldt dat:
                      er maximum 4 en minium 3 cijfers zijn.
                      De laatste 2 cijfers hebben als getal samen de volgende range [0, 59] en
                      de andere cijfers hun samengevoegd getal hebben als range [0, 23]
                      vb. 23u30 -> 2330
        postcondities: Er wordt een nieuwe vertoning aangemaakt

        :param id: integer
        :param zaalnummer: integer
        :param slot: integer
        :param datum: integer
        :param filmid: integer
        :param vrije_plaatsen: integer
        :data afspelend: bool
        :data vrije_plaatsenFysiek
        :data vrije_plaatsen
        """
        if isinstance(id, int) and isinstance(filmid, int) and isinstance(zaalnummer, int) and isinstance(slot, int) and isinstance(vrije_plaatsen, int): # dit zal ik nog veranderen naar unsigend integers
            self.id = id
            self.zaalnummer = zaalnummer
            self.slot = slot
            self.datum = datum # datum moet waarschijnlijk nog aangepast worden naar juiste formaat
            self.filmid = filmid
            self.vrije_plaatsenVirtueel = vrije_plaatsen
            self.afspelend = None
            self.vrije_plaatsenFysiek = vrije_plaatsen
            self.vrije_plaatsen = vrije_plaatsen

    def verminder_plaatsenVirtueel(self, hoeveelheid):
        """
        Deze functie verminderd het aantal beschikbare plaatsen voor de vertoning

        preconditie: Er moeten meer plaatsen beschikbaar zijn dan dat er verdwijnen.
        postconditie: Het aantal plaatsen worden verminderd.
        :param hoeveelheid: integer (geeft weer hoeveel plaatsen minder er beschikbaar zijn)
        """
        if self.vrije_plaatsenVirtueel - hoeveelheid < 0:
            self.vrije_plaatsenVirtueel = self.vrije_plaatsenVirtueel - hoeveelheid
            return True
        return False

    def verminder_plaatsenFysiek(self, hoeveelheid):
        """
        Deze functie verminderd het aantal beschikbare plaatsen voor de vertoning

        preconditie: Er moeten meer plaatsen beschikbaar zijn dan dat er verdwijnen.
        postconditie: Het aantal plaatsen worden verminderd.
        :param hoeveelheid: integer (geeft weer hoeveel plaatsen minder er beschikbaar zijn)
        """
        if self.vrije_plaatsenFysiek - hoeveelheid < 0:
            self.vrije_plaatsenFysiek = self.vrije_plaatsenFysiek - hoeveelheid
            return True
        return False

    def set_plaatsen(self, plaatsen): # dit moet toch niet meer bestaan
        """
        Er wordt aangepast hoeveel vrije plaatsen er zijn
        preconditie: Er wordt 1 parameter gegeven dat een positieve integer is
        postconditie: Het aantal vrije plaatsen wordt gewijzigd
        :param plaatsen: integer
        """
        pass

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

    def stop(self):
        """
        Stopt de vertoning
        preconditie: De film moet al gestart zijn
        postconditie: De vertoning wordt beëindigd (gestart = false)
        """
        self.afspelend = False
        self.vrije_plaatsenFysiek = self.vrije_plaatsen
        self.vrije_plaatsenVirtueel = self.vrije_plaatsen