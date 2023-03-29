from ADT import MyRedBlackTreeAnas

class Tabel:
    def __init__(self, main_adt):
        self.adt = main_adt

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

                sub_adt.tableInsert(key2, value)
                return self.adt.tableInsert(key, sub_adt) #hiero

    def TableRetrieve(self, key):
        if isinstance(key, int):
            return self.adt.tableRetrieve(key)
        elif isinstance(key, tuple):
            key, key2 = key
            current_adt, found = self.adt.tableRetrieve(key)
            if not found:
                return None, False

            return current_adt.tableRetrieve(key2)


t = Tabel(MyRedBlackTreeAnas.RedBlackTreeTable())
t.TableInsert(("hermans", 0), 1, MyRedBlackTreeAnas.RedBlackTreeTable())
t.TableInsert(("hermans", 2), 3, MyRedBlackTreeAnas.RedBlackTreeTable())
t.TableInsert(("pieter", 4), 5, MyRedBlackTreeAnas.RedBlackTreeTable())
print(t.TableRetrieve(("hermans", 0)))
print(t.TableRetrieve(("hermans", 2)))
print(t.TableRetrieve(("pieter", 4)))
