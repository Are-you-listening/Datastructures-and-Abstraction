import sys

from ProtoType import Reservatiesysteem
import os
from ADT import MyBSTAnas, MyCircularLinkedChainAnas, MyQueueAnas, MyRedBlackTreeAnas, MyStackAnas
from ADT import MyBSTEmil, MyCircularLinkedChainEmil, MyQueueEmil, MyTwoThreeFourTreeEmil, MyStackEmil
from ADT import MyBSTKars, MyCircularLinkedChainKars, MyQueueKars, MyTwoThreeFourTreeKars, MyStackKars
from ADT import MyBSTTibo, MyCircularLinkedChainTibo, MyQueueTibo, MyTwoThreeFourTreeTibo, MyStackTibo

def test(input_files, controle_files, **kwargs):
    if len(input_files) != len(controle_files):
        raise Exception("niet evenveel inputfiles als outputfiles")

    args = None
    if "args_tup" in kwargs:
        args = kwargs["args_tup"]

    for i, v_in in enumerate(input_files):
        v_out = controle_files[i]

        if args != None:
            r = Reservatiesysteem.Reservatiesysteem(display_mode="", path=f"../testfiles/{v_in}", adt_args=args)
        else:
            r = Reservatiesysteem.Reservatiesysteem(display_mode="", path=f"../testfiles/{v_in}")

        file_compare("../testfiles/log_test.html", f"../testfiles/{v_out}")

#test(file="system_test1.txt")

def file_compare(path1, path2):
    f1 = open(path1, "rt")
    f2 = open(path2, "rt")
    l1 = f1.readlines()
    l2 = f2.readlines()
    if len(l1) != len(l2):
        raise Exception("not matching log file")


    for line_i in range(len(l1)):
        l1t = l1[line_i]
        l2t = l2[line_i]

        l1t = l1t.replace(" ", "")
        l2t = l2t.replace(" ", "")

        if l1t != l2t:
            raise Exception("not matching log file")


adt_dict = {}
with open("../testfiles/ADTFiles.txt") as f:
    for file in f.readlines():

        if file.startswith("#"):
            continue

        file = file.replace("\n", "")
        line_list = file.split(" ")
        adt = line_list[0]

        for i in range(1, len(line_list)):
            t = adt_dict.get(line_list[i], [])
            t.append(adt)
            adt_dict[line_list[i]] = t


index = 0
for i0 in adt_dict.get("0"):
    for i1 in adt_dict.get("1"):
        for i2 in adt_dict.get("2"):
            for i3 in adt_dict.get("3"):
                for i4 in adt_dict.get("4"):
                    for i5 in adt_dict.get("5"):
                        for i6 in adt_dict.get("6"):
                            for i7 in adt_dict.get("7"):
                                for i8 in adt_dict.get("8"):
                                    for i9 in adt_dict.get("9"):
                                        if index % 1000 == 0:
                                            print(index)
                                        test(["system_test9.txt", "system.txt", "system_test6.txt"], ["test_controle9.html", "test_controle0.html", "test_controle6.html"],
                                             args_tup=(i0, i1, i2, i3, i4, i5, i6, i7, i8, i9))
                                        index += 1





