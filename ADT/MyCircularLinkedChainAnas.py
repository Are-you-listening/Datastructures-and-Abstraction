import copy

class Node:
    # constructer
    """
        Creëert een node die over een doorgekregen value bezit

        :param value: De value dat de Node moet hebben

        preconditions: geen

        postconditions: Er wordt een lege LinkedChain gecreëered

        :return: niets
        """
    def __init__(self, value):
        self.value = value
        self.nextNode = None
        self.previousNode = None


class LinkedChain:

    # constructer
    """
    Creëert een lege LinkedChain

    preconditions: geen

    postconditions: Er wordt een lege LinkedChain gecreëered

    :return: niets
    """
    def __init__(self):
        self.head = None

    ## functionaliteit
    def isEmpty(self):
        """
        Controleert de opgegeven LinkedChain of die leeg is of niet en geeft naarmate hiervan een booleaanse waarde terug.
        True als de stack LinkedChain leeg is, False als dit niet het geval is.

        De LinkedChain waarvan bepaald moet worden of deze leeg is, of niet, wordt doorgegeven als Container type.

        parameters: Geen

        preconditions: Er bestaat een LinkedChain met de opgegeven benaming doorgekregen van de user.

        postconditions: De functie geeft een booleaanse waarde weer.
        Er vinden geen gegevens wijzigingen plaats.

        :return: De functie geeft naarmate de LinkedChain vol of leeg is een booleaanse waarde terug.
        """
        if self.head == None:
            return True
        else:
            return False

    ## functionaliteit
    def insert(self, index, value):
        """
        Plaatst een gegeven value op een bepaalde positie in de linkedChain

        :param index: De positie waar de value geplaatst moet worden
        :param value: De value dat een bepaalde index van de linkedchain moet bezitten

        preconditions: De index ligt niet buiten bereik van de LinkedChain

        postconditions: De linkedChain bezit over de doorgekregen value, de value zit op de doorgekregen index
        Er vinden gegevens wijzigingen plaats.

        :return: Geeft true terug als het inserten gelukt is
        """
        if index > self.getLength() + 1:
            return False
        if index == 1 and self.head == None:
            newNode = Node(value)
            self.head = newNode
            return True
        elif self.head == None:
            return False
        node = self.head
        newNode = Node(value)
        b = False

        while index != 1:
            index -= 1
            if node.nextNode == None:
                b = True
                break;
            node = node.nextNode
        if b:
            node.nextNode = newNode
            newNode.previousNode = node
        elif node.previousNode == None:
            node1 = copy.deepcopy(self.head)
            self.head = newNode
            newNode.nextNode = node1
            node1.previousNode = newNode
        else:
            node.previousNode.nextNode = newNode
            newNode.previousNode = node.previousNode
            newNode.nextNode = node
            node.previousNode = newNode
        return True

    ## functionaliteit
    def retrieve(self, index):
        """
        Retrieved de value op de gegeven index

        :param index: De positie waar de gezochte value zich bevindt

        preconditions: De index ligt niet buiten bereik van de LinkedChain

        postconditions: De functie return een pair met de gezochte value en een bool die weergeeft of het retrieven gelukt is of niet
        als het retrieven niet gelukt is wordt een pair gereturned met waarden: 0 en false
        Er vinden geen gegevens wijzigingen plaats.

        :return: een pair met de gezochte value en een bool
         """
        if index > self.getLength() + 1:
            return (0, False)
        if self.head == None:
            return (0, False)
        if index == 1:
            return (self.head.value, True)
        node = self.head
        while index != 1:
            index -= 1
            if node.nextNode == None:
                b = True
                break;
            node = node.nextNode
        return (node.value, True)

    ## functionaliteit
    def getLength(self):
        """
        Weergeeft de LinkedChain zijn lengte

        preconditions: Er word een LinkedChain doorgegeven

        postconditions: De functie return de lengte van de LinkedChain, een empty LinkedChain heeft als lengte 0
        Er vinden geen gegevens wijzigingen plaats.

        :return: De lengte van de LinkedChain
        """
        count = 1
        if self.head == None:
            return 0
        node = self.head.nextNode
        while node != None:
            node = node.nextNode
            count = count + 1
        return count

    ## functionaliteit
    def save(self):
        """
        Weergeeft de LinkedChain als string formaat

        preconditions: Er word een LinkedChain doorgegeven

        postconditions: De functie return de LinkedChain als een list in string form
        Er vinden geen gegevens wijzigingen plaats.

        :return: De LinkeChain als list in string from
        """
        c = "["
        c += str(self.head.value)
        node = self.head.nextNode
        while node != None:
            c += "," + str(node.value)
            node = node.nextNode
        c += "]"
        return c

    ## functionaliteit
    def load(self, l):
        """
        Creëert een LinkedChain van de doorgekregen list en vervangt de doorgekregen LinkedChain met de Gecreëerde LinkedChain

        :param l: Een list

        preconditions: Er word een LinkedChain doorgegeven en een list doorgegeven

        postconditions: De doorgekregen LinkedChain is vervangen worden met de LinkedChain die de waarden van de list bezit
        Er vinden gegevens wijzigingen plaats.

        :return: niets
        """
        lcopy = LinkedChain();
        count = 1
        for i in l:
            lcopy.insert(count, i)
            count += 1;
        self.head = lcopy.head

    ## functionaliteit
    def delete(self, index):
        """
        Verwijdert de node die over de doorgekregen index bezit uit de LinkedChain

        :param index: De positie in de LinkedChain van de te verwijderen node

        preconditions: de index ligt niet buiten bereik van de LinkedChain

        postconditions: De doorgekregen LinkedChain bezit niet meer over de node die over de doorgekregen index bezitte
        Er vinden gegevens wijzigingen plaats.

        :return: True als het verwijderen gelukt en false als niet
        """
        if index > self.getLength():
            return False
        if index == 1 and self.head.nextNode == None:
            del self.head
            return True
        if index < 1:
            return False

        node = self.head
        b = False

        while index != 1:
            index -= 1
            if node.nextNode == None:
                b = True
                break
            node = node.nextNode

        if node.nextNode == None:
            node.previousNode.nextNode = None
            node.previousNode = None
            del node

        elif node.previousNode == None:
            self.head = self.head.nextNode
            self.head.previousNode = None

        else:
            node.previousNode.nextNode = node.nextNode
            node.nextNode.previousNode = node.previousNode
            del node
        return True

