class LinkedChainItem:
    def __init__(self, value):
        """
        Definieert een LinkedChainItem, dat een pointer naar zowel zijn voorganger als zijn opvolger heeft.
        Ook bewaard het zijn waarde
        """
        self.next = None
        self.pre = None
        self.value = value


class LinkedChain:
    def __init__(self):
        """
        Initialiseer de linkedchain door middel van een dummyhead knoop.
        Hierdoor is er geen speciaal geval indien er nog geen knopen aanwezig zijn.

        Preconditie: er zijn geen parameters gegeven.
        Postconditie: er is een Circulaire Dubbelgelinkte ketting aangemaakt, met een lengte van 0.
        """
        self.head = LinkedChainItem(None)
        self.head.next = self.head
        self.head.pre = self.head
        self.length = 0

    def insert(self, location, item):
        """
        Er wordt een item toevevoegd aan de gelinkte ketting.

        precondities: de locatie waar het element wordt toegevoegd is groter dan 0 en kleiner of gelijk aan de lengte+1.
                      De locatie is een postieve integer zonder 0. Er zijn 2 parameters gegeven.

        postconditie: de gelinkte ketting zal een lengte 1 groter hebben dan voordien, er zal een nieuw element worden
        toegevoegd aan de ketting op de gekozen locatie

        :param location: Beslist waar in de ketting het element wordt toegevoegd, (postieve integer zonder 0)
        :param item: de waarde die we wensen op te slaan
        :return: True indien geslaagd en False indien niet succesvol.
        """
        if location > self.length+1 or location <= 0:
            return False

        item = LinkedChainItem(item)

        n = self.head
        for i in range(location-1):
            n = n.next

        temp = n.next
        n.next = item
        item.next = temp
        item.pre = n
        temp.pre = item

        self.length += 1
        return True

    def isEmpty(self):
        """
        Controleert dat de gelinkte ketting leeg is.

        Preconditie: er zijn geen parameters gegeven.
        Postconditie: er wordt een boolean terug gegeven dat True/False is afhankelijk van dat de ketting leeg is.

        :return: True als de ketting leeg is en false als de ketting niet leeg is
        """
        if self.length == 0:
            return True
        else:
            return False

    def getLength(self):
        """
        Geeft terug hoeveel elementen er in de ketting zitten

        Preconditie: er zijn geen parameters gegeven.
        Postconditie: er wordt een Integer teruggegeven dat weergeeft hoeveel elementen er in de ketting zitten.

        :return: Integer, met het als waarde het aantal elementen in de ketting
        """
        return self.length

    def retrieve(self, location):
        """
        Geeft terug het element dat zich op een bepaalde plaats bevindt.

        Preconditie: er is 1 parameter location gegeven, deze paramter is groter dan 0 en kleiner of gelijk aan de lengte
        Postconditie: er wordt een waarde teruggeven samen met een boolean die aantoont dat het gelukt is.

        :param location: Beslist welk element wordt uitgelezen, (postieve integer zonder 0)

        :return: Een waarde en een boolean worden teruggegeven
        """
        if location > self.length or location <= 0:
            return None, False

        n = self.head
        for i in range(location):
            n = n.next

        return n.value, True

    def delete(self, loc):
        """
        Verwijdert het item op de i-de plaats

        Preconditie: er is 1 parameter location gegeven, deze paramter is groter dan 0 en kleiner of gelijk aan de lengte
        Postconditie: de circulaire linked chain is 1 kleiner dan voordien

        :return: Een boolean wordt teruggegeven die aangeeft dat de operatie al dan niet geslaagd is.
        """
        if loc > self.length or loc <= 0:
            return False

        n = self.head
        for i in range(loc):
            n = n.next

        n.pre.next = n.next
        n.next.pre = n.pre

        self.length -= 1

        return True

    def load(self, lst):
        """
        Laad een array/lijst aan waardes in de circulaire linked chain
        Preconditie: er is 1 parameter van het type array/lijst gegeven.
        Postconditie: de circulaire linked chain bevat een lengte gelijk aan de lengte van de lijst
        """
        self.head = LinkedChainItem(None)
        self.length = len(lst)

        last = self.head
        for el in lst:
            el = LinkedChainItem(el)
            last.next = el
            el.pre = last
            last = el

        last.next = self.head
        self.head.pre = last

    def save(self):
        """
            Geeft alle elementen in de ketting weer
            Preconditie: er zijn geen parameters gegeven, de lijst is niet leeg
            Postconditie: de ketting blijft onveranderd
        """
        if self.isEmpty():
            return []

        lst = [None]*self.length
        n = self.head
        for l in range(self.length):
            n = n.next
            lst[l] = n.value

        return lst

class LinkedChainTable():
    def __init__(self):
        self.l = LinkedChain()

    def tableIsEmpty(self):
        return self.l.isEmpty()

    def tableInsert(self, item):
        return self.l.insert(0, item)

    def tableRetrieve(self,key):
        for i in range(self.l.length):
            val = self.l.retrieve(i)
            if val == key:
                return val
        return False

    def traverseTable(self, func):
        for i in range(self.l.length):
            val = self.l.retrieve(i)
            func(val)

    def save(self):
        return self.l.save()

    def load(self, dict):
        return self.l.load(dict)

    def tableDelete(self, key):
        for i in range(self.l.length):
            val = self.l.retrieve(i)
            if val == key:
                self.l.delete(i)
                return True
        return False