"""
Deze ADT is een 234Tree, waar er gegevens kunnen worden opgeslagen door middel van een sleutel en een value
"""

def createTreeItem(k, v):
    """zet de key en value om naar een TwoThreeFourTreeType"""
    return TwoThreeFourTreeType(k, v)


class TwoThreeFourTreeType:
    def __init__(self, key, value):
        """
        Deze klasse staat voor een TwoThreeFourTreeType (knnop) in de 234Tree
        Dit heeft een pointer naar de parent van de knoop.
        Het bevat een array (key_array) van grootte 3 die de sleutels bevat.
        Het grootste mogelijke aantal sleutels in een knoop is 3.
        Indien er minder sleutels in deze knoop zitten zullen er enkele plaatsen in deze array leeg(None zijn)
        De sleutels zullen altijd zoveel mogelijk rechts zijn.

        Ook is er een array (children) van grootte 4, die pointers bevat naar de children van de knoop.
        Indien er geen 4 kinderen zijn zullen de kinderen meest rechts staan en zal de rest van de array leeg blijven (None).
        Elk kind komt ook overeen met de keys zodat:
        c1<  k1 < c2 < k2 < c3 < k3 < c4
        met ci elke key van het i-de child en ki de i-de key van de key array.

        We hebben ook nog een value array (lengte 3) waarbij ki overeenkomt met het i-de element van de value array.

        precondities: Deze functie wordt enkel opgeroepen door TwoThreeFourTree, het bevat 2 parameters: 1 key en 1 value
                      de parameter key is een integer.
        postcondities: Er zal een nieuwe knoop aangemaakt worden met enkel een key op de eerste plek in de key array
                       en een value op de eerste plek in de value array.
        """
        self.parent = None

        self.key_array = [None]*3
        self.key_array[0] = key
        self.value_array = [None]*3
        self.value_array[0] = value

        self.children = [None]*4

    def count_nodes(self):
        """
        Geeft weer hoeveel sleutels er in deze knoop zitten

        precondities: er worden geen parameters gegevens
        postcondities: er wordt een integer teruggegeven tussen 0 en 3, die weergeeft hoeveel sleutels er in deze knoop zitten
        :return count integer: aantal sleutels in de knoop
        """

        """we controleren het aantal sleutels door 
        te tellen hoeveel waardes niet gelijk zijn aan None in de key array"""
        count = 0
        for key in self.key_array:
            if key != None:
                count += 1

        return count

    def count_children(self):
        """
        Geeft weer hoeveel kinderen er in deze knoop zitten

        precondities: er worden geen parameters gegevens
        postcondities: er wordt een integer teruggegeven tussen 0 en 4, die weergeeft hoeveel kinderen deze knoop heeft
        :return count integer: aantal kinderen van deze knoop
        """

        """we controleren het aantal sleutels door 
        te tellen hoeveel waardes niet gelijk zijn aan None in de children array"""
        count = 0
        for key in self.children:
            if key != None:
                count += 1

        return count

    def isleaf(self):
        """
        Geeft weer dat de knoop een blad is
        preconditie: er worden geen paramters gegeven
        postconditie: er wordt een boolean teruggegeven die True is als de knoop een blad is.
                      De knoop zal onveranderd worden.
        :return: True indien het een blad is
        """
        return self.count_children() == 0

    def add_key(self, key, value):
        """
        Voegt een sleutel en zijn waarde toe aan de knoop
        Dit wordt gedaan door eerst te zoeken op welke positie de sleutel hoort te staan.
        Daarna shiften we de andere sleutels en waardes zodat die niet overschreven worden.
        Tot slot voegen we de sleutel en de waarde toe

        precondities: er worden 2 parameters gegeven key en value.
                      de parameter key is een integer.
                      deze knoop zit niet vol.
                      Deze functie mag enkel intern of door TwoThreeFourTree aangeroepen worden.
        postcondities: er wordt een sleutel en waarde toegevoegd aan de knoop.

        :return True indien geslaagd
        """

        """ga alle posities af, indien de nieuwe sleutel kleiner is dan de oorspronkelijke sleutel op een positie,
           dan stoppen we met zoeken en bewaren we die positie."""
        location = 2
        for i, node_key in enumerate(self.key_array):
            if node_key != None:
                if key < node_key:
                    location = i
                    break
            else:
                location = i
                break

        """nu gaan we alle posities van van 2 tot en met 0.
           Als de positie groter of gelijk is aan de voordien gevonden locatie, 
           dan verplaatsen we de sleutel en de overeenkomstige waarde naar de volgende positie."""
        for i in range(2, -1, -1):
            node_key = self.key_array[i]
            node_value = self.value_array[i]
            if i >= location and node_key != None:
                self.key_array[i+1] = node_key
                self.value_array[i + 1] = node_value

        """we voegen de nieuwe sleutel en waarde toe op de gevonden positie 
            (die door de voorgaande overschreven mag worden)"""
        self.key_array[location] = key
        self.value_array[location] = value

        return True

    def add_child(self, child, index):
        """
        Voegt een child toe aan de knoop op de gegeven index
        we shiften alle kinderen dat zich bevinden op de index of op een grotere index.
        Daarna voegen we het kind toe op de index.

        precondities: er worden 2 parameters gegeven child en index.
                      de parameter child is een integer groter of gelijk aan 0 en kleiner dan 4.
                      deze knoop heeft nog plaats voor een kind.
                      Deze functie mag enkel intern of door TwoThreeFourTree aangeroepen worden.
        postcondities: er wordt een kind toegevoegd aan de knoop.

        :return True indien geslaagd
        """

        """shift al de kinderen gelijk of groter dan index 1 plek naar rechts"""
        for i in range(2, -1, -1):
            if i >= index:

                self.children[i+1] = self.children[i]

        """voegt kind toe op de array op de gegeven index"""
        self.children[index] = child

        return True

    def remove_key_merge(self, key):
        """
        Deze functie verwijderd een sleutel zodat het werkt voor een merge.
        Bij de key array zoeken we naar de sleutel en verwijderen we deze sleutel
        Alle sleutels op een hogere index in de array zullen naar links shiften.

        Het linker en het rechter kind van de sleutel zullen ook verwijderd worden.

        preconditie: De gegeven parameter key zit in de key array.
                     Deze functie mag enkel intern of door TwoThreeFourTree aangeroepen worden.
        postcondities: de knoop heeft 1 sleutel minder en maximum 2 kinderen minder

        :return een tuple met daarin de sleutel, het linker kind, het rechter kind
        """

        """verwijder de gegeven sleutel en shift alles groter dan zijn index naar links"""
        key_loc = None
        for i, node_key in enumerate(self.key_array):
            if node_key == key:
                key_loc = i
                self.key_array[i] = None
                self.value_array[i] = None
            elif i > 0 and self.key_array[i-1] is None:
                self.key_array[i-1] = self.key_array[i]
                self.key_array[i] = None

                self.value_array[i-1] = self.value_array[i]
                self.value_array[i] = None

        """vraag de kinderen na de verwijderde sleutel op"""
        left = self.children[key_loc]
        right = self.children[key_loc+1]

        """verwijder de kinderen"""
        for i, node_child in enumerate(self.children):
            if i == key_loc or i == key_loc + 1:
                self.children[i] = None
            elif i >= 2 and self.children[i - 2] is None:
                self.children[i - 2] = self.children[i]
                self.children[i] = None

        return key, left, right

    def remove_key(self, key):
        """
        De gegeven sleutel wordt verwijderd uit de knoop.
        preconditie: De gegeven parameter key zit in de key array.
                     Deze functie mag enkel intern of door TwoThreeFourTree aangeroepen worden.
        postcondities: de knoop heeft 1 sleutel minder.

        :param key: de sleutel van het item dat verwijderd moet worden
        """

        """verwijder de gegeven sleutel en shift alles groter dan zijn index naar links"""
        for i, node_key in enumerate(self.key_array):
            if node_key == key:
                self.key_array[i] = None
                self.value_array[i] = None
            elif i > 0 and self.key_array[i-1] is None:
                self.key_array[i-1] = self.key_array[i]
                self.key_array[i] = None

                self.value_array[i - 1] = self.value_array[i]
                self.value_array[i] = None

    def remove_child(self, child):
        """
        Het gegeven kind wordt verwijderd uit de knoop.
        preconditie: De gegeven parameter child zit in de kinderen array (children).
                     Deze functie mag enkel intern of door TwoThreeFourTree aangeroepen worden.
        postcondities: de knoop heeft 1 kind minder.

        :param child: de knoop dat naar het kind wijst dat verwijderd moet worden.
        """

        """zoek de index van het kind en shift alle kindern groter dan deze index naar links"""
        index = self.children.index(child)
        for i in range(4):
            if index == i:
                self.children[i] = None
            elif i > index:
                self.children[i-1] = self.children[i]
                self.children[i] = None

    def add_key_split(self, key, value, c1, c2):
        """
        voeg een sleutel, waarde en 2 kinderen toe aan de knoop.
        Deze waardes komen oorspronkelijk uit 1 van de kinderen. Dit kind wordt gesplitst.
        preconditie: Deze functie mag enkel door de TwoThreeFourTree opgeroepen worden, of intern.
        postconditie: De knoop wordt gewijzigd.
        :param key: de sleutel die moet worden toe gevoegd aan de knoop
        :param value: de waarde van de sleutel die moet worden toe gevoegd aan de knoop
        :param c1: het relatieve linkerkind van de sleutel dat moet worden toegevoegd als kind van de knoop.
        :param c2: het relatieve rechterkind van de sleutel dat moet worden toegevoegd als kind van de knoop.
        :return: True indien geslaagd.
        """

        """zoek de locatie waar de nieuwe sleutel komt te staan"""
        location = 2
        for i, node_key in enumerate(self.key_array):
            if node_key != None:
                if key < node_key:
                    location = i
                    break
            else:
                location = i
                break

        """
        We verplaatsen alle sleutels en waardes groter of gelijk aan de gevonden index naar rechts
        We verplaatsen deze kinderen ook 1 naar rechts, maar enkel die van index i+1
        Hierdoor overschrijven we de pointer naar het kind waar de sleutel en de c1 en c2 oorspronkelijk vandaan komen
        """
        for i in range(1, -1, -1):
            node_key = self.key_array[i]
            node_value = self.value_array[i]
            if i >= location and node_key != None:
                self.key_array[i + 1] = node_key
                self.value_array[i + 1] = node_value
                self.children[i + 2] = self.children[i+1]

        self.children[location] = c1
        self.children[location+1] = c2

        self.key_array[location] = key
        self.value_array[location] = value


        return True

    def add_key_merge(self, key, value, c1, c2):
        """
        voeg een sleutel, waarde en 2 kinderen toe aan de knoop
        preconditie: Deze functie mag enkel door de TwoThreeFourTree opgeroepen worden, of intern.
        postconditie: De knoop wordt gewijzigd.
        :param key: de sleutel die moet worden toe gevoegd aan de knoop
        :param value: de waarde van de sleutel die moet worden toe gevoegd aan de knoop
        :param c1: het relatieve linkerkind van de sleutel dat moet worden toegevoegd als kind van de knoop.
        :param c2: het relatieve rechterkind van de sleutel dat moet worden toegevoegd als kind van de knoop.
        :return: True indien geslaagd.
        """

        location = 2
        for i, node_key in enumerate(self.key_array):
            if node_key != None:
                if key < node_key:
                    location = i
                    break
            else:
                location = i
                break

        for i in range(1, -1, -1):
            node_key = self.key_array[i]
            node_value = self.value_array[i]
            if i >= location and node_key != None:
                self.key_array[i + 1] = node_key
                self.value_array[i + 1] = node_value
                self.children[i + 2] = self.children[i]

        self.children[location] = c1
        self.children[location + 1] = c2

        self.key_array[location] = key
        self.value_array[location] = value

        return True

    def get_next(self, key):
        """
        Deze functie geeft het kind terug waar de sleutel in zit / kan zitten
        of dit kind is een voorvader van de doelknoop.
        preconditie: Deze functie mag enkel door de TwoThreeFourTree opgeroepen worden, of intern.
        postconditie: De knoop wordt niet gewijzigd.
        :param key: de sleutel die bepaald welk kind we nemen
        :return: TwoThreeFourTreeType
        """
        for i in range(self.count_nodes()):
            if self.key_array[i] == None or key < self.key_array[i]:
                return self.children[i]

        return self.children[self.count_children()-1]

    def replace_child(self, old_node, new_node):
        """
        Vervangt een kind door een ander kind
        :param old_node: oorspronkelijke kind
        :param new_node: nieuwe kind
        preconditie: Deze functie mag enkel door de TwoThreeFourTree opgeroepen worden, of intern.
        postconditie: De knoop wordt gewijzigd.
        """
        for i, n in enumerate(self.children):
            if n == old_node:
                self.children[i] = new_node
                break

    def replace_key(self, old_key, new_key, new_value):
        """
        Vervangt een sleutel door een ander sleutel
        :param old_key: oorspronkelijke sleutel
        :param new_key: nieuwe sleutel
        :param new_value: nieuwe value
        preconditie: Deze functie mag enkel door de TwoThreeFourTree opgeroepen worden, of intern.
        postconditie: De knoop wordt gewijzigd.
        """
        for i, k in enumerate(self.key_array):
            if k == old_key:
                self.key_array[i] = new_key
                self.value_array[i] = new_value
                break

    def get_relative_child(self, key):
        """
        Geeft de relatieve linker- en rechterkind van een gegeven sleutel terug
        preconditie: Deze functie mag enkel door de TwoThreeFourTree opgeroepen worden, of intern.
        postconditie: De knoop wordt gewijzigd.
        """
        for i, k in enumerate(self.key_array):
            if k == key:
                return self.children[i], self.children[i+1]

    def get_value(self, key):
        for i, node_key in enumerate(self.key_array):
            if node_key == key:
                return self.value_array[i]


