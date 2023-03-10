import copy

## functionaliteit
def createTreeItem(key,val):
    """
    Creëert een RedBlackTree met lege deelbomen die bezit over de doorgekrege key en value

    :param key: Een integer die vastgebonden is aan een value.
    :param val: De value van de BinarySearchTree

    preconditions: De key is een integer

    postconditions: Er is een RedBlackTree gecreëerd met lege deelbomen die bezit over de doorgekrege key en value
    Er is nog geen kleur toegewezen

    :return: BinarySearchTree met lege deelbomen die bezit over de doorgekrege key en value
    """
    Tree=RedBlackTree(key,val)
    return Tree

class RedBlackTree:
    # constructer
    def __init__(self, *args):
        """
        Creëert een RedBlackTree met lege deelbomen die bezit over een doorgekrege key en value als er key en value waarden zijn doorgegeven

        :param args: Een lijst die leeg is of de elementen key en value bevatten

        preconditions: Als er een key wordt doorgegeven dan is dit een integer en staat het op index 1
        value staat op index 0

        postconditions: Er is een RedBlackTree gecreëerd met lege deelbomen die bezit over de doorgekrege key en value
        als die waarden zijn doorgegeven, er is nog geen kleur toegewezen

        :return: RedBlackTree met lege deelbomen die bezit over de doorgekrege key en value als die waarden zijn doorgegeven
        """
        if len(args) ==0:
            self.leftTree = None
            self.rightTree = None
            self.value = None
            self.key = None
            self.color = None
        else:
            self.leftTree = None
            self.rightTree = None
            self.color = None
            self.value = args[0]
            self.key = args[1]

    ## functionaliteit
    def isEmpty(self):
        """
        Controleert de opgegeven RedBlackTree of die leeg is of niet en geeft naarmate hiervan een booleaanse waarde terug.
        True als de stack RedBlackTree leeg is, False als dit niet het geval is.

        preconditions: Er word een RedBlackTree doorgegeven

        postconditions: De functie geeft een booleaanse waarde weer.
        Er vinden geen gegevens wijzigingen plaats.

        :return: De functie geeft naarmate de RedBlackTree vol of leeg is een booleaanse waarde terug.
        """
        if self.value == None or self.key == None:
            return True
        return False

    ## functionaliteit
    def rotateRight(self):
        """
        HULPFUNCTIE: dient niet gehanteerd te worden door de user
            Roteert de Tree naar rechts en kleurt de boom in
        """
        newRoot = copy.deepcopy(self.leftTree)
        oldRoot = copy.deepcopy(self)
        oldRoot.leftTree = None
        newRoot.color = "black"
        oldRoot.color = "red"
        self = newRoot
        self.rightTree = oldRoot
        return self

    ## functionaliteit
    def rotateLeft(self):
        """
        HULPFUNCTIE: dient niet gehanteerd te worden door de user
            Roteert de boom naar links en kleurt de boom in
        """
        newRoot = copy.deepcopy(self.rightTree)
        oldRoot = copy.deepcopy(self)
        oldRoot.rightTree = None
        newRoot.color = "black"
        oldRoot.color = "red"
        self = newRoot
        self.leftTree = oldRoot
        return self

    ## functionaliteit
    def rotateRightFull(self):
        """
        HULPFUNCTIE: dient niet gehanteerd te worden door de user
            Roteert de boom naar rechts
        """
        newRoot = copy.deepcopy(self.leftTree)
        oldRoot = copy.deepcopy(self)
        oldRoot.leftTree = newRoot.rightTree
        newRoot.rightTree = oldRoot
        self = newRoot
        return self

    ## functionaliteit
    def rotateLeftFull(self):
        """
        HULPFUNCTIE: dient niet gehanteerd te worden door de user
            roteert de boom naar links
        """
        newRoot = copy.deepcopy(self.rightTree)
        oldRoot = copy.deepcopy(self)
        oldRoot.rightTree = newRoot.leftTree
        newRoot.leftTree = oldRoot
        self=newRoot
        return self

    ## functionaliteit
    def turnRedBlack(self):
        """
        HULPFUNCTIE: dient niet gehanteerd te worden door de user
            Wisselt alle bomen hun kleur, rood -> zwart en zwart -> rood
        """
        if self.color == "black":
            self.color = "red"
        else:
            self.color = "black"

        if self.leftTree != None:
            self.leftTree.turnRedBlack()
        if self.rightTree != None:
            self.rightTree.turnRedBlack()

    ## functionaliteit
    def turnRedBlack2(self):
        """
        HULPFUNCTIE: dient niet gehanteerd te worden door de user
            Kleurt de root van een boom rood als de deelbomen ervan rood zijn en minstensen een van de deelbomen van
            de deelbomen rood zijn. De deelbomen worden zwart, de root wordt rood, de rest blijft hetzelfde
        """
        lastColor = self.color
        if lastColor == "red":
            if self.leftTree != None:
                if self.leftTree.color == lastColor:
                    return True

            if self.rightTree != None:
                if self.rightTree.color == lastColor:
                    return True

        if self.leftTree != None:
            if self.leftTree.turnRedBlack2():
                if self.leftTree!=None and self.rightTree!=None:
                    self.color="red"
                    self.leftTree.color="black"
                    self.rightTree.color="black"

        if self.rightTree != None:
            if self.rightTree.turnRedBlack2():
                if self.leftTree!=None and self.rightTree!=None:
                    self.color="red"
                    self.leftTree.color="black"
                    self.rightTree.color="black"

        return False

    ## functionaliteit
    def colorAfterRotation(self):
        """
        HULPFUNCTIE: dient niet gehanteerd te worden door de user
            Kleurt een boom in na een rotatie
        """
        if self.color == "red":
            self.color = "black"
            if self.leftTree.color == "black":
                self.leftTree.color = "red"
            else:
                self.rightTree.color = "red"
        return

    ## functionaliteit
    def treeRotate2(self):
        """
        HULPFUNCTIE: dient niet gehanteerd te worden door de user
            Roteert de boom om Dubbel rood(een overvolle Node) weg te krijgen als mogelijk
        """
        if self.leftTree != None:
            if self.leftTree.leftTree != None:
                if self.leftTree.color == "red" and self.leftTree.leftTree.color == "red":
                    self = self.rotateRightFull()
                    return self

            if self.leftTree.rightTree != None:
                if self.leftTree.color == "red" and self.leftTree.rightTree.color == "red":
                    self.leftTree = self.leftTree.rotateLeftFull()
                    return self

        if self.rightTree != None:
            if self.rightTree.leftTree != None:
                if self.rightTree.color == "red" and self.rightTree.leftTree.color == "red":
                    self.rightTree = self.rightTree.rotateRightFull()
                    return self

            if self.rightTree.rightTree != None:
                if self.rightTree.color == "red" and self.rightTree.rightTree.color == "red":
                    self = self.rotateLeftFull()
                    return self

        if self.leftTree != None:
            self.leftTree=self.leftTree.treeRotate2()

        if self.rightTree != None:
            self.rightTree=self.rightTree.treeRotate2()
        return self

    ## functionaliteit
    def insertItem(self,tree):
        """
        Plaats een tree in de RedBlackTree volgens de BinarySearchTree algoritme
        en balanceerd vervolgens de tree om zo een minimale hoogte als mogelijk
        te bereiken

        :param Tree: RedBlackTree met None Deelbomen

        preconditions: De doorgegeven tree zijn deelbomen zijn None

        postconditions: De RedBlackTree bezit nu over de toegevoegde tree en is geblanceerd
        Er vinden gegevens wijzigingen plaats.

        :return: RedBlackTree met nieuwe deelboom
        """
        result = self.insertionItem(tree)
        UpdatedTree = self.treeCorrecter(tree)
        self.__dict__.update(UpdatedTree.__dict__)
        return result

    ## functionaliteit
    def treeRotate(self):
        """
        HULPFUNCTIE: dient niet gehanteerd te worden door de user
            Roteert de boom om Dubbel rood(een overvolle Node) weg te krijgen als mogelijk
            Roteert in minder situaties dan treeRotate2.
        """
        if self.leftTree != None and self.leftTree.leftTree != None and self.rightTree == None:
            if self.color == "black" and self.leftTree.color == "red" and self.leftTree.leftTree.color == "red":
                self=self.rotateRight()

        if self.rightTree != None and self.rightTree.rightTree != None and self.leftTree == None:
            if self.color == "black" and self.rightTree.color == "red" and self.rightTree.rightTree.color == "red":
                self=self.rotateLeft()

        if self.leftTree != None:
            self.leftTree=self.leftTree.treeRotate()

        if self.rightTree != None:
            self.rightTree=self.rightTree.treeRotate()
        return self

    ## functionaliteit
    def treeSwitch(self, color):
        """
        HULPFUNCTIE: dient niet gehanteerd te worden door de user
            Geeft true als de boom over Dubbel red(een overvolle node) bezit.
        """
        needColorSwitch = False
        lastColor = self.color
        if lastColor==color:
            if self.leftTree != None:
                if self.leftTree.color == lastColor:
                    needColorSwitch = True
                    return needColorSwitch

            if self.rightTree != None:
                if self.rightTree.color == lastColor:
                    needColorSwitch = True
                    return needColorSwitch

        if self.leftTree != None:
            needColorSwitch=self.leftTree.treeSwitch(color)

        if needColorSwitch:
            return needColorSwitch

        if self.rightTree != None:
            needColorSwitch=self.rightTree.treeSwitch(color)
        return needColorSwitch

    ## functionaliteit
    def compareTree(self,tree):
        """
        HULPFUNCTIE: dient niet gehanteerd te worden door de user
            Vergelijkt twee bomen en geeft true als ze gelijk aan elkaar zijn
        """
        equal=False
        if self.key==tree.key and self.value==tree.value:
            equal=True

        if self.leftTree != None and tree.leftTree != None:
            equal=self.leftTree.compareTree(tree.leftTree)
        if not equal:
            return equal
        if self.rightTree != None and tree.rightTree != None:
            equal=self.rightTree.compareTree(tree.rightTree)
        return equal

    ## functionaliteit
    def treeColor(self):
        """
        HULPFUNCTIE: dient niet gehanteerd te worden door de user
            Bekijkt of turnRedBlack2() uitgevoerd kan worden en geeft true als dit mogelijk is.
        """
        color=False
        if self.leftTree!=None and self.rightTree!=None:
            if self.rightTree.rightTree!=None:
                if self.leftTree.color=="red" and self.rightTree.color=="red" and self.rightTree.rightTree.color=="red":
                    color=True
                    return color

            if self.rightTree.leftTree!=None:
                if self.leftTree.color=="red" and self.rightTree.color=="red" and self.rightTree.leftTree.color=="red":
                    color=True
                    return color

            if self.leftTree.rightTree!=None:
                if self.leftTree.color=="red" and self.rightTree.color=="red" and self.leftTree.rightTree.color=="red":
                    color=True
                    return color

            if self.leftTree.leftTree!=None:
                if self.leftTree.color=="red" and self.rightTree.color=="red" and self.leftTree.leftTree.color=="red":
                    color=True
                    return color

        if self.leftTree != None:
            color=self.leftTree.treeColor()

        if self.rightTree != None:
            color=self.rightTree.treeColor()
        return color

    ## functionaliteit
    def splitRoot(self):
        """
        HULPFUNCTIE: dient niet gehanteerd te worden door de user
            verandert de kleur van de twee deelbomen om de boom te splitsen
        """
        if self.rightTree != None and self.leftTree != None:
            if self.leftTree.color == "red" and self.rightTree.color == "red":
                self.leftTree.color="black"
                self.rightTree.color="black"
                return True
        return False

    ## functionaliteit
    def treeCorrecter(self, tree):
        """
        HULPFUNCTIE: dient niet gehanteerd te worden door de user
            Maakt de boom terug geldig nadat er een insert gebeurd is
        """
        self=self.treeRotate()
        self.splitRoot()
        if self.treeSwitch("red"):
            self.turnRedBlack2()
            while self.treeColor():
                self.turnRedBlack2()
            self.color = "black"
            tree.color = "red"
            while self.treeSwitch("red"):
                BeforeRotation=copy.deepcopy(self)
                self=self.treeRotate2()
                self=self.treeRotate()
                if self.compareTree(BeforeRotation):
                    self.colorAfterRotation()
        return self

    ## functionaliteit
    def insertionItem(self, tree):
        """
        HULPFUNCTIE: dient niet gehanteerd te worden door de user
            Hulp functie voor insertItem()
            voegt de item toe aan de boom zoals een BinarySearchTree
        """
        if self.isEmpty():
            if tree.color == None:
                tree.color = "black"
            self.leftTree = tree.leftTree
            self.rightTree = tree.rightTree
            self.value = tree.value
            self.key = tree.key
            self.color = tree.color
            return True

        if tree.color==None:
            tree.color="red"

        if tree.key<self.key:
            if self.leftTree != None:
                self.leftTree.insertionItem(tree)
            else:
                self.leftTree=tree
                return True

        elif tree.key>self.key:
            if self.rightTree != None:
                self.rightTree.insertionItem(tree)
            else:
                self.rightTree = tree
                return True

        elif tree.key == self.key:
            self.leftTree = tree.leftTree
            self.rightTree = tree.rightTree
            self.value = tree.value
            self.key = tree.key
            self.color = tree.color
        return True

    ## functionaliteit
    def save(self):
        """
        Weergeeft de doorgekregen RedBlackTree in string form

        preconditions: Er word een RedBlackTree doorgegeven

        postconditions: De functie returned een string voorstelling van de RedBlackTree
        Er vinden geen gegevens wijzigingen plaats.

        :return: String form van de RedBlackTree
        """
        c = "{"
        c += "\'root\': " + str(self.key) + ",'color': '" + self.color + "'"
        if self.leftTree == None and self.rightTree == None:
            c += "}"
            return c
        c += ",\'children\':["

        if self.leftTree != None:
            c += self.leftTree.save()
        else:
            c += "None"

        if self.rightTree != None:
            c += ","
            c += self.rightTree.save()
        else:
            c += ",None"

        c += "]"
        c += "}"
        return c

    ## functionaliteit
    def retrieveItem(self,key):
        """
        Weergeeft de value van de RedBlackTree die bezit over de doorgegeven key

        :param key: Een integer die gelinkt staat met een bepaalde value in de RedBlackTree

        preconditions: De doorgegeven RedBlackTree bezit over een key die gelijk aan de doorgegeven key

        postconditions: De value die verbonden staat met de doorgekregen key wordt doorgegeven
        Er vinden geen gegevens wijzigingen plaats.

        :return: pair met de gezochte value en true als de key zich bevindt in de BinarySearchTree, anders (0,False)
        """
        if key==self.key:
            return (self.value,True)

        elif key>self.key:
            if self.rightTree==None:
                return (0,False)
            else:
                return self.rightTree.retrieveItem(key)

        elif key<self.key:
            if self.leftTree==None:
                return (0,False)
            else:
                return self.leftTree.retrieveItem(key)

    ## functionaliteit
    def inorderTraverse(self, arg):
        """
        Voert een bepaalde functie (arg) uit op values in de RedBlackTree in inorderTraverse volgorde

        :param arg: Functie die wordt uitgevoerd op de values van de RedBlackTree in inorderTraverse volgorde

        preconditions: arg is een valide functie die verschillende data types als input kan hebben

        postconditions: De functie arg wordt in inorderTraverse volgorde op de values uitgevoerd
        Er kunnen gegevens wijzigingen plaats vinden naarmate wat de arg functie.

        :return: Returned het resultaat van de arg functie, kan niets zijn
        """
        if self.leftTree != None:
            self.leftTree.inorderTraverse(arg)
        arg(self.value)
        if self.rightTree != None:
            self.rightTree.inorderTraverse(arg)

    ## functionaliteit
    def load(self, args):
        """
        Creëert een RedBlackTree met de doorgekregen parameters

        :param args: parameters volgens output formaat van save functie, niet in string form

        preconditions: args heeft het formaat van de output formaat van save functie

        postconditions: De doorgekregen RedBlackTree is vervangen worden met de gecreëerde RedBlackTree
        Er vinden gegevens wijzigingen plaats.

        """
        tempRedBlackTree = RedBlackTree()
        for w, i in args.items():
            if w=="root":
                temp2RedBlackTree = RedBlackTree(i,i)
            if w=="color":
                temp2RedBlackTree.color = i
                tempRedBlackTree.insertItem(temp2RedBlackTree)
            if w=="children":
                if i[0]!=None:
                    temp3RedBlackTree= RedBlackTree()
                    temp3RedBlackTree.load(i[0])
                    tempRedBlackTree.insertItem(temp3RedBlackTree)
                if i[1]!=None:
                    temp3RedBlackTree = RedBlackTree()
                    temp3RedBlackTree.load(i[1])
                    tempRedBlackTree.insertItem(temp3RedBlackTree)
        self.__dict__.update(tempRedBlackTree.__dict__)

    ## functionaliteit
    def retrieveTree(self,key):
        """
        HULPFUNCTIE: dient niet gehanteerd te worden door de user
            Zie retrieveItem(), Deze functie werkt hetzelfde en returned in plaats
            van de value, een tree
        """
        if key==self.key:
            return (self,True)

        elif key>self.key:
            if self.rightTree==None:
                return (None,False)
            else:
                return self.rightTree.retrieveTree(key)

        elif key<self.key:
            if self.leftTree==None:
                return (None,False)
            else:
                return self.leftTree.retrieveTree(key)

    ## functionaliteit
    def inorderSuccesorList(self):
        """
        HULPFUNCTIE: dient niet gehanteerd te worden door de user
            Creëert een list met de elementen van de boom gesorteerd in inorder traverse
        """
        l = []
        if self.leftTree != None:
            l += self.leftTree.inorderSuccesorList()
        l.append(self.value)
        if self.rightTree != None:
            l += self.rightTree.inorderSuccesorList()
        return l

    ## functionaliteit
    def inorderSuccesor(self,key):
        """
        HULPFUNCTIE: dient niet gehanteerd te worden door de user
            Hanteert inorderSuccesorList om de inorder succesor van een key te verkrijgen
        """
        l=self.inorderSuccesorList()
        i=-1
        for w in l:
            i+=1
            if i+1==len(l):
                return None
            if l[i]==key:
                inorderSuccesorKEY=l[i+1]
                return self.retrieveTree(inorderSuccesorKEY)[0]

    ## functionaliteit
    def deleteItem(self, key):
        """
        Verwijdert de doorgekregen RedBlackTree deelboom(Node) die bezit over de key uit de RedBlackTree
        door gebruik te maken van merges en inorder succesor switch als nodig
        Hanteert de 2-3-4 boom delete algrotime

        :param key: Een integer die gelinkt staat met een bepaalde value in de RedBlackTree

        preconditions: De doorgegeven RedBlackTree bezit over een key die gelijk aan de doorgegeven key

        postconditions: De doorgegeven RedBlackTree bezit niet meer over een deelboom die een key bezitte die gelijk aan de doorgegeven key was
        De RedBlackTree is nog steeds gebalanceerd
        Er vinden gegevens wijzigingen plaats.

        :return: Geeft True terug als het verwijderen gelukt is en false als niet
        """
        tree = RedBlackTree
        if self.deletionItem(key):
            updatedTree = self.treeCorrecter(tree)
            self.splitTree2()
            if self.color == "red":
                self.turnRedBlack()
            self.ThreeBlack()
            self.__dict__.update(updatedTree.__dict__)
            return True
        else:
            return False

    ## functionaliteit
    def splitTree2(self):
        """
        HULPFUNCTIE: dient niet gehanteerd te worden door de user
            Loopt doorheen heel de boom en splitst waar mogelijk met behulp van splitRoot
        """
        if self.splitRoot():
            self.color = "red"
        if self.leftTree != None:
            self.leftTree.splitTree2()
        if self.rightTree != None:
            self.rightTree.splitTree2()

    ## functionaliteit
    def merge(self):
        """
        HULPFUNCTIE: dient niet gehanteerd te worden door de user
            Merged de functie naar een 4-knoop door een colorchange
        """
        if self.leftTree != None and self.rightTree != None:
            self.leftTree.color = "red"
            self.rightTree.color = "red"

    ## functionaliteit
    def merge2Left(self):
        """
        HULPFUNCTIE: dient niet gehanteerd te worden door de user
            Merged de functie naar een 4-knoop door een colorchange
            De linkerboom wordt van kleur veranderd
        """
        if self.leftTree != None:
            self.leftTree.color = "black"
            if self.leftTree.leftTree!=None and self.leftTree.rightTree!=None:
                self.leftTree.leftTree.color = "red"
                self.leftTree.rightTree.color = "red"

    ## functionaliteit
    def merge2Right(self):
        """
        HULPFUNCTIE: dient niet gehanteerd te worden door de user
            Merged de functie naar een 4-knoop door een colorchange
            De rechterboom wordt van kleur veranderd
        """
        if self.rightTree != None:
            self.rightTree.color = "black"
            if self.rightTree.leftTree != None and self.rightTree.rightTree != None:
                self.rightTree.leftTree.color = "red"
                self.rightTree.rightTree.color = "red"

    ## functionaliteit
    def merge3Left(self):
        """
        HULPFUNCTIE: dient niet gehanteerd te worden door de user
            Roteert de boom naar links om Nodes te mergen
        """
        updatedTree = self.rotateLeftFull()
        updatedTree.leftTree.color = "red"
        updatedTree.leftTree.leftTree.leftTree.color = "red"
        updatedTree.leftTree.leftTree.rightTree.color = "red"
        self.__dict__.update(updatedTree.__dict__)

    ## functionaliteit
    def merge3Right(self):
        """
        HULPFUNCTIE: dient niet gehanteerd te worden door de user
            Roteert de boom naar rechts om Nodes te mergen
        """
        updatedTree = self.rotateRightFull()
        updatedTree.rightTree.color = "red"
        updatedTree.rightTree.rightTree.rightTree.color = "red"
        updatedTree.rightTree.rightTree.leftTree.color = "red"
        self.__dict__.update(updatedTree.__dict__)

    ## functionaliteit
    def merge3Mid(self):
        """
        HULPFUNCTIE: dient niet gehanteerd te worden door de user
            Roteert de boom naar links om Nodes te mergen
            Andere deelbomen worden van kleur verandert dan merge3Left()
        """
        updatedTree = self.rotateLeftFull()
        updatedTree.leftTree.color = "red"
        updatedTree.leftTree.rightTree.rightTree.color = "red"
        updatedTree.leftTree.rightTree.leftTree.color = "red"
        self.__dict__.update(updatedTree.__dict__)

    ## functionaliteit
    def mergeTree(self):
        """
        HULPFUNCTIE: dient niet gehanteerd te worden door de user
            Doorloopt een stuk van de boom en merged waar mogelijk
        """
        if self.leftTree != None and self.rightTree != None:
            if self.leftTree.color == "black" and self.rightTree.color == "black":
                self.merge()

        if self.leftTree != None and self.leftTree.leftTree != None and self.leftTree.rightTree != None:
            if self.leftTree.color == "red" and self.leftTree.leftTree.color == "black" and self.leftTree.rightTree.color == "black":
                self.merge2Left()

        if self.rightTree != None and self.rightTree.leftTree != None and self.rightTree.rightTree != None:
            if self.rightTree.color == "red" and self.rightTree.leftTree.color == "black" and self.rightTree.rightTree.color == "black":
                self.merge2Right()

        if self.leftTree != None and self.rightTree != None and self.leftTree.leftTree != None and self.leftTree.rightTree != None:
            if self.leftTree.color == "red" and self.rightTree.color == "red" and self.leftTree.leftTree == "black" and self.leftTree.rightTree == "black":
                self.merge3Left()

        if self.leftTree != None and self.rightTree != None and self.rightTree.leftTree != None and self.rightTree.rightTree != None:
            if self.leftTree.color == "red" and self.rightTree.color == "red" and self.rightTree.leftTree == "black" and self.rightTree.rightTree == "black":
                self.merge3Right()

        if self.leftTree != None and self.rightTree != None and self.leftTree.rightTree != None and self.rightTree.leftTree != None:
            if self.leftTree.color == "red" and self.rightTree.color == "red" and self.leftTree.rightTree == "black" and self.rightTree.leftTree == "black":
                self.merge3Mid()

    ## functionaliteit
    def treeCorrecter2(self):
        """
        HULPFUNCTIE: dient niet gehanteerd te worden door de user
            Roept mergeTree() aan
        """
        self.mergeTree()
        return self

    ## functionaliteit
    def Turn4Nodes(self,key):
        """
        HULPFUNCTIE: dient niet gehanteerd te worden door de user
            Doorloopt de functie todat die de doorgekregen key bereikt en verandert onderweg naar
            de key alle nodes naar 4-Nodes
        """
        updatedTree=self.treeCorrecter2()
        self.__dict__.update(updatedTree.__dict__)
        if key==self.key:
            return

        elif key>self.key:
            self.rightTree.Turn4Nodes(key)

        elif key<self.key:
            self.leftTree.Turn4Nodes(key)

    def ThreeBlack(self):
        if self.rightTree != None and self.rightTree.rightTree != None and self.color == "black" and self.rightTree.color == "black" and self.rightTree.rightTree.color == "black":
            if self.rightTree.leftTree == None:
                self.rightTree =self.rightTree.rotateLeftFull()
                self.rightTree.leftTree.color = "red"

        if self.leftTree != None and self.leftTree.leftTree != None and self.color == "black" and self.leftTree.color == "black" and self.leftTree.leftTree.color == "black":
            if self.leftTree.rightTree == None:
                self.leftTree = self.leftTree.rotateRightFull()
                self.leftTree.rightTree.color = "red"

        if self.leftTree != None:
            self.leftTree.ThreeBlack()
        if self.rightTree != None:
            self.rightTree.ThreeBlack()

    def redistrubteLeft(self,key):
        if self.leftTree != None and self.leftTree.key == key:
            if self.rightTree != None:
                if self.rightTree.leftTree != None and self.rightTree.leftTree.color == "red" and self.rightTree.leftTree.rightTree != None and self.rightTree.leftTree.leftTree != None:
                    Temp = RedBlackTree()
                    Temp.color = self.color
                    Temp.key = self.key
                    Temp.value = self.value
                    Temp2 = RedBlackTree()
                    Temp2.color = self.rightTree.leftTree.color
                    Temp2.key = self.rightTree.leftTree.key
                    Temp2.value = self.rightTree.leftTree.value
                    self.leftTree.rightTree = Temp
                    self.leftTree.rightTree.color = "red"
                    self.deleteItem(key)
                    self.key = Temp2.key
                    self.color = Temp2.color
                    self.value = Temp2.value
                    return True

                elif self.rightTree.rightTree != None and self.rightTree.rightTree.color == "red" and self.rightTree.rightTree.leftTree == None and self.rightTree.rightTree.rightTree == None:
                    Temp = RedBlackTree()
                    Temp.color = self.color
                    Temp.key = self.key
                    Temp.value = self.value
                    self.deleteItem(key)
                    self.__dict__.update(self.rightTree.__dict__)
                    self.leftTree = Temp
                    self.leftTree.color = "red"
                    return True
        return False

    def redistrubteRight(self, key):
        if self.rightTree != None and self.rightTree.key == key:
            if self.leftTree != None:
                if self.leftTree.leftTree != None and self.leftTree.leftTree.color == "red" and self.leftTree.leftTree.leftTree == None and self.leftTree.leftTree.rightTree == None:
                    Temp = RedBlackTree()
                    Temp.color = self.color
                    Temp.key = self.key
                    Temp.value = self.value
                    self.deleteItem(key)
                    self.__dict__.update(self.leftTree.__dict__)
                    self.rightTree = Temp
                    self.rightTree.color = "red"
                    return True

                elif self.leftTree.rightTree != None and self.leftTree.rightTree.color == "red" and self.leftTree.rightTree.leftTree == None and self.leftTree.rightTree.rightTree == None:
                    Temp = RedBlackTree()
                    Temp.color = self.color
                    Temp.key = self.key
                    Temp.value = self.value
                    Temp2 = RedBlackTree()
                    Temp2.color = self.leftTree.rightTree.color
                    Temp2.key = self.leftTree.rightTree.key
                    Temp2.value = self.leftTree.rightTree.value
                    self.rightTree.leftTree = Temp
                    self.rightTree.leftTree.color = "red"
                    self.deleteItem(self.leftTree.rightTree.key)
                    self.key = Temp2.key
                    self.color = Temp2.color
                    self.value = Temp2.value
                    return True
        return False

    ## functionaliteit
    def deletionItem(self, key):
        """
        HULPFUNCTIE: dient niet gehanteerd te worden door de user
            Verwijdert een item uit de boom door behulp van
            de 2-3-4 boom delete algoritme
        """
        if not self.retrieveTree(key)[1]:
            return False

        DeletionNode = self.retrieveTree(key)[0]
        if DeletionNode.leftTree == None and DeletionNode.rightTree == None and DeletionNode.color == "red":
            TempTree = self.completeDeletion(DeletionNode.key)
            if TempTree == None:
                self.__dict__.update(RedBlackTree().__dict__)
                return True
            self.__dict__.update(TempTree.__dict__)
            return True

        if DeletionNode.leftTree != None and DeletionNode.leftTree.color == "red" and self.inorderSuccesor(key) == None:
            COPYLeftTree = copy.deepcopy(DeletionNode.leftTree)
            DeletionNode.value = COPYLeftTree.value
            DeletionNode.key = COPYLeftTree.key
            DeletionNode.leftTree = COPYLeftTree.leftTree
            DeletionNode.rightTree = COPYLeftTree.rightTree
            return True

        if DeletionNode.leftTree == None and DeletionNode.rightTree == None:
            if self.redistrubteLeft(key):
                self.deletionItem(key)
                return True

            elif self.redistrubteRight(key):
                self.deletionItem(key)
                return True

        self.Turn4Nodes(key)

        if DeletionNode.leftTree == None and DeletionNode.rightTree == None and DeletionNode.color == "red":
            TempTree = self.completeDeletion(DeletionNode.key)
            if TempTree == None:
                self.__dict__.update(RedBlackTree().__dict__)
                return True
            self.__dict__.update(TempTree.__dict__)
            return True

        InorderSuccesor = self.inorderSuccesor(key)
        COPYInorderSuccesor = copy.deepcopy(InorderSuccesor)
        self.Turn4Nodes(InorderSuccesor.key)
        self.deletionItem(InorderSuccesor.key)
        DeletionNode.value = COPYInorderSuccesor.value
        DeletionNode.key = COPYInorderSuccesor.key
        return True

    ## functionaliteit
    def completeDeletion(self, key):
        """
        HULPFUNCTIE: dient niet gehanteerd te worden door de user
            Doorloopt de Tree en verwijdert de tree met de doorgegeven tree definitief
        """
        if key == self.key:
            self = None
            return self

        if key > self.key:
            self.rightTree = self.rightTree.completeDeletion(key)
            return self

        if key < self.key:
            self.leftTree = self.leftTree.completeDeletion(key)
            return self

class RedBlackTreeTable():
    def __init__(self):
        self.RBT = RedBlackTree()

    def tableIsEmpty(self):
        return self.RBT.isEmpty()

    def tableInsert(self,key,val):
        tree = createTreeItem(key,val)
        return self.RBT.insertItem(tree)

    def tableRetrieve(self,key):
        return self.RBT.retrieveItem(key)

    def traverseTable(self,arg):
        return self.RBT.inorderTraverse(arg)

    def save(self):
        return self.RBT.save()

    def load(self,args):
        return self.RBT.load(args)

    def tableDelete(self,key):
        return self.RBT.deleteItem(key)

    def clear(self):
        self.RBT = RedBlackTree()