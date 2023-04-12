"""ADT: Linkbased-Array Implementation of a Binary Search Tree (BST)"""

#Possible Improvements:
#1. Is TreeItemType correct geïmplementeerd?
#2. Hoe verwijder je een TreeItemType uit de boom? Het is nu unlinked =? verwijdert? "How does memory work?"
#3. Fix inception: parent=gwn waarde -> indien kiddos hiervan nodig of parent nodig, gwn search gebruiken? -> Aanpassen kost wat werk maar verhoogt efficientie aanzienlijk
#4. Mogelijs Delete nalopen, (voorwaardes veranderen regel +/- 240) "#Wat als in_ordersuccessor zelf een kind heeft? (Special scenario met 13)"

"""Data"""
def createTreeItem(KeyType, ValueType):
    """
    Methode om elementen aan te maken volgens de class 'TreeItemType'.
    :parameter in ; ''KeyType': integer , 'ValueType': object (Mag elke waarde zijn)
    :parameter out ; TreeItemType
    Preconditie: 'KeyType' is een unieke integer die nog niet in de BST voorkomt. 'ValueType' is een Python-Object wat in een static-array geplaatst kan worden.
    Postconditie: Er wordt een statische array meegegeven met alle parameters van TreeItemType. Initieel is dit: ['KeyType', 'ValueType', None, None, None, False]
    """
    NewItem = TreeItemType(KeyType, ValueType)
    return [NewItem.searchkey, NewItem.value, NewItem.leftchild, NewItem.rightchild, NewItem.parent, NewItem.traversal_ind]

class TreeItemType:
    """
    TreeItemType is het type van de elementen in de binaire zoekboom.
    Een element van dit type heeft een zoeksleutel-veld van het type KeyType en een (of meerdere) zoeksleutelwaarde-veld(en) van het type 'ValueType'.
    :parameter in ; 'KeyType': integer & 'ValueType': object (Mag elke waarde zijn)
    :parameter out ; 'KeyType': integer , 'ValueType': object (Mag elke waarde zijn), 'leftchild' : TreeItemType , 'rightchild': TreeItTemType , 'parent': TreeItTemType, 'traversal_ind': boolean,
    Initieel worden de waarden als volgt ingevuld: [SearchKey,Value,None,None,None,False]
    Preconditie: 'ValueType' is een Python-Object wat in een static-array geplaatst kan worden. 'KeyType' is een integer en is een unieke searchkey, dat wil zeggen; Er is nog geen searchkey met deze waarde in de BST.
    Postconditie: 'KeyType', 'ValueType', 'leftchild', 'rightchild', 'upper' & 'traversal' zijn gedefinieerd.
    """
    def __init__(self, KeyType, ValueType=None, leftchild=None, rightchild=None, upper=None, traversal=False):
        self.searchkey = KeyType
        self.value = ValueType
        self.leftchild = leftchild
        self.rightchild = rightchild
        self.parent = upper #root erboven
        self.traversal_ind = traversal #Duidt aan (indicator) of er een traversal-actie ('Functiontype') is gebeurt over dit element
        #self.full = [self.searchkey , self.value , self.leftchild , self.rightchild , self.parent , self.traversal_ind]

class FunctionType:
    """
    FunctionType is het type Python-Functie die wordt toegepast bij een traverse.
    :parameter in ; 'visit'
    :parameter out; 'visit'
    Preconditie: 'visit' is een Python-operatie zoals bv. "print". Het bevat volgend formaat: "'visit'( 'KeyType' )
    Postconditie: 'visit' is gedefinieerd.
    """
    def __init__(self , visit):
        self.visit = visit

