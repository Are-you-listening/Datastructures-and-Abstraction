"""ADT: Linked Based Implementatie van een Stack"""

""" 'ItemType', het type van de items in de Stack. (Python Object) """

"""Data"""
class StackItemType:
    """
    StackItemType is het type (string, boolean, integer,...) van de elementen in de stack.
    :parameter in; 'ItemType', het type van de items in de stack
    :parameter out; Geen
    Preconditie: 'ItemType' is een object wat in een Python List gestopt kan worden.
    Postconditie: 'StackItemType' is gedefinieerd. Het bevat een paramater 'prev' (=None) & 'ItemType'=(ItemType).
    """
    def __init__(self,ItemType):
        self.ItemType=ItemType
        self.prev=None


"""Functionaliteit"""
class MyStack:
    def __init__(self):
        """
        Creëert een lege stack.
        :parameter in ; Geen
        :parameter out ; Geen
        Preconditie:
        Postconditie: Er is een lege stack ('items') aangemaakt met een top ingesteld op None.
        """
        self.top=None

    def isEmpty(self):
        """
        Bepaalt of een stack leeg is.
        :parameter in; Geen
        :parameter out; Boolean (True/False) // "boolean {query}"
        Preconditie: Er is een stack aangemaakt.
        Postconditie: Geeft True als de stack leeg is, False als de stack gevuld is.
        """
        if self.top==None:
            return True
        else:
            return False

    def push(self, newItem):
        """
        Voegt het element ‘newItem’ toe op de top van een stack.
        :parameter in; ‘newItem’ is eenzelfde type/object als ItemType. // in newItem:ItemType
        :parameter out; Boolean (True/False) // out success:boolean
        Preconditie: ‘newItem’ geeft het toe te voegen element mee met ItemType: ‘ItemType’. Er is een stack aangemaakt.
        Postconditie: Er wordt True teruggegeven bij een geslaagde operatie, False bij een niet geslaagde operatie. Bij een geslaagde operatie is ‘newItem’ toegevoegd aan de top van de stack.
        """
        newItem=StackItemType(newItem)
        if self.top==None:
            self.top=newItem
            return True
        else:
            temp=self.top
            self.top=newItem
            newItem.prev=temp
            return True

    def pop(self):
        """
        Verwijdert de top van een stack. ‘success’ duidt aan of het verwijderen gelukt is.
        :parameter in; Geen
        :parameter out; Tuple van 'prepop_StackTop.ItemType' & een Boolean. 'prepop_StackTop.ItemType' is de top van de stack voordat er een pop-operatie is uitgevoerd. // out prepop_StackTop.ItemType:ItemType, out success:boolean
        Preconditie: Er is een stack aangemaakt.
        Postconditie: Als de stack niet leeg is dan kan de top van de stack verwijdert worden.  Bij een geslaagde operatie is de top van een stack, d.w.z. het laatst toegevoegd element, verwijdert van de stack. Als de stack leeg is, is de operatie niet geslaagd. Er wordt een tupel van de 'prepop_StackTop' & 'True' teruggegeven bij een geslaagde operatie of een tuple van 'None' (Er is geen top) & 'False' teruggegeven bij een niet geslaagde operatie. // out success:boolean
        """
        if self.top!=None:
            prepop_StackTop = self.top
            self.top=prepop_StackTop.prev
            return (prepop_StackTop.ItemType,True)
        return (None,False)

    def getTop(self):
        """
        Geeft de huidige top van een stack mee.
        :parameter in; Geen
        :parameter out; Tuple van de 'StackTop' & een Boolean. 'Stacktop' (self.top.ItemType) is de top van de stack. (d.i. het laatst toegevoegde element)
        Preconditie: Er is een stack aangemaakt.
        Postconditie: Als de stack niet leeg is wordt een tupel met 'StackTop' en 'True' meegegeven. De stack blijft ongewijzigd. Als de stack leeg is, wordt er een tuple van 'None' & 'False' meegegeven. De top van de stack bestaat dan niet, en bedraagt dus 'None'. // out stackTop:ItemType, out success:boolean) {query}
        """
        if self.top!=None:
            return (self.top.ItemType, True)
        else:
            return (None, False)

    def save(self):
        """
        Geeft de huidige stack als lijst mee.
        :parameter in; Geen
        :parameter out; 'save', de lijst die alle elementen uit de stack bevat.
        Preconditie: Er is een stack aangemaakt. 'save' is een lege lijst.
        Postconditie: De lege lijst 'save' wordt opgevuld met de elementen uit de stack en vervolgens meegegeven.
        """
        save=[]
        temp=self.top

        while(temp!=None):
            save.append(temp.ItemType)
            temp=temp.prev

        save2=[]
        z=len(save)
        for i in range(z):
            save2.append(save[z-1-i])

        return save2

    def load(self,aStack):
        """
        Maakt een stack aan/laadt een stack in.
        :parameter in; 'aStack', een stack gerepresenteerd in een Python lijst.
        :parameter out; Geen
        Preconditie: De volgordes van de PythonLijst is de volgorde van toevoegen aan de Stack.
        Postconditie: Er wordt een stack aangemaakt die de elementen van 'aStack' bevat. De oude stack wordt verwijdert.
        """
        self.top=None
        z=len(aStack)
        for i in range(len(aStack)):
            self.push(aStack[i])
