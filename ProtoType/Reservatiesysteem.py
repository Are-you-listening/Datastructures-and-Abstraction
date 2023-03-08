from ADT import MyCircularLinkedChainAnas, MyQueueKars, MyQueueTibo, MyBSTAnas, MyStackKars
from Film import Film
from Zaal import Zaal
from Vertoning import Vertoning
from Reservatie import Reservatie
from Gebruiker import Gebruiker
from InstructionParser import InstructionParser

"""
Deze ADT geeft een reservatiesysteem weer dat gebruik maakt van de andere ADT

data:
self.vertoningen: Boom van Vertoning objecten (de aangemaakte vertoningen worden hier bewaard)
self.films: ketting van Film objecten (de aangemaakte film worden hier bewaard)
self.zalen: ketting van Zaal objecten (de aangemaakte zaal worden hier bewaard)
self.gebruikers: ketting van aangemaakte Gebruiker objecten (de aangemaakte gebruiker worden hier bewaard)
self.reservaties: queue van tupels(tijdstip,aangemaakte Reservatie Objecten)
self.reservaties_archief: ketting van aangemaakte Reservatie objecten die niet meer in de queue zitten 
                          (om later nog steeds reservaties terug te vinden)
self.tijdstip: integer (= 0 default)  (geeft weer op welk tijdstip het programma zich bevindt)
"""