"""Functionaliteit"""
class BST:
    def __init__(self):
        """
        Creeërt een lege BST
        :parameter in ;
        :parameter out ; 'root': TreeItemType, 'traversal': boolean, 'count': integer
        Preconditie:
        Postconditie: Er is een lege BST aangemaakt.
        """
        self.root=[None,None,None,None,None,False]
        self.traversal=True     #True als traversal is oneven maal geweest (niet) - False indien even maal geweest, vergelijkt hiervan self.traversal_ind)
        self.count=0            #Een hulpvariable om bepaalde functies hun recursie te tellen. Gaat na of het save- of load- algoritme is gepasseerd over de BST of geeft de diepte aan van de inorderTraverse

    def isEmpty(self):
        """
        Geeft aan of een BST leeg is of gevuld is.
        :parameter in ;
        :parameter out ; boolean
        Preconditie: Er is een BST aangemaakt.
        Postconditie: Geeft True als de BST leeg is, False als de BST gevuld is.
        """
        if self.root[0]==None:
            return True
        else:
            return False

    def search(self,root,searchKey):
        """
        Zoekt in de binaire zoekboom vanaf (inclusief) een positie ('root') naar het item met searchKey als zoeksleutel.
        :parameter in ; 'root': TreeItemType, 'searchKey': TreeItemType
        :parameter out ; Static-Array: [Succes: boolean, root: TreeItemType , Right/Left-child_Searchkey: boolean (of None)]
        Preconditie: 'searchKey' & 'root' zijn van het type 'TreeItemType'.
        Postconditie: Er is een Static-Array meegegeven volgens het bovenstaande formaat. 'succes' geeft aan of het gelukt is. 'root' geeft de positie in de boom mee. 'Right/Left-child_Searchkey' geeft resp. aan of de searchkey kleiner/Links/True, groter/Rechts/False of gelijkaan/root/none is t.o.v. de 'root'.
        """

        if self.isEmpty():
            return [False, root, False]

        if searchKey[0] == root[0]: #Root is evengroot als searchkey
            return [True, root, None]

        if root[0] > searchKey[0]: #Als kleiner dan root, zoek in leftchild
            if root[2]!=None:
                return self.search(root[2], searchKey)
            else:
                if (root[0] != searchKey[0]): # Edit on 12-04-2023 | Geeft altijd True mee anders?
                    return [False, root, True] # Edit on 12-04-2023 | Geeft altijd True mee anders?
                return [True, root, True]  #Geef True, gevonden positie(root & leftchild=TRUE) mee

        elif root[0] < searchKey[0]: #Is dus groter dan root, zoek dan in rightchild=FALSE
            if root[3]!=None:
                return self.search(root[3], searchKey)
            else:
                if (root[0] != searchKey[0]):  # Edit on 29-03-2023 | Geeft altijd True mee anders?
                    return [False, root, False]  # Edit on 29-03-2023 | Geeft altijd True mee anders?

                return [True, root, False]
        else:                               #Zoeken faalt, return False
            return [False, False, False]

    def searchTreeInsert(self, NewItem):
        """
        Voegt newItem toe aan een binaire zoekboom met items met unieke
        zoeksleutels verschillend van de zoeksleutel van newItem. Success
        geeft weer of het toevoegen gelukt is.
        :parameter in ; NewItem: TreeItemType
        :parameter out ; succes: boolean
        Preconditie: Er is een BST aangemaakt. NewItem bevat een zoeksleutel die uniek is, en dus nog niet in de boom zit.
        Postconditie: NewItem is toegevoegd aan de BST.
        """

        found=self.search(self.root, NewItem)
        succes=found[0]     #Succeeded search operation
        node=found[1]       #Node in which left or right has place
        position=found[2]   #Left=True & Right=False

        if(self.root[0]==None): #Lege Boom
            self.root = NewItem
            return True

        if succes==False: #No subtrees
            if position==True: #Left
                node[2] = NewItem  # knoop wordt gelinked aan NewItem
                NewItem[4] = node
                return True
            elif position==False:
                node[3] = NewItem  # knoop wordt gelinked aan NewItem
                NewItem[4] = node
                return True
            else:
                print("BST INSERT ERROR :'(")

        if (succes==True) and (position==True):#Links inserten
            node[2]=NewItem #knoop wordt gelinked aan NewItem
            NewItem[4] = node
            return True

        if (succes==True) and (position==False):#Rechts inserten
            node[3] = NewItem  # knoop wordt gelinked aan NewItem
            NewItem[4] = node
            return True

        else:
            return False

    def searchTreeDelete(self,SearchKey):
        """
        Verwijdert een zoeksleutel uit de BST. (Unlinken van de zoeksleutel)
        :parameter in ; 'SearchKey': KeyType
        :parameter out ; 'success': boolean
        Preconditie: Er is een BST aangemaakt.
        Postconditie: 'Searchkey' is verwijdert uit de BST.
        """
        SearchItem = TreeItemType(SearchKey) #Maakt een tijdelijke Full_SearchItem aan, zodat deze voldoet aan de precondities van de search-methode.
        Full_SearchItem = [SearchItem.searchkey, SearchItem.value, SearchItem.leftchild, SearchItem.rightchild,SearchItem.parent, SearchItem.traversal_ind]

        found = self.search(self.root, Full_SearchItem)
        succes = found[0]  # Succeeded search operation
        node = found[1]  # Node in which left or right has place = N
        position = found[2]  # Left=True & Right=False

        if succes == False:  # Lege Boom
            return False

        if position!=None: #Indien de searchkey niet gelijk aan iets is/Niet gevonden, kan deze niet gedelete worden!
            return False

        if (succes == True): # Searchkey-Node gevonden
            #check of 0-1-2 nodes leeg zijn

            # N heeft geen kinderen=Blad
            if ((node[2]==None) and (node[3]==None)):
                if self.root == node: #Verwijderen van root is specialer geval
                    self.root=[None, None, None, None, None, False]
                    return True

                parent = node[4]

                if node==parent[2]: #N is een linkerkind
                    parent[2]=None
                    return True
                else: #N zelf is dus een rechterkind
                    parent[3] = None
                    return True

            # N heeft 1 kind
            elif ((node[2]==None) or(node[3]==None)):
                parent=node[4]
                #Zit node zelf als linker of als rechter kind? (check parent)
                #Moeten we linker of rechter kind swappen van node? (check node)

                if parent==None: #root deleten is speciaal geval
                    if node[2] != None:  # Linkerkind swappen | (parent - kind koppelen, kind-parent koppelen)
                        leftchild=node[2]
                        self.root = leftchild #Linkerkind is nieuwe root
                        leftchild[4] = None #Parent is er niet meer
                        return True
                    else:  # Rechterkind swappen | (parent - kind koppelen, kind-parent koppelen)
                        rightchild = node[3]
                        self.root = rightchild  # Rechterkind is nieuwe root
                        rightchild[4] = None  # Parent is er niet meer
                        return True

                elif parent[2]==node: #Node is zelf een linkerkind
                    if node[2]!= None:  # Linkerkind van node swappen
                        leftchild = node[2]
                        parent[2] = leftchild  # Nieuw-Linkerkind van 'parent' is nu Node-kind
                        leftchild[4] = parent  #Node-kind dr parent is nu 'parent'
                        return True
                    else: #Rechterkind van node swappen
                        rightchild = node[3]
                        parent[2] = rightchild  # Nieuw-Linkerkind van 'parent' is nu Node-kind
                        rightchild[4] = parent  # Node-kind dr parent is nu 'parent'
                        return True

                else: #Node is zelf dus een rechter kind
                    if node[2] != None:  # Linkerkind van node swappen
                        leftchild = node[2]
                        parent[3] = leftchild  # Nieuw-Linkerkind van 'parent' is nu Node-kind
                        leftchild[4] = parent  # Node-kind dr parent is nu 'parent'
                        return True
                    else:  # Rechterkind van node swappen
                        rightchild = node[3]
                        parent[3] = rightchild  # Nieuw-Linkerkind van 'parent' is nu Node-kind
                        rightchild[4] = parent  # Node-kind dr parent is nu 'parent'
                        return True

            # N heeft 2 kinderen
            elif ((node[2]!=None) and (node[3]!=None)):
                # zoek inorder successor = kleinste knoop in rechterdeelboom
                #3 gevallen: hoogte verschil=1, =2 of >2 -> tellen hulpfunctie?
                right_tree=node[3]
                left_tree=node[2]
                inorder_successor=self.find_inorder_successor(right_tree)
                parent = node[4]

                #SWAP met inorder successor

            #Link kinderen
                #Link bij inorder
                inorder_successor[2]=node[2]
                if inorder_successor!=node[3]: #Als het niet hetzelfde is (anders krijg je interception) (Kan alleen bij rechterdeelboom inprincipe, want inorder_successor is rechter deelboOm)
                    inorder_successor[3]=node[3]
                #Link kinderen
                if right_tree!=inorder_successor: #Als het niet hetzelfde is (anders krijg je interception) (Kan alleen bij rechterdeelboom inprincipe, want inorder_successor is rechter deelbom)
                    right_tree[4] = inorder_successor
                left_tree[4]=inorder_successor
            #Unlink parent(inorder_succesoor)_left child
            parent_of_inordersuccessor=inorder_successor[4]
            parent_of_inordersuccessor[2]=None

            #Link parents
            if self.root!=node: #node is geen root
                #Link bij Parents
                    #Is node zelf een linker of rechterkind?
                if parent[2]==node: #Node is zelf een linkerkind
                    parent[2]=inorder_successor
                else: #Node is zelf een rechterkind
                    parent[3]=inorder_successor
                #Link bij inorder_successor
                inorder_successor[4]=parent
                self.count = 0 #Reset counter
                return True

            else: #node is dus rootzelf
                # Link bij Parents
                self.root=inorder_successor
                # Link bij inorder_successor
                inorder_successor[4] = None
                self.count=0 #Reset counter
                return True

        self.count = 0 #Reset counter
        return False

    def find_inorder_successor(self,root):
        """
        Een hulpfunctie om de inorder_successor te vinden van een root. Dit is een hulpfunctie en mag enkel intern worden opgeroepen.
        :parameter in ; 'root': TreeItemType
        :parameter out ; 'root': TreeItemType
        Preconditie: Er is een BST aangemaakt.
        Postconditie: Geeft de inorder_successor terug. Wijzigt geen waarden van de BST.
        """
        left=root[2]
        self.count+=1 #Wordt gereset in delete functie
        if (left != None):
            self.find_inorder_successor(left) # Ga helemaal naar links onder
            return left
        else:
            return root

    def searchTreeRetrieve(self,SearchKey):
        """
        Zoekt een zoeksleutel en geeft de waarde ervan mee.
        :parameter in ; 'SearchKey":KeyType
        :parameter out ; tuple("Value': ValueType, 'Succes": boolean)
        Preconditie: Er is een BST aangemaakt.
        Postconditie: Er is een tuple meegegeven met bovenstaande parameters. De BST blijft onveranderd.
        """
        SearchItem = TreeItemType(SearchKey)
        Full_SearchItem=[SearchItem.searchkey, SearchItem.value, SearchItem.leftchild, SearchItem.rightchild, SearchItem.parent, SearchItem.traversal_ind]

        found=self.search(self.root, Full_SearchItem)
        succes = found[0]  # Succeeded search operation
        node = found[1]  # Node in which left or right has place = N

        if succes:
            return (node[1], True)

        return (None, False)

    def inorderTraverse(self,visit,root=None):
        """
        Doorloopt een BST volgens het inorderTraverse algoritme.
        :parameter in ; 'visit': FunctionType
        :parameter out ; 'Zoeksleutel': KeyType
        Preconditie: Er is een boom aangemaakt.
        Postconditie: De BST is doorlopen volgens een inorderTraverse waarbij iedere zoeksleutel is onderworpen aan de 'visit' operatie.
        """
        if self.isEmpty():
            return False

        if (root==None):
            root = self.root

        left=root[2]
        right = root[3]

        if (left != None) and (left[5]!=self.traversal):
            self.inorderTraverse(visit,left) #Ga eerst helemaal naar links onder

        else:
            if (root[5] != self.traversal): #Na links, visit & print root
                visit(root[1])
                root[5]=self.traversal
                if right != None: #Ga evt. naar rechts
                    self.inorderTraverse(visit,right)
                else: #  right == None => # Go up
                    self.inorderTraverse(visit,root[4])
            elif root[4]!=None: #Indien root, links & rechts gehad, ga omhoog
                self.inorderTraverse(visit,root[4])

            else: #Als alles is geweest, exit & reset/verander traversal
                if self.traversal ==False:
                    self.traversal = True
                else:
                    self.traversal = False
                pass

    def save(self, root=None, dict=None):
        """
        Doorloopt een BST volgens het algoritme aangegeven in de opgave en slaat dit op in een Python-map.
        :parameter in ; 'root': TreeItemType
        :parameter out ; 'dict': Python-Dictionary
        Preconditie: Er is een boom aangemaakt. Initieel zijn 'root' en 'dict' "None".
        Postconditie: Er wordt een map teruggegeven die iedere zoeksleutel uit de BST bevat volgens de aangegeven volgorde.
        """

        if self.isEmpty(): #Als de boom leeg is, is de map ook leeg
            return {'root': None}

        if self.count==0: #Als dit de eerste keer is, stel een aantal standaar waarden in
            if dict is None: #Verandert dict in een lege map
                dict = {}

            if root is None:
                root = self.root #Stel de 'root' in op self.root
        self.count+=1

        dict['root']=root[0] #1e waarde is de zoeksleutel van de root

        left = root[2]
        right = root[3]

        if (left!=None) and (right!=None): #Als de root 2 kinderen heeft, herhaal voor deze 2
            dict['children']=[self.save(left,{}),self.save(right,{})]
            self.count = 0 #Zet voordat de map wordt teruggegeven, alles weer in standaard positions
            return dict

        elif (left==None) and (right==None): #Als de root geen kinderen heeft, zijn we klaar
            self.count = 0 #Zet voordat de map wordt teruggegeven, alles weer in standaard positions
            return dict

        elif (left!=None) or (right!=None):  #Indien de root 1 kind heef
            if left==None: #Bij een rechterkind (left is dus None)
                dict['children'] = [None, self.save(right,{})]
                self.count = 0 #Zet voordat de map wordt teruggegeven, alles weer in standaard positions
                return dict
            else: #Right is none
                dict['children'] = [self.save(left, {}),None]
                self.count = 0 #Zet voordat de map wordt teruggegeven, alles weer in standaard positions
                return dict

        else: #Indien geen optie geselecteerd, is er iets verkeerds gegaan. Return False
            self.count = 0 #Zet voordat de map wordt teruggegeven, alles weer in standaard positions
            return False

    def load(self,map,count=0):
        """
        Laad een BST in en overschrijf hierbij de huidige BST.
        :parameter in ; 'map': Python-Map volgens de format uit de opgave.
        :parameter out ;
        Preconditie: Er is een BST class aangemaakt.
        Postconditie: De BST opgegegevn via de map is ingeladen als BST.
        """
        if count==0: #Indien er nog geen load is geweest;
            self.root=[None,None,None,None,None,False] #Reset huidige tree == Overschrijven huidige boom
            self.count+=1 #Tel eentje bij count op zodat recursie niet constant de root op None zet

        SearchItem = TreeItemType(map['root']) #Format ieder item naar een TreeItemType
        Full_SearchItem = [SearchItem.searchkey, SearchItem.value, SearchItem.leftchild, SearchItem.rightchild, SearchItem.parent, SearchItem.traversal_ind]
        self.searchTreeInsert(Full_SearchItem) #Insert item

        if 'children' in map.keys(): #Indien er kinderen zijn, insert deze:
            if (map['children'][0]!=None): #Bij 2 kinderen
                count += 1
                self.load(map['children'][0],count) #Linkerkind

            if (map['children'][1]!=None): #Bij 1 kind
                count += 1
                self.load(map['children'][1],count)

            else: #Als er geen kinderen zijn, stop
                #self.count=0
                return
        else: #ALs er geen kinderen zijn, stop
            self.count=0
            return

class BSTTable:
    def __init__(self):
        self.boom = BST()
        self.id = None

    def tableIsEmpty(self):
        return self.boom.isEmpty()

    def tableInsert(self,key,value):
        return self.boom.searchTreeInsert(createTreeItem(key,value))

    def tableDelete(self,searchkey):
        return self.boom.searchTreeDelete(searchkey)

    def tableRetrieve(self,searchkey):
        return self.boom.searchTreeRetrieve(searchkey)

    def traverseTable(self,function):
        return self.boom.inorderTraverse(function)

    def load(self,list):
        return self.boom.load(list)

    def save(self):
        return self.boom.save()

    def clear(self):
        self.boom = BST()

    def get_id(self):
        return self.id

class Kees:
    def __init__(self, naam):
        self.naam = naam

"""
t = BSTTable()
Kees3 = Kees("ka")
Kees5 = Kees("John no cee me")

print(t.tableInsert(3,3))
print(t.tableInsert(5,5))

#print(t.tableInsert(3,Kees3))

print(t.tableRetrieve(3))
print(t.tableRetrieve(5))

print(t.tableRetrieve(4))"""

