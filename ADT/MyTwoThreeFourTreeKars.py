"""ADT: Implementation of a TwoThreeFourTree (234T)"""

#Possible Improvements:
#1. Limiteer het heruitberekenen van bv keycounts, en geeft dit door als resultaat (hogere efficientie; minder x berekenen)

"""Data"""
def createTreeItem(key,value):
    """
    Methode om elementen aan te maken volgens de class 'TreeItemType'.
    :parameter in ; 'key': getal , 'value': object (Mag elke waarde/Python Object zijn wat in een Python List ([]) past)
    :parameter out ; TreeItemType
    Preconditie: 'key' is een unieke integer die nog niet in de 234T voorkomt. 'value' is een Python-Object wat in een static-array geplaatst kan worden.
    Postconditie: Er wordt een TreeItemType meegegeven met paramaters 'key' & 'value'. De andere paramaters (left,middleleft,middleright,right,parent) zijn geïnitaliseerd op "None".
    """
    return TreeItemType(key,value)

class TreeItemType:
    """
    TreeItemType is het soort elementen die de 234T bevat.
    :parameter in ; 'key': integer , 'value': object (Mag elke waarde/Python Object zijn wat in een Python List ([]) past) 'left': TreeItemType , 'middleleft': TreeItemType , 'middleright': TreeItemType , 'right': TreeItemType , 'parent': TreeItemType
    :parameter out ; TreeItemType (Defined:Constructed)
    Preconditie: 'key' is een unieke integer die nog niet in de 234T voorkomt. 'value' is een Python-Object wat in een static-array geplaatst kan worden. 'left','middleleft',middleright','right','parent' zijn niet dezelfde TreeItemType EN zijn niet het aangemaakte TreeItemType zelf.
    Postconditie: Er wordt een TreeItemType meegegeven met paramaters 'key' & 'value'. De andere paramaters (left,middleleft,middleright,right,parent) zijn geïnitaliseerd op "None" indien er geen waarde is meegegeven.
    """
    def __init__(self,key,value,left=None,middleleft=None,middleright=None,right=None,parent=None):
        self.key =[key,None,None]       #key #Searckey[0] correspondert met Value[0]
        self.value = [value,None,None]  #Values
        self.left = left                #Linker deelboom
        self.middleleft= middleleft     #Middelste deelboom links   #Als slechts 1 middelste deelboom; left in use/voorrang #Link=links & rechts=right
        self.middleright= middleright   #Middelste deelboom rechts
        self.right = right              #Rechterdeelboom
        self.parent = parent            #Root/parent van huidige tree

class FunctionType:
    """
    FunctionType is het type Python-Functie die wordt toegepast bij een traverse op de 'key' van ieder TreeItemType.
    :parameter in ; 'visit'
    :parameter out; 'visit'
    Preconditie: 'visit' is een Python-operatie zoals bv. "print". Het bevat volgend formaat: "'visit'( 'key' ). De Python-Operatie moet uitvoerbaar zijn op een elemenent van het type 'key'.
    Postconditie: 'visit' is gedefinieerd/geconstrueerd.
    """
    def __init__(self , visit):
        self.visit = visit              #Pyhon Functie

