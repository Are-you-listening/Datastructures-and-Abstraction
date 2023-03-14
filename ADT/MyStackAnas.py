# ADT stack
## data
items=[]

class StackItemType:
    ## functionaliteit
    def __init__(self,value):
        """
        Creëert een type, StackItemType, dat het type is van de elementen in de stack.

        parameters: Een waarde dat de StackItemType type moet verkrijgen.

        preconditions: Er bestaat geen andere stack met dezelfde benaming.

        postconditions: De doorgekregen value heeft nu als type, StackItemType.

        :return: Niets
        """
        self.value=value

class MyStack:
    ## functionaliteit
    def __init__(self, max_size):
        """
        Creëert een lege stack.

        parameters: Maximum grootte van de queue.

        preconditions: Er bestaat geen andere stack met dezelfde benaming.
        Max_size parameter is een unsigned integer.

        postconditions: De aangemaakte stack is empty.

        :return: Niets
        """
        self.items=[None]*max_size
        self.size = 0
        return None

    ## functionaliteit
    def isEmpty(self):
        """
        Controleert de opgegeven stack of die leeg is of niet en geeft naarmate hiervan een booleaanse waarde terug.
        True als de stack leeg is, False als dit niet het geval is.

        De stack waarvan bepaald moet worden of deze leeg is, of niet, wordt doorgegeven als Container type, initialisatie van deze command ziet er dan als volgt uit:
        "stack.isEmpty()".

        parameters: Geen

        preconditions: Er bestaat een stack met de opgegeven benaming doorgekregen van de user.

        postconditions: De functie geeft een booleaanse waarde weer.
        Er vinden geen gegevens wijzigingen plaats.

        :return: De functie geeft naarmate de stack vol of leeg is een booleaanse waarde terug.
        """
        if self.size == 0:
            return True
        return False

    ## functionaliteit
    def push(self,newItem):
        """
        Plaatst een item die doorgegeven word via de parameter "newItem" aan de top van de doorgekregen stack.

        Initialisatie is als volgt: "stack.push(item)".

        parameters: Een item die dient toegevoegd te worden aan de stack.

        preconditions: Er bestaat een stack met de opgegeven benaming doorgekregen van de user.

        postconditions: De stack bevat de item die diende toegevoegd te worden. De length/size van de stack is vergroot met 1 item.
        Er vindt een gegevens wijziging plaats.

        :return: De functie geeft een booleaanse waarde aan die dient aan te duiden of de toevoeging gelukt is of niet. True als het gelukt is en False als niet.
        """
        if self.size == len(self.items):
            return False
        self.items[self.size] = newItem
        self.size +=1
        return True

    ## functionaliteit
    def pop(self):
        """
        Verwijdert de top van de doorgekregen stack, en zo dus ook het laatst toegevoegde item van een stack.

        initialisatie is als volgt: "stack.pop()".

        parameters: Geen

        preconditions: Er bestaat een stack met de opgegeven benaming doorgekregen van de user.
        De stack is niet "empty".

        postconditions: De stack bevat een item minder, de top van de stack, en is verkleint met 1 item in length/size.
        Er vindt een gegevens wijziging plaats.

        :return: De functie geeft de top van de stack weer.
                 De functie geeft een booleaanse waarde aan die dient aan te duiden of de verwijdering gelukt is of niet. True als het gelukt is en False als niet.
        """
        if self.size == 0:
            return (0, False)
        stackTop=self.items[self.size-1]
        self.items[self.size-1]=None
        self.size-=1
        return (stackTop,True)

    ## functionaliteit
    def getTop(self):
        """
        Verkrijgt de waarde van de top van de doorgekregen stack en plaatst deze waarde in stackTop.

        Initialisatie is als volgt: "stack.getTop()".

        parameters: Geen

        preconditions: Er bestaat een stack met de opgegeven benaming doorgekregen van de user.
        De stack is niet "empty".

        postconditions: De doorgekregen stack is ongedeerd en stackTop bezit de waarde van de top van de doorgekregen stack.
        Er vindt geen gegevens wijziging plaats.

        :return: De functie geeft de top van de stack weer.
                 De functie geeft een booleaanse waarde aan die dient aan te duiden of stackTop de waarde van de top van de stack bezit of niet. True als dit het geval is en False als niet.
        """
        if self.size == 0:
            return (0,False)
        return (self.items[self.size-1],True)

    def save(self):
        """
        Vormt een stack om naar een string die een list in python voorstelt

        Initialisatie is als volgt: "stack.save()".

        parameters: Geen

        preconditions: Er bestaat een stack met de opgegeven benaming doorgekregen van de user.

        postconditions: Er bestaat een string die over de waarden van de stack bezit.
        De gegevens van de stack blijven ongewijzigd.

        :return: De functie geeft een Python list als string weer.
        """
        a=0
        b="["
        while a!=self.size:
            if self.items[a] in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
                b+="'"
                b+=str(self.items[a])
                b += "'"
            else:
                b += str(self.items[a])
            if a!=self.size-1:
                b+=","
            a+=1
        b+="]"
        return b

    def load(self,l):
        """
        Creëert een lege object en vult vervolgens de lege object met de doorgekregen list.

        Initialisatie is als volgt: "stack.load()".

        parameters: Een subscriptable object.

        preconditions: Er bestaat een stack met de opgegeven benaming doorgekregen van de user.

        postconditions: Er bestaat een object die de doorgekregen list zijn waarden bezit.


        :return: Niets
        """
        emptyObject=MyStack(len(l))
        for w in l:
            if w!="[" and w!="," and w!="]":
                emptyObject.push(str(w))
        self.items=emptyObject.items
        self.size=emptyObject.size
        return None

class MyStackTable:
    def __init__(self):
        self.Stack = MyStack(1)

    def tableIsEmpty(self):
        return self.Stack.isEmpty()

    def tableInsert(self, value):
        if not self.Stack.push(value):
            temp = MyStack(self.Stack.size +1)
            for i in range(self.Stack.size):
                item = self.Stack.pop()[0]
                temp.push(item)
            self.Stack = temp

    def tableFirst(self):
        return self.Stack.getTop()

    def save(self):
        return self.Stack.save()

    def load(self, l):
        self.Stack.load(l)

    def tableDelete(self):
        self.Stack.pop()

    def clear(self):
        self.Stack = MyStack(1)

