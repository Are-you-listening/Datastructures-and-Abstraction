"""ADT BST
Deze ADT wordt gebruikt om gegevens op te slaan en terug te vinden met behulp van een sleutel"""

def createTreeItem(key,val):
    return TreeTypeItem(key, val)


class TreeTypeItem:
    def __init__(self, key, value):
        """
        Initialiseerd een binary tree item.
        Dit item komt overeen met een node in een bianry search tree
        het bevat 2 pointers naar de kinderen en 1 pointer naar de parent.

        precondities: er zijn 2 parameters gegeven: 1 sleutel (key) en 1 waarde(value)
                      de parameter (key) is een positieve integer.

        postcondities: er wordt een TreeTypeItem aangemaakt die de key en de value bewaard, met 3 nullpointers
        """
        self.key = key
        self.value = value

        self.parent = None
        self.left_child = None
        self.right_child = None


class BST:
    def __init__(self):
        """
        Initialiseerd een binary tree door een pointer naar de root aan te maken.

        precondities: er worden geen parameters gegeven.
        postcondities: er wordt een pointer naar de root aangemaakt.
        """
        self.root = None

    def isEmpty(self):
        """
        Geeft terug of de binary tree leeg is of niet, dit kunnen we zien door te controleren dat de pointer naar
        de root een nullpointer is.

        precondities: er worden geen parameters gegeven.
        postcondities: er wordt een boolean teruggegeven

        :return: als de Binary Search Tree leeg is, dan wordt True teruggegeven en anders False.
        """
        if self.root == None:
            return True
        return False

    def searchTreeInsert(self, item, node=None):
        """
        We voegen een item toe aan de BinarySearchTree
        indien de BST leeg is, is het een speciaal geval.

        Bij de andere situaties wordt er gezocht op welke locatie het item terecht zou moeten komen, er wordt het daar
        nadien toegevoegd.

        precondities: Er wordt 1 parameter gegeven: item. (Indien extern gebruikt)
                      Deze parameter is van het type TreeTypeItem
                      De sleutel in dit TreeTypeItem bevindt zich nog niet in deze Binary Search Tree

        postcondities: De binary search tree zal 1 extra knoop bevatten, de hoogte van de Boom zal even groot of 1 groter zijn dan voordien.
                       Deze extra knoop zal een blad zijn.

        :return: Een Boolean die weergeeft dat de oepratie succesvol geslaagd is.
        """
        if self.isEmpty():
            self.root = item
        else:
            if node == None:
                n = self.root
            else:
                n = node

            if item.key < n.key:
                """indien we kijken naar het linkerkind, controleren we dat dit het einde is van het pad,
                anders gaan we verder zoeken"""
                if n.left_child is None:
                    n.left_child = item
                    item.parent = n
                else:
                    self.searchTreeInsert(item, n.left_child)

            else:
                """indien we kijken naar het rechterkind, controleren we dat dit het einde is van het pad,
                anders gaan we verder zoeken"""
                if n.right_child is None:
                    n.right_child = item
                    item.parent = n
                else:
                    self.searchTreeInsert(item, n.right_child)



        return True

    def searchTreeRetrieve(self, key, node=None):
        """
        Hier wordt de knoop dat de sleutel bevat zijn waarde teruggeven

        precondities: Er wordt 1 parameter gegeven: key dat een positieve integer is.
                      De binary search tree is niet leeg.

        postcondities: De binary search tree zal onveranderd blijven..

        :param key: een integer
        :return: de gevonden waarde en nadien True indien gevonden.
        """
        if self.isEmpty():
            return None, False

        if node == None:
            n = self.root
        else:
            n = node

        if key < n.key:
            if n.left_child is None:
                return None, False
            else:
                return self.searchTreeRetrieve(key, n.left_child)

        elif key == n.key:
            return n.value, True

        else:
            if n.right_child is None:
                return None, False
            else:
                return self.searchTreeRetrieve(key, n.right_child)

    def searchTreeDelete(self, key, node=None, parent_left=None):
        """
        hier wordt de knoop dat de sleutel bevat verwijderd

        precondities: Er wordt 1 parameter gegeven: key dat een positieve integer is.
                      De binary search tree is niet leeg.

        postcondities: De binary search tree zal 1 knoop minder bevatten.

        :param key: een integer
        :return: True indien geslaagd
        """
        if self.isEmpty():
            return False

        if node == None:
            n = self.root
        else:
            n = node

        if key < n.key:
            if n.left_child is None:
                return False
            else:
                return self.searchTreeDelete(key, n.left_child, True)

        elif key == n.key:
            """indien het te verwijderen item gevonden is."""
            parent = n.parent
            left = n.left_child
            right = n.right_child

            if left is None and right is None:
                """indien het te verwijderen item een blad is, wordt het blad verwijdered door 
                de parent pointer niet meer naar het blad te laten wijzen"""
                if parent == None:
                    self.root = None
                    return True

                if parent_left:
                    parent.left_child = None
                else:
                    parent.right_child = None

                return True


            elif left is not None and right is not None:
                """indien het item 2 kinderen heeft"""
                succesor = self.find_inorder_succesor(n)

                temp_right = succesor.right_child

                """zorgt ervoor dat we later een child van de succesor doorgeven"""
                move = False
                isleft = False
                p = succesor.parent
                if temp_right:
                    move = True

                    if p.left_child == succesor:
                        isleft = True


                succesor_parent = succesor.parent

                """we zorgen dat de parent wijst naar de inorder succesor, en de succesor zijn parent ook die parent is"""
                if parent != None:
                    if parent_left:
                        parent.left_child = succesor
                    else:
                        parent.right_child = succesor
                else:
                    self.root = succesor

                succesor.parent = parent

                """we zoeken uit dat de succesor het linker of het rechterkind was,
                deze info bewaren we in de Boolean sparent_left"""
                if succesor_parent.left_child is not None:
                    if succesor_parent.left_child.key == succesor.key:
                        sparent_left = True
                    else:
                        sparent_left = False
                else:
                    sparent_left = False

                """vervolgens zorgen we dat de succesor niet meer zijn parent zijn child is."""
                if sparent_left:
                    succesor_parent.left_child = None
                else:
                    succesor_parent.right_child = None

                """we geven de kinderen van het te verwijderen item door naar de plaats inemende succesor"""

                succesor.left_child = n.left_child
                succesor.right_child = n.right_child

                """we wisselen ook de parents van deze items om"""
                if n.left_child:
                    n.left_child.parent = succesor

                if n.right_child:
                    n.right_child.parent = succesor

                """geeft child van de succesor door"""
                if move:
                    if isleft:
                        p.left_child = temp_right
                    else:
                        p.right_child = temp_right


            else:
                """indien het item 1 kind heeft, zorgen we ervoor dat de ouder wijst naar het kind in 
                de plaatst van het te verwijderen item"""
                if left:
                    node = left
                else:
                    node = right

                if parent != None:
                    if parent_left:
                        parent.left_child = node

                    else:
                        parent.right_child = node
                else:
                    self.root = node

                node.parent = parent

            return True

        else:
            if n.right_child is None:
                return False
            else:

                return self.searchTreeDelete(key, n.right_child, False)

    def find_inorder_succesor(self, n):
        """zoekt de inorder succesor
        preconditie: n heeft een rechter kind
        """
        n = n.right_child
        while n.left_child != None:
            n = n.left_child

        return n

    def save(self):
        """vormt de binary tree om naar dict formaat"""
        if self.root is not None:
            return self.get_sub_tree(self.root)
        else:
            return {}

    def get_sub_tree(self, n):
        """vraagt alle deelbomen op"""
        d = {"root": n.key}
        lst = [None]*2
        count = 0
        if n.left_child is not None:
            lst[0] = self.get_sub_tree(n.left_child)
            count += 1
        if n.right_child is not None:
            lst[1] = self.get_sub_tree(n.right_child)
            count += 1
        if count != 0:
            d.update({"children": lst})

        return d

    def load(self, d):
        """laad de gegeven BST
        preconditie: er wordt 1 parameter (d) gegeven.
                     Deze parameter heeft de gevraagde structuur: {root: "keyvalue"}, children[deelboom0, deelboom1].
                     (deelbomen kunnen eventueel gelijk zijn aan None).
                     De dictionary heeft een geldige BST structuur en is niet leeg.

        postcondities: De binary search tree zal veranderd worden naar de geladen tree.

        """

        """check if empty"""
        if len(d.keys()) == 0:
            return

        self.load_sub_tree(d, None)

    def load_sub_tree(self, d, parent, left=True):

        key = d["root"]
        node = TreeTypeItem(key, key)
        if "children" in d:
            children = d["children"]
            if children[0] != None:
                    self.load_sub_tree(children[0], node, True)
            if children[1] != None:
                self.load_sub_tree(children[1], node, False)

        if parent != None:
            if left and node.key < parent.key:
                parent.left_child = node
            else:
                parent.right_child = node

            node.parent = parent
        else:
            self.root = node


    def inorderTraverse(self, pri, item=None, root=True):
        """toont de inorder traverse waardes
        precondities: er worden een parameter meegegeven, deze parameter is een functie,
        die op elke waarde in de inorder traverse wordt toegepast.
        postcondities: de BST blijft onveranderd

        :param: pri: de functie
        """

        """nothing to do when empty"""
        if self.isEmpty():
            return

        if item == None:
            if root:
                item = self.root
            else:
                return

        self.inorderTraverse(pri, item.left_child, False)
        pri(item.value)
        self.inorderTraverse(pri, item.right_child, False)