"""Functionaliteit"""
class TwoThreeFourTree:
    """
    TwoThreeFourTree is de klasse van de 234T die elementen bevat, bestaande uit TreeItemType's. De klasse bevat een aantal functie om de 234T te gebruiken, evenals een aantal hulpfunctie's  die niet voor extern gebruik zijn. Dit is een interent implementatie.
    :parameter in ; /
    :parameter out; 'root': TreeItemType
    Preconditie:  /
    Postconditie: 'root' is gedefineerd/geconstrueerd.
    """
    def __init__(self):
        self.root=TreeItemType(None,None)   #Create empty root

    def isEmpty(self):
        """
        Geeft aan of de 234T leeg is.
        :parameter in ; /
        :parameter out; bool
        Preconditie: Er is een 234T aangemaakt.
        Postconditie: Als de 234T leeg is, wordt er True meegegeven. Indien de 234T niet leeg is, wordt er False meegegeven.
        """
        if self.root.key[0]==None: #Root heeft geen keys, dus is leeg
            return True
        return False

    def insertItem(self, TreeItemType, Tree=None):
        """
        Voegt een item toe in een blad van de 234T
        :parameter in ; 'TreeItemType': TreeItemType , 'Tree': TreeItemType
        :parameter out; bool
        Preconditie: Er is een 234T aangemaakt. 'TreeItemType' is een uniek element met een 'key' die nog niet voorkomt in de 234T.
        Postconditie: Als de operatie geslaagd is, wordt er True meegegeven. Als de operatie niet slaagt, wordt er False meegegeven.
        """
        if Tree==None:                  #Indien er geen Tree wordt meegegeven, initaliseer deze op 'root' (zodat recursie mogelijk is)
            Tree=self.root

        if (self.keyCount(Tree)==3):    #Splits elke 4-knoop (3 searchkeys) die je tegenkomt
            Tree=self.split(Tree)[2]    #De 234T verandert eventueel door het splitten van vorm. Assign de juiste TreeItemType terug aan Tree.

        #Bij een insert moeten we een blad vinden: self.subtree_count==0 (Geen deelbomen/Alle deelbomen zijn "None") AND self.keyCount!=3 (Er moet een plek zijn om een key te inserten)
        #If not: vergelijk 'key' en ga recursief de subtree's na.
        #Key Format: Left is als laatste != None, right als 3e != None, middeleft als 2e != None & middleright als 1e !=None

        a=self.subtree_count(Tree)

        if a==1: #1 subtree, & key, zou niet mogen voorkomen
            return False #Error

        elif a==2:  #2 subtrees: 2-node (1 key)
            #Go to correct subtree
            if TreeItemType.key[0]<Tree.key[0]:
                return self.insertItem(TreeItemType , Tree.left)
            elif TreeItemType.key[0]>Tree.key[0]:
                return self.insertItem(TreeItemType , Tree.right)
            else:
                return False #Error

        elif a==3: #3-Node (2 keys)
            #Go to subtrees
            if TreeItemType.key[0]<Tree.key[0]:
                return self.insertItem(TreeItemType , Tree.left)
            elif TreeItemType.key[0]<Tree.key[2]:
                return self.insertItem(TreeItemType , Tree.middleleft)
            elif TreeItemType.key[0]>Tree.key[2]:
                return self.insertItem(TreeItemType , Tree.right)
            else:
                return False #Error

        elif a==4:          #Zou deze node gesplits moeten zijn? // Afhankelijk van context?
            #Go to subtrees
            if TreeItemType.key[0]<Tree.key[0]:
                return self.insertItem(TreeItemType , Tree.left)
            elif TreeItemType.key[0]<Tree.key[1]:
                return self.insertItem(TreeItemType , Tree.middleleft)
                return True
            elif TreeItemType.key[0]<Tree.key[2]:
                return self.insertItem(TreeItemType , Tree.middleright)
            elif TreeItemType.key[0]>Tree.key[2]:
                return self.insertItem(TreeItemType , Tree.right)
            else:
                return False #Error

        elif a==0: #Alle deelbomen zijn none, insert dus in de node
            if self.isEmpty():  #Als de boom leeg is, set new root
                self.root=TreeItemType
                return True

            elif Tree.key[2]==None: #Tree.key[0] kan nooit 0 zijn #Node met 1 searchkey
                # Moeten geen nieuwe tree inserten, er is hier plek; enkel keys & values toevoegen
                if TreeItemType.key[0]<Tree.key[0]:
                    #shift keys & values to right (2x) // Keep right format
                    temp_key=Tree.key[0]
                    temp_value=Tree.value[0]
                    Tree.key[0]=TreeItemType.key[0]
                    Tree.value[0]=TreeItemType.value[0]
                    Tree.key[2]=temp_key
                    Tree.value[2]=temp_value
                    return True
                else: #Searchkey is groter dan tree.key[0]
                    Tree.key[2]=TreeItemType.key[0]
                    Tree.value[2]=TreeItemType.value[0]
                    return True

            elif Tree.key[1]==None: #Right value is dus niet leeg, en links ook niet. kijk of middelste none is
                if TreeItemType.key[0]<Tree.key[0]: #Zit helemaal links
                    #shift left key & value to right (1x)
                    temp_key=Tree.key[0]
                    temp_value=Tree.value[0]
                    Tree.key[0]=TreeItemType.key[0]
                    Tree.value[0]=TreeItemType.value[0]
                    Tree.key[1]=temp_key
                    Tree.value[1]=temp_value
                    return True

                elif TreeItemType.key[0]<Tree.key[2]: #Zit tussen in
                    Tree.key[1]=TreeItemType.key[0]
                    Tree.value[1]=TreeItemType.value[0]
                    return True

                elif TreeItemType.key[0]>Tree.key[2]: #Hoort helemaal rechts te zitten
                    #shift right key & value to left (1x)
                    temp_key=Tree.key[2]
                    temp_value=Tree.value[2]
                    Tree.key[2]=TreeItemType.key[0]
                    Tree.value[2]=TreeItemType.value[0]
                    Tree.key[1]=temp_key
                    Tree.value[1]=temp_value
                    return True

            elif Tree.key[1]!=None: #Volle node (3 searchkeys, zou niet mogen! zou gesplit moeten zijn!
                return False

    def split(self,Tree):
        """
        Submethode van insertItem om een TreeItemType te splitsen (keyCount == 3). Dit is een hulpfunctie en mag enkel intern worden opgeroepen.
        :parameter in ; 'Tree': TreeItemType
        :parameter out; Array: ['succes': bool , 'succes': bool , 'parent': TreeItemType] // [True,True,parent]
        Preconditie: Er is een 234T aangemaakt. TreeItemType.keyCount is 3. (Volle node)
        Postconditie: Als de operatie geslaagd is, wordt er True meegegeven. Als de operatie niet slaagt, wordt er False meegegeven. Bij een geslaagde operatie is de volle node opgepitst volgens de algoritme uit de cursus in een nieuwe root (Middle key) & 2 subtrees. (Left & right key)
        """
        parent=Tree.parent #Initalise parent

        #Root splitsen is speciaal geval
        if parent==None and Tree==self.root: #Maak een nieuwe root aan met middelste searchkey
            new_root=TreeItemType(Tree.key[1],Tree.value[1])
            Tree.key[1]=None
            Tree.value[1]=None
            Tree.parent=new_root
            self.root=new_root
            new_root.left=TreeItemType(Tree.key[0], Tree.value[0], Tree.left, None, None, Tree.middleleft, new_root) #Set new left_subtree
            new_root.right=TreeItemType(Tree.key[2], Tree.value[2], Tree.middleright, None, None, Tree.right, new_root) #Set new right_subtree

            #Set new parents - Bij het aanmaken van een nieuw item kan het zijn dat de kind.parent relatie niet vernieuwd wordt, dit bouwt een zekerheid hiervoor in.
            if Tree.left!=None:
                Tree.left.parent=new_root.left
            if Tree.middleleft!=None:
                Tree.middleleft.parent=new_root.left
            if Tree.middleright != None:
                Tree.middleright.parent=new_root.right
            if Tree.right != None:
                Tree.right.parent=new_root.right
            parent = Tree.parent

            return [True,True,parent]

        #if not root; do all of the following (Opgesplits in de gevallen uit de cursus: Dia 112 & 113
        if self.keyCount(parent)==1: #split
            middle_key = Tree.key[1]
            middle_value=Tree.value[1]
            parent_key=parent.key[0]
            parent_value=parent.value[0]

            #Vergelijk keys
            if middle_key < parent_key: #if middle is linkerkind
                parent.key=[middle_key,None,parent_key]         #Set new parent keys
                parent.value=[middle_value,None,parent_value]   #Set new parent values
                #Dia 112a
                parent.left=TreeItemType(Tree.key[0], Tree.value[0], Tree.left, None, None, Tree.middleleft, parent) #TreeItemType(left key,left value,left tree ,middleleft tree, middleright tree, right tree parent)
                parent.middleleft=TreeItemType(Tree.key[2], Tree.value[2], Tree.middleright, None, None, Tree.right, parent)

                #Set new parents - Bij het aanmaken van een nieuw item kan het zijn dat de kind.parent relatie niet vernieuwd wordt, dit bouwt een zekerheid hiervoor in.
                if Tree.left != None:
                    Tree.left.parent = parent.left
                if Tree.middleleft != None:
                    Tree.middleleft.parent = parent.left
                if Tree.middleright != None:
                    Tree.middleright.parent = parent.middleleft
                if Tree.right != None:
                    Tree.right.parent = parent.middleleft
                parent = Tree.parent

                return [True,True,parent]

            elif middle_key > parent_key:  #if middle is rechterkind
                parent.key=[parent_key,None,middle_key]         #Set new parent keys
                parent.value=[parent_value,None,middle_value]   #Set new parent values
                #Dia 112b
                parent.middleleft=TreeItemType(Tree.key[0], Tree.value[0], Tree.left, None, None, Tree.middleleft, parent) #TreeItemType(left key,left value,left tree ,middleleft tree, middleright tree, right tree parent)
                parent.right=TreeItemType(Tree.key[2], Tree.value[2], Tree.right, None, None, Tree.middleright, parent)

                #Set new parents - Bij het aanmaken van een nieuw item kan het zijn dat de kind.parent relatie niet vernieuwd wordt, dit bouwt een zekerheid hiervoor in.
                if Tree.left != None:
                    Tree.left.parent = parent.middleleft
                if Tree.middleleft != None:
                    Tree.middleleft.parent = parent.middleleft
                if Tree.middleright != None:
                    Tree.middleright.parent = parent.right
                if Tree.right != None:
                    Tree.right.parent = parent.right
                parent = Tree.parent

                return [True,True,parent]

        elif self.keyCount(parent)==2:
            middle_key = Tree.key[1]
            middle_value=Tree.value[1]
            parent_keyL=parent.key[0]
            parent_keyR=parent.key[2]
            parent_valueL=parent.value[0]
            parent_valueR= parent.value[2]

            #Kijk of M links,middle of right child is           |           voorwaarde: format gehanteerd
            if middle_key<parent_keyL:                          #Place left: shift trees & values & keys right | Dia113a
                #Step 1: Keys
                parent.key=[middle_key,parent_keyL,parent_keyR]
                #Step 2: Values
                parent.value=[middle_value,parent_valueL,parent_valueR]
                #Step 3: Subtrees                               Parent Format: [Tree , e , None , f ]
                #Initalize
                f=parent.right
                e=parent.middleleft
                a=Tree.left
                b=Tree.middleleft
                c=Tree.middleright
                d=Tree.right
                #Set format
                parent.left=TreeItemType(Tree.key[0], Tree.value[0], a, None, None, b, parent)          #[S_key, S_value , a , None , None , b , parent]
                parent.middleleft=TreeItemType(Tree.key[2], Tree.value[2], c, None, None, d, parent)    #[L_key, L_value , c , None , None , d , parent]
                parent.middleright=e
                parent.right=f

                #Set new parents - Bij het aanmaken van een nieuw item kan het zijn dat de kind.parent relatie niet vernieuwd wordt, dit bouwt een zekerheid hiervoor in.
                if Tree.left != None:
                    Tree.left.parent = parent.left
                if Tree.middleleft != None:
                    Tree.middleleft.parent = parent.left
                if Tree.middleright != None:
                    Tree.middleright.parent = parent.middleleft
                if Tree.right != None:
                    Tree.right.parent = parent.middleleft
                parent = Tree.parent

                return [True,True,parent]

            elif parent_keyL<middle_key<parent_keyR: #Place middle: insert in mid           |           Dia113b
                #Step 1: Keys
                parent.key[1]=middle_key
                #Step 2: Values
                parent.value[1]=middle_value
                #Step 3: Subtrees
                #Initalize
                b=Tree.left
                c=Tree.middleleft
                d=Tree.middleright
                e=Tree.right
                #Set format
                parent.middleleft=TreeItemType(Tree.key[0], Tree.value[0], b, None, None, c, parent)
                parent.middleright=TreeItemType(Tree.key[2], Tree.value[2], d, None, None, e, parent)

                #Set new parents - Bij het aanmaken van een nieuw item kan het zijn dat de kind.parent relatie niet vernieuwd wordt, dit bouwt een zekerheid hiervoor in.
                if Tree.left != None:
                    Tree.left.parent = parent.middleleft
                if Tree.middleleft != None:
                    Tree.middleleft.parent = parent.middleleft
                if Tree.middleright != None:
                    Tree.middleright.parent = parent.middleright
                if Tree.right != None:
                    Tree.right.parent = parent.middleright
                parent = Tree.parent

                return [True,True,parent]

            elif middle_key>parent_keyR: #Place right: shift trees & values & keys left     |     Dia113c
                #Step 1: Keys
                parent.key=[parent_keyL,parent_keyR,middle_key]
                #Step 2: Values
                parent.value = [parent_valueL, parent_valueR, middle_value]
                #Step 3: Subtrees
                #Initalize
                a=parent.left
                b=parent.middleleft
                c=Tree.left
                d=Tree.middleleft
                e=Tree.middleright
                f=Tree.right
                #Set format
                parent.left=a
                parent.middleleft=b
                parent.middleright=TreeItemType(Tree.key[0], Tree.value[0], c, None, None, d, parent)
                parent.right=TreeItemType(Tree.key[2], Tree.value[2], e, None, None, f, parent)

                #Set new parents - Bij het aanmaken van een nieuw item kan het zijn dat de kind.parent relatie niet vernieuwd wordt, dit bouwt een zekerheid hiervoor in.
                if Tree.left != None:
                    Tree.left.parent = parent.middleright
                if Tree.middleleft != None:
                    Tree.middleleft.parent = parent.middleright
                if Tree.middleright != None:
                    Tree.middleright.parent = parent.right
                if Tree.right != None:
                    Tree.right.parent = parent.right
                parent = Tree.parent

                return [True,True,parent]

        elif self.keyCount(parent)==3: #Parent mag geen 4 knoop zijn
            return [False,"Error",None]

        else:
            return [False,"Error",None]

    def keyCount(self,Tree):
        """
        Hulpfunctie om het aantal keys van een node te bepalen (en dus +/- de soort knoop: 2-knoop: 1 item | 3-knoop: 2 keys | 4-knoop: 3 keys. Dit is een hulpfunctie en mag enkel intern worden opgeroepen.
        :parameter in ; 'Tree': TreeItemType
        :parameter out; 'count': Unsigned Integer
        Preconditie: Er is een 234T aangemaakt.
        Postconditie: Het aantal keys wordt meegegeven. De 234T blijft onveranderd. {query}
        """
        count=0
        if Tree==None:
            return count
        if Tree.key[1]!=None:
            count+=1
        if Tree.key[2]!=None:
            count+=1
        if Tree.key[0] != None:
            count+=1
        return count

    def subtree_count(self,Tree): #Geeft het aantal niet-lege deelbomen mee
        """
        Hulpfunctie om het aantal subtrees van een root te bepalen. Dit is een hulpfunctie en mag enkel intern worden opgeroepen.
        :parameter in ; 'Tree': TreeItemType
        :parameter out; 'count': Unsigned Integer
        Preconditie: Er is een 234T aangemaakt.
        Postconditie: Het aantal subtrees wordt meegegeven. De 234T blijft onveranderd. {query}
        """
        count=0
        if Tree.left!=None:
            count+=1
        if Tree.middleleft!=None:
            count +=1
        if Tree.middleright!=None:
            count+=1
        if Tree.right!=None:
            count+=1

        return count

    def retrieveItem(self,key,Tree=None):
        """
        Zoekt een 'key' in de 234T (Of specifiekere subtree hiervan) en geeft de waarde hiervan mee, indien gevonden. Er wordt extra (evt. debug- informatie meegegeven die intern wordt gebruikt bij andere operatie, hiermee maakt de retrieve zichzelf ook tot een hulpfunctie.
        :parameter in ; 'key', Getal & 'Tree': TreeItemType (Geïnitaliseerd op "None")
        :parameter out; Static Array ['value' , 'succes': bool , 'Tree': TreeItemType , 'positie": Integer: 0,1,2,3 , 'key']
        Preconditie: Er is een 234T aangemaakt.
        Postconditie: Indien de key in de 234T zit wordt deze meegeven en is de operatie geslaagd ('succes'=True). Indien de operatie niet geslaagd is, wordt er [False,False,False,False,False] mee gegeven. De 234T blijft onveranderd. {query}
        """
        if Tree==None:  #Initaliseer standaard-waarde (Vereist voor recursie)
            Tree=self.root

        if key==Tree.key[1] or key==Tree.key[0] or key==Tree.key[2]: #Als de key in de huidige node zit, return
            if key==Tree.key[0]:
                return (Tree.value[0], True, Tree,0 , Tree.key[0])
            elif key==Tree.key[1]:
                return (Tree.value[1], True , Tree,1 , Tree.key[1])
            elif key==Tree.key[2]:
                return (Tree.value[2], True, Tree,2 , Tree.key[2])

        a=self.keyCount(Tree)                                   #We splitsen op in gevallen afh. van het #keys

        if a==0:                                                #a bevat geen knopen; item niet gevonden
            return [False,False,False,False]

        elif a==1:                                              #Tree bevat 1 searchkey
            if key<Tree.key[0]:                                 #Indien kleiner
                if Tree.left!=None:                             #Zoek in linkerdeelboom, als die bestaat
                    return self.retrieveItem(key,Tree.left)
                else:                                           #Linkerdeelboom == None/Bestaat niet/is leeg
                    return [False,False,False,False,False]      #Anders; blad; key niet gevonden

            elif key>Tree.key[0]:
                if Tree.right!=None:
                    return self.retrieveItem(key, Tree.right)
                else: #Rechterdeelboom is leeg
                    return [False,False,False,False]            #Anders; blad; key niet gevonden

        elif a==2:
            if key < Tree.key[0]:                               # Indien kleiner dan kleinste item
                if Tree.left != None:                           # Zoek in linkerdeelboom, als die bestaat
                    return self.retrieveItem(key, Tree.left)
                else:                                           # Linkerdeelboom == None/Bestaat niet/is leeg
                    return [False,False,False,False]            # Anders; blad; key niet gevonden

            elif key > Tree.key[2]:                             #Indien groter dan grootste item
                if Tree.right != None:
                    return self.retrieveItem(key, Tree.right)
                else:                                           # Rechterdeelboom is leeg
                    return [False,False,False,False]            # Anders; blad; key niet gevonden

            elif Tree.key[0] < key < Tree.key[2]:               #key zit tussen de 2 waarden in
                if Tree.middleleft != None:
                    return self.retrieveItem(key,Tree.middleleft)
                else:                                           #Indien boom == Leeg
                    return [False,False,False,False]

        elif a==3:
            if key < Tree.key[0]:                               # Indien kleiner dan kleinste item
                if Tree.left != None:                           # Zoek in linkerdeelboom, als die bestaat
                    return self.retrieveItem(key, Tree.left)
                else:                                           # Linkerdeelboom == None/Bestaat niet/is leeg
                    return [False,False,False,False]            # Anders; blad; key niet gevonden

            elif key > Tree.key[2]:                             # Indien groter dan grootste item
                if Tree.right != None:
                    return self.retrieveItem(key, Tree.right)
                else:                                           # Rechterdeelboom is leeg
                    return [False,False,False,False]            # Anders; blad; key niet gevonden

            elif Tree.key[0] < key < Tree.key[1]:               # key zit tussen de 2 waarden in (left & middle)
                if Tree.middleleft != None:
                    return self.retrieveItem(key, Tree.middleleft)
                else:                                           # Indien boom == Leeg
                    return [False,False,False,False]

            elif Tree.key[1] < key < Tree.key[2]:               # key zit tussen de 2 waarden in (middle & right)
                if Tree.middleright != None:
                    return self.retrieveItem(key, Tree.middleright)
                else:                                           # Indien boom == Leeg
                    return [False,False,False,False]
        else:                                                   #Een node met meer dan 3 items bestaat niet!
            return [False,False,False,False]

    def inorderTraverse(self,FunctionType,Tree=None):
        """
        Doorloopt de 234T volgens het inordertravers-alogritme.
        :parameter in ; 'FunctionType': FunctionType. 'Tree': TreeItemType (Geïnitaliseerd op "None")
        :parameter out; FunctionType('key')
        Preconditie: Er is een 234T aangemaakt.
        Postconditie: De 234T is doorlopen en op elke 'key' is er een actie van het type 'FunctionType' uitgevoerd. Afhankelijk van de 'FunctionType' kan de 234T onverander blijven.
        """
        if self.isEmpty():
            return False                                                #Traverse niet mogelijk

        if (Tree==None):                                                #Initaliseer een standaardwaarde, indien "None"
            Tree = self.root

        a=self.keyCount(Tree)
        t=self.subtree_count(Tree)

        if t==0:                                                        #Geen subtrees
            if Tree.key[0]!=None:
                FunctionType(Tree.value[0])
            if Tree.key[1]!=None:
                FunctionType(Tree.value[1])
            if Tree.key[2]!=None:
                FunctionType(Tree.value[2])
            return

        if a==3:                                                        #3 keys & (en ook 4 Subtrees)
            if Tree.left!=None:
                self.inorderTraverse(FunctionType, Tree.left)           # Ga eerst helemaal naar links onder
            FunctionType(Tree.key[0])                                   #Print 1e root searchkey
            if Tree.middleleft!=None:
                self.inorderTraverse(FunctionType, Tree.middleleft)     #Ga naar middeleft tree
            FunctionType(Tree.key[1])                                   #Print 2e root searchkey
            if Tree.middleright!=None:
                self.inorderTraverse(FunctionType, Tree.middleright)    #Ga naar middleright tree
            FunctionType(Tree.key[2])                                   #Print 3e root searchkey
            if Tree.right!=None:
                self.inorderTraverse(FunctionType, Tree.right)          #Ga naar right tree
            return

        if a==2:                                                        #2 keys, 3 subtrees
            if Tree.left!=None:
                self.inorderTraverse(FunctionType, Tree.left)           # Ga eerst helemaal naar links onder
            FunctionType(Tree.key[0])                                   #Print 1e root searchkey
            if Tree.middleleft!=None:
                self.inorderTraverse(FunctionType, Tree.middleleft)     #Ga naar middeleft tree
            FunctionType(Tree.key[2])                                   #Print 2e root searchkey
            if Tree.right!=None:
                self.inorderTraverse(FunctionType, Tree.right)          #Ga naar right tree
            return

        if a==1:                                                        #Als er 1 key in de tree zit
            if (Tree.left != None):                                     #and (left[5]!=self.traversal):
                self.inorderTraverse(FunctionType,Tree.left)            #Ga eerst helemaal naar links onder
            FunctionType(Tree.key[0])                                   # Print 1e root searchkey
            if Tree.right!=None:
                self.inorderTraverse(FunctionType, Tree.right)          #Ga naar right tree
            return

        return False

    def save(self,Tree=None):
        """
        Exporteert de 234T naar een Python-map.
        :parameter in ; 'Tree': TreeItemType (Geïnitaliseerd op "None")
        :parameter out; 'dict': Python-map
        Preconditie: Er is een 234T aangemaakt.
        Postconditie: Er is een Python-map meegegeven volgens het format uit de opgave. De 234T blijgt onverandert. {query}
        """
        if self.isEmpty():                                  #Als de boom leeg is, is de map ook leeg
            return {'root': None}

        if Tree==None:
            Tree=self.root

        dict={}
        keys=[]
        a=self.keyCount(Tree)

        if Tree.key[0]!=None:
            keys.append(Tree.key[0])
        if Tree.key[1]!=None:
            keys.append(Tree.key[1])
        if Tree.key[2]!=None:
            keys.append(Tree.key[2])

        dict['root']=keys                                       #1e waarde is de zoeksleutel van de root

        if a==3:                                                #3 keys & (en ook 4 Subtrees)
            list=[]
            if (Tree.left != None):                             #Voeg linkerdeelboom toe aan children
                list.append(self.save(Tree.left))
            if Tree.middleleft!=None:
                list.append(self.save(Tree.middleleft))         #Voeg middleleft toe
            if Tree.middleleft!=None:
                list.append(self.save(Tree.middleright))        #Voeg middleright toe
            if Tree.right!=None:
                list.append(self.save(Tree.right))              #Voeg right toe
            if list!=[]:
                dict['children']=list
            return dict

        if a==2:                                                #2 keys, 3 subtrees
            list=[]
            if (Tree.left != None):                             #Voeg linkerdeelboom toe aan children
                list.append(self.save(Tree.left))
            if Tree.middleleft!=None:
                list.append(self.save(Tree.middleleft))         #Voeg middleleft toe
            if Tree.right!=None:
                list.append(self.save(Tree.right))              #Voeg right toe
            if list!=[]:
                dict['children']=list
            return dict

        if a==1:                                                #Als er 1 key in de tree zit
            list=[]
            if (Tree.left != None):
                list.append(self.save(Tree.left))               #Voeg linkerdeelboom toe aan children
            if Tree.right!=None:
                list.append(self.save(Tree.right))              #Voeg right toe
            if list!=[]:
                dict['children']=list
            return dict

    def load(self,dict,reset=True):
        """
        Laadt een Python-map in en voegt ieder element toe aan een nieuwe 234T.
        :parameter in ; 'dict': Python-map (Geformateerd volgens het format uit de opgave) , 'reset': Bool (Geïnitaliseerd op "True")
        :parameter out; /
        Preconditie: Er is een 234T aangemaakt. Er is een Python-map meegegeven volgens het format uit de opgave.
        Postconditie: Er wordt een volledige nieuwe 234T aangemaakt. Iedere key is toegevoegd met eenzelfde value als de key aan de nieuwe 234T volgens de algoritmen uit deze implementatie.
        """
        if reset==True:                         #Overschrijf current tree
            self.root=TreeItemType(None,None)

        for i in range(len(dict['root'])):      #Voeg iedere parent/root key toe (Insert)
            self.insertItem(createTreeItem(dict['root'][i],dict['root'][i]))

        if 'children' in dict.keys():           # Indien er kinderen zijn, insert deze:
            for i in range(len(dict['children'])):
                self.load(dict['children'][i],False)
        return True

    def deleteItem(self,key):
        """
        Verwijder een 'key' uit de 234T.
        :parameter in ; 'key': Getal
        :parameter out; 'succes': bool
        Preconditie: Er is een 234T aangemaakt.
        Postconditie: Indien de operatie geslaagd is; werd de 'key' verwijdert & de 234T eventueel geherstructureerd voordat de 'key' werd verwijdert. Indien de operatie niet slaagde, is de boom mogelijks geherstructureerd maar is de 'key' niet verwijdert uit de boom. (De 'key' bestaat bv. niet of er trad een fout op)
        """
        check1=self.retrieveItem(key)
        if check1[0]==False:                                        #Key not found
            return False

        z=self.search(key)                                          #Find key to delete + change nodes (redistribute, else merge)
        if z[1]==False:                                             #If 'key' not found; "Error"
            return False

        k=self.inorderSuccessor(key, z[2], z[3])                    #Find inordersuccessor
        if k==False:                                                #Geen inordersuccessor -> key zou in een blad moeten zitten
            z=self.retrieveItem(key)                                #Search again key (if tree has changed with redistribute/merge we might need another subtree)
            if z[1]==False:                                         #If 'key' not found; "Error"
                return False

            #Just remove key from tree
            z[2].key[z[3]]=None                                     #Key to delete wordt overschreven met "None"
            z[2].value[z[3]] = None                                 #Value too
            return True

        else:
            s=self.search(k)                                        #Find inorder successor again and now change nodes
            if s[1]==False:
                return False

            z=self.retrieveItem(key)                                #Research key (if tree has changed with redistribute, we might need another subtree
            if z[1]==False:
                return False

            #Alles oke: swap items & remove
            z[2].key[z[3]]=s[0]                                     #Key to delete wordt overschreven door inordersuccessor op exacte positie van key
            z[2].value[z[3]] = s[2].value[s[3]]                     #Value too (Is this going alright?)

            #Verwijder inordersuccessor uit oorspronkelijk blad
            position=s[3]
            if self.keyCount(s[2])==2:                              #Als inordersuccessor tree 2 keys heeft
                if position==0:                                     #Overschrijf 1e key & reformat
                    s[2].key[0] = s[2].key[2]
                    s[2].key[2] = None
                    s[2].value[0] = s[2].value[2]
                    s[2].value[2] = None
                    return True
                elif position==2:                                   #Overschrijf 2e key (rechter) & reformat
                    s[2].key[2]=None
                    s[2].value[2] = None
                    return True
            elif self.keyCount(s[2])==3:                            #Als inordersuccessor tree 3 keys heeft
                if position==0:                                     #Overschrijf 1e key & reformat
                    s[2].key[0] = s[2].key[1]
                    s[2].key[1] = None
                    s[2].value[0] = s[2].value[1]
                    s[2].value[1] = None
                    return True
                elif position==1:                                   #Overschrijf 2e key (midden) & reformat
                    s[2].key[1] = None
                    s[2].value[1] = None
                    return True
                elif position==2:                                   #Overschrijf 3e key (rechts) & reformat
                    s[2].key[2] = s[2].key[1]
                    s[2].key[1] = None
                    s[2].value[2] = s[2].value[1]
                    s[2].value[1] = None
                    return True

    def search(self,key,Tree=None):
        """
        Hulpfunctie waarin er gezocht wordt naar een 'key' terwijl 2-nodes zullen worden omgevormd. Dit is een hulpfunctie en mag enkel intern worden opgeroepen.
        :parameter in ; 'key': Getal , 'Tree': TreeItemType (Geïnitaliseerd op "None"; recursie mogelijk)
        :parameter out; Static Array ['key' , 'succes': bool , 'Tree': TreeItemType , 'position': 0,1,2 (Unsigned Integer) ]
        Preconditie: Er is een 234T aangemaakt.
        Postconditie: Iedere tegengekomen 2-node is omgevormd, indien mogelijk. De te zoeken key is meegegeven, indien deze in de boom zat. Als de operatie geslaagd is wordt er [False, False, False, False] meegegeven.
        """
        if Tree==None:                                              #Initaliseer standaard-waarde
            Tree=self.root

        a = self.keyCount(Tree)

        if ((a==1) and (Tree!=self.root)):                          #Tree bevat 1 searchkey  = 2-node

            check=self.redistribute(Tree)                           #First try redistribute

            if check[0]==False:
                check2=self.merge(key,Tree)
                if check2[0]==False:
                    return [False, False, False, False]
                else:
                    Tree=check2[1]                                  #Update tree
                    a = self.keyCount(Tree)                         #Update keycount

        if key==Tree.key[1] or key==Tree.key[0] or key==Tree.key[2]:#Key gevonden
            if key==Tree.key[0]:
                return [Tree.key[0], True, Tree, 0]
            elif key==Tree.key[1]:
                return [Tree.key[1], True , Tree, 1]
            elif key==Tree.key[2]:
                return [Tree.key[2], True, Tree, 2]

        if a==0:                                                    #a bevat geen knopen; item niet gevonden
            return [False,False,False,False]

        elif ((a==1) and (Tree==self.root)):
            if key < Tree.key[0]:                                   # Indien kleiner dan kleinste item
                if Tree.left != None:                               # Zoek in linkerdeelboom, als die bestaat
                    return self.search(key, Tree.left)
                else:                                               # Linkerdeelboom == None/Bestaat niet/is leeg
                    return [False,False,False,False]                # Anders; blad; key niet gevonden

            elif key > Tree.key[0]:                                 #Indien groter dan grootste item
                if Tree.right != None:
                    return self.search(key, Tree.right)
                else:                                               # Rechterdeelboom is leeg
                    return [False,False,False,False]                # Anders; blad; key niet gevonden


        elif a==2:
            if key < Tree.key[0]:                                   # Indien kleiner dan kleinste item
                if Tree.left != None:                               # Zoek in linkerdeelboom, als die bestaat
                    return self.search(key, Tree.left)
                else:                                               # Linkerdeelboom == None/Bestaat niet/is leeg
                    return [False,False,False,False]                # Anders; blad; key niet gevonden

            elif key > Tree.key[2]:                                 #Indien groter dan grootste item
                if Tree.right != None:
                    return self.search(key, Tree.right)
                else:                                               # Rechterdeelboom is leeg
                    return [False,False,False,False]                # Anders; blad; key niet gevonden

            elif Tree.key[0] < key < Tree.key[2]:                   #key zit tussen de 2 waarden in
                if Tree.middleleft != None:
                    return self.search(key,Tree.middleleft)
                else:                                               #Indien boom == Leeg
                    return [False,False,False,False]

        elif a==3:
            if key < Tree.key[0]:                                   # Indien kleiner dan kleinste item
                if Tree.left != None:                               # Zoek in linkerdeelboom, als die bestaat
                    return self.search(key, Tree.left)
                else:                                               # Linkerdeelboom == None/Bestaat niet/is leeg
                    return [False,False,False,False]                # Anders; blad; key niet gevonden

            elif key > Tree.key[2]:                                 # Indien groter dan grootste item
                if Tree.right != None:
                    return self.search(key, Tree.right)
                else:                                               # Rechterdeelboom is leeg
                    return [False,False,False,False]                # Anders; blad; key niet gevonden

            elif Tree.key[0] < key < Tree.key[1]:                   # key zit tussen de 2 waarden in (left & middle)
                if Tree.middleleft != None:
                    return self.search(key, Tree.middleleft)
                else:                                               # Indien boom == Leeg
                    return [False,False,False,False]

            elif Tree.key[1] < key < Tree.key[2]:                   # key zit tussen de 2 waarden in (middle & right)
                if Tree.middleright != None:
                    return self.search(key, Tree.middleright)
                else:                                               # Indien boom == Leeg
                    return [False,False,False,False]

        else:                                                       #Een node met meer dan 3 items bestaat niet!
            return [False,False,False,False]

    def redistribute(self,tree):
        """
        Hulpfunctie die de redistribute uitvoerd. Dit is een hulpfunctie en mag enkel intern worden opgeroepen.
        :parameter in ;'tree': TreeItemType
        :parameter out; Static Array ['succes': bool , 'position': 0,1,2,(Geeft aan op welke index van de key-array de key zit)'a': Aantal keys van de parent]
        Preconditie: Er is een 234T aangemaakt. Tree is een 2-node waarin een extra key moet komen. Tree heeft een parent die niet None is waarvan er een directe sibling bestaat van Tree waaruit een key kan worden geherdistribueert. (De functie controleert deze voorwaarde)
        Postconditie: Indien de operatie geslaagd is; is er een merge uitgevoerd volgens het algoritme uit de cursus. Indien de operatie gefaald is, wordt er False meegegeven.
        """
        #Preconditie: tree is een 2-node waarin een extra key moet komen
        #Voorwaarden checken: 1 subtree heeft 2 of 3 keys
        #Zie ook eigen notes voor illustraties
        parent = tree.parent #parent kan elke node zijn behalve root
        position = self.locate(parent,tree)
        a = self.keyCount(parent)
        if a == 1:
            if position==0: #Tree zit left
                if self.keyCount(parent.right)>1: #Als siblingbuurtje een key heeft om te swappen
                    if self.keyCount(parent.right)==2: #Maak een tekening per scenario om dit te begrijpen! (subtrees worden genummer van links naar rechts, resp. a - z)
                        """Edit keys & values"""
                        #Initaliaze sibling
                        sibling_key=parent.right.key[0]
                        sibling_value=parent.right.value[0]
                        #Shift sibling
                        parent.right.key[0]=parent.right.key[2]
                        parent.right.value[0]=parent.right.value[2]
                        parent.right.key[2]=None
                        parent.right.value[2]=None
                        #Initialize parent
                        parent_key=parent.key[0]
                        parent_value=parent.value[0]
                        #Edit parent
                        parent.key[0]=sibling_key
                        parent.value[0]=sibling_value
                        #Edit tree
                        tree.key[2]=parent_key
                        tree.value[2]=parent_value
                        """Edit subtrees"""
                        #Initalise subtrees
                        a=parent.left.left
                        b=parent.left.right
                        c=parent.right.left
                        d=parent.right.middleleft
                        e=parent.right.right
                        #Edit subtrees
                        parent.left.middleleft=b
                        parent.left.right=c
                        parent.right.left=d
                        parent.right.middleleft=None

                        # Set new parent link
                        if parent.left != None:
                            parent.left.parent = parent
                        if parent.middleleft != None:
                            parent.middleleft.parent = parent
                        if parent.middleright != None:
                            parent.middleright.parent = parent
                        if parent.right != None:
                            parent.right.parent = parent

                        return [True,position,a]

                    elif self.keyCount(parent.right)==3: #Maak een tekening per scenario om dit te begrijpen! (subtrees worden genummer van links naar rechts, resp. a - z)
                        """Edit keys & values"""
                        #Initaliaze sibling
                        sibling_key=parent.right.key[0]
                        sibling_value=parent.right.value[0]
                        #Shift sibling
                        parent.right.key[0]=parent.right.key[1]
                        parent.right.value[0]=parent.right.value[1]
                        parent.right.key[1]=None
                        parent.right.value[1]=None
                        #Initialize parent
                        parent_key=parent.key[0]
                        parent_value=parent.value[0]
                        #Edit parent
                        parent.key[0]=sibling_key
                        parent.value[0]=sibling_value
                        #Edit tree
                        tree.key[2]=parent_key
                        tree.value[2]=parent_value
                        """Edit subtrees"""
                        #Initalise subtrees
                        a=parent.left.left
                        b=parent.left.right
                        c=parent.right.left
                        d=parent.right.middleleft
                        e=parent.right.middleright
                        f=parent.right.right
                        #Edit subtrees
                        parent.left.middleleft=b
                        parent.left.right=c
                        parent.right.left=d
                        parent.right.middleleft=e
                        parent.middleright=None

                        # Set new parent link
                        if parent.left != None:
                            parent.left.parent = parent
                        if parent.middleleft != None:
                            parent.middleleft.parent = parent
                        if parent.middleright != None:
                            parent.middleright.parent = parent
                        if parent.right != None:
                            parent.right.parent = parent

                        return [True,position,a]

                return [False,position,a] #Else, return False: need merge

            elif position==3: #Tree zit right
                if self.keyCount(parent.left)>1: #Als siblingbuurtje een key heeft om te swappen
                    if self.keyCount(parent.left) == 2: #Maak een tekening per scenario om dit te begrijpen! (subtrees worden genummer van links naar rechts, resp. a - z)
                        """Edit keys & values"""
                        #Initaliaze sibling
                        sibling_key=parent.left.key[2]
                        sibling_value=parent.left.value[2]
                        #Shift sibling
                        parent.left.key[2]=None
                        parent.left.value[2]=None
                        #Initialize parent
                        parent_key=parent.key[0]
                        parent_value=parent.value[0]
                        #Edit parent
                        parent.key[0]=sibling_key
                        parent.value[0]=sibling_value
                        #Edit tree
                        tree_key=tree.key[0]
                        tree_value=tree.value[0]
                        tree.key[0]=parent_key
                        tree.value[0]=parent_value
                        tree.key[2]=tree_key
                        tree.value[2]=tree_value
                        """Edit subtrees"""
                        #Initalise subtrees
                        a=parent.left.left
                        b=parent.left.middleleft
                        c=parent.left.right
                        d=parent.right.left
                        e=parent.right.right
                        #Edit subtrees
                        parent.left.middleleft=None
                        parent.left.right=b
                        parent.right.left=c
                        parent.right.middleleft=d
                        parent.right.right=e

                        # Set new parent link
                        if parent.left != None:
                            parent.left.parent = parent
                        if parent.middleleft != None:
                            parent.middleleft.parent = parent
                        if parent.middleright != None:
                            parent.middleright.parent = parent
                        if parent.right != None:
                            parent.right.parent = parent

                        return [True,position,a]

                    elif self.keyCount(parent.left) == 3: #Maak een tekening per scenario om dit te begrijpen! (subtrees worden genummer van links naar rechts, resp. a - z)
                        """Edit keys & values"""
                        #Initaliaze sibling
                        sibling_key=parent.left.key[2]
                        sibling_value=parent.left.value[2]
                        #Shift sibling
                        parent.left.key[2]=parent.left.key[1]
                        parent.left.value[2]=parent.left.value[1]
                        parent.left.key[1]=None
                        parent.left.value[1]=None
                        #Initialize parent
                        parent_key=parent.key[0]
                        parent_value=parent.value[0]
                        #Edit parent
                        parent.key[0]=sibling_key
                        parent.value[0]=sibling_value
                        #Edit tree
                        tree.key[2]=tree.key[0]
                        tree.value[2]=tree.value[0]
                        tree.key[0]=parent_key
                        tree.value[0]=parent_value
                        """Edit subtrees"""
                        #Initalise subtrees
                        a=parent.left.left
                        b=parent.left.middleleft
                        c=parent.left.middleright
                        d=parent.left.right
                        e=parent.right.left
                        f=parent.right.right
                        #Edit subtrees
                        parent.left.middleright=None
                        parent.left.right=c
                        parent.right.left=d
                        parent.right.middleleft=e
                        parent.right.right=f

                        # Set new parent link
                        if parent.left != None:
                            parent.left.parent = parent
                        if parent.middleleft != None:
                            parent.middleleft.parent = parent
                        if parent.middleright != None:
                            parent.middleright.parent = parent
                        if parent.right != None:
                            parent.right.parent = parent

                        return [True,position,a]

                return [False,position,a] #Else, return False: need merge

        elif a == 2:
            if position==0: #Tree zit left
                if self.keyCount(parent.middleleft)>1: #Als siblingbuurtje een key heeft om te swappen
                    if self.keyCount(parent.middleleft) == 2: #Maak een tekening per scenario om dit te begrijpen! (subtrees worden genummer van links naar rechts, resp. a - z)
                        """Edit keys & values"""
                        #Initaliaze sibling
                        sibling_key=parent.middleleft.key[0]
                        sibling_value=parent.middleleft.value[0]
                        #Shift sibling
                        parent.middleleft.key[0]=parent.middleleft.key[2]
                        parent.middleleft.value[0]=parent.middleleft.value[2]
                        parent.middleleft.key[2]=None
                        parent.middleleft.value[2]=None
                        #Initialize parent
                        parent_key=parent.key[0]
                        parent_value=parent.value[0]
                        #Edit parent
                        parent.key[0]=sibling_key
                        parent.value[0]=sibling_value
                        #Edit tree
                        tree.key[2]=parent_key
                        tree.value[2]=parent_value
                        """Edit subtrees"""
                        #Initalise subtrees
                        a=parent.left.left
                        b=parent.left.right
                        c=parent.middleleft.left
                        d=parent.middleleft.middleleft
                        e=parent.middleleft.right
                        #Edit subtrees
                        parent.left.middleleft=b
                        parent.left.right=c
                        parent.middleleft.left=d
                        parent.middleleft.middleleft=None
                        parent.middleleft.right=e

                        # Set new parent link
                        if parent.left != None:
                            parent.left.parent = parent
                        if parent.middleleft != None:
                            parent.middleleft.parent = parent
                        if parent.middleright != None:
                            parent.middleright.parent = parent
                        if parent.right != None:
                            parent.right.parent = parent

                        return [True,position,a]

                    elif self.keyCount(parent.middleleft) == 3: #Maak een tekening per scenario om dit te begrijpen! (subtrees worden genummer van links naar rechts, resp. a - z)
                        """Edit keys & values"""
                        # Initaliaze sibling
                        sibling_key = parent.middleleft.key[0]
                        sibling_value = parent.middleleft.value[0]
                        # Shift sibling
                        parent.middleleft.key[0] = parent.middleleft.key[1]
                        parent.middleleft.value[0] = parent.middleleft.value[1]
                        parent.middleleft.key[1] = None
                        parent.middleleft.value[1] = None
                        # Initialize parent
                        parent_key = parent.key[0]
                        parent_value = parent.value[0]
                        # Edit parent
                        parent.key[0] = sibling_key
                        parent.value[0] = sibling_value
                        # Edit tree
                        tree.key[2] = parent_key
                        tree.value[2] = parent_value
                        """Edit subtrees"""
                        # Initalise subtrees
                        a = parent.left.left
                        b = parent.left.right
                        c = parent.middleleft.left
                        d = parent.middleleft.middleleft
                        e = parent.middleleft.middleright
                        f = parent.middleleft.right
                        # Edit subtrees
                        parent.left.middleleft = b
                        parent.left.right = c
                        parent.middleleft.left = d
                        parent.middleleft.middleleft = e
                        parent.middleleft.middleright = None
                        parent.middleleft.right = f

                        # Set new parent link
                        if parent.left != None:
                            parent.left.parent = parent
                        if parent.middleleft != None:
                            parent.middleleft.parent = parent
                        if parent.middleright != None:
                            parent.middleright.parent = parent
                        if parent.right != None:
                            parent.right.parent = parent

                        return [True, position, a]

                return [False,position,a] #Else, return False: need merge

            elif position==1: #Tree zit middleleft
                if self.keyCount(parent.left)>1: #Als siblingbuurtje een key heeft om te swappen
                    if self.keyCount(parent.left) == 2: #Maak een tekening per scenario om dit te begrijpen! (subtrees worden genummer van links naar rechts, resp. a - z)
                        """Edit keys & values"""
                        # Initaliaze sibling
                        sibling_key = parent.left.key[2]
                        sibling_value = parent.left.value[2]
                        # Shift sibling
                        parent.left.key[2] = None
                        parent.left.value[2] = None
                        # Initialize parent
                        parent_key = parent.key[0]
                        parent_value = parent.value[0]
                        # Edit parent
                        parent.key[0] = sibling_key
                        parent.value[0] = sibling_value
                        # Edit tree
                        tree.key[2] = tree.key[0]
                        tree.value[2] = tree.value[0]
                        tree.key[0]= parent_key
                        tree.value[0] = parent_value
                        """Edit subtrees"""
                        # Initalise subtrees
                        a = parent.left.left
                        b = parent.left.middleleft
                        c = parent.left.right
                        d = parent.middleleft.left
                        e = parent.middleleft.right
                        # Edit subtrees
                        parent.left.middleleft = None
                        parent.left.right = b
                        parent.middleleft.left = c
                        parent.middleleft.middleleft = d
                        parent.middleleft.right = e

                        # Set new parent link
                        if parent.left != None:
                            parent.left.parent = parent
                        if parent.middleleft != None:
                            parent.middleleft.parent = parent
                        if parent.middleright != None:
                            parent.middleright.parent = parent
                        if parent.right != None:
                            parent.right.parent = parent

                        return [True, position, a]

                    elif self.keyCount(parent.left) == 3: #Maak een tekening per scenario om dit te begrijpen! (subtrees worden genummer van links naar rechts, resp. a - z)
                        """Edit keys & values"""
                        # Initaliaze sibling
                        sibling_key = parent.left.key[2]
                        sibling_value = parent.left.value[2]
                        # Shift sibling
                        parent.left.key[2] = parent.left.key[1]
                        parent.left.value[2] = parent.left.value[1]
                        parent.left.key[1] = None
                        parent.left.value[1] = None
                        # Initialize parent
                        parent_key = parent.key[0]
                        parent_value = parent.value[0]
                        # Edit parent
                        parent.key[0] = sibling_key
                        parent.value[0] = sibling_value
                        # Edit tree
                        tree.key[2] = tree.key[0]
                        tree.value[2] = tree.value[0]
                        tree.key[0]=parent_key
                        tree.value[0] = parent_value
                        """Edit subtrees"""
                        # Initalise subtrees
                        a = parent.left.left
                        b = parent.left.middleleft
                        c = parent.left.middleright
                        d = parent.left.right
                        e = parent.middleleft.left
                        f = parent.middleleft.right
                        # Edit subtrees
                        parent.left.middleright = None
                        parent.left.right = c
                        parent.middleleft.left = d
                        parent.middleleft.middleleft = e
                        parent.middleleft.right = f

                        # Set new parent link
                        if parent.left != None:
                            parent.left.parent = parent
                        if parent.middleleft != None:
                            parent.middleleft.parent = parent
                        if parent.middleright != None:
                            parent.middleright.parent = parent
                        if parent.right != None:
                            parent.right.parent = parent

                        return [True, position, a]

                elif self.keyCount(parent.right)>1:
                    if self.keyCount(parent.right) == 2: #Maak een tekening per scenario om dit te begrijpen! (subtrees worden genummer van links naar rechts, resp. a - z)
                        """Edit keys & values"""
                        # Initaliaze sibling
                        sibling_key = parent.right.key[0]
                        sibling_value = parent.right.value[0]
                        # Shift sibling
                        parent.right.key[0] = parent.right.key[2]
                        parent.right.value[0] = parent.right.value[2]
                        parent.right.key[2] = None
                        parent.right.value[2] = None
                        # Initialize parent
                        parent_key = parent.key[2]
                        parent_value = parent.value[2]
                        # Edit parent
                        parent.key[2] = sibling_key
                        parent.value[2] = sibling_value
                        # Edit tree
                        tree.key[2]=parent_key
                        tree.value[2] = parent_value
                        """Edit subtrees"""
                        # Initalise subtrees
                        a = parent.middleleft.left
                        b = parent.middleleft.right
                        c = parent.right.left
                        d = parent.right.middleleft
                        e = parent.right.right
                        # Edit subtrees
                        parent.middleleft.middleleft= b
                        parent.middleleft.right = c
                        parent.right.left = d
                        parent.right.middleleft = None
                        parent.right.right = e

                        # Set new parent link
                        if parent.left != None:
                            parent.left.parent = parent
                        if parent.middleleft != None:
                            parent.middleleft.parent = parent
                        if parent.middleright != None:
                            parent.middleright.parent = parent
                        if parent.right != None:
                            parent.right.parent = parent

                        return [True, position, a]

                    elif self.keyCount(parent.right) == 3: #Maak een tekening per scenario om dit te begrijpen! (subtrees worden genummer van links naar rechts, resp. a - z)
                        """Edit keys & values"""
                        # Initaliaze sibling
                        sibling_key = parent.right.key[0]
                        sibling_value = parent.right.value[0]
                        # Shift sibling
                        parent.right.key[0] = parent.right.key[1]
                        parent.right.value[0] = parent.right.value[1]
                        parent.right.key[1] = None
                        parent.right.value[1] = None
                        # Initialize parent
                        parent_key = parent.key[2]
                        parent_value = parent.value[2]
                        # Edit parent
                        parent.key[2] = sibling_key
                        parent.value[2] = sibling_value
                        # Edit tree
                        tree.key[2]=parent_key
                        tree.value[2] = parent_value
                        """Edit subtrees"""
                        # Initalise subtrees
                        a = parent.middleleft.left
                        b = parent.middleleft.right
                        c = parent.right.left
                        d = parent.right.middleleft
                        e = parent.right.middleright
                        f = parent.right.right
                        # Edit subtrees
                        parent.middleleft.middleleft= b
                        parent.middleleft.right = c
                        parent.right.left = d
                        parent.right.middleleft = e
                        parent.right.middleright = None
                        parent.right.right = f

                        # Set new parent link
                        if parent.left != None:
                            parent.left.parent = parent
                        if parent.middleleft != None:
                            parent.middleleft.parent = parent
                        if parent.middleright != None:
                            parent.middleright.parent = parent
                        if parent.right != None:
                            parent.right.parent = parent

                        return [True, position, a]

                return [False,position,a] #Else, return False: need merge

            elif position==3: #Tree zit right
                if self.keyCount(parent.middleleft)>1: #Als siblingbuurtje een key heeft om te swappen
                    if self.keyCount(parent.middleleft) == 2:  # Maak een tekening per scenario om dit te begrijpen! (subtrees worden genummer van links naar rechts, resp. a - z)
                        """Edit keys & values"""
                        # Initaliaze sibling
                        sibling_key = parent.middleleft.key[2]
                        sibling_value = parent.middleleft.value[2]
                        # Shift sibling
                        parent.middleleft.key[2] = None
                        parent.middleleft.value[2] = None
                        # Initialize parent
                        parent_key = parent.key[2]
                        parent_value = parent.value[2]
                        # Edit parent
                        parent.key[2] = sibling_key
                        parent.value[2] = sibling_value
                        # Edit tree
                        tree.key[2]=tree.key[0]
                        tree.value[2] = tree.value[0]
                        tree.key[0]=parent_key
                        tree.value[0] = parent_value
                        """Edit subtrees"""
                        # Initalise subtrees
                        a = parent.middleleft.left
                        b = parent.middleleft.middleleft
                        c = parent.middleleft.right
                        d = parent.right.left
                        e = parent.right.right
                        # Edit subtrees
                        parent.middleleft.middleleft= None
                        parent.middleleft.right = b
                        parent.right.left = c
                        parent.right.middleleft = d
                        parent.right.right = e

                        # Set new parent link
                        if parent.left != None:
                            parent.left.parent = parent
                        if parent.middleleft != None:
                            parent.middleleft.parent = parent
                        if parent.middleright != None:
                            parent.middleright.parent = parent
                        if parent.right != None:
                            parent.right.parent = parent

                        return [True, position, a]

                    elif self.keyCount(parent.middleleft) == 3:  # Maak een tekening per scenario om dit te begrijpen! (subtrees worden genummer van links naar rechts, resp. a - z)
                        """Edit keys & values"""
                        # Initaliaze sibling
                        sibling_key = parent.middleleft.key[2]
                        sibling_value = parent.middleleft.value[2]
                        # Shift sibling
                        parent.middleleft.key[2] = parent.middleleft.key[1]
                        parent.middleleft.value[2] = parent.middleleft.value[1]
                        parent.middleleft.key[1] = None
                        parent.middleleft.value[1] = None
                        # Initialize parent
                        parent_key = parent.key[2]
                        parent_value = parent.value[2]
                        # Edit parent
                        parent.key[2] = sibling_key
                        parent.value[2] = sibling_value
                        # Edit tree
                        tree.key[2]=tree.key[0]
                        tree.value[2] = tree.value[0]
                        tree.key[0]=parent_key
                        tree.value[0] = parent_value
                        """Edit subtrees"""
                        # Initalise subtrees
                        a = parent.middleleft.left
                        b = parent.middleleft.middleleft
                        c = parent.middleleft.middleright
                        d = parent.middleleft.right
                        e = parent.right.left
                        f = parent.right.right
                        # Edit subtrees
                        parent.middleleft.middleright= None
                        parent.middleleft.right = c
                        parent.right.left = d
                        parent.right.middleleft = e
                        parent.right.right = f

                        # Set new parent link
                        if parent.left != None:
                            parent.left.parent = parent
                        if parent.middleleft != None:
                            parent.middleleft.parent = parent
                        if parent.middleright != None:
                            parent.middleright.parent = parent
                        if parent.right != None:
                            parent.right.parent = parent

                        return [True, position, a]

                return [False,position,a] #Else, return False: need merge

        elif a == 3:

            if position == 0:  # Tree zit left
                if self.keyCount(parent.middleleft) > 1:  # Als siblingbuurtje een key heeft om te swappen
                    if self.keyCount(parent.middleleft) == 2: #Maak een tekening per scenario om dit te begrijpen! (subtrees worden genummer van links naar rechts, resp. a - z)
                        """Edit keys & values"""
                        #Initaliaze sibling
                        sibling_key=parent.middleleft.key[0]
                        sibling_value=parent.middleleft.value[0]
                        #Shift sibling
                        parent.middleleft.key[0]=parent.middleleft.key[2]
                        parent.middleleft.value[0]=parent.middleleft.value[2]
                        parent.middleleft.key[2]=None
                        parent.middleleft.value[2]=None
                        #Initialize parent
                        parent_key=parent.key[0]
                        parent_value=parent.value[0]
                        #Edit parent
                        parent.key[0]=sibling_key
                        parent.value[0]=sibling_value
                        #Edit tree
                        tree.key[2]=parent_key
                        tree.value[2]=parent_value
                        """Edit subtrees"""
                        #Initalise subtrees
                        a=parent.left.left
                        b=parent.left.right
                        c=parent.middleleft.left
                        d=parent.middleleft.middleleft
                        e=parent.middleleft.right
                        #Edit subtrees
                        parent.left.middleleft=b
                        parent.left.right=c
                        parent.middleleft.left=d
                        parent.middleleft.middleleft=None
                        parent.middleleft.right=e

                        # Set new parent link
                        if parent.left != None:
                            parent.left.parent = parent
                        if parent.middleleft != None:
                            parent.middleleft.parent = parent
                        if parent.middleright != None:
                            parent.middleright.parent = parent
                        if parent.right != None:
                            parent.right.parent = parent

                        return [True,position,a]

                    elif self.keyCount(parent.middleleft) == 3:  # Maak een tekening per scenario om dit te begrijpen! (subtrees worden genummer van links naar rechts, resp. a - z)
                        """Edit keys & values"""
                        #Initaliaze sibling
                        sibling_key=parent.middleleft.key[0]
                        sibling_value=parent.middleleft.value[0]
                        #Shift sibling
                        parent.middleleft.key[0]=parent.middleleft.key[1]
                        parent.middleleft.value[0]=parent.middleleft.value[1]
                        parent.middleleft.key[1]=None
                        parent.middleleft.value[1]=None
                        #Initialize parent
                        parent_key=parent.key[0]
                        parent_value=parent.value[0]
                        #Edit parent
                        parent.key[0]=sibling_key
                        parent.value[0]=sibling_value
                        #Edit tree
                        tree.key[2]=parent_key
                        tree.value[2]=parent_value
                        """Edit subtrees"""
                        #Initalise subtrees
                        a=parent.left.left
                        b=parent.left.right
                        c=parent.middleleft.left
                        d=parent.middleleft.middleleft
                        e=parent.middleleft.middleright
                        f=parent.middleleft.right
                        #Edit subtrees
                        parent.left.middleleft=b
                        parent.left.right=c
                        parent.middleleft.left=d
                        parent.middleleft.middleleft=e
                        parent.middleleft.middleright=None

                        # Set new parent link
                        if parent.left != None:
                            parent.left.parent = parent
                        if parent.middleleft != None:
                            parent.middleleft.parent = parent
                        if parent.middleright != None:
                            parent.middleright.parent = parent
                        if parent.right != None:
                            parent.right.parent = parent

                        return [True,position,a]

                return [False, position, a]  # Else, return False: need merge

            elif position == 1:  # Tree zit middleleft
                if self.keyCount(parent.left) > 1:  # Als siblingbuurtje een key heeft om te swappen
                    if self.keyCount(parent.left) == 2: #Maak een tekening per scenario om dit te begrijpen! (subtrees worden genummer van links naar rechts, resp. a - z)
                        """Edit keys & values"""
                        #Initaliaze sibling
                        sibling_key=parent.left.key[2]
                        sibling_value=parent.left.value[2]
                        #Shift sibling
                        parent.left.key[2]=None
                        parent.left.value[2]=None
                        #Initialize parent
                        parent_key=parent.key[0]
                        parent_value=parent.value[0]
                        #Edit parent
                        parent.key[0]=sibling_key
                        parent.value[0]=sibling_value
                        #Edit tree
                        tree.key[2]=tree.key[0]
                        tree.value[2]=tree.value[0]
                        tree.key[0]=parent_key
                        tree.value[0]=parent_value
                        """Edit subtrees"""
                        #Initalise subtrees
                        a=parent.left.left
                        b=parent.left.middleleft
                        c=parent.left.right
                        d=parent.middleleft.left
                        e=parent.middleleft.right
                        #Edit subtrees
                        parent.left.middleleft=None
                        parent.left.right=b
                        parent.middleleft.left=c
                        parent.middleleft.middleleft=d
                        parent.middleleft.right=e

                        # Set new parent link
                        if parent.left != None:
                            parent.left.parent = parent
                        if parent.middleleft != None:
                            parent.middleleft.parent = parent
                        if parent.middleright != None:
                            parent.middleright.parent = parent
                        if parent.right != None:
                            parent.right.parent = parent

                        return [True,position,a]

                    elif self.keyCount(parent.left) == 3:  # Maak een tekening per scenario om dit te begrijpen! (subtrees worden genummer van links naar rechts, resp. a - z)
                        """Edit keys & values"""
                        #Initaliaze sibling
                        sibling_key=parent.left.key[2]
                        sibling_value=parent.left.value[2]
                        #Shift sibling
                        parent.left.key[2]=parent.left.key[1]
                        parent.left.value[2]=parent.left.value[1]
                        parent.left.key[1]=None
                        parent.left.value[1]=None
                        #Initialize parent
                        parent_key=parent.key[0]
                        parent_value=parent.value[0]
                        #Edit parent
                        parent.key[0]=sibling_key
                        parent.value[0]=sibling_value
                        #Edit tree
                        tree.key[2]=tree.key[0]
                        tree.value[2]=tree.value[0]
                        tree.key[0]=parent_key
                        tree.value[0]=parent_value
                        """Edit subtrees"""
                        #Initalise subtrees
                        a=parent.left.left
                        b=parent.left.middleleft
                        c=parent.left.middleright
                        d=parent.left.right
                        e=parent.middleleft.left
                        f=parent.middleleft.right
                        #Edit subtrees
                        parent.left.middleright=None
                        parent.left.right=c
                        parent.middleleft.left=d
                        parent.middleleft.middleleft=e
                        parent.middleleft.right=f

                        # Set new parent link
                        if parent.left != None:
                            parent.left.parent = parent
                        if parent.middleleft != None:
                            parent.middleleft.parent = parent
                        if parent.middleright != None:
                            parent.middleright.parent = parent
                        if parent.right != None:
                            parent.right.parent = parent

                        return [True,position,a]

                elif self.keyCount(parent.middleright) > 1:
                    if self.keyCount(parent.middleright) == 2: #Maak een tekening per scenario om dit te begrijpen! (subtrees worden genummer van links naar rechts, resp. a - z)
                        """Edit keys & values"""
                        #Initaliaze sibling
                        sibling_key=parent.middleright.key[0]
                        sibling_value=parent.middleright.value[0]
                        #Shift sibling
                        parent.middleright.key[0]=parent.middleright.key[2]
                        parent.middleright.value[0]=parent.middleright.value[2]
                        parent.middleright.key[2]=None
                        parent.middleright.value[2]=None
                        #Initialize parent
                        parent_key=parent.key[1]
                        parent_value=parent.value[1]
                        #Edit parent
                        parent.key[1]=sibling_key
                        parent.value[1]=sibling_value
                        #Edit tree
                        tree.key[2]=parent_key
                        tree.value[2]=parent_value
                        """Edit subtrees"""
                        #Initalise subtrees
                        a=parent.middleleft.left
                        b=parent.middleleft.right
                        c=parent.middleright.left
                        d=parent.middleright.middleleft
                        e=parent.middleright.right
                        #Edit subtrees
                        parent.middleleft.middleleft=b
                        parent.middleleft.right=c
                        parent.middleright.left=d
                        parent.middleright.right=e

                        # Set new parent link
                        if parent.left != None:
                            parent.left.parent = parent
                        if parent.middleleft != None:
                            parent.middleleft.parent = parent
                        if parent.middleright != None:
                            parent.middleright.parent = parent
                        if parent.right != None:
                            parent.right.parent = parent

                        return [True,position,a]

                    elif self.keyCount(parent.middleright) == 3:  # Maak een tekening per scenario om dit te begrijpen! (subtrees worden genummer van links naar rechts, resp. a - z)
                        """Edit keys & values"""
                        #Initaliaze sibling
                        sibling_key=parent.middleright.key[0]
                        sibling_value=parent.middleright.value[0]
                        #Shift sibling
                        parent.middleright.key[0]=parent.middleright.key[1]
                        parent.middleright.value[0]=parent.middleright.value[1]
                        parent.middleright.key[1]=None
                        parent.middleright.value[1]=None
                        #Initialize parent
                        parent_key=parent.key[1]
                        parent_value=parent.value[1]
                        #Edit parent
                        parent.key[1]=sibling_key
                        parent.value[1]=sibling_value
                        #Edit tree
                        tree.key[2]=parent_key
                        tree.value[2]=parent_value
                        """Edit subtrees"""
                        #Initalise subtrees
                        a=parent.middleleft.left
                        b=parent.middleleft.right
                        c=parent.middleright.left
                        d=parent.middleright.middleleft
                        e=parent.middleright.middleright
                        f=parent.middleright.right
                        #Edit subtrees
                        parent.middleleft.middleleft=b
                        parent.middleleft.right=c
                        parent.middleright.left=d
                        parent.middleright.middleleft=e
                        parent.middleright.middleright= None

                        # Set new parent link
                        if parent.left != None:
                            parent.left.parent = parent
                        if parent.middleleft != None:
                            parent.middleleft.parent = parent
                        if parent.middleright != None:
                            parent.middleright.parent = parent
                        if parent.right != None:
                            parent.right.parent = parent

                        return [True,position,a]

                return [False, position, a]  # Else, return False: need merge

            elif position == 2:  # Tree zit middleright
                if self.keyCount(parent.middleleft) > 1:  # Als siblingbuurtje een key heeft om te swappen
                    if self.keyCount(parent.middleleft) == 2: #Maak een tekening per scenario om dit te begrijpen! (subtrees worden genummer van links naar rechts, resp. a - z)
                        """Edit keys & values"""
                        #Initaliaze sibling
                        sibling_key=parent.middleleft.key[2]
                        sibling_value=parent.middleleft.value[2]
                        #Shift sibling
                        parent.middleleft.key[2]=None
                        parent.middleleft.value[2]=None
                        #Initialize parent
                        parent_key=parent.key[1]
                        parent_value=parent.value[1]
                        #Edit parent
                        parent.key[1]=sibling_key
                        parent.value[1]=sibling_value
                        #Edit tree
                        tree.key[2]=tree.key[0]
                        tree.value[2]=tree.value[0]
                        tree.key[0]=parent_key
                        tree.value[0]=parent_value
                        """Edit subtrees"""
                        #Initalise subtrees
                        a=parent.middleleft.left
                        b=parent.middleleft.middleleft
                        c=parent.middleleft.right
                        d=parent.middleright.left
                        e=parent.middleright.right
                        #Edit subtrees
                        parent.middleleft.middleleft=None
                        parent.middleleft.right=b
                        parent.middleright.left=c
                        parent.middleright.middleleft=d
                        parent.middleright.right= e

                        # Set new parent link
                        if parent.left != None:
                            parent.left.parent = parent
                        if parent.middleleft != None:
                            parent.middleleft.parent = parent
                        if parent.middleright != None:
                            parent.middleright.parent = parent
                        if parent.right != None:
                            parent.right.parent = parent

                        return [True,position,a]

                    elif self.keyCount(parent.middleleft) == 3:  # Maak een tekening per scenario om dit te begrijpen! (subtrees worden genummer van links naar rechts, resp. a - z)
                        """Edit keys & values"""
                        #Initaliaze sibling
                        sibling_key=parent.middleleft.key[2]
                        sibling_value=parent.middleleft.value[2]
                        #Shift sibling
                        parent.middleleft.key[2]=parent.middleleft.key[1]
                        parent.middleleft.value[2]=parent.middleleft.value[1]
                        parent.middleleft.key[1]=None
                        parent.middleleft.value[1]=None
                        #Initialize parent
                        parent_key=parent.key[1]
                        parent_value=parent.value[1]
                        #Edit parent
                        parent.key[1]=sibling_key
                        parent.value[1]=sibling_value
                        #Edit tree
                        tree.key[2]=tree.key[0]
                        tree.value[2]=tree.value[0]
                        tree.key[0]=parent_key
                        tree.value[0]=parent_value
                        """Edit subtrees"""
                        #Initalise subtrees
                        a=parent.middleleft.left
                        b=parent.middleleft.middleleft
                        c=parent.middleleft.middleright
                        d=parent.middleleft.right
                        e=parent.middleright.left
                        f=parent.middleright.right
                        #Edit subtrees
                        parent.middleleft.middleright=None
                        parent.middleleft.right=c
                        parent.middleright.left=d
                        parent.middleright.middleleft=e
                        parent.middleright.right= f

                        # Set new parent link
                        if parent.left != None:
                            parent.left.parent = parent
                        if parent.middleleft != None:
                            parent.middleleft.parent = parent
                        if parent.middleright != None:
                            parent.middleright.parent = parent
                        if parent.right != None:
                            parent.right.parent = parent

                        return [True,position,a]

                elif self.keyCount(parent.right) > 1:
                    if self.keyCount(parent.right) == 2: #Maak een tekening per scenario om dit te begrijpen! (subtrees worden genummer van links naar rechts, resp. a - z)
                        """Edit keys & values"""
                        #Initaliaze sibling
                        sibling_key=parent.right.key[0]
                        sibling_value=parent.right.value[0]
                        #Shift sibling
                        parent.right.key[0]=parent.right.key[2]
                        parent.right.value[0]=parent.right.value[2]
                        parent.right.key[2]=None
                        parent.right.value[2]=None
                        #Initialize parent
                        parent_key=parent.key[2]
                        parent_value=parent.value[2]
                        #Edit parent
                        parent.key[2]=sibling_key
                        parent.value[2]=sibling_value
                        #Edit tree
                        tree.key[2]=parent_key
                        tree.value[2]=parent_value
                        """Edit subtrees"""
                        #Initalise subtrees
                        a=parent.middleright.left
                        b=parent.middleright.right
                        c=parent.right.left
                        d=parent.right.middleleft
                        e=parent.right.right
                        #Edit subtrees
                        parent.middleright.middleleft=b
                        parent.middleright.right=c
                        parent.right.left=d
                        parent.right.middleleft=None
                        parent.right.right= e

                        # Set new parent link
                        if parent.left != None:
                            parent.left.parent = parent
                        if parent.middleleft != None:
                            parent.middleleft.parent = parent
                        if parent.middleright != None:
                            parent.middleright.parent = parent
                        if parent.right != None:
                            parent.right.parent = parent

                        return [True,position,a]

                    elif self.keyCount(parent.right) == 3:  # Maak een tekening per scenario om dit te begrijpen! (subtrees worden genummer van links naar rechts, resp. a - z)
                        """Edit keys & values"""
                        #Initaliaze sibling
                        sibling_key=parent.right.key[0]
                        sibling_value=parent.right.value[0]
                        #Shift sibling
                        parent.right.key[0]=parent.right.key[1]
                        parent.right.value[0]=parent.right.value[1]
                        parent.right.key[1]=None
                        parent.right.value[1]=None
                        #Initialize parent
                        parent_key=parent.key[2]
                        parent_value=parent.value[2]
                        #Edit parent
                        parent.key[2]=sibling_key
                        parent.value[2]=sibling_value
                        #Edit tree
                        tree.key[2]=parent_key
                        tree.value[2]=parent_value
                        """Edit subtrees"""
                        #Initalise subtrees
                        a=parent.middleright.left
                        b=parent.middleright.right
                        c=parent.right.left
                        d=parent.right.middleleft
                        e=parent.right.middleright
                        f=parent.right.right
                        #Edit subtrees
                        parent.middleright.middleleft=b
                        parent.middleright.right=c
                        parent.right.left=d
                        parent.right.middleleft=e
                        parent.right.middleright=None
                        parent.right.right= f

                        # Set new parent link
                        if parent.left != None:
                            parent.left.parent = parent
                        if parent.middleleft != None:
                            parent.middleleft.parent = parent
                        if parent.middleright != None:
                            parent.middleright.parent = parent
                        if parent.right != None:
                            parent.right.parent = parent

                        return [True,position,a]

                return [False, position, a]  # Else, return False: need merge

            elif position == 3:  # Tree zit right
                if self.keyCount(parent.middleright) > 1:  # Als siblingbuurtje een key heeft om te swappen
                    if self.keyCount(parent.middleright) == 2: #Maak een tekening per scenario om dit te begrijpen! (subtrees worden genummer van links naar rechts, resp. a - z)
                        """Edit keys & values"""
                        #Initaliaze sibling
                        sibling_key=parent.middleright.key[2]
                        sibling_value=parent.middleright.value[2]
                        #Shift sibling
                        parent.middleright.key[2]=None
                        parent.middleright.value[2]=None
                        #Initialize parent
                        parent_key=parent.key[2]
                        parent_value=parent.value[2]
                        #Edit parent
                        parent.key[2]=sibling_key
                        parent.value[2]=sibling_value
                        #Edit tree
                        tree.key[2]=tree.key[0]
                        tree.value[2]=tree.value[0]
                        tree.key[0]=parent_key
                        tree.value[0]=parent_value
                        """Edit subtrees"""
                        #Initalise subtrees
                        a=parent.middleright.left
                        b=parent.middleright.middleleft
                        c=parent.middleright.right
                        d=parent.right.left
                        e=parent.right.right
                        #Edit subtrees
                        parent.middleright.middleleft=None
                        parent.middleright.right=b
                        parent.right.left=c
                        parent.right.middleleft=d
                        parent.right.right= e

                        # Set new parent link
                        if parent.left != None:
                            parent.left.parent = parent
                        if parent.middleleft != None:
                            parent.middleleft.parent = parent
                        if parent.middleright != None:
                            parent.middleright.parent = parent
                        if parent.right != None:
                            parent.right.parent = parent

                        return [True,position,a]

                    elif self.keyCount(parent.middleright) == 3:  # Maak een tekening per scenario om dit te begrijpen! (subtrees worden genummer van links naar rechts, resp. a - z)
                        """Edit keys & values"""
                        #Initaliaze sibling
                        sibling_key=parent.middleright.key[2]
                        sibling_value=parent.middleright.value[2]
                        #Shift sibling
                        parent.middleright.key[2]=parent.middleright.key[1]
                        parent.middleright.value[2]=parent.middleright.value[1]
                        parent.middleright.key[1]=None
                        parent.middleright.value[1]=None
                        #Initialize parent
                        parent_key=parent.key[2]
                        parent_value=parent.value[2]
                        #Edit parent
                        parent.key[2]=sibling_key
                        parent.value[2]=sibling_value
                        #Edit tree
                        tree.key[2]=tree.key[0]
                        tree.value[2]=tree.value[0]
                        tree.key[0]=parent_key
                        tree.value[0]=parent_value
                        """Edit subtrees"""
                        #Initalise subtrees
                        a=parent.middleright.left
                        b=parent.middleright.middleleft
                        c=parent.middleright.middleright
                        d=parent.middleright.right
                        e=parent.right.left
                        f=parent.right.right
                        #Edit subtrees
                        parent.middleright.middleright=None
                        parent.middleright.right=c
                        parent.right.left=d
                        parent.right.middleleft=e
                        parent.right.right= f

                        # Set new parent link
                        if parent.left != None:
                            parent.left.parent = parent
                        if parent.middleleft != None:
                            parent.middleleft.parent = parent
                        if parent.middleright != None:
                            parent.middleright.parent = parent
                        if parent.right != None:
                            parent.right.parent = parent

                        return [True,position,a]

                return [False, position, a]  # Else, return False: need merge

        else:
            return [False, position, a]

    def merge(self,key,Tree): # (zoals Dia116-118 cursus)
        """
        Hulpfunctie die een Tree merged. Dit is een hulpfunctie en mag enkel intern worden opgeroepen.
        :parameter in ; 'key': Getal , 'tree': TreeItemType
        :parameter out; Static Array ['succes': bool, TreeItemType]
        Preconditie: Er is een 234T aangemaakt. tree is een 2-node.
        Postconditie: Indien de operatie geslaagd is; is er een merge uitgevoerd volgens het algoritme uit de cursus. Indien de operatie gefaald is, wordt er [False, False] meegegeven.
        """
        if Tree==self.root:                                                                             #Root blijft onaangetast bij merge
            return [True,"root"]

        parent=Tree.parent
        k=self.subtree_count(parent)
        x=self.subtree_count(Tree)

        if k==4:                                                                                        #Parent is 4-node | Dia118
            #Zitten de trees links, midden of rechts?
            if key<parent.key[1]:                                                                       #Links & Middeleft | Dia118a
                # Initalise keys & values
                M = parent.key[0]
                m = parent.value[0]
                S = parent.left.key[0]
                s = parent.left.value[0]
                L = parent.middleleft.key[0]
                l = parent.middleleft.value[0]
                if self.subtree_count(parent.left)!=2 and self.subtree_count(parent.middleleft)!=2:     #Als de trees geen 2-nodes zijn (kun je dus ook niet mergen)
                    return [False, False]
                # Initalize trees
                a = parent.left.left
                b = parent.left.right
                c = parent.middleleft.left
                d = parent.middleleft.right
                # 1: Merge Keys, Values, Subtrees
                parent.key[0] = parent.key[1]                                                           #Shift middle key & value to left position
                parent.key[1] = None
                parent.value[0] = parent.value[1]
                parent.value[1] = None

                parent.left = TreeItemType(M, m, a, b, c, d, parent)
                parent.middleleft = parent.middleright                                                  #Reset format
                parent.middleright = None                                                               #Reset format // Houdt format consistent
                parent.left.key = [S, M, L]
                parent.left.value = [s, m, l]

                #Set new parent link
                if parent.left != None:
                    parent.left.parent = parent
                if parent.middleleft != None:
                    parent.middleleft.parent = parent
                if parent.middleright != None:
                        parent.middleright.parent = parent
                if parent.right != None:
                    parent.right.parent = parent

                return [True, parent.left]

            elif parent.key[0]<key<parent.key[2]:                                                       #Tussen links&  rechts in: middleleft & middleright | Dia118b
                # Initalise keys & values
                M = parent.key[1]
                m = parent.value[1]
                S = parent.middleleft.key[0]
                s = parent.middleleft.value[0]
                L = parent.middleright.key[0]
                l = parent.middleright.value[0]
                if self.subtree_count(parent.middleleft)!=2 and self.subtree_count(parent.middleright)!=2: #Als de trees geen 2-nodes zijn (kun je dus ook niet mergen)
                    return [False, False]
                # Initalize trees
                b = parent.middleleft.left
                c = parent.middleleft.right
                d = parent.middleright.left
                e = parent.middleright.right
                # 1: Merge Keys, Values, Subtrees
                parent.key[1] = None                                                                    #Erase middle key & Value
                parent.value[1] = None

                parent.middleleft = TreeItemType(M, m, b, c, d, e, parent)                              # Reset format / Houdt format consistent
                parent.middleright = None                                                               # Reset format
                parent.middleleft.key = [S, M, L]
                parent.middleleft.value = [s, m, l]

                #Set new parent link
                if parent.left != None:
                    parent.left.parent = parent
                if parent.middleleft != None:
                    parent.middleleft.parent = parent
                if parent.middleright != None:
                        parent.middleright.parent = parent
                if parent.right != None:
                    parent.right.parent = parent

                return [True, parent.middleleft]

            elif key>parent.key[1]:                                                                 #Groter dan de middelste key: middleright & right | Dia118c
                # Initalise keys & values
                M = parent.key[2]
                m = parent.value[2]
                S = parent.middleright.key[0]
                s = parent.middleright.value[0]
                L = parent.right.key[0]
                l = parent.right.value[0]
                if self.subtree_count(parent.right)!=2 and self.subtree_count(parent.middleright)!=2: # ALs de trees geen 2-nodes zijn (kun je dus ook niet mergen)
                    return [False, False]
                # Initalize trees
                c = parent.middleright.left
                d = parent.middleright.right
                e = parent.right.left
                f = parent.right.right
                # 1: Merge Keys, Values, Subtrees
                parent.key[2] = parent.key[1]                                                       #Shift middle value & key to right; consistent format
                parent.value[2] = parent.value[1]
                parent.key[1] = None                                                                #Erase middle key & Value (Only 2 keys now in node)
                parent.value[1] = None

                parent.right = TreeItemType(M, m, c, d, e, f, parent)                               # Reset format / Houdt format consistent
                parent.right.key = [S, M, L]
                parent.right.value = [s, m, l]

                #Set new parent link
                if parent.left != None:
                    parent.left.parent = parent
                if parent.middleleft != None:
                    parent.middleleft.parent = parent
                if parent.middleright != None:
                        parent.middleright.parent = parent
                if parent.right != None:
                    parent.right.parent = parent

                return [True, parent.right]

        elif k==3: #Parent is 3-node | Dia117
            #Zitten de 2 Trees links of rechts? -> Vergelijk key to delete
            if key<parent.key[2]:                                                           #Links | Dia117a
                # Initalise keys & values
                M = parent.key[0]
                m = parent.value[0]
                S = parent.left.key[0]
                s = parent.left.value[0]
                L = parent.middleleft.key[0]
                l = parent.middleleft.value[0]
                if self.keyCount(parent.middleleft)!=1 and self.keyCount(parent.left)!=1:   #Als de trees geen 2-nodes zijn (kun je dus ook niet mergen)
                    return [False, False]
                # Initalize trees
                a = parent.left.left
                b = parent.left.right
                c = parent.middleleft.left
                d = parent.middleleft.right
                # 1: Merge Keys, Values, Subtrees
                parent.key[0]=parent.key[2]
                parent.key[2]=None
                parent.value[0]=parent.value[2]
                parent.value[2]=None

                parent.left=TreeItemType(M,m,a,b,c,d,parent)
                parent.middleleft=None
                parent.left.key=[S,M,L]
                parent.left.value=[s,m,l]

                #Set new parent link
                if parent.left != None:
                    parent.left.parent = parent
                if parent.middleleft != None:
                    parent.middleleft.parent = parent
                if parent.middleright != None:
                        parent.middleright.parent = parent
                if parent.right != None:
                    parent.right.parent = parent

                return [True,parent.left]

            else: #Rechts | Dia117b
                # Initalise keys & values
                M = parent.key[2]
                m = parent.value[2]
                S = parent.middleleft.key[0]
                s = parent.middleleft.value[0]
                L = parent.right.key[0]
                l = parent.right.value[0]
                if self.keyCount(parent.right)!=1 and self.keyCount(parent.middleleft)!=1:      #Als de trees geen 2-nodes zijn (kun je dus ook niet mergen)
                    return [False, False]
                # Initalize trees
                b = parent.middleleft.left
                c = parent.middleleft.right
                d = parent.right.left
                e = parent.right.right
                # 1: Merge Keys, Values, Subtrees
                parent.key[2] = None
                parent.value[2] = None

                parent.right = TreeItemType(M, m, b, c, d,e, parent)
                parent.middleleft = None
                parent.left.key = [S, M, L]
                parent.left.value = [s, m, l]

                #Set new parent link
                if parent.left != None:
                    parent.left.parent = parent
                if parent.middleleft != None:
                    parent.middleleft.parent = parent
                if parent.middleright != None:
                        parent.middleright.parent = parent
                if parent.right != None:
                    parent.right.parent = parent

                return [True, parent.left]

        elif k==2: #Parent is 2-node | Dia116             #Subtrees zouden altijd 2 knoop moeten zijn!
            #Initalise keys & values
            M=parent.key[0]
            m=parent.value[0]
            S=parent.left.key[0]
            s=parent.left.value[0]
            L=parent.right.key[0]
            l=parent.right.value[0]
            if self.keyCount(parent.left)!=self.keyCount(parent.right)!=1: #ALs de trees geen 2-nodes zijn (kun je dus ook niet mergen)
                return [False,False]
            #Initalize trees
            a = parent.left.left
            b = parent.left.right
            c = parent.right.left
            d = parent.right.right
            #1: Merge Keys
            parent.key=[S,M,L]
            #2: Merge Values
            parent.value=[s,m,l]
            #3: Merge subtrees
            parent.left=a
            parent.middleleft=b
            parent.middleright=c
            parent.right=d

            # Set new parent link
            if parent.left != None:
                parent.left.parent = parent
            if parent.middleleft != None:
                parent.middleleft.parent = parent
            if parent.middleright != None:
                parent.middleright.parent = parent
            if parent.right != None:
                parent.right.parent = parent

            return [True,parent]

        else: #Als k<2 of k>4, niet mogelijk
            return [False,False]

    def inorderSuccessor(self,key, tree, position): #Position = place of key, 0=left; 1=middle; 2=right
        """
        Hulpfunctie die de inorderSuccessor zoekt van een key. Dit is een hulpfunctie en mag enkel intern worden opgeroepen.
        :parameter in ; 'key': Getal , 'tree': TreeItemType , 'position': 0,1,2
        :parameter out; 'succes': bool OR 'key'
        Preconditie: Er is een 234T aangemaakt.
        Postconditie: Indien de operatie geslaagd is; wordt de inorderSuccessor meegegeven. Indien er geen inordersuccessor gevonden kon worden (bestaat niet of ERROR) wordt er "False" meegegeven;
        """
        a=self.keyCount(tree)
        z=self.subtree_count(tree)                                      #Telt aantal bestaande subtrees
        parent=tree.parent
        if parent!=None:
            pa=self.keyCount(parent)
            pz=self.subtree_count(parent)

        #1. Check if closest subtree (at right) has items
        #2. kijken of er keys zijn rechts in de boom
        #3. Check parents (if parents==None => root, evt none)

        if z>0:                                                         #There are subtrees
            if z==2:                                                    #Er is een rechter om te checken
                return self.inorderSuccessor(key,tree.right,0)          #Positie wordt altijd 0, omdat je de meest dichtte opvolger moet nemen (dus kleinste van volgende subtree)
            elif z==3 and position==0:                                  #Check middleleft subtree (key zelf zit links)
                return self.inorderSuccessor(key,tree.middleleft,0)
            elif z==3 and position==2:                                  #Check rechterdeelboom (key zelf zit rechts)
                return self.inorderSuccessor(key,tree.right,0)
            elif z==4 and position==0:                                  #Check middleleft
                return self.inorderSuccessor(key,tree.middleleft,0)
            elif z==4 and position==1:                                  #Check middleright
                return self.inorderSuccessor(key,tree.middleright,0)
            elif z==4 and position==2:                                  #Check right
                return self.inorderSuccessor(key,tree.right,0)

        else:                                                           #Check keys to right (no subtrees)
            if position==1:                                             #Bestaat dus een rechterkey
                return tree.key[2]
            elif position==0:
                return tree.key[0]
            else:                                                       #Key zelf zit links, en heeft geen subtrees -> Check parents OR tree zit helemaal rechts #if position!=2: # if position would be 2, there was No right key => Check parents
                if parent==None:
                    return False
                if tree==parent.right:
                    return False
                elif parent.key[1]!=None and key<parent.key[1]:
                    return parent.key[2]
                elif parent.key[2]!=None and key<parent.key[2]:
                    return parent.key[2]

                return False

    def locate(self,parent,tree):
        """
        Hulpfunctie die de positie van een tree t.o.v. de parent meegeeft. Dit is een hulpfunctie en mag enkel intern worden opgeroepen.
        :parameter in ; 'parent': TreeItemType, 'tree': TreeItemType
        :parameter out; Unsigned Integer: 0,1,2,3
        Preconditie: Er is een 234T aangemaakt. tree is een subtree van parent.
        Postconditie: De positie van de tree wordt meegegeven. De 234T blijft onverandert. {query}
        """
        if tree==parent.left:
            return 0
        if tree==parent.middleleft:
            return 1
        if tree==parent.middleright:
            return 2
        if tree==parent.right:
            return 3

