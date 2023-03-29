
from ADT.Tabel import Tabel
from ProtoType.Zaal import Zaal
from ADT import MyBSTAnas, MyCircularLinkedChainAnas, MyQueueAnas, MyRedBlackTreeAnas, MyStackAnas
from ADT import MyBSTEmil, MyCircularLinkedChainEmil, MyQueueEmil, MyTwoThreeFourTreeEmil, MyStackEmil
from ADT import MyBSTKars, MyCircularLinkedChainKars, MyQueueKars, MyTwoThreeFourTreeKars, MyStackKars
from ADT import MyBSTTibo, MyCircularLinkedChainTibo, MyQueueTibo, MyTwoThreeFourTreeTibo, MyStackTibo


adt_dict = {}
with open("../testfiles/ADTFiles.txt") as f:
    for file in f.readlines():
        file = file.replace("\n", "")
        line_list = file.split(" ")
        adt = line_list[0]
        for i in range(1, len(line_list)):
            t = adt_dict.get(line_list[i], [])
            t.append(adt)
            adt_dict[line_list[i]] = t