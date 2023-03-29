class ChainItemType:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedChain:
    def __init__(self):
        """
        preconditie:
        postconditie: creëert een lege ketting
        """
        self.length = 0
        self.dummyhead = ChainItemType(None)
        self.dummyhead.next = self.dummyhead
        self.dummyhead.prev = self.dummyhead

    def isEmpty(self):
        """
        preconditie:
        postconditie: de ketting wordt niet aangepast
        :return: True als de ketting leeg is, anders False
        """
        if self.length == 0:
            return True
        else:
            return False

    def getLength(self):
        """
        preconditie:
        postconditie: de Ketting wordt niet aangepast
        :return: de lengte van de ketting
        """
        return self.length

    def insert(self, positie, newItem):
        """
        preconditie: de positie ligt binnen de grenzen van de ketting: 1<= positie <= getLength()+1
        postconditie: de lengte van de ketting is met 1 verhoogt en alle items na 'positie' zijn met 1 verplaatst
        :param positie: de index waar we het nieuwe Item moeten invoegen
        :param newItem: het Item dat moet worden ingevoegd
        :return: True als het invoegen gelukt is, anders False
        """
        newLink = ChainItemType(newItem)

        if positie > self.length+1 or positie < 1:
            return False

        currentChain = self.dummyhead
        count = 0

        if positie == self.length+1:
            if self.length == 0:
                self.dummyhead.next = newLink
                self.dummyhead.prev = newLink
                newLink.prev = self.dummyhead
                newLink.next = self.dummyhead
                self.length += 1
                return True
            else:
                currentChain = self.dummyhead.prev
                currentChain.next = newLink
                newLink.prev = currentChain
                newLink.next = self.dummyhead
                self.dummyhead.prev = newLink
                self.length += 1
                return True

        while count != positie:
            currentChain = currentChain.next
            count += 1
        currentChain.prev.next = newLink
        newLink.prev = currentChain.prev
        newLink.next = currentChain
        currentChain.prev = newLink
        self.length += 1
        return True

    def delete(self, positie):
        """
        preconditie: de ketting bevat een item op 'positie'
        postconditie: de lengte van de ketting is met 1 verlaagt en alle items na 'positie' zijn met 1 naar links verschoven
        :param positie: de index van het Item dat verwijderd moet worden
        :return: True als het gelukt is, anders False
        """
        if positie > self.length+1 or positie < 1:
            return False

        currentLink = self.dummyhead

        if positie == 1:
            self.dummyhead.next = self.dummyhead.next.next
            self.dummyhead.next.prev = self.dummyhead
            self.length -= 1
            return True
        if positie == self.length:
            self.dummyhead.prev = self.dummyhead.prev.prev
            self.dummyhead.prev.next = self.dummyhead
            self.length -= 1
            return True
        if positie <= self.length/2:
            count = 0
            while count != positie:
                currentLink = currentLink.next
                count += 1
        elif positie > self.length/2:
            count = self.length + 1
            while count != positie:
                currentLink = currentLink.prev
                count -= 1
        currentLink.prev.next = currentLink.next
        currentLink.next.prev = currentLink.prev
        self.length -= 1
        return True

    def retrieve(self, positie):
        """
        preconditie: de ketting bevat een item op 'positie'
        postconditie: de ketting wordt niet gewijzigd
        :param positie: de index van het item dat we zoeken
        :return: het Item op 'positie' en True als het gelukt is, anders None en False
        """

        if positie > self.length+1 or positie < 1:
            return None, False

        currentLink = self.dummyhead

        if positie <= self.length/2:
            count = 0
            while count != positie:
                currentLink = currentLink.next
                count += 1
        elif positie > self.length/2:
            count = self.length + 1
            while count != positie:
                currentLink = currentLink.prev
                count-=1
        return currentLink.value, True

    def save(self):
        """
        preconditie:
        postconditie: de ketting wordt niet aangepast
        :return: de ketting in de vorm van een string
        """
        result = "["
        currentLink = self.dummyhead.next

        while currentLink != self.dummyhead.prev:
            result += str(currentLink.value) + ", "
            currentLink = currentLink.next
        result += str(currentLink.value)
        result += "]"
        return result

    def load(self, input):
        """
        preconditie:
        postconditie: de ketting in self wordt overschreven met de ketting uit input
        """
        while self.dummyhead.next != self.dummyhead:
            self.delete(1)
        ketting = list(input)
        for i in range(len(ketting)):
            self.insert(i+1, ketting[i])

class LCTable:

    def __init__(self):
        self.chain = LinkedChain()

    def tableIsEmpty(self):
        return self.chain.isEmpty()

    def tableInsert(self, index, newItem):
        self.chain.insert(index, newItem)

    def tableRetrieve(self, plaats):
        return self.chain.retrieve(plaats)

    def tableRetrieve(self, searchkey):
        currentNode = self.chain.dummyhead.next
        while currentNode != self.chain.dummyhead:
            if currentNode.value.get_id() == searchkey:
                return currentNode.value
            currentNode = currentNode.next
        return False

    def tableDelete(self, key):
        currentNode = self.chain.dummyhead
        count = 0
        while currentNode.next != self.chain.dummyhead:
            if currentNode.value == key:
                self.chain.delete(count)
                return True
            currentNode = currentNode.next
            count += 1
        return False

    def traverseTable(self, visitfunction):
        currentNode = self.chain.dummyhead
        while currentNode.next != self.chain.dummyhead:
            visitfunction(currentNode.value)

    def tableGetLength(self):
        return self.chain.getLength()

    def save(self):
        return self.chain.save()

    def load(self, input):
        return self.chain.load(input)

    def clear(self):
        self.chain = LinkedChain()