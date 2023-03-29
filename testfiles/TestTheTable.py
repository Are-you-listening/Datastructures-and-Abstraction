
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
lst = adt_dict['0']
lst.extend(adt_dict['3'])
"""
for i in range(len(lst)):
    for j in range(len(lst)):
        print(i, j, lst[i], lst[j])
        t = Tabel(eval(lst[i]))
        zaaltje = Zaal(0, 200)
        zaaltje_yoopie = Zaal(2, 200)
        zaaltje_yay = Zaal(4, 200)
        t.TabelInsert(("hermans", 0), zaaltje, eval(lst[j]))
        t.TabelInsert(("hermans", 2), zaaltje_yoopie, eval(lst[j]))
        t.TabelInsert(("pieter", 4), zaaltje_yay, eval(lst[j]))
        print(t.TabelRetrieve((0,))[0].get_id())
        print(t.TabelRetrieve((2,))[0].get_id())
        print(t.TabelRetrieve((4,))[0].get_id())
        print(t.TabelRetrieve((1,)))
"""
i = 0
j = 3
print(i, j, lst[i], lst[j])
t = Tabel(eval(lst[i]), True)
zaaltje = Zaal(0, 200)
zaaltje_yoopie = Zaal(2, 200)
zaaltje_yay = Zaal(4, 200)
zaaltje_nohappy = Zaal(8,200)
t.TabelInsert("hermans", zaaltje, eval(lst[j]))
t.TabelInsert("hermans", zaaltje_yoopie, eval(lst[j]))
t.TabelInsert("hermans", zaaltje_nohappy, eval(lst[j]))
t.TabelInsert("pieter", zaaltje_yay, eval(lst[j]))
print(t.TabelRetrieve(0)[0].get_id())
print(t.TabelRetrieve(2)[0].get_id())
print(t.TabelRetrieve(8)[0].get_id())
print(t.TabelRetrieve(4)[0].get_id())
print(t.TabelRetrieve(1))
