import copy
from copy import deepcopy

class KeyType:
    def __init__(self, key):
        self.key = key

class TreeItemType:
    def __init__(self, key, val):
        self.key = KeyType(key)
        self.val = val

def createTreeItem(key,val):
    return TreeItemType(key, val)

class BST:
    def __init__(self):
        """
        precondities:
        postcondities: er is een nieuwe BST aangemaakt
        """
        self.content = createTreeItem(None,None)
        self.leftchild = None
        self.rightchild = None


    def isEmpty(self):
        """
        preconditie:
        postconditie: de BST wordt niet aangepast
        :return: True als de BST leeg is, anders False
        """
        if self.content.key.key == None:
            return True
        else:
            return False

    def searchTreeInsert(self, newItem):
        """
        preconditie: de BST bevat nog geen item met dezelfde key als newItem
        postconditie: er is een blad met newItem aan de BST toegevoegd
        :param newItem: de key en value dat aan de BST moeten worden toegevoegd
        :return: True als het toevoegen gelukt is, anders False
        """
        if self.content.key.key == None:
            self.content = newItem
            return True

        currentTree = self
        newTree = BST()
        newTree.content = newItem
        while True:
            if newItem.key.key < currentTree.content.key.key and currentTree.leftchild != None:
                currentTree = currentTree.leftchild
            elif newItem.key.key < currentTree.content.key.key and currentTree.leftchild == None:
                currentTree.leftchild = newTree
                return True
            elif newItem.key.key > currentTree.content.key.key and currentTree.rightchild != None:
                currentTree = currentTree.rightchild
            elif newItem.key.key > currentTree.content.key.key and currentTree.rightchild == None:
                currentTree.rightchild = newTree
                return True


    def searchTreeDelete(self,searchKey):
        """
        preconditie: de BST bevat een item met een key die gelijk is aan searchKey
        postconditie: Het item met als searchKey als key is uit de boom verwijderd
        :param searchKey: de key van het item dat we moeten verwijderen
        :return: True als het item succesvol verwijderd is, anders False
        """
        previousTree = BST()
        replacingTree = BST()
        previousReplacingTree = BST()
        tempContent = TreeItemType
        currentTree = self
        while currentTree.content.key.key != searchKey:
            if searchKey < currentTree.content.key.key:
                if currentTree.leftchild != None:
                    previousTree = currentTree
                    currentTree = currentTree.leftchild
                else:
                    return False
            elif searchKey > currentTree.content.key.key:
                if currentTree.rightchild != None:
                    previousTree = currentTree
                    currentTree = currentTree.rightchild
                else:
                    return False

        if currentTree.leftchild == None and currentTree.rightchild == None:
            if currentTree.content.key.key < previousTree.content.key.key:
                previousTree.leftchild = None
                return True
            elif currentTree.content.key.key > previousTree.content.key.key:
                previousTree.rightchild = None
                return True
        elif (currentTree.leftchild == None and currentTree.rightchild != None) or (currentTree.leftchild != None  and currentTree.rightchild == None):
            if currentTree.content.key.key < previousTree.content.key.key:
                if currentTree.leftchild != None:
                    previousTree.leftchild = currentTree.leftchild
                else:
                    previousTree.leftchild = currentTree.rightchild
                return True
            elif currentTree.content.key.key > previousTree.content.key.key:
                if currentTree.leftchild != None:
                    previousTree.rightchild = currentTree.leftchild
                else:
                    previousTree.rightchild = currentTree.rightchild
                return True
        elif currentTree.leftchild != None and currentTree.rightchild != None:
            replacingTree = currentTree.rightchild
            while replacingTree.leftchild != None:
                previousReplacingTree = replacingTree
                replacingTree = replacingTree.leftchild
            tempContent = currentTree.content
            currentTree.content = replacingTree.content
            replacingTree.content = tempContent
            if previousReplacingTree.content.val == None:
                currentTree.rightchild = None
                return True
            else:
                if replacingTree.rightchild != None:
                    previousReplacingTree.leftchild = replacingTree.rightchild
                else:
                    previousReplacingTree.leftchild = None
                return True
        return False
    def searchTreeRetrieve(self, searchKey):
        """
        preconditie: de BST bevat een item met key gelijk aan searchkey
        postconditie: de BST wordt niet aangepast
        :param searchKey: de key dat we moeten zoeken
        :return: (treeItem: het item met searchKey als key, True als het gevonden is, anders False)
        """
        currentTree = self

        if currentTree == None:
            return tuple([None, False])

        while True:
            if currentTree == None:
                return tuple([None, False])
            elif searchKey < currentTree.content.key.key:
                currentTree = currentTree.leftchild
            elif searchKey > currentTree.content.key.key:
                currentTree = currentTree.rightchild
            elif searchKey == currentTree.content.key.key:
                return tuple([currentTree.content.val, True])


    def preorderTraverse(self, visit):
        """
        preconditie: de BST mag niet leeg zijn
        postconditie: de BST wordt niet aangepast
        :param visit: de functie dat op de nodes moet uitgevoerd worden
        """
        currentTree = self
        visit(currentTree.content.val)
        if currentTree.leftchild != None:
            currentTree.leftchild.preorderTraverse(visit)
        if currentTree.rightchild != None:
            currentTree.rightchild.preorderTraverse(visit)

    def inorderTraverse(self, visit):
        """
        preconditie: de BST mag niet leeg zijn
        postconditie: de BST wordt niet aangepast
        :param visit: de functie dat op de nodes moet uitgevoerd worden
        """
        currentTree = self
        if currentTree.leftchild != None:
            currentTree.leftchild.inorderTraverse(visit)
        visit(currentTree.content.val)
        if currentTree.rightchild != None:
            currentTree.rightchild.inorderTraverse(visit)

    def postorderTraverse(self, visit):
        """
        preconditie: de BST mag niet leeg zijn
        postconditie: de BST wordt niet aangepast
        :param visit: de functie dat op de nodes moet worden uitgevoerd
        """
        currentTree = self
        if currentTree.leftchild != None:
            currentTree.leftchild.postorderTraverse(visit)
        if currentTree.rightchild != None:
            currentTree.rightchild.postorderTraverse(visit)
        visit(currentTree.content.val)

    def save_helper(self, count):
        currentTree = self

        result = ""
        result += "{'root': " + str(currentTree.content.val)
        if currentTree.leftchild != None or currentTree.rightchild != None:
            result += ",'children':["
            if currentTree.leftchild != None:
                count -= 1
                result += currentTree.leftchild.save_helper(count)
                count += 1
                result += "}"
            else:
                result += "None"
            result += ","
            if currentTree.rightchild != None:
                count -= 1
                result += currentTree.rightchild.save_helper(count)
                count += 1
                result += "}"
            else:
                result += "None"
            result += "]"
        if count == 0:
            result += "}"
        return str(result)


    def save(self):
        """
        er wordt gebruikt gemaakt van recursie om alle delen van de boom toe te voegen
        Maar er moest op het einde van de functie, als alle recursies afgelopen zijn, nog een "}" worden toegevoegd
        Dus wordt er gebruik gemaakt van een count die 0 is als het de originele functie is en kleiner is als 0 als dit niet zo is
        Er wordt dus gebruik gemaakt van een save_helper zodat we dezelfde syntax voor save kunnen behouden

        preconditie: de BST is niet leeg
        postconditie: de BST wordt niet aangepast en de inhoud wordt naar het scherm geprint
        """
        return self.save_helper(0)

    def load(self, input):
        """
        preconditie: de input string is een geldige BST
        postconditie: de BST in self wordt overschreven met de BST beschreven in input
        :param input: een BST in de vorm van een string
        """
        tempTree = BST()
        currentdict = dict(input)
        self.content = createTreeItem(currentdict['root'], currentdict['root'])
        if 'children' in currentdict:
            if currentdict['children'][0] != None:
                tempTree.load(currentdict['children'][0])
                self.leftchild = copy.deepcopy(tempTree)
            else:
                self.leftchild = None
            if currentdict['children'][1] != None:
                tempTree.load(currentdict['children'][1])
                self.rightchild = copy.deepcopy(tempTree)
            else:
                self.rightchild = None

class BSTTable:
    def __init__(self):
        self.BST = BST()
        self.id = None

    def tableIsEmpty(self):
        return self.BST.isEmpty()

    def tableInsert(self, key, newItem):
        return self.BST.searchTreeInsert(createTreeItem(key, newItem))

    def tableRetrieve(self, key):
        return self.BST.searchTreeRetrieve(key)

    def tableDelete(self, key):
        return self.BST.searchTreeDelete(key)

    def traverseTable(self, visitfunction):
        return self.BST.inorderTraverse(visitfunction)

    def save(self):
        return self.BST.save()

    def load(self, input):
        return self.BST.load(input)

    def clear(self):
       self.BST = BST()

    def get_id(self):
        return self.id