class TwoThreeFourTree:
    def __init__(self):
        """
        Initialiseer een TwoThreeFourTree
        met een pointer naar de root.
        Deze pointer is vanaf het begin een nullptr.

        Preconditie: er worden geen parameters gegeven.
        Postcondities: er wordt een pointer naar de root aangemaakt.
        """
        self.root = None

    def isEmpty(self):
        """
        Geeft weer dat de 234Tree leeg is
        Preconditie: er worden geen parameters gegeven.
        Postcondities: er wordt een boolean teruggeven, de 234Tree wordt niet aangepast
        :return: True indien de 234TRee leeg is
        """
        if self.root == None:
            return True
        return False

    def insertItem(self, treeitem, node=None):
        """
        Voegt een Treeitemtype toe aan de TwoThreeFourTree

        Preconditie: er wordt 1 parameter gegeven indien de functie extern gebruikt wordt,
                     indien de functie intern gebruikt wordt, mogen er 2 parameters gegeven worden.
                     De eerste parameter is een treeitemtype en de eventuele 2de paramter is een knoop (Node).

        Postcondities: er wordt een boolean teruggeven, de 234Tree zal 1 item meer bevatten

        :param treeitem: het treeitem dat moet worden toegevoegd
        :param node: knoop waarin we zoeken.
        :return:True indien geslaagd
        """
        key = treeitem.key_array[0]
        value = treeitem.value_array[0]

        """controleer dat de node een root is of niet"""
        if node == None:
            n = self.root
            """special case (indien nog geen knoop in boom"""
            if self.root == None:
                self.root = TwoThreeFourTreeType(key, value)
                return True

        else:
            n = node

        """controleer dat de knoop een 4-knoop is"""

        if n.count_nodes() == 3:
            """indien 4-knoop: split"""
            n = self.split(n)

        """indien aangekomen in blad: voeg key toe"""
        if n.isleaf():
            n.add_key(key, value)
            return True

        """bereken volgende knoop voor recursie"""
        n = n.get_next(key)

        return self.insertItem(treeitem, n)

    def retrieveItem(self, key, n=None):
        """
        Geeft de value van de gegeven sleutel weer

        Preconditie: er wordt 1 parameter gegeven indien de functie extern gebruikt wordt,
                     indien de functie intern gebruikt wordt, mogen er 2 parameters gegeven worden.
                     De eerste parameter is een integer en de eventuele 2de paramter is een knoop (Node).

        Postcondities: er wordt een tuple teruggeven met 2 elementen, eerste de value en 2de of het gevonden was.

        :param key: de sleutel waarvan de waarde opgevraagd wordt
        :param n: de huidige knoop waarin we zoeken.
        :return: een tuple met als eerste argument de waarde en als 2de argument of de waarde gevonden is.
                 Indien de waarde niet gevonden is: (None, False)
        """

        """Als de 234Tree leeg is, dan kan het element niet teruggegeven worden"""
        if self.isEmpty():
            return None, False

        if n == None:
            n = self.root

        """indien de sleutel in de 234Tree zit"""
        if key in n.key_array:
            index = n.key_array.index(key)
            return n.value_array[index], True

        """indien het een blad is en het item er niet in zit, zal het item niet in de 234Tree zitten"""
        if n.isleaf():
            return None, False

        """zoek verder in overeenkomstig kind"""
        return self.retrieveItem(key, n.get_next(key))

    def retrieveKey(self, key, n=None):
        """
        Geeft de knoop weer waarin de gegeven sleutel zit

       Preconditie: De functie wordt intern gebruikt, er mogen 2 parameters gegeven worden.
       De eerste parameter is een integer en de eventuele 2de paramter is een knoop (Node).
       De gevraagde key moet in de 234Tree zitten.

       Postcondities: er wordt een knoop teruggeven.

       :param key: de sleutel waarvan de waarde opgevraagd wordt
       :param n: de huidige knoop waarin we zoeken.
       :return: de knoop waarin de gevraagde key zit
       """

        if n == None:
            n = self.root

        if key in n.key_array:
            return n

        return self.retrieveKey(key, n.get_next(key))

    def deleteItem(self, key, node=None):
        """
        Verwijderd het item en zijn sleutel indien het in de 234Tree zit
        Preconditie: er wordt 1 parameter gegeven indien de functie extern gebruikt wordt,
                     indien de functie intern gebruikt wordt, mogen er 2 parameters gegeven worden.
                     De eerste parameter is een integer en is de sleutel en de eventuele 2de paramter is een knoop (Node).
                     De 234Tree is niet leeg

        Postcondities: de 234Tree zal 1 item kleiner zijn indien de sleutel in de 234Tree zit,
        er wordt een boolean teruggeven die weergeeft dat de operatie geslaagd is
        :return: True indien geslaaagd
        """

        """indien lege 234tree"""
        if self.root == None:
            return False

        if node == None:
            """indien eerste keer"""
            n = self.root
        else:
            """voor de andere gevallen"""
            n = node

        """indien we een blad bereikt hebben waar de sleutel niet in zit"""
        if n == None or (n.isleaf() and (key not in n.key_array)):
            return False

        """redistributie"""
        if (n.count_nodes() == 1) and (n.parent != None):
            """is een 2-knoop"""
            self.redistribute(n)

        if (n.count_nodes() == 1) and (n.parent != None):
            """2-knoop"""

            """check dat merge mogelijk is
            indien ja, voer deze merge ook uit
            """
            self.merge(n)

        """controleer dat de sleutel in de key array zit"""
        if key in n.key_array:

            """controleer dat de sleutel in een blad zit"""
            if n.isleaf():
                n.remove_key(key)
                return True
            else:
                """Indien de sleutel niet in een blad zit, swap met de inorder succesor"""
                """swap with inorder succesor"""
                succesor_key, succesor = self.find_succesor(n, key)
                succesor_key_value = succesor.get_value(succesor_key)

                """Indien dat de te verwijderen sleutel verwisseld is van plaats door het zoeken naar de inorder succesor, 
                moeten we terug de knoop vinden waar de sleutel zich bevind. Dit keer zonder de 234Tree aan te passen.
                """
                n = self.retrieveKey(key)
                key_value = n.get_value(key)

                n.replace_key(key, succesor_key, succesor_key_value)
                succesor.replace_key(succesor_key, key, key_value)

                succesor.remove_key(key)

                return True

        """bepaal volgende knoop om in verder te zoeken"""
        n = n.get_next(key)

        """delete recursief de sleutel in de nieuwe knoop"""
        return self.deleteItem(key, n)

    def split(self, n):
        """
        Splitst de knoop n
        precondities: Deze functie wordt enkel intern opgeroepen
        postcondities: De knoop n zal gesplitst worden.
                       De middelste sleutel zal toegevoegd worden aan de parent en
                       De linker en rechter sleutel zullen elk individuele 2-knopen worden, met
                       als parent de knoop waarin de middelste sleutel zit.
                       Deze knoop zal ook deze 2 individuele knopen als kinderen hebben.
        """

        """neem de parent"""
        parent = n.parent

        """neem de middelste key en maak 2 nieuwe knopen voor het nieuwe linker en rechter kind"""
        middle = n.key_array[1]
        middle_value = n.value_array[1]

        left_child = TwoThreeFourTreeType(n.key_array[0], n.value_array[0])
        right_child = TwoThreeFourTreeType(n.key_array[2], n.value_array[2])

        """zorg ervoor dat de kinderen van voor de split worden doorgegeven"""
        left_child.children[0] = n.children[0]
        left_child.children[1] = n.children[1]

        right_child.children[0] = n.children[2]
        right_child.children[1] = n.children[3]

        if left_child.children[0] != None:
            left_child.children[0].parent = left_child

        if left_child.children[1] != None:
            left_child.children[1].parent = left_child

        if right_child.children[0] != None:
            right_child.children[0].parent = right_child

        if right_child.children[1] != None:
            right_child.children[1].parent = right_child

        """indien geen parent: nieuwe root"""
        if parent == None:
            parent = TwoThreeFourTreeType(middle, middle_value)
            parent.children[0] = left_child
            parent.children[1] = right_child
            self.root = parent
        else:
            """voeg de middelste sleutel en de nieuwe kinderen toe aan de parent knoop"""
            parent.add_key_split(middle, middle_value, left_child, right_child)

        """zorg dat de kinderen naar de juiste parent verwijzen"""
        left_child.parent = parent
        right_child.parent = parent
        return parent


    def find_succesor(self, n, key):
        """
        In deze functie wordt er naar de inorder succesor gezocht.
        Onderweg wordt ook steeds elke 2-knoop omgezet naar een 3-knoop of een 4-knoop.
        Precondities: Deze functie wordt enkel intern opgeroepen
        Postcondities: Er zal een succesor sleutel teruggegeven worden samen met de knoop waar de succesor sleutel in zit.

        :param n: knoop vanwaar we beginnen zoeken.
        :param key: sleutel waarvan we de inorder succesor zoeken.
        :return: tuple: (succesor_sleutel, succesor_knoop).
        """
        left, right = n.get_relative_child(key)
        n = right
        """we blijven zoeken totdat we in een blad zitten"""
        while not n.isleaf():
            """redistributie indien van toepassing"""

            if (n.count_nodes() == 1) and (n.parent != None):
                """is een 2-knoop"""
                self.redistribute(n)

            if n.count_nodes() == 1:
                self.merge(n)

            child_index = 0
            while n.children[child_index].key_array[0] < key:
                child_index += 1

            n = n.children[child_index]

        """we moeten op het einde nog een keer redistribute en merge uitvoeren"""
        if (n.count_nodes() == 1) and (n.parent != None):
            """is een 2-knoop"""
            self.redistribute(n)

        if n.count_nodes() == 1:
            self.merge(n)

        return n.key_array[0], n

    def merge(self, n):
        """
        Voert een merge uit.
        Er wordt een knoop n gegeven. Eerst wordt er geprobeerd een left-merge
        uit te voeren en als dat niet werkt een richt-merge.
        Precondities: Deze functie wordt enkel intern opgeroepen
        Postcondities: Er zal een merge gebeuren als dit mogelijk is.
        :param n: de knoop dat merged samen met 1 sleutel uit de parent en 1 sibling.
        """
        parent = n.parent
        if parent == None:
            return
        node_index = parent.children.index(n)

        before = True
        after = True

        before_index = None
        after_index = None

        """Controleer dat een left-merge mogelijk is"""
        if (node_index > 0) and parent.children[node_index - 1].count_nodes() == 1:
            before_index = node_index-1
        else:
            before = False

        """Controleer dat een right-merge mogelijk is"""
        if (node_index < parent.count_children()-1) and parent.children[node_index + 1].count_nodes() == 1:
            after_index = node_index + 1
        else:
            after = False


        if before:
            """indien left-merge mogelijk is"""
            middle_key = parent.key_array[node_index-1]
            middle_key_value = parent.value_array[node_index - 1]

            """neem de linker-sibling knoop"""
            before_node = parent.children[before_index]

            """voeg gegevens toe aan n"""
            parent.remove_key_merge(middle_key)
            n.add_key(middle_key, middle_key_value)
            n.add_key_merge(before_node.key_array[0], before_node.value_array[0], before_node.children[0], before_node.children[1])

            """before_index is de add child locatie"""
            parent.add_child(n, before_index)

            """neem de kinderen over"""
            if before_node.children[0] != None:
                before_node.children[0].parent = n
            if before_node.children[1] != None:
                before_node.children[1].parent = n

        elif after:
            """indien right-merge mogelijk is"""
            middle_key = parent.key_array[node_index]
            middle_key_value = parent.value_array[node_index]

            """neem de rechter-sibling knoop"""
            after_node = parent.children[after_index]

            """voeg gegevens toe aan n"""
            parent.remove_key_merge(middle_key)
            n.add_key(middle_key, middle_key_value)
            n.add_key_merge(after_node.key_array[0], after_node.value_array[0], after_node.children[0], after_node.children[1])

            """after_index-1 is de add child locatie"""
            parent.add_child(n, after_index-1)

            """neem de kinderen over"""
            if after_node.children[0] != None:
                after_node.children[0].parent = n
            if after_node.children[1] != None:
                after_node.children[1].parent = n

        """indien de parent leeg is"""
        if n.parent.count_nodes() == 0:
            master_parent = n.parent.parent
            if master_parent == None:
                """n wordt de nieuwe root"""
                self.root = n
            else:
                """link naar de parent van de parent"""
                i = master_parent.children.index(n.parent)
                master_parent.children[i] = n

            n.parent = n.parent.parent

    def redistribute(self, n):
        """
        In deze functie wordt er gekeken welke redistributes mogelijk zijn.
        De linker-redistribute krijgt prioriteit.
        Als dit kan, dan wordt er gezien dat de rechter-redistribute gedaan kan worden.
        Er wordt een knoop (n) gegeven.
        Deze knoop is een 2-knoop dat door redistribute potentieel een 3-knoop kan worden.
        Precondities: Deze functie wordt enkel intern opgeroepen.
        Postconditie: Geen.
        :param n: De knoop die een extra sleutel kan ontvangen door redistribute
        """
        parent = n.parent

        clockwise = True
        counter_clockwise = True

        before_node = None
        after_node = None

        """controleer dat redisrtibutie van linker sibling mogelijk is"""
        if n == parent.children[0]:
            clockwise = False
        else:
            i = parent.children.index(n)
            before_node = parent.children[i - 1]

        """controleer dat redistributie van rechter sibling mogelijk is"""
        if n == parent.children[parent.count_children() - 1]:
            counter_clockwise = False
        else:
            i = parent.children.index(n)
            after_node = parent.children[i + 1]

        if clockwise and before_node.count_nodes() > 1:
            """indien linker redisrtibutie mogelijk"""
            self.redistribute_clock(n)

        elif counter_clockwise and after_node.count_nodes() > 1:
            """indien rechter redisrtibutie mogelijk"""
            self.redistribute_counter_clock(n)


    def redistribute_clock(self, target_node):
        """
        Voert een linker herverdeling uit.
        Hierbij gaat 1 element van de linker-sibling naar de parent en 1 parent gaat naar de target node
        Precondities: Deze functie wordt enkel intern opgeroepen.
        Postconditie: Een linker distributie is gebeurd.
        :param target_node: De knoop die een extra sleutel kan ontvangen door redistribute
        """

        parent = target_node.parent
        i = parent.children.index(target_node)
        parent_key = parent.key_array[i-1]
        parent_key_value = parent.value_array[i - 1]
        before_node = parent.children[i-1]

        keys = before_node.count_nodes()
        biggest = before_node.key_array[keys-1]
        biggest_value = before_node.value_array[keys - 1]

        biggest_child = before_node.children[keys]

        """Verplaatsen van kind zodat de 234Tree intact blijft"""
        if biggest_child != None:
            before_node.remove_child(biggest_child)
            target_node.add_child(biggest_child, 0)
            biggest_child.parent = target_node

        """Verplaatsen van sleutels"""
        before_node.remove_key(biggest)

        parent.remove_key(parent_key)
        parent.add_key(biggest, biggest_value)
        target_node.add_key(parent_key, parent_key_value)

    def redistribute_counter_clock(self, target_node):
        """
        Voert een rechter herverdeling uit.
        Hierbij gaat 1 element van de rechter-sibling naar de parent en 1 parent gaat naar de target node
        Precondities: Deze functie wordt enkel intern opgeroepen.
        Postconditie: Een rechter distributie is gebeurd.
        :param target_node: De knoop die een extra sleutel kan ontvangen door redistribute
        """

        parent = target_node.parent
        i = parent.children.index(target_node)
        parent_key = parent.key_array[i]
        parent_key_value = parent.value_array[i]
        before_node = parent.children[i + 1]

        smallest = before_node.key_array[0]
        smallest_value = before_node.value_array[0]
        smallest_child = before_node.children[0]

        """Verplaatsen van kind zodat de 234Tree intact blijft"""
        if smallest_child != None:
            before_node.remove_child(smallest_child)
            target_node.add_child(smallest_child, target_node.count_children())
            smallest_child.parent = target_node

        """Verplaatsen van sleutels"""
        before_node.remove_key(smallest)

        parent.remove_key(parent_key)
        parent.add_key(smallest, smallest_value)
        target_node.add_key(parent_key, parent_key_value)

    def save(self):
        """
        Store de TwoThreeFourTree naar een dictionary met een lijst van kinderen.
        Precondities: Er worden geen parameters gegeven.
        Postcondities: Er zal een Dictionary teruggegeven worden die de 234Tree weergeeft.
        :return: Dictionary dat de vorm van de 234Tree weergeeft.
        """
        return self.get_sub_tree(self.root)

    def get_sub_tree(self, n):
        """
        Vraagt de deelboom op.
        Dit geeft een dictionary terug dat de vorm van de 234Tree deelboom weergeeft.
        :return: Dictionary dat de vorm van de 234Tree deelboom weergeeft.
        """
        if n == None:
            return {}

        none_keys = n.key_array.count(None)
        d = {"root": n.key_array[:(3-none_keys)]}

        lst = [None]*(4-n.children.count(None))

        count = 0
        if n.children[0] is not None:
            lst[0] = self.get_sub_tree(n.children[0])
            count += 1
        if n.children[1] is not None:
            lst[1] = self.get_sub_tree(n.children[1])
            count += 1
        if n.children[2] is not None:
            lst[2] = self.get_sub_tree(n.children[2])
            count += 1
        if n.children[3] is not None:
            lst[3] = self.get_sub_tree(n.children[3])
            count += 1

        if count != 0:
            d.update({"children": lst})

        return d

    def load(self, d):
        """
        Laad de gegeven 234Tree in de binary search tree.
        Precondities: Er wordt een dictionary gegeven met de volgende structuur:
        "root": met een array van de sleutels
        "children": met een array van de kinderen
        Deze dictionary structuur zal een correcte 234Tree zijn.
        Postcondities: Er wordt een 234Tree aangemaakt volgens de structuur van de gegeven dictionary.
        :param d: Een dictionary die de 234Tree weergeeft
        """

        """if dict is empty"""
        if len(d.keys()) == 0:
            return

        self.load_sub_tree(d, None)

    def load_sub_tree(self, d, parent, position=0):
        """
        Laad de deelboom.
        De deelboom zal een dictionary zijn.
        We laden de 234Tree recursief. De parent van de deelboom en de root (d) van de deelboom worden gegeven
        Ook kan er eventueel een positie meegegeven worden.
        Dit geeft weer op welke plaats de kinderpointer staat in de parent.

        Precondities: Deze functie wordt enkel intern opgeroepen.
        Er worden 2-3 parameters gegeven. Eerst wordt de knoop gegeven en de parent van de deelboom,
        ook wordt eventueeel de positie meegegeven.
        Postcondities: Er wordt een 234Tree deelboom aangemaakt volgens de structuur van de gegeven dictionary

        :param d: Dictionary van de deelboom.
        :param parent: Geeft de parent van de knoop dat geladen wordt.
        :param position: Geeft weer op welk kindpositie de geladen knoop bewaard moet worden.

        """
        keys = d["root"]
        node = TwoThreeFourTreeType(keys[0], keys[0])
        node.key_array = keys + [None]*(3-len(keys))
        node.value_array = keys + [None]*(3-len(keys))

        if "children" in d:
            children = d["children"]
            for i in range(len(children)):
                self.load_sub_tree(children[i], node, i)
        if parent != None:
            parent.children[position] = node
            node.parent = parent
        else:
            self.root = node

    def inorderTraverse(self, func, item=None, root=True):
        """
        Toont de inorder traverse sleutels
        precondities: er wordt een parameter meegegeven (indien extern opgeroepen), deze parameter is een functie,
        die op elke waarde in de inorder traverse wordt toegepast
        Indien intern opgeroepen wordt, mogen er 3 parameters gegeven worden.
        De 234Tree mag ook niet leeg zijn.
        De eerste parameter (func) moet een geldige functie zijn.
        postcondities: de BST blijft onveranderd

        :param: func: de functie
        """
        """indien de 234Tree leeg is: functie wordt nooit uitgevoerd"""
        if self.isEmpty():
            return

        if item == None:
            if root:
                item = self.root
            else:
                return

        self.inorderTraverse(func, item.children[0], False)
        func(item.value_array[0])
        self.inorderTraverse(func, item.children[1], False)
        if item.key_array[1] != None:
            func(item.value_array[1])
        self.inorderTraverse(func, item.children[2], False)
        if item.key_array[2] != None:
            func(item.value_array[2])
        self.inorderTraverse(func, item.children[3], False)


class TwoThreeFourTreeTable:
    def __init__(self):
        self.tree = TwoThreeFourTree()

    def tableIsEmpty(self):
        return self.tree.isEmpty()

    def tableInsert(self, key, value):
        return self.tree.insertItem(createTreeItem(key, value))

    def tableRetrieve(self,key):
        return self.tree.retrieveItem(key)

    def traverseTable(self, func):
        self.tree.inorderTraverse(func)

    def save(self):
        return self.tree.save()

    def load(self, dict):
        return self.tree.load(dict)

    def tableDelete(self, key):
        return self.tree.deleteItem(key)

    def clear(self):
        self.tree = TwoThreeFourTree()
