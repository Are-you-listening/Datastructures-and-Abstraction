import os
import ADT
from My_BinarySearchTree import BSTTable

for w in os.listdir("./ADT"): # subject to be changed. dit is een soort van template maar moet nog aangepast worden
    test = w.BSTTable()
    if isinstance(test, BSTTable):
        test.tableInsert(55,55)
