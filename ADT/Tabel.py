from ADT import MyCircularLinkedChainAnas, MyRedBlackTreeAnas
from ProtoType.Zaal import Zaal

class Tabel:
    def __init__(self, main_adt):
        self.adt = main_adt

        self.key = None
        self.return_item = (None, False)

    def TableInsert(self, key, value, sub_adt=None):
        if isinstance(key, int):
            return self.adt.tableInsert(key, value)

        elif isinstance(key, tuple):
            key, key2 = key

            if not self.adt.tableIsEmpty():
                current_adt, found = self.adt.tableRetrieve(key)
            else:
                found = False
            if found:
                return current_adt.tableInsert(key2, value)
            else:
                if sub_adt == None or not sub_adt.tableIsEmpty():
                    raise Exception("Preconditie Wrapper string compatible: sub-adt niet empty")

                sub_adt.id = key #Set First ID
                sub_adt.tableInsert(key2, value)
                return self.adt.tableInsert(key, sub_adt)

    def TableRetrieve(self, key):
        if isinstance(key, int):
            return self.adt.tableRetrieve(key)
        elif isinstance(key, tuple):
            self.key = key[0]
            self.adt.traverseTable(self.__TraverseRetrieveCall)

            local_return_item = self.return_item
            self.key = None
            self.return_item = (None, False)

            return local_return_item

    def __TraverseRetrieveCall(self, current_adt):
        item, b = current_adt.tableRetrieve(self.key)
        if b:
            self.return_item = (item, b)

t = Tabel(MyCircularLinkedChainAnas.LCTable())
t.TabelInsert(("hermans", 0), Zaal(0, 200), MyRedBlackTreeAnas.RedBlackTreeTable())
t.TabelInsert(("hermans", 2), Zaal(2, 200), MyRedBlackTreeAnas.RedBlackTreeTable())
t.TabelInsert(("pieter", 4), Zaal(4, 200), MyRedBlackTreeAnas.RedBlackTreeTable())
print(t.TabelRetrieve((0,)))
print(t.TabelRetrieve((2,)))
print(t.TabelRetrieve((4,)))
print(t.TabelRetrieve((1,)))

