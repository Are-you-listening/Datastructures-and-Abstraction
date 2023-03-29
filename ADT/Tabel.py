from ADT import MyBSTTibo
from ProtoType.Zaal import Zaal

class Tabel:
    def __init__(self, main_adt):
        self.adt = main_adt

        self.key = None
        self.return_item = (None, False)

    def TabelInsert(self, key, value, sub_adt=None):
        if isinstance(key, int): #Normal Insert on ID
            return self.adt.tableInsert(key, value)

        elif isinstance(key, tuple): #Insert op bv. achternaam // meerdere keys
            key, key2 = key #Split up keys | key = bv achternaam | key2 = id

            if not self.adt.tableIsEmpty(): #Indien niet leeg; er is al een sub_adt om operaties op aan te roepen
                current_adt, found = self.adt.tableRetrieve(key)
                #current_adt, found = self.TabelRetrieve(key_original)
            else: #Indien leeg  (nog geen sub_adt)
                found = False

            if found: #Er is een sub_adt, insert hierop
                return current_adt.tableInsert(key2, value)
            else: #Er is nog geen sub_adt, plaats de meegegeven sub_adt

                #Check up if newly given sub_adt is correct/valid
                if sub_adt == None or not sub_adt.tableIsEmpty():
                    raise Exception("Preconditie Wrapper string compatible: sub-adt niet empty")

                sub_adt.id = key #Set First ID
                sub_adt.tableInsert(key2, value)
                return self.adt.tableInsert(key, sub_adt)

    def tableRetrieve(self, key):
        if not self.dubbele_key:
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
