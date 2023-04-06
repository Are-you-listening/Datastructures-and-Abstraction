# ADT Queue
## data
items=[]

class QueueItemType:
    def __init__(self, value):
        """
        Creëert een type, QueueItemType, dat het type is van de elementen in de queue.

        parameters: Een waarde dat de QueueItemType type moet verkrijgen.

        preconditions: Er bestaat geen andere queue met dezelfde benaming.

        postconditions: De doorgekregen value heeft nu als type, QueueItemType.

        :return: Niets
        """
        self.value=value

class MyQueue:
    ## functionaliteit
    def __init__(self, max_size):
        """
        Creëert een lege queue.

        parameters: Maximum grootte van de queue.

        preconditions: Er bestaat geen andere queue met dezelfde benaming.
        Max_size parameter is een unsigned integer.

        postconditions: De aangemaakte queue is empty.

        :return: Niets
        """
        self.items=[None] * max_size
        self.size = 0
        return None

    ## functionaliteit
    def isEmpty(self):
        """
        Controleert de opgegeven queue of die leeg is of niet en geeft naarmate hiervan een booleaanse waarde terug.
        True als de queue leeg is, False als dit niet het geval is.

        De queue waarvan bepaald moet worden of deze leeg is, of niet, wordt doorgegeven als object, initialisatie van deze command ziet er dan als volgt uit:
        "queue.isEmpty()".

        parameters: Geen

        preconditions: Er bestaat een queue met de opgegeven benaming doorgekregen van de user.

        postconditions: De functie geeft een booleaanse waarde weer.
        Er vinden geen gegevens wijzigingen plaats.

        :return: De functie geeft naarmate de queue vol of leeg is een booleaanse waarde terug.
        """
        empty=False
        if self.size == 0:
            empty=True
        return empty

    ## functionaliteit
    def enqueue(self,newItem):
        """
        Plaatst een item die doorgegeven word via de parameter "newItem" aan het einde van de queue.

        Initialisatie is als volgt: "queue.enqueue(item)".

        parameters: Een item die dient toegevoegd te worden aan de queue.

        preconditions: Er bestaat een queue met de opgegeven benaming doorgekregen van de user.

        postconditions: De queue bevat de item die diende toegevoegd te worden. De length/size van de queue is vergroot met 1 item.
        Er vindt een gegevens wijziging plaats.

        :return: De functie geeft een booleaanse waarde aan die dient aan te duiden of de toevoeging gelukt is of niet. True als het gelukt is en False als niet.
        """
        if self.size == len(self.items):
            return False
        a=self.size
        while a!=0:
            self.items[a]=self.items[a-1]
            a-=1
        self.items[0] = newItem
        self.size +=1
        return True

    ## functionaliteit
    def dequeue(self):
        """
        Verwijdert de kop van de doorgekregen queue, en zo dus ook het eerst toegevoegde item van een queue.

        initialisatie is als volgt: "queue.dequeue()".

        parameters: Geen

        preconditions: Er bestaat een queue met de opgegeven benaming doorgekregen van de user.
        De queue is niet "empty".

        postconditions: De queue bevat een item minder, de kop van de queue, en is verkleint met 1 item in length/size.
        Er vindt een gegevens wijziging plaats.

        :return: De functie geeft de kop/front van de queue weer.
                 De functie geeft een booleaanse waarde aan die dient aan te duiden of de verwijdering gelukt is of niet. True als het gelukt is en False als niet.
        """
        if self.size == 0:
            return (0,False)
        queueFront = self.items[self.size - 1]
        self.items[self.size-1]=None
        self.size-=1
        return (queueFront,True)

    ## functionaliteit
    def getFront(self):
        """
        Verkrijgt de waarde van de kop van de doorgekregen queue en plaatst deze waarde in queueFront.

        Initialisatie is als volgt: "queue.getFront()".

        parameters: Geen

        preconditions: Er bestaat een queue met de opgegeven benaming doorgekregen van de user.
        De queue is niet "empty".

        postconditions: De doorgekregen queue is ongedeerd en queueFront bezit de waarde van de kop van de doorgekregen queue.
        Er vindt geen gegevens wijziging plaats.

        :return: De functie geeft de kop/front van de queue weer.
                 De functie geeft een booleaanse waarde aan die dient aan te duiden of queueFront de waarde van de kop van de queue bezit of niet. True als dit het geval is en False als niet.
        """
        if self.size == 0:
            return (0,False)
        return (self.items[self.size-1],True)

    ## functionaliteit
    def save(self):
        """
        Vormt een queue om naar een string die een list in python voorstelt

        Initialisatie is als volgt: "queue.save()".

        parameters: Geen

        preconditions: Er bestaat een queue met de opgegeven benaming doorgekregen van de user.

        postconditions: Er bestaat een string die over de waarden van de queue bezit.
        De gegevens van de queue blijven ongewijzigd.

        :return: De functie geeft een Python list als string weer.
        """
        a = 0
        b = "["
        while a != self.size:
            if self.items[a] in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
                b += "'"
                b += str(self.items[a])
                b += "'"
            else:
                b += str(self.items[a])
            if a != self.size - 1:
                b += ","
            a += 1
        b += "]"
        return b

    ## functionaliteit
    def load(self,l):
        """
        Creëert een lege object en vult vervolgens de lege object met de doorgekregen list.

        Initialisatie is als volgt: "queue.load()".

        parameters: Een subscriptable object.

        preconditions: Er bestaat een queue met de opgegeven benaming doorgekregen van de user.

        postconditions: Er bestaat een object die de doorgekregen list zijn waarden bezit.

        :return: Niets
        """
        emptyObject = MyQueue(len(l))
        for w in reversed(l):
            if w != "[" and w != "," and w != "]":
                emptyObject.enqueue(str(w))
        self.items = emptyObject.items
        self.size = emptyObject.size
        return None

class MyQueueTable:
    def __init__(self):
        self.Queue = MyQueue(1)

    def tableIsEmpty(self):
        return self.Queue.isEmpty()

    def tableInsert(self, value):
        if not self.Queue.enqueue(value):
            temp = MyQueue(self.Queue.size * 2)
            for i in range(self.Queue.size):
                item = self.Queue.dequeue()[0]
                temp.enqueue(item)
            temp.enqueue(value)
            self.Queue = temp

    def tableFirst(self):
        return self.Queue.getFront()

    def save(self):
        return self.Queue.save()

    def load(self,l):
        self.Queue.load(l)

    def tableDelete(self):
        return self.Queue.dequeue()

    def clear(self):
        self.Queue = MyQueue(1)
