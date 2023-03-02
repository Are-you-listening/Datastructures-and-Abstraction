#linkbased queue ADT

class QueueItemType:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class MyQueue:
    def __init__(self):
        """
        precondities:
        postcondities: er is een lege queue aangemaakt
        """
        self.first = None

    def isEmpty(self):
        """
        precondities: de queue bestaat
        postcondities: de queue wordt niet gewijzigd
        :return: True als de queue leeg is, anders False
        """
        if self.first == None:  # als de eerste plek in de queue leeg is dan is heel de queue leeg
            return True
        else:
            return False

    def enqueue(self, newItem):
        """
        precondities:
        postcondities: de lengte van de queue is met 1 verhoogt
        :param newItem: Het item dat aan de queue wordt toegevoegd
        :return: True als het succesvol is toegevoegd, anders False
        """
        newElement = QueueItemType(newItem, None)
        newElement.next = self.first
        self.first = newElement
        return True

    def dequeue(self):
        """
        precondities: de queue is niet leeg
        postcondities: de lengte van de queue is met 1 vermindert
        :return: (queueFront: het item dat uit de queue verwijdert wordt, True als dit gelukt is, anders False)
        """
        if self.isEmpty():
            queueFront = None
            return tuple([queueFront, False])
        currentElement = self.first
        while currentElement.next != None:
            previousElement = currentElement
            queueFront = currentElement.next
            currentElement = currentElement.next
        previousElement.next = None
        return tuple([queueFront.value, True])

    def getFront(self):
        """
        precondities: De queue is niet leeg
        postcondities: de queue wordt niet gewijzigd
        :return: (queueFront: het item dat uit de queue verwijdert wordt, True als dit gelukt is, anders False)
        """
        if self.isEmpty():
            queueFront = None
            return tuple([queueFront, False])
        currentElement = self.first
        while currentElement.next != None:
            queueFront = currentElement.next
            currentElement = currentElement.next
        return tuple([queueFront.value, True])

    def save(self):
        """
        preconditie:
        postconditie: de queue wordt niet gewijzigd
        :return: de queue als string voorgesteld
        """
        result = []
        temp = [None]
        currentElement = self.first
        while currentElement != None:
            temp[0] = currentElement.value
            result += temp
            currentElement = currentElement.next
        return str(result)

    def load(self, queue):
        """
        preconditie: de string is een geldige queue
        postconditie:
        :param queue: de string dat naar een queue moet worden omgezet
        :return:
        """
        L = list(queue)
        temp=[None] * len(L)
        for i in range(len(L)):
            temp[i] = L[len(L)-i-1]
        L = temp
        self.first = None
        for item in L:
            self.enqueue(item)

class QueueTable:
    def __init__(self):
        self.queue = MyQueue()

    def tableIsEmpty(self):
        return self.queue.isEmpty()

    def tableInsert(self, newItem):
        return self.queue.enqueue(newItem)

    def tableRetrieve(self):
        return self.queue.getFront()

    def tableDelete(self):
        return self.queue.dequeue()

    def save(self):
        return self.queue.save()

    def load(self, input):
        return self.queue.load(input)