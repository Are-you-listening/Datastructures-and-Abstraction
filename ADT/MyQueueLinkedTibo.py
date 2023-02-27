"""ADT Queue linkedbased implementatie
Deze ADT wordt gebruikt om makkelijk elementen toe te voegen en de eerste elementen weer weg te halen
Hier wordt gebruikgemaakt van een gelinkte ketting"""


class QueueItemType:
    def __init__(self, value):
        self.value = value
        self.next = None


class MyQueue:
    def __init__(self):
        """
        Maakt een lege queue aan, hierbij is er een front en een back pointer
        ook worden het aantal elementen bewaard

        preconditie: er zijn geen parameters gegeven
        postconditie: er is een lege queue aangemaakt met een pointer naar de front en de back
        """
        self.back = None
        self.front = None
        self.length = 0

    def isEmpty(self):
        """
        controleer dat de queue leeg is

        preconditie: er worden geen parameters gegeven, en er bestaat een pointer front
        postconditie: geeft True terug als de queue leeg is (front == None) en False als de queue niet leeg is
        :return: geeft True terug als de queue leeg is en False als de queue niet leeg is
        """
        if self.front== None:
            return True
        return False

    def enqueue(self, item):
        """
        Voegt item toe aan de back van de queue

        preconditie: er wordt 1 parameter gegeven: item
        postconditie: queue is 1 item groter en de back bevat het toegevoegde item
        :param: item: geeft de waarde die toegevoegd moet worden.
        :return: True indien geslaagd
        """
        item = QueueItemType(item)

        if self.front is None:
            self.front = item
            self.back = item
        else:
            self.back.next = item
            self.back = item

        self.length += 1

        return True

    def dequeue(self):
        """
        Verwijdert item dat zich bevindt aan front van de queue

        preconditie: de queue is niet leeg
        postconditie: queue is 1 item kleiner, en het item aan front is verdwenen (top = top.next)
        :return: verwijderde item en True indien geslaagd
        """
        if self.isEmpty():
            return None, False
        item = self.front
        self.front = self.front.next
        self.length -= 1
        return item.value, True

    def getFront(self):
        """
        Geeft het item dat zich bevindt aan front van de queue

        preconditie: de queue is niet leeg
        postconditie: de queue blijft onveranderd
        :return: item dat zich bevindt op front en True indien geslaagd
        """
        if self.isEmpty():
            return None, False
        item = self.front

        return item.value, True

    def load(self, lst):
        """
        overschrijft de queue naar een nieuwe queue

        preconditie: er bestaat 1 parameter dat een lijst van waardes is.
        postconditie: de stack heeft als size = size van de lijst

        :param: lst: lijst met waardes
        :return: True indien geslaagd
        """

        self.back = None
        self.front = None
        self.length = 0

        for i in range(len(lst)-1, -1, -1):
            self.enqueue(lst[i])

        self.length = len(lst)
        return True

    def save(self):
        """
        Geeft een lijst weer met de volgorde in de queue, met de front als laatste element van de lijst

        preconditie: de queue is niet leeg
        postconditie: de queue blijft onveranderd
        :return: queueitemstype hun waardes dat zich bevinden in de queue
        """
        output = [None]*self.length
        v = self.front

        for i in range(self.length):
            output[self.length-1-i] = v.value
            v = v.next

        return output


class MyQueueTable:
    def __init__(self):
        self.queue = MyQueue()

    def tableIsEmpty(self):
        return self.queue.isEmpty()

    def tableInsert(self, value):
        return self.queue.enqueue(value)

    def tableFront(self):
        return self.queue.getFront()

    def save(self):
        return self.queue.save()

    def load(self, array):
        return self.queue.load(array)

    def tableDelete(self):
        return self.queue.dequeue()
