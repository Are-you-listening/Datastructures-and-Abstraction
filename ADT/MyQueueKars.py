"""ADT: Linked Based Implementatie van een Queue"""

"""Data"""

""" 'ItemType', het type van de items in de Queue. (Python Object) """

class QueueItemType:
    """
    QueueItemType is het type (string, boolean, integer,...) van de elementen in de Queue.
    in 'ItemType', het type van de items in de Queue. (Python Object)
    out
    Preconditie: 'ItemType' is een object wat in een Python List gestopt kan worden.
    Postconditie: 'QueItemType' is gedefinieerd. Er is een 'ItemType' toegevoegd en 'next' is ingesteld op "None".
    """
    def __init__(self, ItemType):
        self.ItemType = ItemType
        self.next=None

"""Functionaliteit"""
class MyQueue:
    def __init__(self):
        """
        Creëert een lege queue.
        in
        out
        Preconditie: Geen
        Postconditie: Er is een lege queue aangemaakt met variables: 'front'=None & 'end"=None
        """
        self.front=None   #Eerste in de rij
        self.end=None

    def isEmpty(self):
        """
        Bepaalt of een queue leeg is.
        in
        out Boolean
        Preconditie: Er is een queue aangemaakt.
        Postconditie: Geeft True als de queue leeg is, False als de queue gevuld is.
        """
        if self.front==None:
            return True
        else:
            return False

    def enqueue(self, newItem):
        """
        Voegt het element ‘newItem’ toe achteraan de queue. ('newItem' wordt omgezet in een QueueItemType)
        in newItem: Het type van de items in de Queue. (Python Object)
        out succes:Boolean | 'succes' geeft aan of de operatie geslaagd is.
        Preconditie: Er is een Queue aangemaakt.
        Postconditie: Bij een succesvolle operatie is ‘newItem’ toegevoegd achteraan de queue.
        """
        newItem=QueueItemType(newItem)
        if self.front==None:
            self.front=newItem
            self.end=newItem
            return True
        else:
            temp=self.end
            temp.next=newItem
            self.end=newItem
            return True

    def dequeue(self):
        """
        Verwijdert de front van een Queue.
        in
        out predeque_QueueFront:QueueItemType out succes:Boolean | 'predeque_QueueFront' is de front (eerst toegevoegd element) van de queue voordat er een dequeue-operatie is uitgevoerd. 'succes' geeft aan of de operatie geslaagd is.
        Preconditie: Er is een queue aangemaakt.
        Postconditie: Als de queue niet leeg is dan kan de front van de queue verwijdert worden.  Bij een geslaagde operatie is de front van een queue, d.w.z. het eerst toegevoegd element, verwijdert van de queue. Als de queue leeg is, is de operatie niet geslaagd.
        """
        if self.front!=None:
            predeque_QueueFront = self.front
            self.front=predeque_QueueFront.next
            return (predeque_QueueFront.ItemType,True)

        return (None,False)

    def getFront(self):
        """
        Geeft de huidige front van een queue mee. De queue blijft ongewijzigd.
        in
        out QueueFront.ItemType, succes:Boolean |'QueueFront.ItemType' is het ItemType van de front van de queue. (d.i. het eerst toegevoegde element). 'succes' geeft aan of de operatie geslaagd is.
        Preconditie: Er is een queue aangemaakt.
        Postconditie: Als de queue niet leeg is wordt er een tupel met 'QueueFront' en 'True' meegegeven. Als de Queue leeg is, wordt er een tuple van 'None' & 'False' meegegeven. De front van de queue bestaat dan niet, en bedraagt dus 'None'. De queue blijft ongewijzigd.
        """
        if self.front!=None!=0:
            return (self.front.ItemType, True)
        else:
            return (None, False)

    def save(self):
        """
        Geeft de huidige queue als lijst mee.
        in
        out save:Python List | 'save' is de Python lijst die alle elementen uit de queue bevat.
        Preconditie: Er is een queue aangemaakt. 'save' is een lege lijst.
        Postconditie: De lege lijst 'save' wordt opgevuld met de elementen ('ItemType') uit de queue en vervolgens meegegeven.
        """
        start = self.front
        save=[]
        while(start!=None):
            save.append(self.dequeue()[0])
            start=self.front
        save2=[]
        z=len(save)
        for i in range(z):
            save2.append(save[z-1-i])
            self.enqueue(save[i])

        return save2

    def load(self, aQueue):
        """
        Maakt een queue aan/laadt een nieuwe queue in. (de huidige queue wordt overschreven)
        in aQueue:Python List | 'aQueue' is een queue gerepresenteerd in een Python lijst.
        out
        Preconditie: 'aQueue' is een Python List.
        Postconditie: Er wordt een queue aangemaakt die de elementen van 'aQueue' (omgezet naar 'QueueItemType') bevat.
        """
        self.front=None
        self.end=None
        z=len(aQueue)
        for i in range(z):
            self.enqueue(aQueue[z-1-i])

"""q = MyQueue()
print(q.isEmpty())
print(q.getFront()[1])
print(q.dequeue()[1])
print(q.enqueue(2))
print(q.enqueue(4))
print(q.isEmpty())
print(q.dequeue()[0])
q.enqueue(5) #Check ff wat er gebeurt als we dequeen met 1 item
print(q.save())

q.load(['a', 'b', 'c'])
print(q.save())
print(q.dequeue()[0])
print(q.save())
print(q.getFront()[0])
print(q.save())"""

class MyQueueTable:
    def __init__(self):
        self.queue = MyQueue()

    def tableIsEmpty(self):
        return self.queue.isEmpty()

    def tableInsert(self, ItemType):
        return self.queue.enqueue(ItemType)

    def tableFirst(self):
        return self.queue.getFront()

    def save(self):
        return self.queue.save()

    def load(self, array):
        return self.queue.load(array)

    def tableDelete(self):
        return self.queue.dequeue()

    def clear(self):
        self.queue = MyQueue()