from ADT import MyCircularLinkedChainAnas , MyQueue_LinkedKars , MyQueueLinkedTibo , My_BinarySearchTreeAnas
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
        """
        """
        :param id counter (universeel)
        :param interne paramater met alle tijdslots
        :param **kwargs, kan "displaymode" bevatten die weergeeft hoe we de data weergeven
        """

        self.display_mode = None
        if "display_mode" in kwargs:
            self.display_mode = kwargs["display_mode"]

        self.tijdsstip = 0

        self.films = MyCircularLinkedChainAnas.LCTable() # dit moet veranderd worden naar de table, ik noem mijn table LCtable: Subject to be changed
        self.zalen = MyCircularLinkedChainAnas.LCTable()
        self.gebruikers = MyCircularLinkedChainAnas.LCTable()
        self.vertoningen = My_BinarySearchTreeAnas.BSTTable()
        self.reservaties = MyQueue_LinkedKars.MyQueue()
        self.reservatie_archief = MyCircularLinkedChainAnas.LCTable()
        self.logs = MyCircularLinkedChainAnas.LCTable() #Opslag van Log Strings

        """init voor InputParser"""
        if "path" in kwargs:
            self.instruction_parser = InstructionParser(self, MyQueueLinkedTibo.MyQueueTable(), path=kwargs["path"])
        else:
            self.instruction_parser = InstructionParser(self, MyQueueLinkedTibo.MyQueueTable())
        self.instruction_parser.read_file()

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
        newGebruiker = Gebruiker(id , voornaam, achternaam, mail)
        self.gebruikers.tableInsert(1, newGebruiker)

    #private hulpfunctie per klasse die aangeroepen wordt in maak_.... (roept constructor van klasse aan)

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

    def maak_vertoning(self, id, zaalnummer, slot, datum, filmid): # contract moet veranderd worden, of zelfs heel de methode
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

        if not self.films.tableRetrieveTranverse(filmid): # subject to change: LinkedChain retrieve probleem
            return False

        if isinstance(filmid, int) and isinstance(zaalnummer, int) and isinstance(slot, int) and filmid >= 0 and zaalnummer >= 0 and slot >= 0:
            vrije_plaatsen = self.zalen.tableRetrieveTranverse(zaalnummer)  # moet waarschijnlijk veranderd worden naar tableRetrieve
            vertoning_object = Vertoning(id, zaalnummer, slot, datum, filmid, vrije_plaatsen)
            self.vertoningen.tableInsert(id, vertoning_object)
            return True  # contract moet aangepast worden return
        return False

    def maak_reservatie(self, id , vertoning_id, aantal_plaatsen, tijdstip, gebruiker_id):
        self.display(f"maakt reservatie: {vertoning_id} {aantal_plaatsen} {tijdstip} {gebruiker_id}")
        """
        Maakt een nieuwe reservatie aan en bewaard die in self.reservaties

        precondities: er worden 4 parameters gegeven, allemaal zijn ze positieve integers
        postconditie: er wordt een nieuwe reser aangemaakt en bewaard (de queue reservaties wordt 1 groter)

        :param vertoning_id: integer>0 (id van vertoning) De vertoning met het bijbehorende ID moet bestaan. 
        :param aantal_plaatsen: integer>=0 (aantal plaatsen voor reservatie) 
        :param tijdstip: integer>=0 (tijdstip van reservatie)
        :param gebruiker_id: integer>=0 (id van de gebruiker dat een reservatie maakt). De gebruiker moet bestaan met het bijbehorende ID. 
        """

        # Subject to be changed: aantal_plaatsen; wanneer controleren?
        # Question: Gebruiker zelf geeft wel handmatig een datum is, we would still need the convert-option?

        if not isinstance(vertoning_id, int) and isinstance(aantal_plaatsen, int) and isinstance(tijdstip,int) and isinstance(gebruiker_id,int) and vertoning_id >= 0 and aantal_plaatsen > 0 and gebruiker_id >= 0 and tijdstip>=0:
            raise Exception("Precondition Error: maak_reservatie")

        if not self.vertoningen.tableRetrieve(vertoning_id): #MODULARITY ERROR: Zouden we hier bv geen object in kunnen stoppen? En dan de wrapper het laten oplossen?
            raise Exception("Precondition Error: maak_reservatie, vertoning bestaat niet")

        if not self.gebruikers.tableRetrieveTranverse(gebruiker_id): #Zou dit niet nog een subscript operator moeten hebben "[1]" ?
            raise Exception("Precondition Error: maak_reservatie, gebruiker bestaat niet")

        #Kijk of er plek is in de zaal, bij het aanmaken van de reservatie, verlaag vervolgens het gereserveerd aantal plaatsen

        reservatie = Reservatie(id,vertoning_id, aantal_plaatsen, tijdstip, gebruiker_id)
        self.reservaties.enqueue(reservatie)
        return True

    def get_time(self): #Private
        """
        Geeft het huidige tijdstip terug

        precondities: er worden geen parameters gegeven.
        postconditie: er wordt een integer teruggeven dat het tijdstip weergeeft.
        :return integer (van self.tijdstip) (geeft het huidige tijdstip weer)
        """
        return self.tijdsstip

    def convert_date(self, datum, hour, minutes, seconds): #Private
        """converteert datum naar seconden

        preconditie: datum is een string en hour, minutes, seconds zijn integers (de datum bestaat)
        postconditie: er wordt een integer teruggegeven waarbij de eerste 8 cijfers de datum voorstellen, en de rest stelt hour:minutes:seconds in seconden voor
        """
        if not isinstance(datum, str) and isinstance(hour, int) and isinstance(minutes, int) and isinstance(seconds, int):
            raise Exception("Precondition error: fout type argument in convert_date")
        splitted_datum = datum.split("-")
        jaar = splitted_datum[0]
        maand = splitted_datum[1]
        dag = splitted_datum[2]     #nieuwe functie om te controleren of een datum geldig is? misschien overbodig
        total = jaar+maand+dag+str(hour*3600+minutes*60+seconds)
        total = int(total)
        return total

    def convert_time(self, tijd): #Private
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
        hours = seconds//3600
        minutes = (seconds-hours*3600)//60
        seconds = seconds - hours*3600 - minutes*60
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
        """
        Lees de oudste reservatie uit en verwerkt deze.

        precondities: Er worden geen parameters ingegeven.
        postconditie: De reservatie is succesvol verwerkt. De vertoning heeft een aangepast aantal vrije_plaatsen.

        A. getTop of queeue: & check voorwaarden

        1. deque + lokaal opslagen
        2. aantal personen in de zaal verminderen
        3. check vol
        4. END: voeg toe aan reservatie archive

        :return: bool:succes
        """
        reservatie = self.reservaties.getFront()[1]
        tijdstip = self.reservaties.getFront()[0]
        vertoning = self.vertoningen.tableRetrieve(reservatie.vertoning_id) #Hier wordt nu gezocht op ID, NOT MODULAIR

        # Verwijder reservatie & voeg toe aan archief
        self.verwijder_reservatie()
        #self.verlaag_plaatsen(id,reservatie.aantal_plaatsen) #Subject to be changed: Verlaag het (fysiek) aantal plaatsen

        # Update datum & tijd
        self.set_time(tijdstip)

        #Welke output moet dit outten in de console ter verificatie // Voor de log file?

        # Subject to be changed: Kijk of de vertoning gestart kan worden?
        self.start(reservatie.vertoning_id)
        return True

    def archiveer_reservatie(self): #private function
        """
        verwijder de reservatie van voren aan de queue en bewaar die in het reservatie archief

        precondities: er worden geen parameters gegeven en de queue is niet leeg
        postconditie: de queue self.reservaties wordt 1 kleiner en self.reservatie_archief wordt 1 groter.
        """
        if not self.reservaties.isEmpty():
            reservatie = self.reservaties.dequeue() #Dequeu
            self.reservatie_archief.insert(self.reservatie_archief.getLength(),reservatie) #Insert reservatie
            return True
        else:
            raise Exception("Precondition Failure: archiveer_reservatie | Er is geen reservatie meer om te archiveren. De queue is leeg")
            return False

    def lees_ticket(self, vertoningid, aantal_mensen):
        #Roept Vertoning Lees Ticket aan = String
        #self.logs.insert(String)
        pass

    def verlaag_plaatsenVirtueel(self, vertoningid, plaatsen): #private functie
        """
        Verminderd het aantal vrije plaatsen in een voorstelling.

        precondities: er zijn voldoende plaatsen in de vertoning
        postconditie: het aantal plaatsen van de vertoning dat overeenkomt met het vertoning id
                      wordt verminderd met het gegeven aantal plaatsen

        :param vertoningid: integer (id van de vertoning)
        :param plaatsen: integer (aantal plaatsen dat niet meer beschikbaar zijn)
        """

        #To be changed: Whole function

        vertoning = self.vertoningen.tableRetrieve(vertoningid)

        vol = vertoning.verminder_plaatsenVirtueel(plaatsen)

        if not vol:
            raise Exception("Geen plek meer in deze zaal")         #To discuss: Dit toch checken voordat we uitlezen? Moeten we dit ergens aangeven?

        return vol

    def verlaag_plaatsenFysiek(self, vertoningid, plaatsen): #private functie
        """
        Verminderd het aantal vrije plaatsen in een voorstelling.

        precondities: er zijn voldoende plaatsen in de vertoning
        postconditie: het aantal plaatsen van de vertoning dat overeenkomt met het vertoning id
                      wordt verminderd met het gegeven aantal plaatsen

        :param vertoningid: integer (id van de vertoning)
        :param plaatsen: integer (aantal plaatsen dat niet meer beschikbaar zijn)
        """

        #To be changed: Whole function

        vertoning = self.vertoningen.tableRetrieve(vertoningid) # technisch gezien zou dit nooit een vol melding moeten geven als verlaagplaatsen virtueel correct werkt
                                                                # behalve het geval dat mensen komen opdagen die niet geresveerd hebben en met te veel komen
        vol = vertoning.verminder_plaatsenFysiek(plaatsen)

        if vol:
            if vertoning.check_vol():
                self.start(vertoningid)

        if not vol:
            self.start(vertoningid)       #To discuss: Dit toch checken voordat we uitlezen? Moeten we dit ergens aangeven?

        return vol

    def start(self, vertoningid): #Public
        """
        Start de vertoning
        preconditie: De vertoning start op het juiste tijdstip en er mag geen andere vertoning bezig zijn in deze zaal
        postconditie: De vertoning wordt gestart (gestart = true)
        """

        """Roept vertoning start aan"""
        if self.vertoningen.tableRetrieve(vertoningid)[1]: # ik denk dat een vertoning nooit kan overlappen door het slot systeem en altijd stop bij de volgende slot.
            vertoning_object = self.vertoningen.tableRetrieve(vertoningid)[0]
            vertoning_object.start()
            return True
        raise Exception("Vertoning bestaat niet")

    def stop(self, vertoningid): #Public
        """
        Stopt de vertoning
        preconditie: De film moet al gestart zijn
        postconditie: De vertoning wordt beëindigd (gestart = false)
        """
        if self.vertoningen.tableRetrieve(vertoningid)[1]: # ik denk dat een vertoning nooit kan overlappen door het slot systeem en altijd stop bij de volgende slot.
            vertoning_object = self.vertoningen.tableRetrieve(vertoningid)[0]
            vertoning_object.stop()
            return True
        raise Exception("Vertoning bestaat niet")

    def retrieveFilm(self, id): # interne functie. wij moeten nog bespreken hoe we dit soort functies regelen
        """

        :param id:
        :return:
        """
        l = self.films.save()
        for w in l:
            if w.id == id:  # optioneel: dit zou een getter moeten zijn in het geval de datatype naam van self.id verandert. koppeling van software engineering
                return w

    def retrieveZaal(self, id): # interne functie. wij moeten nog bespreken hoe we dit soort functies regelen
        """

        :param id:
        :return:
        """
        l = self.zalen.save()
        for w in l:
            if w.zaalnummer == id: # optioneel: dit zou een getter moeten zijn in het geval de datatype naam van self.zaalnummer verandert. koppeling van software engineering
                return w

    def verwijder_vertoningen(self):
        """
        Verwijdert alle vertoningen

        precondities: er worden geen parameters gegeven
        postconditie: er bestaan geen vertoningen meer
        """

        """maak nieuwe ketting, overschrijf huidige ketting"""
        #self.vertoningen.clear()
        pass

    def verwijder_films(self):
        """
        Verwijdert alle films

        precondities: er worden geen parameters gegeven
        postconditie: er bestaan geen vertoningen meer
        """
        """maak nieuwe ketting, overschrijf huidige ketting"""
        self.films.clear()

    def verwijder_gebruikers(self):
        """
        Verwijdert alle gebruikers

        precondities: er worden geen parameters gegeven
        postconditie: er bestaan geen vertoningen meer
        """
        """maak nieuwe ketting, overschrijf huidige ketting"""
        self.gebruikers.clear()

    def display(self, msg):
        """private function"""
        if self.display_mode == "print":
            print(msg)



r = Reservatiesysteem(display_mode="print")
