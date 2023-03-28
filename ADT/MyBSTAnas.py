## functionaliteit
def createTreeItem(key,val):
    """
    Creëert een BinarySearchTree met lege deelbomen die bezit over de doorgekrege key en value

    :param key: Een integer die vastgebonden is aan een value.
    :param val: De value van de BinarySearchTree

    preconditions: De key is een integer

    postconditions: Er is een BinarySearchTree gecreëerd met lege deelbomen die bezit over de doorgekrege key en value

    :return: BinarySearchTree met lege deelbomen die bezit over de doorgekrege key en value
    """
    #if isinstance(key, int):
    Tree=BST(key,val)
    #else:
        #Tree=None
    return Tree

class BST:
    # constructer
    """
    Creëert een BinarySearchTree met lege deelbomen die bezit over een doorgekrege key en value als er key en value waarden zijn doorgegeven

    :param args: Een lijst die leeg is of de elementen key en value bevatten

    preconditions: Als er een key wordt doorgegeven dan is dit een integer en staat het op index 1
    value staat op index 0

    postconditions: Er is een BinarySearchTree gecreëerd met lege deelbomen die bezit over de doorgekrege key en value
    als die waarden zijn doorgegeven

    :return: BinarySearchTree met lege deelbomen die bezit over de doorgekrege key en value als die waarden zijn doorgegeven
    """
    def __init__(self, *args):
        if len(args) ==0:
            self.Lefttree=None
            self.Righttree=None
            self.value=None
            self.key=None
        else:
            self.Lefttree = None
            self.Righttree = None
            self.value = args[1]
            #if isinstance(args[0],int):
            self.key = args[0]
            #else:
            #self.key=None

    ## functionaliteit
    def isEmpty(self):
        """
        Controleert de opgegeven BinarySearchTree of die leeg is of niet en geeft naarmate hiervan een booleaanse waarde terug.
        True als de stack BinarySearchTree leeg is, False als dit niet het geval is.

        preconditions: Er word een BinarySearchTree doorgegeven

        postconditions: De functie geeft een booleaanse waarde weer.
        Er vinden geen gegevens wijzigingen plaats.

        :return: De functie geeft naarmate de BinarySearchTree vol of leeg is een booleaanse waarde terug.
        """
        if self.value==None:
            return True
        else:
            return False

    ## functionaliteit
    def searchTreeInsert(self,Tree):
        """
        Plaats een tree in de BinarySearchTree volgens zijn key
        Hoe groter de key, hoe meer rechts de tree geplaatst wordt

        :param Tree: BinarySearchTree met None deelbomen

        preconditions: De doorgegeven tree zijn deelbomen zijn None

        postconditions: De BinarySearchTree bezit nu over de toegevoegde tree als een deelboom
        Er vinden gegevens wijzigingen plaats.

        :return: BinarySearchTree met nieuwe deelboom
        """
        if self.key == None:
            self.value = Tree.value
            self.key = Tree.key
            self.Lefttree = Tree.Lefttree
            self.Righttree = Tree.Righttree

        elif Tree.key == self.key:
            Tree.Lefttree = self.Lefttree
            Tree.Righttree = self.Lefttree


        elif Tree.key > self.key:
            if self.Righttree != None:
                self.Righttree.searchTreeInsert(Tree)
            else:
                self.Righttree = Tree


        elif Tree.key < self.key:
            if self.Lefttree != None:
                self.Lefttree.searchTreeInsert(Tree)
            else:
                self.Lefttree = Tree
        return True

    ## functionaliteit
    def searchTreeRetrieve(self,key):
        """
        Weergeeft de value van de BinarySearchTree die bezit over de doorgegeven key

        :param key: Een integer die gelinkt staat met een bepaalde value in de BinarySearchTree

        preconditions: De doorgegeven BinarySearchTree bezit over een key die gelijk aan de doorgegeven key

        postconditions: De value die verbonden staat met de doorgekregen key wordt doorgegeven
        Er vinden geen gegevens wijzigingen plaats.

        :return: pair met de gezochte value en true als de key zich bevindt in de BinarySearchTree, anders (0,False)
        """
        if key==self.key:
            return (self.value,True)

        elif key>self.key:
            if self.Righttree==None:
                return (0,False)
            else:
                return self.Righttree.searchTreeRetrieve(key)

        elif key<self.key:
            if self.Lefttree==None:
                return (0,False)
            else:
                return self.Lefttree.searchTreeRetrieve(key)

    ## functionaliteit
    def inorderTraverse(self, arg):
        """
        Voert een bepaalde functie (arg) uit op values in de BinarySearchTree in inorderTraverse volgorde

        :param arg: Functie die wordt uitgevoerd op de values van de BinarySearchTree in inorderTraverse volgorde

        preconditions: arg is een valide functie die verschillende data types als input kan hebben

        postconditions: De functie arg wordt in inorderTraverse volgorde op de values uitgevoerd
        Er kunnen gegevens wijzigingen plaats vinden naarmate wat de arg functie.

        :return: Returned het resultaat van de arg functie, kan niets zijn
        """
        if self.Lefttree != None:
            self.Lefttree.inorderTraverse(arg)
        arg(self.value)
        if self.Righttree != None:
            self.Righttree.inorderTraverse(arg)

    ## functionaliteit
    def save(self):
        """
        Weergeeft de doorgekregen BinarySearchTree in string form

        preconditions: Er word een BinarySearchTree doorgegeven

        postconditions: De functie returned een string voorstelling van de BinarySearchTree
        Er vinden geen gegevens wijzigingen plaats.

        :return: String form van de BinarySearchTree
        """
        c="{"
        c+="\'root\': "+ str(self.key)
        if self.Lefttree==None and self.Righttree==None:
            c+="}"
            return c
        c += ",\'children\':["

        if self.Lefttree!=None:
            c+=self.Lefttree.save()
        else:
            c+="None"

        if self.Righttree!=None:
            c+=","
            c += self.Righttree.save()
        else:
            c+=",None"

        c+="]"
        c += "}"
        return c

    ## functionaliteit
    def InorderSuccesor(self):
        """
        HULPFUNCTIE: dient niet gehanteerd te worden door de user
            returned een list die de values van de BinarySearchTree in InorderTraverse bevat
        """
        l=[]
        if self.Lefttree != None:
            l+=self.Lefttree.InorderSuccesor()
        l.append(self.value)
        if self.Righttree != None:
            l+=self.Righttree.InorderSuccesor()
        return l

    ## functionaliteit
    def searchTreeDelete(self,key):
        """
        Verwijdert de BinarySearchTree(deelboom) met de doorgegeven key uit de BinarySearchTree zonder de tree ongeldig te maken

        :param key: Een integer die gelinkt staat met een bepaalde value in de BinarySearchTree

        preconditions: De doorgegeven BinarySearchTree bezit over een key die gelijk aan de doorgegeven key

        postconditions: De doorgegeven BinarySearchTree bezit niet meer over een deelboom die een key bezitte die gelijk aan de doorgegeven key was
        Er vinden gegevens wijzigingen plaats.

        :return: Geeft True terug als het verwijderen gelukt is en false als niet
        """
        if self.Lefttree!=None:
            if self.Lefttree.key == key:
                if self.Lefttree.Lefttree == None and self.Lefttree.Righttree == None:
                    self.Lefttree=None
                    return True

        if self.Righttree!=None:
            if self.Righttree.key == key:
                if self.Righttree.Lefttree == None and self.Righttree.Righttree == None:
                    self.Righttree=None
                    return True

        if key>self.key:
            if self.Righttree==None:
                return False
            else:
                return self.Righttree.searchTreeDelete(key)

        elif key<self.key:
            if self.Lefttree==None:
                return False
            else:
                return self.Lefttree.searchTreeDelete(key)

        if self.key==key:
            InorderList = self.InorderSuccesor()
            i=-1
            for w in InorderList:
                i+=1
                if w==key and len(InorderList)!=2:
                    TempBST2KEY= InorderList[i+1]

                elif w!=key and len(InorderList)==2:
                    TempBST2KEY = w

            self.value = self.searchTreeRetrieve(TempBST2KEY)[0]
            self.searchTreeDelete(TempBST2KEY)
            self.key = TempBST2KEY
            return True
        return False

    ## functionaliteit
    def load(self, args):
        """
        Creëert een BinarySearchTree met de doorgekregen parameters

        :param args: parameters volgens output formaat van save functie, niet in string form

        preconditions: args heeft het formaat van de output formaat van save functie

        postconditions: De doorgekregen BinarySearchTree is vervangen worden met de gecreëerde BinarySearchTree
        Er vinden gegevens wijzigingen plaats.

        :return: De gecreëerde BinarySearchTree
        """
        TempBST= BST()
        for w, i in args.items():
            if w=="root":
                Temp2BST = BST(i,i)
                TempBST.searchTreeInsert(Temp2BST)
            if w=="children":
                if i[0]!=None:
                    Temp3BST = BST()
                    Temp3BST.load(i[0])
                    TempBST.searchTreeInsert(Temp3BST)
                if i[1]!=None:
                    Temp3BST = BST()
                    Temp3BST.load(i[1])
                    TempBST.searchTreeInsert(Temp3BST)
        self.value = TempBST.value
        self.key = TempBST.key
        self.Lefttree = TempBST.Lefttree
        self.Righttree = TempBST.Righttree
        return TempBST


class BSTTable:
    def __init__(self):
        self.T = BST()

    def tableIsEmpty(self):
        return self.T.isEmpty()

    def tableInsert(self, key, val):
        Tree = createTreeItem(key,val)
        return self.T.searchTreeInsert(Tree)

    def tableRetrieve(self,key):
        return self.T.searchTreeRetrieve(key)

    def tableDelete(self,key):
        return self.T.searchTreeDelete(key)

    def traverseTable(self,function):
        return self.T.inorderTraverse(function)

    def load(self, list):
        return self.T.load(list)

    def save(self):
        return self.T.save()

    def clear(self):
        self.T = BST()