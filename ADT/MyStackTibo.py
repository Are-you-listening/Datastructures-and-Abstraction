"""ADT STACK arraybased implementatie
Deze ADT wordt gebruikt om makkelijk elementen toe te voegen en de laatste elementen weer weg te halen
Hier wordt gebruikgemaakt van een Array en een variable size die bijhoudt tot hoever de array gevuld is"""


class StackItemType:
    def __init__(self, value):
        """
        initaliseer een StackItemType
        :param value: is de value die toegewezen wordt aan dit StackItemType
        preconditie: Er is 1 input: value.
        postconditie: de value wordt bewaard
        """
        self.value = value


class MyStack:
    def __init__(self, max_size):
        """
        Maakt een lege stack aan

        preconditie: er is 1 parameter: max_size, maxsize is een integer en max_size > 0
        postconditie: er is een lege stack aangemaakt (size == 0)

        :param int max_size: bepaalt de maximale grootte van een stack en max_size > 0.
        """
        self.items = [None] * max_size
        self.size = 0

    def isEmpty(self):
        """
        controleer dat de stack leeg is

        preconditie: er worden geen parameters gegeven
        postconditie: geeft True terug als de stack leeg is (size == 0) en False als de stack niet leeg is
        :return: geeft True terug als de stack leeg is en False als de stack niet leeg is
        """
        if self.size == 0:
            return True

        return False

    def push(self, item):

        """
        voeg item toe aan de top van de stack
        :param item: het item dat wordt toegevoegd aan de stack.
        preconditie: er is maar 1 parameter aanwezig, de stack heeft nog plek (size < len(items)).
        postconditie: stack is 1 item groter en de top bevat het toegevoegde item.
        :return: True indien geslaagd
        """
        item = StackItemType(item)
        if self.size == len(self.items):
            return False

        self.items[self.size] = item
        self.size += 1
        return True

    def pop(self):
        """
        verwijder item dat zich bevindt aan de top van de stack

        preconditie: de stack is niet leeg en er zijn geen parameters gegeven.
        postconditie: stack is 1 item kleiner, en het item aan de top is verdwenen (size -= 1)
        :return: verwijderde item en True indien geslaagd
        """
        if self.isEmpty():
            return None, False

        item = self.items[self.size - 1]
        self.items[self.size - 1] = None
        self.size -= 1

        return (item.value, True)

    def getTop(self):
        """
        geeft het item dat zich bevindt aan de top van de stack

        preconditie: de stack is niet leeg (size != 0) en er zijn geen parameters gegeven.
        postconditie: de stack blijft onveranderd
        :return: item dat zich bevindt op de top en True indien geslaagd
        """
        if self.isEmpty():
            return None, False

        item = self.items[self.size - 1]

        return (item.value, True)

    def load(self, lst):

        """
        overschrijft de stack naar een nieuwe stack

        preconditie: er bestaat 1 parameter dat een lijst is.
        postconditie: de stack heeft als size = size van de lijst
        :return: item dat zich bevindt op de top en True indien geslaagd
        """

        self.items = [None] * len(lst)
        self.size = 0
        for i, l in enumerate(lst):
            self.items[i] = StackItemType(l)
            self.size += 1
        return True

    def save(self):
        """
        geeft een lijst weer met de volgorde in de stack, met de top als laatste element van de lijst

        preconditie: er zijn geen parameters gegeven, e
    def add_to_info(self,value): #Private
        filmnaam = self.films.tableRetrieveTranverse(value[0].filmid)[0].titel
        current_slot = self.convert_time(self.tijdsstip)[1]*3600 + self.convert_time(self.tijdsstip)[2]*60
n de stack is niet leeg.
        postconditie: de stack blijft onveranderd
        :return: stackitemstype hun waardes dat zich bevinden in de stack
        """
        output = [None] * self.size
        for i in range(self.size):
            output[i] = self.items[i].value

        return output


class MyStackTable:
    def __init__(self):
        self.size = 0
        self.stack = MyStack(10)

    def tableIsEmpty(self):
        return self.stack.isEmpty()

    def tableInsert(self, value):
        b = self.stack.push(value)
        if b:
            self.size += 1
            if self.size > self.stack.size:
                stack2 = MyStack(self.size*2)
                while not self.stack.isEmpty():
                    stack2.push(self.stack.pop()[0])

                self.stack = stack2

        return b

    def tableFirst(self):
        return self.stack.getTop()

    def save(self):
        return self.stack.save()

    def load(self, array):
        return self.stack.load(array)

    def tableDelete(self):
        return self.stack.pop()

    def clear(self):
        self.stack = MyStack(10)
