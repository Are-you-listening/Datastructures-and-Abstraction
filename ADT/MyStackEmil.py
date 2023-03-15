#arraybased stack ADT
class stackItemType:
    def __init__(self, value):
        self.value = value


class MyStack:
    def __init__(self, max_size):
        """
        creëert een lege stack
        precondities: max_size > 0
        postcondities: Nieuwe lege stack aangemaakt (size==0)
        :param max_size: maximale grootte van de stack
        """
        self.max_size = max_size
        self.items = [None] * max_size
        self.size = 0

    def isEmpty(self):
        """
        precondities: De stack bestaat
        postcondities: De stack wordt niet gewijzigd
        :return: True als de stack leeg is, anders False
        """
        if self.size == 0:
            return True
        else:
            return False

    def push(self, newItem):
        """
        precondities: De stack is niet vol
        postcondities: de grootte van de stack is met 1 verhoogt
        :param newItem: Het item dat aan de stack moet worden toegevoegd
        :return: False als het niet kan worden toegevoegd, anders True
        """
        if self.size == self.max_size:
            return False
        self.items[self.size] = newItem
        self.size += 1
        return True

    def pop(self):
        """
        precondities: De stack is niet leeg
        postcondities: de grootte van de stack is met 1 verlaagt
        :return: (stackTop: Item dat verwijderd wordt, True als het succesvol verwijderd is, anders False)
        """
        if self.isEmpty():
            stackTop = None
            return tuple([stackTop, False])
        stackTop = stackItemType(self.items[self.size-1])
        self.items[self.size - 1] = None
        self.size -= 1
        return tuple([stackTop.value, True])

    def getTop(self):
        """
        precondities: De stack is niet leeg
        postcondities: De stack wordt niet gewijzigd
        :return: (stackTop: top van de stack, True als er een item gevonden is, anders False)
        """
        if self.isEmpty():
            stackTop = None
            return tuple([stackTop, False])
        stackTop = stackItemType(self.items[self.size-1])
        return tuple([stackTop.value, True])

    def save(self):
        """
        preconditie: de stack is niet leeg
        postconditie: de stack in self wordt niet aangepast
        :return: De stack als string
        """
        result = [None] * self.size
        for i in range(self.size):
            result[i] = self.items[i]
        result = str(result)
        return result

    def load(self, stack):
        """
        preconditie: de string is een geldige stack
        postconditie: de stack in self wordt vervangen met de nieuwe stack en heeft ook een nieuwe maxsize
        :param stack: de string die naar stack moet worden omgezet
        :return:
        """
        L = list(stack)
        self.size = len(L)
        self.items = L

class MyStackTable:
    def __init__(self):
        self.stack = MyStack(100)

    def tableIsEmpty(self):
        return self.stack.isEmpty()

    def tableInsert(self, newitem):
        if not self.stack.push(newitem):
            newstack = MyStack(self.stack.max_size * 2)
            for i in range(self.stack.size):
                newstack.push(self.stack.pop()[0])
            self.stack = newstack

        return self.stack.push(newitem)


    def tableFirst(self):
        return self.stack.getTop()

    def tableDelete(self):
        return self.stack.pop()

    def save(self):
        return self.stack.save()

    def load(self, input):
        return self.stack.load(input)

    def clear(self):
        self.stack = MyStack()