"""
t = TwoThreeFourTree()
t.load({'root': [5], 'children': [{'root': [2], 'children': [{'root': [1]}, {'root': [3, 4]}]}, {'root': [12], 'children': [{'root': [10]}, {'root': [13, 15,16]}]}]})
print(t.save())
t.deleteItem(13)
print(t.save())
t.deleteItem(10)
print(t.save())
t.deleteItem(16)
print(t.save())
t.root=TreeItemType(None,None)
t.insertItem(createTreeItem(5,5))
print(t.save())
t.insertItem(createTreeItem(10,10))
print(t.save())
t.insertItem(createTreeItem(2,2))
print(t.save())
t.insertItem(createTreeItem(12,12))
print(t.save())
t.insertItem(createTreeItem(15,15))
print(t.save())
t.insertItem(createTreeItem(1,1))
print(t.save())
t.insertItem(createTreeItem(3,3))
print(t.save())
t.insertItem(createTreeItem(4,4))
print(t.save())
t.insertItem(createTreeItem(16,16))
print(t.save())
t.insertItem(createTreeItem(13,13))
print(t.save())
t.inorderTraverse(print)
print(t.save())


t.root=TreeItemType(None,None)
print(t.isEmpty())
print(t.insertItem(createTreeItem(8, 8)))
print(t.save())
print(t.insertItem(createTreeItem(5, 5)))
print(t.save())
print(t.insertItem(createTreeItem(10, 10)))
print(t.save())
print(t.insertItem(createTreeItem(15, 15)))
print(t.save())
print(t.isEmpty())
print(t.retrieveItem(5)[0])
print(t.retrieveItem(5)[1])
t.inorderTraverse(print)
print(t.save())


t.load({'root': [10], 'children': [{'root': [5]}, {'root': [11]}]})
print(t.save())
print(t.insertItem(createTreeItem(15, 15)))
print(t.save())
print(t.deleteItem(0))
print(t.save())
print(t.deleteItem(10))
print(t.save())
"""
"""
t.load({'root': [5], 'children': [{'root': [2], 'children': [{'root': [1]}, {'root': [3, 4]}]}, {'root': [12], 'children': [{'root': [10]}, {'root': [13, 15,16]}]}]})
print(t.save())
t.deleteItem(13)
t.deleteItem(10)
t.deleteItem(16)
print(t.save())
t.insertItem(createTreeItem(5,5))
t.insertItem(createTreeItem(10,10))
t.insertItem(createTreeItem(2,2))
t.insertItem(createTreeItem(12,12))
t.insertItem(createTreeItem(15,15))
t.insertItem(createTreeItem(1,1))
t.insertItem(createTreeItem(3,3))
t.insertItem(createTreeItem(4,4))
t.insertItem(createTreeItem(16,16))
t.insertItem(createTreeItem(13,13))
t.inorderTraverse(print)
print(t.save())

print(t.isEmpty())
print(t.insertItem(createTreeItem(8, 8)))
print(t.insertItem(createTreeItem(5, 5)))
print(t.insertItem(createTreeItem(10, 10)))
print(t.insertItem(createTreeItem(15, 15)))
print(t.isEmpty())
print(t.retrieveItem(5)[0])
print(t.retrieveItem(5)[1])
t.inorderTraverse(print)
print(t.save())
t.load({'root': [10], 'children': [{'root': [5]}, {'root': [11]}]})
t.insertItem(createTreeItem(15, 15))
print(t.deleteItem(0))
print(t.save())
print(t.deleteItem(10))
print(t.save())
"""

class TwoThreeFourTreeTable:
    def __init__(self):
        self.t = TwoThreeFourTree()

    def tableIsEmpty(self):
        return self.t.isEmpty()

    def tableInsert(self,item):
        return self.t.insertItem(item)

    def tableRetrieve(self,key):
        return self.t.retrieveItem(key)

    def tableDelete(self,key):
        return self.t.deleteItem(key)

    def traverseTable(self,function):
        return self.t.inorderTraverse(function)

    def save(self):
        return self.t.save()

    def load(self,map):
        return self.t.load(map)

    def clear(self):
        self.t = TwoThreeFourTree()