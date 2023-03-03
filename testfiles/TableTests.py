import os
import ADT
from ADT.MyCircularLinkedChainAnas import LCTable
from ADT.My_BinarySearchTreeAnas import BSTTable
from ADT.My234treeTibo import TwoThreeFourTreeTable
from ADT.MyRedBlackTreeAnas import RedBlackTreeTable

for w in os.listdir("./ADT"): # subject to be changed. dit is een soort van template maar moet nog aangepast worden
    try:
        test = w.BSTTable() # dit zal waarschijnlijk meerder malen gedaan moeten worden met verschillende namespaces maar moet ik nog uitesten, zie import voor waarom
    except AttributeError:
        test = None
    if isinstance(test, BSTTable):
        test.tableInsert(55,55)

    try:
        test = w.LCTable()
    except AttributeError:
        test = None
    if isinstance(test, LCTable):
        test.tableInsert(55,55)

    try:
        test = w.TwoThreeFourTreeTable()
    except AttributeError:
        test = None
    if isinstance(test, TwoThreeFourTreeTable):
        test.tableInsert(55,55)

    try:
        test = w.RedBlackTreeTable()
    except AttributeError:
        test = None
    if isinstance(test, RedBlackTreeTable):
        test.tableInsert(55,55)