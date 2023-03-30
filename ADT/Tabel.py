import random
from ADT import MyBSTAnas, MyCircularLinkedChainAnas, MyQueueAnas, MyRedBlackTreeAnas, MyStackAnas
from ADT import MyBSTEmil, MyCircularLinkedChainEmil, MyQueueEmil, MyTwoThreeFourTreeEmil, MyStackEmil
from ADT import MyBSTKars, MyCircularLinkedChainKars, MyQueueKars, MyTwoThreeFourTreeKars, MyStackKars
from ADT import MyBSTTibo, MyCircularLinkedChainTibo, MyQueueTibo, MyTwoThreeFourTreeTibo, MyStackTibo
from ProtoType.Zaal import Zaal

class Tabel:
    def __init__(self, main_adt, dubbele_key=False):
        self.adt = main_adt

        self.dubbele_key = dubbele_key

        self.key = None
        self.return_item = (None, False)

        self.traverse_function = None

        self.linked_chain = MyCircularLinkedChainAnas.LCTable()
        self.linked_chain.load(["MyBSTAnas.BSTTable()", "MyBSTEmil.BSTTable()", "MyBSTTibo.BSTTable()", "MyBSTKars.BSTTable()",
                                "MyCircularLinkedChainAnas.LCTable()", "MyCircularLinkedChainEmil.LCTable()",
                                "MyCircularLinkedChainKars.LCTable()", "MyCircularLinkedChainTibo.LCTable()",
                                "MyRedBlackTreeAnas.RedBlackTreeTable()", "MyTwoThreeFourTreeEmil.TwoThreeFourTreeTable()", "MyTwoThreeFourTreeKars.TwoThreeFourTreeTable()", "MyTwoThreeFourTreeTibo.TwoThreeFourTreeTable()"])


    def tableInsert(self, key, value, sub_adt=None):
        if not self.dubbele_key: #Normal Insert on ID
            return self.adt.tableInsert(key, value)

        else: #Insert op bv. achternaam // meerdere keys

            if (isinstance(value, tuple)): #The only value tuple is (Vertoning,Stack): This is to prevent that we can actually call .get_id()
                value_id = value[0].get_id()
            else:
                value_id = value.get_id()
            key, key2 = (key, value_id) #Split up keys | key = bv achternaam | key2 = id

            if not self.adt.tableIsEmpty(): #Indien niet leeg; er is al een sub_adt om operaties op aan te roepen
                current_adt, found = self.adt.tableRetrieve(key)
                #current_adt, found = self.TabelRetrieve(key_original)
            else: #Indien leeg  (nog geen sub_adt)
                found = False

            if found: #Er is een sub_adt, insert hierop
                return current_adt.tableInsert(key2, value)
            else: #Er is nog geen sub_adt, plaats de meegegeven sub_adt
                #Check up if newly given sub_adt is correct/valid
                if sub_adt == None:
                    r = random.randint(0, 11)
                    sub_adt = eval(self.linked_chain.tableRetrieveIndex(r)[0])
                if sub_adt == None or not sub_adt.tableIsEmpty():
                    raise Exception("Preconditie Wrapper string compatible: sub-adt niet empty")

                sub_adt.id = key #Set First ID
                sub_adt.tableInsert(key2, value)
                return self.adt.tableInsert(key, sub_adt)

    def tableRetrieve(self, key):
        if not self.dubbele_key:
            return self.adt.tableRetrieve(key)
        else:
            self.key = key
            self.adt.traverseTable(self.__TraverseRetrieveCall)

            local_return_item = self.return_item
            self.key = None
            self.return_item = (None, False)
            return local_return_item

    def __TraverseRetrieveCall(self, current_adt):
        if (isinstance(current_adt, tuple)):  # The only value tuple is (Vertoning,Stack): This is to prevent that we can actually call .get_id()
            current_adt = current_adt[0]
        else:
            current_adt = current_adt

        item, b = current_adt.tableRetrieve(self.key)
        if b:
            self.return_item = (item, b)

    def tableIsEmpty(self):
        return self.adt.tableIsEmpty()

    def clear(self):
        self.adt.clear()

    def traverseTable(self, function):
        if not self.dubbele_key:
            self.adt.traverseTable(function)

        else:
            self.traverse_function = function
            self.adt.traverseTable(self.__traverse)

    def __traverse(self, current_adt):
        if current_adt != None:
            current_adt.traverseTable(self.traverse_function)