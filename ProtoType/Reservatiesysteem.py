from ADT import MyBST, My_BinarySearchTree, MyCircularLinkedChain, MyLinkedChain, MyQueue_Linked, MyTwoThreeFourTree
from Film import Film
from Zaal import Zaal
from Vertoning import Vertoning
from Reservatie import Reservatie
from Gebruiker import Gebruiker

"""
Deze ADT geeft een reservatiesysteem weer dat gebruik maakt van de andere ADT

data:
self.vertoningen: Boom van Vertoning objecten (de aangemaakte vertoningen worden hier bewaard)
self.films: ketting van Film objecten (de aangemaakte film worden hier bewaard)
self.zalen: ketting van Zaal objecten (de aangemaakte zaal worden hier bewaard)
self.gebruikers: ketting van aangemaakte Gebruiker objecten (de aangemaakte gebruiker worden hier bewaard)
self.reservaties: queue van aangemaakte Reservatie Objecten
self.reservaties_archief: ketting van aangemaakte Reservatie objecten die niet meer in de queue zitten 
                          (om later nog steeds reservaties terug te vinden)
self.tijdstip: integer (= 0 default)  (geeft weer op welk tijdstip het programma zich bevindt)
"""


class Reservatiesysteem:
    def __init__(self):
        """
        Het object Reservatiesysteem wordt aangemaakt.
        precondities: er worden geen parameters gegeven
        postconditie: een Reservatiesysteem object wordt aangemaakt
        """
        """
        :param id counter (universeel)
        :param interne paramater met alle tijdslots
        """

        self.id_counter = 0

        self.films = MyLinkedChain.LinkedChain()
        self.zalen = MyLinkedChain.LinkedChain()
        self.vertoningen = My_BinarySearchTree.BSTTable()

    def maak_gebruiker(self, voornaam, achternaam, mail):
        """
        Maakt een nieuwe gebruiker aan en bewaard die in self.gebruikers

        precondities: er worden 4 parameters gegeven, id is een positieve integer en voornaam, achternaam en mail zijn  strings
        postconditie: er wordt een nieuwe gebruiker aangemaakt en bewaard (de ketting gebruikers wordt 1 groter)

        :param id: integer (id van de gebruiker)
        :param voornaam: string (voornaam van de gebruiker)
        :param achternaam: string (achternaam van de gebruiker)
        :param mail: string (e-amil adres van gebruiker)
        """
        pass

    #private hulpfunctie per klasse die aangeroepen wordt in maak_.... (roept constructor van klasse aan)

    def maak_film(self,titel, rating):
        """
        Maakt een nieuwe film aan en bewaard die in self.films

        precondities: er worden 3 parameters gegeven, id is een positieve integer, titel is een string en rating is een float
        postconditie: er wordt een nieuwe film aangemaakt en bewaard (de ketting films wordt 1 groter)


        :param id: integer (id van film)
        :param titel: string (titel van film)
        :param rating: float (rating van film)
        """
        film_object = Film(self.id_counter, titel, rating)

        self.id_counter += 1

        self.films.insert(0, film_object)

    def maak_zaal(self, nummer, maxplaatsen):
        """
        Maakt een nieuwe zaal aan en bewaard die in self.zaal

        precondities: er worden 2 parameters gegeven, beide zijn positieve integers
        postconditie: er wordt een nieuwe zaal aangemaakt en bewaard (de ketting zalen wordt 1 groter)

        :param nummer: integer (zaalnummer van de zaal)
        :param maxplaatsen: integer (max plaatsen van de zaal)
        """

        zaal_object = Zaal(nummer, maxplaatsen)

        self.zalen.insert(0, zaal_object)

    def maak_vertoning(self, filmid, zaalnummer, slot):
        """
        Maakt een nieuwe vertoning aan en bewaard die in self.vertoningen

        precondities: er worden 4 parameters gegeven, allemaal zijn ze positieve integers
        postconditie: er wordt een nieuwe vertoningen aangemaakt en bewaard (de boom vertoningen wordt 1 groter)

        :param id: integer (id van de vertoning)
        :param filmid: integer (id van de film)
        :param zaalnummer: integer (nummer van de zaal)
        :param slot: integer (tijdslot van vertoning, integer heeft volgend format uurMinuten vb. 23u30 -> 2330)
        """
        vrijePlaatsen = self.zalen.retrieve()
        vertoning_object = Vertoning(self.id_counter, filmid, zaalnummer, slot,)
        self.vertoningen.tableInsert(self.id_counter, vertoning_object)
        pass

    def maak_reservatie(self, vertooningID, hoeveel, tijdstip, gebruikerid):
        """
        Maakt een nieuwe reservatie aan en bewaard die in self.reservaties

        precondities: er worden 4 parameters gegeven, allemaal zijn ze positieve integers
        postconditie: er wordt een nieuwe vertoningen aangemaakt en bewaard (de queue reservaties wordt 1 groter)

        :param vertooningID: integer (id van vertoning)
        :param hoeveel: integer (aantal plaatsen voor reservatie)
        :param tijdstip: integer (tijdstip van reservatie)
        :param gebruikerid: integer (id van de gebruiker dat een reservatie maakt)
        """
        pass

    def get_time(self):
        """
        Geeft het huidige tijdstip terug

        precondities: er worden geen parameters gegeven.
        postconditie: er wordt een integer teruggeven dat het tijdstip weergeeft.
        :return integer (van self.tijdstip) (geeft het huidige tijdstip weer)
        """

        pass

    def convert_date(self):
        """converteert datum naar seconden"""
        pass
    def convert_time(self):
        pass
        """converteert seconden naar daum"""

    def set_time(self, value):
        """
        zet het huidige tijdstip naar een andere waarde

        precondities: er wordt 1 parameter gegeven dat een positieve integer is.
        postconditie: het tijdstip veranderd naar de gegeven waarde

        :param value: integer (nieuwe waarde voor de tijd)
        """
        pass

    def increase_time(self):
        """
        Verhoogd de tijd met 1

        precondities: er worden geen parameter gegeven.
        postconditie: het tijdstip wordt met 1 verhoogd
        """

        pass

    def lees_reservatie(self):
        """
        Lees de reservatie dat eerst staat in de queue

        precondities: er worden geen parameter gegeven.
        postconditie: er wordt een reservatie object teruggeven

        A. getTop of queeue: & check voorwaarden

        1. deque + lokaal opslagen
        2. aantal personen in de zaal verminderen
        3. check vol

        END: voeg toe aan reservatie archive

        :return: reservatie object dat vanvoor aan de queu staat
        :return: of de reservatie succersvol is verwerkt
        """
        pass

    def verlaag_plaatsen(self, vertoningid, plaatsen): #private functie
        """
        Verminderd het aantal vrije plaatsen in een voorstelling.

        precondities: er zijn voldoende plaatsen in de vertoning
        postconditie: het aantal plaatsen van de vertoning dat overeenkomt met het vertoning id
                      wordt verminderd met het gegeven aantal plaatsen

        :param vertoningid: integer (id van de vertoning)
        :param plaatsen: integer (aantal plaatsen dat niet meer beschikbaar zijn)
        """
        pass

    def verwijder_reservatie(self): #private function
        """
        verwijder de reservatie van voren aan de queue en bewaar die in het reservatie archief

        precondities: er worden geen parameters gegeven en de queue is niet leeg
        postconditie: de queue self.reservaties wordt 1 kleiner en self.reservatie_archief wordt 1 groter.
        """

        pass

    def verwijder_vertoningen(self):
        """
        Verwijdert alle vertoningen

        precondities: er worden geen parameters gegeven
        postconditie: er bestaan geen vertoningen meer
        """

        """maak nieuwe ketting, overschrijf huidige ketting"""
        pass

    def verwijder_films(self):
        """
        Verwijdert alle films

        precondities: er worden geen parameters gegeven
        postconditie: er bestaan geen vertoningen meer
        """
        """maak nieuwe ketting, overschrijf huidige ketting"""
        self.films = MyLinkedChain.LinkedChain()

    def verwijder_gebruikers(self):
        """
        Verwijdert alle gebruikers

        precondities: er worden geen parameters gegeven
        postconditie: er bestaan geen vertoningen meer
        """
        """maak nieuwe ketting, overschrijf huidige ketting"""
        pass