class LCTable:
    def __init__(self):
        self.LC = LinkedChain()
        self.id = None

    def tableIsEmpty(self):
        return self.LC.isEmpty()

    def tableInsert(self, index, val):
        if isinstance(index, int) and index<self.tableGetLength():
            return self.LC.insert(index,val)
        return self.LC.insert(1,val)

    def tableRetrieveIndex(self, index):
        return self.LC.retrieve(index)

    def tableRetrieve(self, id):
        count = 0

        object_tuple = self.tableRetrieveIndex(count)
        object = object_tuple[0]


        if (isinstance(object, tuple)):
             object = object[0]
        #else:
        #    return (object, object_tuple[1])


        while object.get_id() != id:
            if self.tableRetrieveIndex(count)[1] == False:
                return (None, False)
            count += 1
            if count == self.LC.getLength():
                return (None, False)
            object = self.tableRetrieveIndex(count)[0]
            if (isinstance(object, tuple)): # Tuple(Vertoning,Stack) heeft geen functie .get_id()
                object = object[0]
        return (self.tableRetrieveIndex(count)[0], True)

    def traverseTable(self, arg):
        for i in range(self.tableGetLength()):
            arg(self.tableRetrieveIndex(i)[0])

    def tableDelete(self, index):
        return self.LC.delete(index)

    def tableGetLength(self):
        return self.LC.getLength()

    def load(self, list):
        return self.LC.load(list)

    def save(self):
        return self.LC.save()

    def clear(self):
        self.LC = LinkedChain()

    def get_id(self):
        return self.id