class Reservatiesysteem:
    def __init__(self, **kwargs):
        """
        Het object Reservatiesysteem wordt aangemaakt.
        precondities: er worden geen parameters gegeven
        postconditie: een Reservatiesysteem object wordt aangemaakt

        :param id counter (universeel)
        :param interne paramater met alle tijdslots
        :param **kwargs, kan "displaymode" bevatten die weergeeft hoe we de data weergeven
        """
        self.display_mode = None
        if "display_mode" in kwargs:
            self.display_mode = kwargs["display_mode"]

        self.tijdsstip = 0

        self.films = MyCircularLinkedChainAnas.LCTable()  # dit moet veranderd worden naar de table, ik noem mijn table LCtable: Subject to be changed
        self.zalen = MyCircularLinkedChainAnas.LCTable()
        self.gebruikers = MyCircularLinkedChainAnas.LCTable()
        self.vertoningen = MyBSTAnas.BSTTable()
        self.reservaties = MyQueueKars.MyQueueTable()
        self.reservatie_archief = MyCircularLinkedChainAnas.LCTable()
        
        """init voor InputParser"""
        if "path" in kwargs:
            self.instruction_parser = InstructionParser(self, MyQueueTibo.MyQueueTable(), path=kwargs["path"])
        else:
            self.instruction_parser = InstructionParser(self, MyQueueTibo.MyQueueTable())
        self.instruction_parser.read_file()
        self.instruction_parser.main_thread()

    def maak_gebruiker(self, id, voornaam, achternaam, mail):
        self.display(f"maak gebruiker: {voornaam} {achternaam} {mail}")
        """
        Maakt een nieuwe gebruiker aan en bewaard die in self.gebruikers

        precondities: er worden 4 parameters gegeven, id is een positieve integer en voornaam, achternaam en mail zijn  strings
        postconditie: er wordt een nieuwe gebruiker aangemaakt en bewaard (de ketting gebruikers wordt 1 groter)

        :param id: integer (id van de gebruiker)
        :param voornaam: string (voornaam van de gebruiker)
        :param achternaam: string (achternaam van de gebruiker)
        :param mail: string (e-mail adres van gebruiker)
        """
        newGebruiker = Gebruiker(id, voornaam, achternaam, mail)
        self.gebruikers.tableInsert(1, newGebruiker)

    def maak_film(self, filmid, titel, rating):
        """
        Maakt een nieuwe film aan en bewaard die in self.films

        precondities: er worden 3 parameters gegeven, id is een positieve integer, titel is een string en rating is een float
        postconditie: er wordt een nieuwe film aangemaakt en bewaard (de ketting films wordt 1 groter)


        :param id: integer (id van film)
        :param titel: string (titel van film)
        :param rating: float (rating van film)
        """

        if not (isinstance(filmid, int) and isinstance(titel, str) and isinstance(rating, float) and filmid >= 0):
            raise Exception("Precondition Failed: in maak_film")

        self.display(f"maakt film {titel} {rating}")

        film_object = Film(filmid, titel, rating)

        self.films.tableInsert(1, film_object)

    def maak_zaal(self, nummer, maxplaatsen):

        """
        Maakt een nieuwe zaal aan en bewaard die in self.zaal

        precondities: er worden 2 parameters gegeven, beide zijn positieve integers
        postconditie: er wordt een nieuwe zaal aangemaakt en bewaard (de ketting zalen wordt 1 groter)

        :param nummer: integer (zaalnummer van de zaal)
        :param maxplaatsen: integer (max plaatsen van de zaal)
        """

        if not (isinstance(nummer, int) and isinstance(maxplaatsen, int) and nummer >= 0 and maxplaatsen >= 0):
            raise Exception("Precondition Failed: in maak_zaal")

        self.display(f"maakt zaal {nummer} {maxplaatsen}")

        zaal_object = Zaal(nummer, maxplaatsen)

        self.zalen.tableInsert(1, zaal_object)

    def maak_vertoning(self, id, zaalnummer, slot, datum, filmid,vrije_plaatsen):  # contract moet veranderd worden, of zelfs heel de methode
        self.display(f"maakt vertoning: {zaalnummer} {slot} {datum} {filmid}")
        """
        Maakt een nieuwe vertoning aan en bewaard die in self.vertoningen

        precondities: er worden 3 parameters gegeven, allemaal zijn ze positieve integers
        postconditie: er wordt een nieuwe vertoningen aangemaakt en bewaard (de boom vertoningen wordt 1 groter)

        :param filmid: integer (id van de film)
        :param zaalnummer: integer (nummer van de zaal)
        :param slot: integer (tijdslot van vertoning, integer heeft volgend format uurMinuten vb. 23u30 -> 2330)
        """
        if not self.zalen.tableRetrieveTranverse(zaalnummer):
            return False

        if not self.films.tableRetrieveTranverse(filmid):  # subject to change: LinkedChain retrieve probleem
            return False

        if isinstance(filmid, int) and isinstance(zaalnummer, int) and isinstance(slot,
                                                                                  int) and filmid >= 0 and zaalnummer >= 0 and slot >= 0:
            vertoning_object = Vertoning(id, zaalnummer, slot, datum, filmid, vrije_plaatsen)
            stack = MyStackKars.MyStackTable()
            self.vertoningen.tableInsert(id, (vertoning_object,stack) ) # kijk uit met tuple van drie waarden, vraag meneer als dit mag

            return True  # contract moet aangepast worden return
        return False

    def maak_reservatie(self, id, vertoning_id, aantal_plaatsen, tijdstip, gebruiker_id):
        """
        Maakt een nieuwe reservatie aan en bewaard die in self.reservaties

        precondities: er worden 4 parameters gegeven, allemaal zijn ze positieve integers
        postconditie: er wordt een nieuwe reser aangemaakt en bewaard (de queue reservaties wordt 1 groter)

        :param vertoning_id: integer>0 (id van vertoning) De vertoning met het bijbehorende ID moet bestaan. 
        :param aantal_plaatsen: integer>=0 (aantal plaatsen voor reservatie) 
        :param tijdstip: integer>=0 (tijdstip van reservatie)
        :param gebruiker_id: integer>=0 (id van de gebruiker dat een reservatie maakt). De gebruiker moet bestaan met het bijbehorende ID. 
        """
        self.display(f"maakt reservatie: {vertoning_id} {aantal_plaatsen} {tijdstip} {gebruiker_id}")

        if not isinstance(vertoning_id, int) and isinstance(aantal_plaatsen, int) and isinstance(tijdstip,
                                                                                                 int) and isinstance(
                gebruiker_id,
                int) and vertoning_id >= 0 and aantal_plaatsen > 0 and gebruiker_id >= 0 and tijdstip >= 0:
            raise Exception("Precondition Error: maak_reservatie")

        if not self.vertoningen.tableRetrieve(vertoning_id):
            raise Exception("Precondition Error: maak_reservatie, vertoning bestaat niet")

        if not self.gebruikers.tableRetrieveTranverse(gebruiker_id):  # Subscript operator?
            raise Exception("Precondition Error: maak_reservatie, gebruiker bestaat niet")

        ReservatieItem = (tijdstip, Reservatie(id, vertoning_id, aantal_plaatsen, tijdstip, gebruiker_id))
        self.reservaties.tableInsert(ReservatieItem)

        return True

    def get_time(self):  # Private
        """
        Geeft het huidige tijdstip terug

        precondities: er worden geen parameters gegeven.
        postconditie: er wordt een integer teruggeven dat het tijdstip weergeeft.
        :return integer (van self.tijdstip) (geeft het huidige tijdstip weer)
        """
        return self.tijdsstip

    def convert_date(self, datum, hour, minutes, seconds):  # Private
        """converteert datum naar seconden

        preconditie: datum is een string en hour, minutes, seconds zijn integers (de datum bestaat)
        postconditie: er wordt een integer teruggegeven waarbij de eerste 8 cijfers de datum voorstellen, en de rest stelt hour:minutes:seconds in seconden voor
        """
        if not isinstance(datum, str) and isinstance(hour, int) and isinstance(minutes, int) and isinstance(seconds,
                                                                                                            int):
            raise Exception("Precondition error: fout type argument in convert_date")
        splitted_datum = datum.split("-")
        jaar = splitted_datum[0]
        maand = splitted_datum[1]
        dag = splitted_datum[2]  # nieuwe functie om te controleren of een datum geldig is? misschien overbodig
        total = jaar + maand + dag + str(hour * 3600 + minutes * 60 + seconds)
        total = int(total)
        return total

    def convert_time(self, tijd):  # Private
        pass
        """converteert seconden naar datum

        preconditie: het argument tijd is een positieve integer waarbij de eerste digits jjjjmmdd zijn, de rest is de tijd in seconden
        postconditie: de tijd wordt omgezet en gereturned
        """
        if not isinstance(tijd, int):
            raise Exception("Precondition error: tijd is niet van type int in convert_time")
        if tijd < 0:
            raise Exception("Precondition error: tijd kan niet negatief zijn in convert_time")
        temp = str(tijd)
        datum = f"{temp[:4]}-{temp[4:6]}-{temp[6:8]}"
        seconds = int(temp[8:])
        hours = seconds // 3600
        minutes = (seconds - hours * 3600) // 60
        seconds = seconds - hours * 3600 - minutes * 60
        return (datum, hours, minutes, seconds)

    def set_time(self, tijd):
        """
        zet het huidige tijdstip naar een andere waarde

        precondities: er wordt 1 parameter gegeven dat een positieve integer is.
        postconditie: het tijdstip veranderd naar de gegeven waarde

        :param value: integer (nieuwe waarde voor de tijd)
        """
        if not isinstance(tijd, int):
            raise Exception("Precondition error: tijd is niet van type int in set_time")
        if tijd < 0:
            raise Exception("Precondition error: tijd kan niet negatief zijn in set_time")
        self.tijdsstip = tijd

    def lees_reservatie(self):
        self.display(f"leest reservatie")
        """
        Lees de reservaties uit self.reservaties en verwerkt deze.

        precondities: Er worden geen parameters ingegeven. self.reservaties bevat enkel reservaties van eenzelfde tijdstip. self.verlaag_plaatsenVirtueel controleert autonoom of dat er plek is in het systeem.
        postconditie: De reservatie is succesvol verwerkt en toegevoegd aan het archief. De vertoning heeft eventueel een aangepast aantal vrije_plaatsen.

        :return: bool:succes
        """
        while self.reservaties.tableIsEmpty() == False:
            reservatie = self.reservaties.tableFirst()[0][1]
            tijdstip = self.reservaties.tableFirst()[0][0]

            # Verlaag virtuele plaatsen (Independent of dit slaagt of niet)
            self.verhoog_plaatsenVirtueel(reservatie.vertoning_id, reservatie.aantal_plaatsen)

            # Verwijder reservatie & voeg toe aan archief
            self.archiveer_reservatie()

            # Update datum & tijd
            self.set_time(tijdstip)

        return True

    def archiveer_reservatie(self):  # Private function
        """
        Verplaats de reservatie van voor uit self.reservaties naar self.reservaties_archief.

        precondities: Er worden geen parameters ingegeven.
        postconditie: self.reservaties wordt 1 kleiner en self.reservatie_archief wordt 1 groter.
        """
        reservatie = self.reservaties.tableDelete()[0]  # Dequeu
        self.reservatie_archief.tableInsert(1, reservatie)  # Insert reservatie

    def lees_ticket(self, vertoningid, aantal_mensen):  # To be discussed: Private Function?


        #Verlaag aantal plaatsen & chance stack
        self.verlaag_plaatsenFysiek(vertoningid,aantal_mensen)

        #Push back logs
        print("["+self.convert_time(self.tijdsstip)+"] De vertoning met ID: "+vertoningid+" is verlaagd met: "+aantal_mensen)

    def verhoog_plaatsenVirtueel(self, vertoningid, plaatsen):  # private functie
        """
        Verminderd het aantal vrije plaatsen in een voorstelling.

        precondities: er zijn voldoende plaatsen in de vertoning
        postconditie: het aantal plaatsen van de vertoning dat overeenkomt met het vertoning id
                      wordt verminderd met het gegeven aantal plaatsen

        :param vertoningid: integer (id van de vertoning)
        :param plaatsen: integer (aantal plaatsen dat niet meer beschikbaar zijn)
        """
        for i in range(plaatsen):
            self.vertoningen.tableRetrieve(vertoningid)[0][1].tableInsert(i)  #[0] = value-type, hiervan [1]: de stack

        return self.vertoningen.tableRetrieve(vertoningid)[0][0].verminder_plaatsenVirtueel(plaatsen)

    def verlaag_plaatsenFysiek(self, vertoningid, plaatsen):  # private functie
        """
        Verminderd het aantal vrije plaatsen in een voorstelling.

        precondities: er zijn voldoende plaatsen in de vertoning
        postconditie: het aantal plaatsen van de vertoning dat overeenkomt met het vertoning id
                      wordt verminderd met het gegeven aantal plaatsen

        :param vertoningid: integer (id van de vertoning)
        :param plaatsen: integer (aantal plaatsen dat niet meer beschikbaar zijn)
        """

        # To be changed: Whole function
        vol =self.vertoningen.tableRetrieve(vertoningid)[0][0].verhoog_plaatsenfysiek(plaatsen)
        if vol:
            for i in range(plaatsen):
                self.vertoningen.tableRetrieve(vertoningid)[0][1].tablePop()
            return
        raise Exception("Stack overflow")


    def start(self, vertoningid):  # Public
        """
        Start de vertoning
        preconditie: De vertoning start op het juiste tijdstip en er mag geen andere vertoning bezig zijn in deze zaal
        postconditie: De vertoning wordt gestart (gestart = true)
        """

        """Roept vertoning start aan"""
        if self.vertoningen.tableRetrieve(vertoningid)[1]:  # ik denk dat een vertoning nooit kan overlappen door het slot systeem en altijd stop bij de volgende slot.
            vertoning_object = self.vertoningen.tableRetrieve(vertoningid)[0]
            vertoning_object.start()
            return True
        raise Exception("Vertoning bestaat niet")

    def stop(self, vertoningid):  # Public
        """
        Stopt de vertoning
        preconditie: De film moet al gestart zijn
        postconditie: De vertoning wordt beëindigd (gestart = false)
        """
        if self.vertoningen.tableRetrieve(vertoningid)[
            1]:  # ik denk dat een vertoning nooit kan overlappen door het slot systeem en altijd stop bij de volgende slot.
            vertoning_object = self.vertoningen.tableRetrieve(vertoningid)[0]
            vertoning_object.stop()
            return True
        raise Exception("Vertoning bestaat niet")

    def retrieveFilm(self, id):  # interne functie. wij moeten nog bespreken hoe we dit soort functies regelen
        """
        :param id:
        :return:
        """
        l = self.films.save()
        for w in l:
            if w.id == id:  # optioneel: dit zou een getter moeten zijn in het geval de datatype naam van self.id verandert. koppeling van software engineering
                return w

    def retrieveZaal(self, id):  # interne functie. wij moeten nog bespreken hoe we dit soort functies regelen
        """
        :param id:
        :return:
        """
        l = self.zalen.save()
        for w in l:
            if w.zaalnummer == id:  # optioneel: dit zou een getter moeten zijn in het geval de datatype naam van self.zaalnummer verandert. koppeling van software engineering
                return w

    def verwijder_vertoningen(self):
        """
        Verwijdert alle vertoningen.

        precondities: Er worden geen parameters ingegeven.
        postconditie: self.vertoningen is gecleared.
        """
        self.vertoningen.clear()

    def verwijder_films(self):
        """
        Verwijdert alle films.

        precondities: Er worden geen parameters ingegeven
        postconditie: self.films is gecleared.
        """
        self.films.clear()

    def verwijder_gebruikers(self):
        """
        Verwijdert alle gebruikers

        precondities: Er worden geen parameters ingegeven
        postconditie: self.gebruikers is gecleared.
        """
        self.gebruikers.clear()

    def display(self, msg):
        """private function"""
        if self.display_mode == "print":
            print(msg)

    def log(self):

        pass


r = Reservatiesysteem(display_mode="print")
