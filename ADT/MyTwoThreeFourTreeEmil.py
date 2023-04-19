import copy
from copy import deepcopy

class TreeItemType:
    def __init__(self, key, val):
        self.key = key
        self.val = val

def createTreeItem(key,val):
    return TreeItemType(key, val)

class TwoThreeFourTree:
    def __init__(self):
        """
        enkele aannames:
         - zowel de content als de children worden van links naar rechts opgevuld
         - in een knoop met minder dan 4 kinderen wordt de overschot opgevuld met None
         - er kan geen None zijn tussen 2 niet-None waarden    (bv. [2, None, 4] kan niet)
        preconditie:
        postconditie: er is een nieuwe 2-3-4 boom aangemaakt
        """
        self.content = [None, None, None]
        self.LLchild = None
        self.LRchild = None
        self.RLchild = None
        self.RRchild = None

    def isEmpty(self):
        """
        precoditie:
        postconditie: de boom wordt niet aangepast
        :return: True als de boom leeg, is anders False
        """

        if self.content == [None, None, None]:
            return True
        else:
            return False

    def isLeaf(self):
        """
        hulpfunctie om code later overzichtelijker te maken
        preconditie:
        postconditie:
        :return: True als de huidige node een blad is, anders False
        """
        if self.LLchild != None or self.LRchild != None or self.RLchild != None or self.RRchild != None:
            return False
        else:
            return True

    def insertinNode(self, newItem):
        """
        hulpfunctie van insert dat het Item op de juiste plaats in een node toevoegd
        preconditie: De node bevat altijd max 2 items omdat insertItem de nodes al opsplitst
        postconditie: De node bevat minstens 1 en max 3 items en we vullen de nodes van links naar rechts op (bij een node met 2 waardes is rightcontent == None)
        :param newItem: Item dat wordt toegevoegd
        :return: True als het inserten gelukt is anders False
        """

        if self.content[0] == None:
            self.content[0] = newItem
            return True
        elif self.content[1] == None and self.content[0] != None:
            if newItem.key > self.content[0].key:
                self.content[1] = newItem
                return True
            elif newItem.key < self.content[0].key:
                self.content[1] = self.content[0]
                self.content[0] = newItem
                return True
            else:
                return False
        elif self.content[2] == None and self.content[1] != None and self.content[0] != None:
            if newItem.key < self.content[0].key:
                self.content[2] = self.content[1]
                self.content[1] = self.content[0]
                self.content[0] = newItem
            elif newItem.key > self.content[0].key and newItem.key < self.content[1].key:
                self.content[2] = self.content[1]
                self.content[1] = newItem
                return True
            elif newItem.key > self.content[1].key:
                self.content[2] = newItem
                return True
        else:
            return False        # de node bevat al 3 elementen

    def isFull(self):
        """
        hulpfunctie: test of een node vol is en opgesplitst moet worden
        preconditie:
        postconditie:
        :return: True als de Node vol is, anders False
        """
        if self.content[0] != None and self.content[1] != None and self.content[2] != None:
            return True
        else:
            return False

    def split(self, parent):
        """
        hulpfunctie om tijdens het doorlopen met insert een node op te splitsen
        """

        newLefttree = TwoThreeFourTree()
        newLefttree.content[0] = self.content[0]
        newLefttree.LLchild = self.LLchild
        newLefttree.LRchild = self.LRchild

        newRighttree = TwoThreeFourTree()
        newRighttree.content[0] = self.content[2]
        newRighttree.LLchild = self.RLchild
        newRighttree.LRchild = self.RRchild


        if parent == None:

            self.LLchild = newLefttree
            self.LRchild = newRighttree
            self.RLchild = None
            self.RRchild = None
            self.content[0] = self.content[1]
            self.content[1] = None
            self.content[2] = None
        else:
            parent.insertinNode(self.content[1])
            if parent.content[1] != None and parent.content[2] == None:
                if newLefttree.content[0].key < parent.content[0].key:
                    parent.RRchild = parent.RLchild
                    parent.RLchild = parent.LRchild
                    parent.LLchild = newLefttree
                    parent.LRchild = newRighttree
                elif newLefttree.content[0].key > parent.content[0].key and newLefttree.content[0].key < parent.content[1].key:
                    parent.RRchild = parent.RLchild
                    parent.LRchild = newLefttree
                    parent.RLchild = newRighttree
            elif parent.content[2] != None:
                if newLefttree.content[0].key < parent.content[0].key:
                    parent.LLchild = newLefttree
                    parent.LRchild = newRighttree
                elif newLefttree.content[0].key > parent.content[0].key and newLefttree.content[0].key < parent.content[1].key:
                    parent.LRchild = newLefttree
                    parent.RRchild = parent.RLchild
                    parent.RLchild = newRighttree
                elif newLefttree.content[0].key > parent.content[1].key:
                    parent.RLchild = newLefttree
                    parent.RRchild = newRighttree



    def insertItem(self, newItem):
        """
        preconditie: newItem is al van de vorm TreeItemType, en de boom bevat nog geen item met dezelfde key als newItem
        postconditie: newItem is aan de boom toegevoegd en alle volle noden op het pad van root naar het juiste blad zijn gesplitst
        :param newItem: het Item dat aan de boom moet worden toegevoegd
        :return: True als het gelukt is, anders False
        """

        currentTree = self
        previousTree = None
        if self.isFull():
            self.split(previousTree)

        if newItem.key == 15:
            debug = True

        while not currentTree.isLeaf():
            if currentTree.isFull():
                currentTree.split(previousTree)
            if currentTree.content[0] != None and currentTree.content[1] == None:
                if newItem.key < currentTree.content[0].key:
                    previousTree = currentTree
                    currentTree = currentTree.LLchild
                elif newItem.key > currentTree.content[0].key:
                    previousTree = currentTree
                    currentTree = currentTree.LRchild
            elif currentTree.content[1] != None and currentTree.content[2] == None:
                if newItem.key < currentTree.content[0].key:
                    previousTree = currentTree
                    currentTree = currentTree.LLchild
                elif newItem.key > currentTree.content[0].key and newItem.key < currentTree.content[1].key:
                    previousTree = currentTree
                    currentTree = currentTree.LRchild
                elif newItem.key > currentTree.content[1].key:
                    previousTree = currentTree
                    currentTree = currentTree.RLchild
            elif currentTree.content[2] != None:
                if newItem.key < currentTree.content[0].key:
                    previousTree = currentTree
                    currentTree = currentTree.LLchild
                elif newItem.key > currentTree.content[0].key and newItem.key < currentTree.content[1].key:
                    previousTree = currentTree
                    currentTree = currentTree.LRchild
                elif newItem.key > currentTree.content[1].key and newItem.key < currentTree.content[2].key:
                    previousTree = currentTree
                    currentTree = currentTree.RLchild
                elif newItem.key > currentTree.content[2].key:
                    previousTree = currentTree
                    currentTree = currentTree.RRchild


        if currentTree.isFull():
            currentTree.split(previousTree)
            previousTree.insertItem(newItem)
        else:
            currentTree.insertinNode(newItem)

        return True

    def retrieveItem(self, searchkey):
        """
        preconditie: De key is als type int
        postconditie: De boom wordt niet aangepast
        :param searchkey: De key van het item dat we zoeken
        :return: (Value van het item met key=searchkey, True als het gevonden is, anders False)
        """
        currentTree = self


        while True:
            if currentTree == None:
                return (None, False)
            if currentTree.content[0] != None and currentTree.content[1] == None:       #De huidige node bevat 1 item
                if searchkey < currentTree.content[0].key:
                    currentTree = currentTree.LLchild
                elif searchkey > currentTree.content[0].key:
                    currentTree = currentTree.LRchild
                else:
                    break

            elif currentTree.content[0] != None and currentTree.content[1] != None and currentTree.content[2] == None:      #de huidige node bevat 2 items
                if searchkey < currentTree.content[0].key:
                    currentTree = currentTree.LLchild
                elif searchkey > currentTree.content[0].key and searchkey < currentTree.content[1].key:
                    currentTree = currentTree.LRchild
                elif searchkey > currentTree.content[1].key:
                    currentTree = currentTree.RLchild

                else:
                    break

            else:                                                 #de huidige node bevat 3 items
                if searchkey < currentTree.content[0].key:
                    currentTree = currentTree.LLchild
                elif searchkey > currentTree.content[0].key and searchkey < currentTree.content[1].key:
                    currentTree = currentTree.LRchild
                elif searchkey > currentTree.content[1].key and searchkey < currentTree.content[2].key:
                    currentTree = currentTree.RLchild
                elif searchkey > currentTree.content[2].key:
                    currentTree = currentTree.RRchild
                else:
                    break

        #Het te zoeken Item zit nu in de huidige boom
        if currentTree.content[0].key == searchkey:
            return (currentTree.content[0].val, True)
        elif currentTree.content[1].key == searchkey:
            return (currentTree.content[1].val, True)
        elif currentTree.content[2].key == searchkey:
            return (currentTree.content[2].val, True)
        else:
            return (None, False)

    def merge(self, parent):
        """
        helperfunctie die een 2-knoop omvormt naar een 3-knoop of een 4-knoop
        preconditie: er wordt nooit herstructureerd in de root van de boom, en parent is ook echt de parent van de te herstructureren node
        postconditie: de node self is omgevormd, afhankelijk van de omstandigheden zijn sommige delen van de hele boom aangepast
        :param parent: De parentboom van de node dat moet gemerged worden
        """
        #vindt eerst de sibling(s)
        if parent.LLchild == self:
            leftSibling = None
            rightSibling = parent.LRchild
            leftparentposition = None           #parentposition is the position of the item between the 2 siblings
            rightparentposition = 0
        elif parent.LRchild == self:
            leftSibling = parent.LLchild
            rightSibling = parent.RLchild
            leftparentposition = 0
            rightparentposition = 1
        elif parent.RLchild == self:
            leftSibling = parent.LRchild
            rightSibling = parent.RRchild
            leftparentposition = 1
            rightparentposition = 2
        elif parent.RRchild == self:
            leftSibling = parent.RLchild
            rightSibling = None
            leftparentposition = 2
            rightparentposition = None


        if leftSibling != None and leftSibling.content[2] != None:              #heeft de sibling 3 elementen?
            temp1 = leftSibling.content[2]
            temp2 = parent.content[rightparentposition]
            treemove = leftSibling.RRchild

            leftSibling.content[2] = None
            leftSibling.RRchild = None           #de sibling heeft nu het nodige afgegeven en is in orde

            parent.content[rightparentposition] = temp1

            self.content[1] = self.content[0]
            self.content[0] = temp2
            self.RLchild = self.LRchild
            self.LRchild = self.LLchild
            self.LLchild = treemove
        elif leftSibling != None and leftSibling.content[1] != None and leftSibling.content[2] == None:         #heeft de sibling 2 elementen?
            temp1 = leftSibling.content[1]
            temp2 = parent.content[leftparentposition]
            treemove = leftSibling.RLchild

            leftSibling.content[1] = None
            leftSibling.RLchild = None

            parent.content[leftparentposition] = temp1

            self.content[1] = self.content[0]
            self.content[0] = temp2
            self.RLchild = self.LRchild
            self.LRchild = self.LLchild
            self.LLchild = treemove
        elif (leftSibling == None or leftSibling.content[1] == None) and rightSibling != None and rightSibling.content[1] != None:        #de sibling moet minstens 2 elementen hebben om er 1 te kunnen afgeven
            temp1 = rightSibling.content[0]
            temp2 = parent.content[rightparentposition]
            treemove = rightSibling.LLchild

            rightSibling.content[0] = None
            rightSibling.LLchild = None
            rightSibling.rearrangeNode()
            parent.content[rightparentposition] = temp1

            self.content[1] = temp2
            self.RLchild = treemove

        else:               #we kunnen geen redistribute doen dus zullen we moeten mergen
            if leftSibling != None and rightSibling == None and leftSibling.content[1] == None and parent.content[1] == None:                #zowel de sibling als de parent zij een 2-knoop -> beide siblings komen samen in de parent
                parent.content[1] = parent.content[0]
                parent.content[0] = leftSibling.content[0]
                parent.content[2] = self.content[0]
                temptree = leftSibling
                parent.LLchild = temptree.LLchild
                parent.LRchild = temptree.LRchild
                parent.RLchild = self.LLchild
                parent.RRchild = self.LRchild
            elif rightSibling != None and leftSibling == None and rightSibling.content[1] == None and parent.content[1] == None:
                parent.content[1] = parent.content[0]
                parent.content[0] = self.content[0]
                parent.content[2] = rightSibling.content[0]
                temptree = rightSibling
                parent.LLchild = self.LLchild
                parent.LRchild = self.LRchild
                parent.RLchild = temptree.LLchild
                parent.RRchild = temptree.LRchild
            elif leftSibling != None and leftSibling.content[1] == None and parent.content[1] != None:
                temp1 = parent.content[leftparentposition]
                temp2 = leftSibling.content[0]
                temptree1 = leftSibling.LLchild
                temptree2 = leftSibling.LRchild
                self.content[2] = self.content[0]
                self.content[1] = temp1
                self.content[0] = temp2
                self.RRchild = self.LRchild
                self.RLchild = self.LRchild
                self.LRchild = temptree2
                self.LLchild = temptree1
                parent.content[leftparentposition] = None

                if parent.LLchild == leftSibling:
                    parent.LLchild = None
                elif parent.LRchild == leftSibling:
                    parent.LRchild = None
                elif parent.RLchild == leftSibling:
                    parent.RLchild = None
                elif parent.RRchild == leftSibling:
                    parent.RRchild = None

                parent.rearrangeNode()
            elif rightSibling != None and leftSibling == None and rightSibling.content[1] == None and parent.content[1] != None:
                temp1 = parent.content[rightparentposition]
                temp2 = rightSibling.content[0]
                temptree1 = rightSibling.LLchild
                temptree2 = rightSibling.LRchild
                self.content[1] = temp1
                self.content[2] = temp2
                self.RLchild = temptree1
                self.RRchild = temptree2
                parent.content[rightparentposition] = None

                if parent.LLchild == rightSibling:
                    parent.LLchild = None
                elif parent.LRchild == rightSibling:
                    parent.LRchild = None
                elif parent.RLchild == rightSibling:
                    parent.RLchild = None
                elif parent.RRchild == rightSibling:
                    parent.RRchild = None

                parent.rearrangeNode()




    def rearrangeNode(self):
        """
        helperfunctie die alle content en pointers in een node terug in de juiste volgorde zet
        preconditie: alle nodes onder de huidige node zijn geldige 2-3-4 bomen
        postconditie: enkel de huidige node is gewijzigd en er zijn geen waarden verdwenen of toegevoegd
        """
        tempcontent = []
        for x in self.content:
            if x != None:
                tempcontent.append(x.key)

        tempcontent = sorted(tempcontent)
        while len(tempcontent) != 3:
            tempcontent.append(None)

        content = [None, None, None]

        for i in range(2):
            for x in self.content:
                if x != None:
                    if x.key == tempcontent[i]:
                        content[i] = x

        self.content = content

        tempLLchild = self.LLchild
        tempLRchild = self.LRchild
        tempRLchild = self.RLchild
        tempRRchild = self.RRchild
        self.LLchild = None
        self.LRchild = None
        self.RLchild = None
        self.RRchild = None
        for child in [tempLLchild, tempLRchild, tempRLchild, tempRRchild]:
            if child != None:
                if child.content[0].key < self.content[0].key:
                    self.LLchild = child
                elif child.content[0].key > self.content[0].key and child.content[0].key < self.content[1].key:
                    self.LRchild = child
                elif child.content[0].key > self.content[1].key and child.content[0].key < self.content[2].key:
                    self.RLchild = child
                elif child.content[0].key > self.content[2].key:
                    self.RRchild = child


    def deleteItem(self, searchkey):
        """
        preconditie: de searchkey is van het type int
        postconditie: Het gezochte item is uit de boom verwijderd en alle 2-knopen op het pad naar de gezochte knoop zijn omgevormd naar 3-knopen of 4-knopen
        :param searchkey: de key van het item dat verwijderd moet worden
        :return: True als het verwijderen is gelukt, anders False
        """
        currentTree = self
        previousTree = None

        if self.retrieveItem(searchkey)[1] == False:
            return False

        if currentTree.isEmpty():
            return False
        else:
            while True:
                if currentTree == None:
                    return False

                if currentTree.content[0] != None and currentTree.content[1] == None:  # De huidige node bevat 1 item, dus herstructureer voor we verdergaan
                    if previousTree != None:                #in de root moeten we niet herstructureren
                        currentTree.merge(previousTree)
                        currentTree = previousTree
                    else:
                        if searchkey < currentTree.content[0].key:
                            previousTree = currentTree
                            currentTree = currentTree.LLchild
                        elif searchkey > currentTree.content[0].key:
                            previousTree = currentTree
                            currentTree = currentTree.LRchild
                        else:
                            break

                elif currentTree.isLeaf():
                    break


                elif currentTree.content[0] != None and currentTree.content[1] != None and currentTree.content[2] == None:  # de huidige node bevat 2 items
                    if searchkey < currentTree.content[0].key:
                        previousTree = currentTree
                        currentTree = currentTree.LLchild
                    elif searchkey > currentTree.content[0].key and searchkey < currentTree.content[1].key:
                        previousTree = currentTree
                        currentTree = currentTree.LRchild
                    elif searchkey > currentTree.content[1].key:
                        previousTree = currentTree
                        currentTree = currentTree.RRchild
                    else:
                        break

                else:  # de huidige node bevat 3 items
                    if searchkey < currentTree.content[0].key:
                        previousTree = currentTree
                        currentTree = currentTree.LLchild
                    elif searchkey > currentTree.content[0].key and searchkey < currentTree.content[1].key:
                        previousTree = currentTree
                        currentTree = currentTree.LRchild
                    elif searchkey > currentTree.content[1].key and searchkey < currentTree.content[2].key:
                        previousTree = currentTree
                        currentTree = currentTree.RLchild
                    elif searchkey > currentTree.content[2].key:
                        previousTree = currentTree
                        currentTree = currentTree.RRchild
                    else:
                        break

            # het te zoeken item zit nu in currentTree

            if currentTree.isLeaf():        #we moeten niet verder zoeken naar een successor, we kunnen het gewoon verwijderen
                if currentTree.content[0].key == searchkey:
                    currentTree.content[0] = None
                elif currentTree.content[1].key == searchkey:
                    currentTree.content[1] = None
                elif currentTree.content[2].key == searchkey:
                    currentTree.content[2] = None
                currentTree.rearrangeNode()
                return True


            originalTree = currentTree

            if currentTree.content[0].key == searchkey:
                originalValue = currentTree.content[0]
                previousTree = currentTree
                currentTree = currentTree.LRchild
            elif currentTree.content[1].key == searchkey:
                originalValue = currentTree.content[1]
                previousTree = currentTree
                currentTree = currentTree.RLchild
            elif currentTree.content[2].key == searchkey:
                originalValue = currentTree.content[2]
                previousTree = currentTree
                currentTree = currentTree.RRchild

            if currentTree.content[1] == None:
                currentTree.merge(previousTree)

            #zoek de inorder successor
            while not currentTree.isLeaf():
                if currentTree.content[1] == None:
                    currentTree.merge(previousTree)
                previousTree = currentTree
                currentTree = currentTree.LLchild

            temp = currentTree.content[0]
            currentTree.content[0] = None
            currentTree.rearrangeNode()

            if temp.key == searchkey:
                return True
            if originalTree.content[0].key == searchkey:
                originalTree.content[0] = temp
            elif originalTree.content[1].key == searchkey:
                originalTree.content[1] = temp
            elif originalTree.content[2].key == searchkey:
                originalTree.content[2] = temp
            return True

    def inorderTraverse(self, visit):
        """
        preconditie: de 2-3-4 boom is niet leeg
        postconditie: de functie inorderTraverse zelf past de boom niet aan, het kan wel dat de boom verandert door de gegeven functie visit
        :param visit: de functie dat op elk element moet toegepast worden
        """
        if self.LLchild != None:
            self.LLchild.inorderTraverse(visit)
        if self.content[0] != None:
            visit(self.content[0].val)

        if self.LRchild != None:
            self.LRchild.inorderTraverse(visit)

        if self.content[1] != None:
            visit(self.content[1].val)

            if self.RLchild != None:
                self.RLchild.inorderTraverse(visit)

        if self.content[2] != None:
            visit(self.content[2].val)

            if self.RRchild != None:
                self.RRchild.inorderTraverse(visit)

    def save(self):
        """
        preconditie: de boom is niet leeg
        postconditie: de boom wordt niet aangepast
        :return: de boom in string vorm
        """
        result = dict()
        if not self.isEmpty():
            temp = []
            for x in self.content:
                if x != None:
                    temp.append(x.val)
            result['root'] = temp

            if self.LLchild != None:
                result['children'] = []
                temp = dict(self.LLchild.save())
                result['children'].append(temp)
            if self.LRchild != None:
                temp = dict(self.LRchild.save())
                result['children'].append(temp)
            if self.RLchild != None:
                temp = dict(self.RLchild.save())
                result['children'].append(temp)
            if self.RRchild != None:
                temp = dict(self.RRchild.save())
                result['children'].append(temp)

        return result

    def load(self, input):
        """
        preconditie: de gegeven input is een geldige string
        postconditie: de boom in self wordt vervangen door de gegeven input
        :param input: de gegeven boom in string vorm
        """

        currentdict = dict(input)
        temptree = TwoThreeFourTree()


        for i in range(len(currentdict['root'])):
            self.content[i] = (createTreeItem(currentdict['root'][i], (currentdict['root'][i])))

        if 'children' in currentdict:
            if len(currentdict['children']) >= 2:
                temptree.load(currentdict['children'][0])
                self.LLchild = copy.deepcopy(temptree)
                temptree = TwoThreeFourTree()
                temptree.load(currentdict['children'][1])
                self.LRchild = copy.deepcopy(temptree)
                if len(currentdict['children']) >= 3:
                    temptree = TwoThreeFourTree()
                    temptree.load(currentdict['children'][2])
                    self.RLchild = copy.deepcopy(temptree)
                    if (len(currentdict['children'])) == 4:
                        temptree = TwoThreeFourTree()
                        temptree.load(currentdict['children'][3])
                        self.RRchild = copy.deepcopy(temptree)


class TwoThreeFourTreeTable:
    def __init__(self):
        self.tree = TwoThreeFourTree()
        self.id = None

    def tableInsert(self, key, newItem):
        return self.tree.insertItem(createTreeItem(key, newItem))

    def tableRetrieve(self, key):
        return self.tree.retrieveItem(key)

    def tableIsEmpty(self):
        return self.tree.isEmpty()

    def tableDelete(self, key):
        return self.tree.deleteItem(key)

    def traverseTable(self, visitfunction):
        self.tree.inorderTraverse(visitfunction)

    def save(self):
        return self.tree.save()

    def load(self, input):
        return self.tree.load(input)

    def clear(self):
        self.tree = TwoThreeFourTree()

    def get_id(self):
        return self.id

class O:
    def __init__(self):
        pass
t = TwoThreeFourTreeTable()
for i in [1, 2, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 21]:
    t.tableInsert(i, O())
