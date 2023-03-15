from ADT import MyBSTAnas, MyCircularLinkedChainAnas, MyQueueAnas, MyRedBlackTreeAnas, MyStackAnas
from ADT import MyBSTEmil, MyCircularLinkedChainEmil, MyQueueEmil, MyTwoThreeFourTreeEmil, MyStackEmil
from ADT import MyBSTKars, MyCircularLinkedChainKars, MyQueueKars, MyTwoThreeFourTreeKars, MyStackKars
from ADT import MyBSTTibo, MyCircularLinkedChainTibo, MyQueueTibo, MyTwoThreeFourTreeTibo, MyStackTibo

from Film import Film
from Zaal import Zaal
from Vertoning import Vertoning
from Reservatie import Reservatie
from Gebruiker import Gebruiker
from InstructionParser import InstructionParser
from Log import Log

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

        self.tijdsstip = 0 #Houdt het tijdstip bij
        self.films = MyCircularLinkedChainAnas.LCTable() #Verzameling van alle films
        self.zalen = MyCircularLinkedChainAnas.LCTable() #Bijhouden van alle zalen
        self.gebruikers = MyCircularLinkedChainAnas.LCTable() #Bijhouden van alle gebruikers
        self.vertoningen = MyBSTAnas.BSTTable() #Bijhouden van alle vertoningen
        self.reservaties = MyQueueKars.MyQueueTable() #Bijhouden van alle TE verwerken reservaties
        self.reservatie_archief = MyCircularLinkedChainAnas.LCTable() #Opslaan van alle verwerkte reservaties
        self.slots = MyCircularLinkedChainTibo.LCTable() #Bijhouden van tijdslots

        self.slots.load([14*3600+30*60,17*3600,20*3600,22*3600+30*60])  #14:30 	17:00 	20:00 	22:30 #Initaliseert de huidige slots

        self.stack_string = "MyStackKars.MyStackTable()"
        self.log_string = "MyBSTAnas.BSTTable()"
        self.ip_string = "MyQueueTibo.MyQueueTable()"

        if "adt_args" in kwargs:
            adt_args = kwargs["adt_args"]
            self.films = eval(adt_args[0])
            self.zalen = eval(adt_args[1])
            self.gebruikers = eval(adt_args[2])
            self.vertoningen = eval(adt_args[3])
            self.reservaties = eval(adt_args[4])
            self.reservatie_archief = eval(adt_args[5])
            self.slots = eval(adt_args[6])
            self.ip_string = adt_args[7]
            self.stack_string = adt_args[8]
            self.log_string = adt_args[9]

        """init voor InputParser"""
        if "path" in kwargs:
            self.instruction_parser = InstructionParser(self, eval(self.ip_string), path=kwargs["path"])
        else:
            self.instruction_parser = InstructionParser(self, eval(self.ip_string))
        self.instruction_parser.read_file()
        self.instruction_parser.main_thread()

    def maak_gebruiker(self, id, voornaam, achternaam, mail):
        self.__display(f"maak gebruiker: {voornaam} {achternaam} {mail}")
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

        self.__display(f"maakt film {titel} {rating}")

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

        self.__display(f"maakt zaal {nummer} {maxplaatsen}")

        zaal_object = Zaal(nummer, maxplaatsen)

        self.zalen.tableInsert(1, zaal_object)

    def maak_vertoning(self, id, zaalnummer, slot, datum, filmid, vrije_plaatsen):  # contract moet veranderd worden, of zelfs heel de methode
        """
        Maakt een nieuwe vertoning aan en bewaard die in self.vertoningen.

        :param id: unsigned integer (een nieuw uniek id voor de vertoning)
        :param filmid: integer (id van de film)
        :param zaalnummer: integer (nummer van de zaal)
        :param slot: integer (tijdslot van vertoning, integer heeft volgend format uurMinuten vb. 23u30 -> 2330)


        Precondities: Er worden 3 parameters gegeven, allemaal zijn ze positieve integers. Het tijdslot moet bestaan/al zijn toegevoegd. De film met filmid moet bestaan. De zaal met zaalnummer moet bestaan
        Postconditie: Er wordt een nieuwe vertoningen aangemaakt en bewaard (de boom vertoningen wordt 1 groter).
        """
        self.__display(f"maakt vertoning: {zaalnummer} {slot} {datum} {filmid}")
        if not self.zalen.tableRetrieveTranverse(zaalnummer):
            return False

        if not self.films.tableRetrieveTranverse(filmid):  # subject to change: LinkedChain retrieve probleem
            return False

        if isinstance(filmid, int) and isinstance(zaalnummer, int) and isinstance(slot,
                                                                                  int) and filmid >= 0 and zaalnummer >= 0 and slot >= 0:

            slot = self.slots.tableRetrieve(slot)[0] #Vraag tijd van het slot op
            vertoning_object = Vertoning(id, zaalnummer, slot, datum, filmid, vrije_plaatsen)
            stack = eval(self.stack_string)
            self.vertoningen.tableInsert(id, (vertoning_object,stack) )

            return True  # contract moet aangepast worden return
        return False

    def maak_reservatie(self, id, vertoning_id, aantal_plaatsen, tijdstip, gebruiker_id):
        """
        Maakt een nieuwe reservatie aan en bewaard die in self.reservaties

        :param vertoning_id: integer>0 (id van vertoning) De vertoning met het bijbehorende ID moet bestaan.
        :param aantal_plaatsen: integer>=0 (aantal plaatsen voor reservatie)
        :param tijdstip: integer>=0 (tijdstip van reservatie)
        :param gebruiker_id: integer>=0 (id van de gebruiker dat een reservatie maakt). De gebruiker moet bestaan met het bijbehorende ID.

        Precondities: Er worden 4 parameters gegeven, allemaal zijn ze positieve integers
        Postconditie: Er wordt een nieuwe reservatie aangemaakt en bewaard (de queue reservaties wordt 1 groter)
        """
        self.__display(f"maakt reservatie: {vertoning_id} {aantal_plaatsen} {tijdstip} {gebruiker_id}")

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

    def __get_time(self):
        """
        Geeft het huidige tijdstip terug.:return integer (van self.tijdstip) (geeft het huidige tijdstip weer)

        Precondities: Er worden geen parameters gegeven.
        Postconditie: Er wordt een integer teruggeven dat het tijdstip weergeeft in seconden.
        """
        return self.tijdsstip

    def convert_date(self, *args):  # Private
        """
        Converteert een datum naar seconden.

        ::param *args: kan ofwel van de vorm {datum, hour, minutes, seconds} of {hour, minutes, seconds} zijn

        Preconditie: datum is een string en hour, minutes, seconds zijn integers (de datum bestaat)
        Postconditie: er wordt een integer teruggegeven waarbij de eerste 8 cijfers de datum voorstellen, en de rest stelt hour:minutes:seconds in seconden voor
        """
        if len(args) == 4:
            datum = args[0]
            splitted_datum = datum.split("-")
            jaar = splitted_datum[0]
            maand = splitted_datum[1]
            dag = splitted_datum[2]
            total = jaar + maand + dag
            hour = args[1]
            minutes = args[2]
            seconds = args[3]

        else:
            total = ""
            hour = args[0]
            minutes = args[1]
            seconds = args[2]

        total += str(hour * 3600 + minutes * 60 + seconds)
        total = int(total)
        return total

    def convert_time(self, tijd):  # Private
        """
        Converteert seconden naar datum

        :param tijd: unsigned int (tijd representeert seconden)

        Preconditie: Het argument tijd is een positieve integer waarbij de eerste digits jjjjmmdd zijn, de rest is de tijd in seconden.
        Postconditie: De tijd wordt omgezet en gereturned in een datum-formaat.
        """
        if not isinstance(tijd, int):
            raise Exception("Precondition error: tijd is niet van type int in convert_time")
        if tijd < 0:
            raise Exception("Precondition error: tijd kan niet negatief zijn in convert_time")
        temp = str(tijd)
        if (len(temp) >= 8):
            datum = f"{temp[:4]}-{temp[4:6]}-{temp[6:8]}"
            seconds = int(temp[8:])
        else:
            datum = "0000-00-00"
            seconds = int(tijd)
        hours = seconds // 3600
        minutes = (seconds - hours * 3600) // 60
        seconds = seconds - hours * 3600 - minutes * 60
        return (datum, hours, minutes, seconds)

    def set_time(self, tijd):
        """
        Zet het huidige tijdstip naar een andere waarde.

        :param tijd: unsigned integer (nieuwe waarde voor de tijd in seconden)

        Precondities: Er wordt 1 parameter gegeven dat een positieve integer is wat de tijd in seconden representeert.
        Postconditie: Het huidige tijdstip wordt aangepast naar de ingegeven waarde.
        """
        if not isinstance(tijd, int):
            raise Exception("Precondition error: tijd is niet van type int in set_time")
        if tijd < 0:
            raise Exception("Precondition error: tijd kan niet negatief zijn in set_time")
        self.tijdsstip = tijd

    def lees_reservatie(self):
        """
        Lees de reservaties uit self.reservaties en verwerkt deze.

        Precondities: Er worden geen parameters ingegeven. self.reservaties bevat enkel reservaties van eenzelfde tijdstip. self.verlaag_plaatsenVirtueel controleert autonoom of dat er plek is in het systeem.
        Postconditie: De reservatie is succesvol verwerkt en toegevoegd aan het archief. De vertoning heeft eventueel een aangepast aantal vrije_plaatsen.

        :return: bool:succes
        """
        self.__display(f"leest reservatie") #Display eventueel info naar de console

        while self.reservaties.tableIsEmpty() == False: #Zolang er nog onverwerkte reservaties zijn
            reservatie = self.reservaties.tableFirst()[0][1]
            tijdstip = self.reservaties.tableFirst()[0][0]

            # Verlaag virtuele plaatsen (Independent of dit slaagt of niet)
            self.__verhoog_plaatsenVirtueel(reservatie.vertoning_id, reservatie.aantal_plaatsen)

            # Verwijder reservatie & voeg toe aan archief
            self.__archiveer_reservatie()

            # Update datum & tijd
            self.set_time(tijdstip)
        return True

    def __archiveer_reservatie(self):
        """
        Archiveert de huidige reservatie.

        Precondities: Er worden geen parameters ingegeven.
        Postconditie: self.reservaties wordt 1 kleiner en self.reservatie_archief wordt 1 groter. Verplaats de reservatie van voor uit self.reservaties naar self.reservaties_archief.
        """
        reservatie = self.reservaties.tableDelete()[0]  #Dequeu huidige reservatie queue
        self.reservatie_archief.tableInsert(1, reservatie)  #Insert reservatie in archief

    def lees_ticket(self, vertoningid, aantal_mensen):
        """
        Leest een ticket bij aankomst in de zaal uit. (Verlaagt plaatsen, en kijkt of de film gestart kan worden)

        Precondities: vertoningid verwijst naar een bestaande vertoning en is op te vragen via self.vertoningen. aantal_mensen is een unsigned int.
        Postcondities: Het ticket is verwerkt, het aantal_vrijeplaatsen van de vertoning is geüpdated en de vertoning is eventueel gestart.

        :param vertoningid: id van de vertoning, int
        :param aantal_mensen: unsigned int
        :return:
        """
        #Verlaag aantal plaatsen & chance stack
        self.__verlaag_plaatsenFysiek(vertoningid,aantal_mensen)

        #Out logs
        self.__display("["+str(self.convert_time(self.tijdsstip))+"] De vertoning met ID: "+str(vertoningid)+" is verlaagd met: "+str(aantal_mensen))

        #Check of de film gestart kan worden
        self.start(vertoningid)

    def __verhoog_plaatsenVirtueel(self, vertoningid, plaatsen):
        """
        Verminderd het aantal vrije plaatsen in een voorstelling.

        :param vertoningid: integer (id van de vertoning)
        :param plaatsen: integer (aantal plaatsen dat niet meer beschikbaar zijn)

        precondities: er zijn voldoende plaatsen in de vertoning. De vertoning bestaat en is toegevoegd aan self.vertoningen. Plaatsen is een unsigned integer.
        postconditie: het aantal plaatsen van de vertoning dat overeenkomt met het vertoning id
                      wordt verminderd met het gegeven aantal plaatsen
        """
        for i in range(plaatsen):
            self.vertoningen.tableRetrieve(vertoningid)[0][1].tableInsert(i)  #[0] = value-type, hiervan [1]: de stack

        return self.vertoningen.tableRetrieve(vertoningid)[0][0].verminder_plaatsenVirtueel(plaatsen)

    def __verlaag_plaatsenFysiek(self, vertoningid, plaatsen):
        """
        Verminderd het aantal vrije plaatsen in een voorstelling.

        :param vertoningid: integer (id van de vertoning)
        :param plaatsen: integer (aantal plaatsen dat niet meer beschikbaar zijn)

        precondities: Er zijn voldoende plaatsen in de vertoning. De vertoning met het id bestaat en is correct op te vragen. Plaatsen is een unsigned integer (+ en groter dan 0)
        postconditie: het aantal plaatsen van de vertoning dat overeenkomt met het vertoning id
                      wordt verminderd met het gegeven aantal plaatsen
        """

        # To be changed: Whole function
        notVol = self.vertoningen.tableRetrieve(vertoningid)[0][0].verhoog_plaatsenFysiek(plaatsen)
        if notVol:
            for i in range(plaatsen):
                self.vertoningen.tableRetrieve(vertoningid)[0][1].tableDelete()
            return
        raise Exception("Stack overflow")

    def start(self, vertoningid):
        """
        Start de vertoning.

        Preconditie: De vertoning start op het juiste tijdstip en er mag geen andere vertoning bezig zijn in deze zaal. De vertoning met vertoningid moet bestaan en correct in self.vertoningen zijn toegevoegd.
        Postconditie: De vertoning wordt gestart (gestart = true)

        :param vertoningid: int
        """
        if self.vertoningen.tableRetrieve(vertoningid)[1]: #Indien de vertoning bestaat
            if self.vertoningen.tableRetrieve(vertoningid)[0][1].tableIsEmpty(): #Kijk of de stack empty is (geen reservaties meer)
                vertoning_object = self.vertoningen.tableRetrieve(vertoningid)[0][0]
                vertoning_object.start()
            return True
        raise Exception("Vertoning bestaat niet")

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
        Verwijdert alle gebruikers.

        Precondities: Er worden geen parameters ingegeven
        Postconditie: self.gebruikers is gecleared.
        """
        self.gebruikers.clear()

    def log(self):
        """
        Creëert een log-file.

        Precondities: Er worden geen parameters ingegeven.
        Postcondities: Er is een logbestand gecreërd.
        """
        logger = Log(self, eval(self.log_string) )
        logger.create_log()

    def add_tijdslot(self,tijdslot):
        """
        Voegt een tijdslot toe aan de verzameling met bestaande tijdslots.
                
        :param tijdslot: int 
        
        Precondities: Tijdslot is een integer wat het aantal seconden representeert
        Postcondities: Het tijdslot is achteraan de lijst toegevoegd.
        """
        self.slots.tableInsert(self.slots.tableGetLength()+1 , tijdslot) #PRE: lijst index is currentnr+1

    def __display(self, msg):
        if self.display_mode == "print":
            print(msg)

if __name__ == '__main__':
    r = Reservatiesysteem(display_mode="print")