class BSTTable():
    def __init__(self):
        self.bst = BST()

    def tableIsEmpty(self):
        return self.bst.isEmpty()

    def tableInsert(self, key, val, adt=None):

        if isinstance(key, int):
            return self.bst.searchTreeInsert(createTreeItem(key, val))
        elif isinstance(key, tuple):
            key, key2 = key
            current_adt, found = self.bst.searchTreeRetrieve(key)

            if adt == None or not adt.empty():
                raise Exception("Preconditie BST Tibo: sub-adt niet empty")

            if found:
                return current_adt.tableInsert(key2, val)
            else:
                adt.tableInsert(key2, val)
                return self.bst.searchTreeInsert(createTreeItem(key,adt))

    def tableRetrieve(self, key):
        if isinstance(key, int):
            return self.bst.searchTreeRetrieve(key)
        elif isinstance(key, tuple):
            key, key2 = key
            current_adt, found = self.bst.searchTreeRetrieve(key)
            if not found:
                return None, False

            return current_adt.tableRetrieve(key2)

    def traverseTable(self, func):
        self.bst.inorderTraverse(func)

    def save(self):
        return self.bst.save()

    def load(self, dict):
        return self.bst.load(dict)

    def tableDelete(self, key):
        if isinstance(key, int):
            return self.bst.searchTreeDelete(key)
        elif isinstance(key, tuple):
            key, key2 = key
            current_adt, found = self.bst.searchTreeRetrieve(key)
            if not found:
                return False

            suc6 = current_adt.tableDelete(key2)
            if current_adt.tableIsEmpty():
                self.bst.searchTreeDelete(key)
            return suc6

    def clear(self):
        self.bst = BST()

