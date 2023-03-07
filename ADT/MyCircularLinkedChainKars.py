"""ADT: Implementation of a Circulair Linked Chain (CLC)"""

#Possible Improvements:
#1. Wider use of retrieve-operation (Less code-lines, algorithm +/-= same)

"""Data"""
"""ListItemType is het type van elementen, mogelijks te plaatsen in een Python-List"""
class ChainItemType:
    """'ChainItemType' is het type van elementen in de Linkedchain."""
    def __init__(self, value):
        """
        Creëert een 'ChainItemType'. // Constructor
        Précondities: 'value' is een object wat in een Python-List (ListItemType) geplaatst kan worden. in value:ListItemType
        Postcondities: Maakt een object volgens type 'ChainItemype' aan. Dit type bevat een 'value', de inhoud van een node. 'next' is zelf een 'ChainItemType' en wordt geïnitaliseerd op "None".
        """
        self.value = value
        self.next = None

"""Functionaliteit"""
class MyLinkedChain:
    def __init__(self):
        """
        Creëert een lege ketting. // Constructor
        Précondities:
        Postcondities: Maakt een lege ketting aan waarvan de 'head' is geïnitaliseerd op None (zowel 'value' als 'next').
        """
        self.head = ChainItemType(None)

    def isEmpty(self):
        """
        Bepaalt of een lijst leeg is.
        Précondities: Er is een 'LinkedChain' aangemaakt.
        Postcondities: Geeft true als de lijst leeg is en false als de lijst niet leeg is. boolean {query}
        """
        if self.head.value==None: #Check if there is something placed as head
            return True
        return False #Else

    def getLength(self):
        """
        Bepaalt de lengte (het aantal elementen) van de lijst.
        Précondities: Er is een 'LinkedChain' aangemaakt.
        Postcondities: Geeft het aantal elementen in de lijst terug. integer {query}
        """
        lenght = 0 #Initalize length on 0
        if self.isEmpty():
            return lenght
        else:
            lenght = 1 #There is at least a head, so lengt=1
            temp = self.head
            while (temp.next != self.head): #Go through chain & calculate length+1 by every element passed until back at head
                temp = temp.next
                lenght += 1
            return lenght

    def insert(self, positie, newItem):
        """
        Voegt een element toe op een bepaalde positie in de lijst.
        Précondities: Er is een 'LinkedChain' aangemaakt. ‘positie’ duidt de plaats aan waar het element ‘newItem’ moet worden toegevoegd. in positie:integer, in newItem:ListItemType
        Postcondities: Als het toevoegen lukte, dan zit ‘newItem’ op ‘positie’ in de lijst en is ‘success’ true. Als in de oorspronkelijke lijst positie <= getLength(), dan zijn de elementen als volgt hernummerd: het element op ‘positie’ naar ‘positie+1’, het element op ‘positie+1’ naar ‘positie+2’, enz.. ‘success’ is false als het toevoegen niet lukte, bvb. als positie < 1 of positie > getLength()+1. out success:boolean)
        """
        if ((positie>self.getLength()+1) or (positie<=0)):
            return False

        if self.head.value==None: #Inserten bij lege list is een iets ander geval
            newItem = ChainItemType(newItem)
            self.head=newItem
            self.head.next=newItem
            return True
        elif positie==1: #Inserten op positie 1=root aanpassen (net iets anders)
            nonlinked = ChainItemType(newItem) #Make new item
            #Find predecessor
            i = 0
            predecessor = self.head
            while (i < positie ): #Predecessor=last item
                predecessor = predecessor.next
                i += 1
            #Find position
            temp=predecessor.next #position = simpelweg de volgende

            predecessor.next=nonlinked #Voeg tussen in toe
            nonlinked.next=temp

            self.head=nonlinked #Head is new item
            return True
        else:
            nonlinked = ChainItemType(newItem) #Make new item
            #Find predecessor
            i = 0
            predecessor = self.head
            while (i < positie -2 ):
                predecessor = predecessor.next
                i += 1
            #Find position
            temp=predecessor.next #position = simpelweg de volgende

            predecessor.next=nonlinked #Voeg tussen in toe
            nonlinked.next=temp
            return True

    def delete(self, positie):
        """
        Verwijdert het element op een bepaalde positie uit de lijst.
        Précondities: Er is een 'LinkedChain' aangemaakt. ‘positie’ duidt de plaats aan van het element dat moet verwijderd worden. in positie:integer
        Postcondities: Als in de oorspronkelijke lijst 1 <= positie <= getLength(), dan is het element op ‘positie’ uit de lijst verwijderd en als positie < getLength(), dan zijn de elementen als volgt hernummerd: het element op ‘positie+1’ naar ‘positie’, het element op ‘positie+2’ naar ‘positie+1’, enz.. ‘success’ is true als het verwijderen lukte en false als het niet lukte. out success:boolean
        """
        if self.isEmpty() or positie>self.getLength() or positie<=0: #Précondities "niet" voldaan
            return False

        if positie==1:  #=Head deleten       #Predecessor=laatste item
            Predecessor=self.head
            #Find last item     #Had ook gekund met retrieve
            while(Predecessor.next!=self.head):
                Predecessor=Predecessor.next
            Predecessor.next=self.head.next #Het 1e item wordt het item na de head // Opvolger van predecessor
            self.head=self.head.next #De head wordt nu de eerst volgende
            return True

        else:
            predecessor=self.retrieve(positie-2)  # Find predecessor
            predecessor[2].next=predecessor[2].next.next #next wordt de 2e volgende
            #OP%: qua geheugen structuur, moet hier dan het itemzelf.next op None gezet worden?
            return True

    def retrieve(self, positie):
        """
        Vraagt het element op een bepaalde positie in de lijst op.
        Précondities: Er is een 'LinkedChain' aangemaakt. ‘positie’ duidt de plaats aan van het op te vragen element. in positie:integer
        Postcondities: Als in de oorspronkelijke lijst 1 <= positie <= getLength(), dan bevat ‘dataItem’ het element van de lijst op ‘positie’. De lijst blijft onveranderd bij deze bewerking.‘Success’ is true als het opvragen lukte en false als het niet lukte. out dataItem:ListItemType, out success:boolean {query}
        """
        if positie>self.getLength() or self.isEmpty(): #Précondities "niet" voldaan
            return (False,False)

        else:
            i=0
            temp=self.head
            while(i < positie): #Loop over elementen totdat we bij de juiste positie zijn
                temp=temp.next
                i+=1

            return(temp.value,True,temp)

    def save(self):
        """
        Exporteert een LinkedChain als een Python-List.
        Précondities: Er is een 'LinkedChain' aangemaakt.
        Postcondities: Geeft een Python-List met alle elementen uit de LinkedChain mee in volgorde van head tot het laatste element. out save:Python-List {query}
        """
        save= []
        if self.isEmpty():
            return save

        temp = self.head.next
        save.append(self.head.value)
        while (temp != self.head):
            save.append(temp.value)
            temp = temp.next
        return save

    def load(self,list):
        """
        Converteert een Python-List naar een LinkedChain en verwijdert hierbij de, eventueel bestaande, LinkedChain.
        Précondities:
        Postcondities: Voegt ieder element in volgorde uit de Python-List toe aan de nieuw aangemaakte LinkedChain.
        """
        self.head=ChainItemType(None)
        positie=1
        for i in range(len(list)):
            self.insert(positie,list[i])
            positie+=1
        return

class LCTable:
    def __init__(self):
        self.chain = MyLinkedChain()

    def tableIsEmpty(self):
        return self.chain.isEmpty()

    def tableInsert(self, index, val):
        return self.chain.insert(index,val)

    def tableRetrieve(self, index):
        return self.chain.retrieve(index)

    def tableRetrieveTranverse(self, id):
        counts = 0
        value = self.chain.head.value
        while counts<self.chain.getLength():
            tuple = self.chain.retrieve(self,counts)
            if tuple[1]==False:
                return False
            if tuple[0].id == id:
                return value
            counts += 1
        return False

    def tableDelete(self, index):
        return self.chain.delete(index)

    def tableGetLength(self):
        return self.chain.getLength()

    def load(self, list):
        return self.chain.load(list)

    def save(self):
        return self.chain.save()

    def clear(self):
        self.chain = MyLinkedChain()