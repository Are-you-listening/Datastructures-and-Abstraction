from ProtoType import Reservatiesysteem
import os

def test(**kwargs):
    if "file" in kwargs:
        r = Reservatiesysteem.Reservatiesysteem(display_mode="print", path=f"../testfiles/{kwargs['file']}")
    else:
        for file in os.listdir("../testfiles"):
            if file.endswith(".txt") and not file == "ADTFiles.txt":
                #print(f"running {file}")
                #print()

                if "args_tup" in kwargs:
                    r = Reservatiesysteem.Reservatiesysteem(display_mode="", path=f"../testfiles/{file}", adt_args=kwargs["args_tup"])
                else:
                    r = Reservatiesysteem.Reservatiesysteem(display_mode="print", path=f"../testfiles/{file}")
                #print()
                #print()
                #print()

                #print("-" * 50)

    file_compare("../testfiles/log_test.html", "../testfiles/test_controle.html")

#test(file="system_test1.txt")

def file_compare(path1, path2):
    f1 = open(path1, "rt")
    f2 = open(path2, "rt")
    l1 = f1.readlines()
    l2 = f2.readlines()
    if len(l1) != len(l2):
        raise Exception("not matching log file")
    for line_i in range(len(l1)):
        if l1[i] != l2[i]:
            raise Exception("not matching log file")


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

"""
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
                                        print(index, (i0, i1, i2, i3, i4, i5, i6, i7, i8, i9))

                                        #print((i0, i1, i2, i3, i4, i5, i6, i7, i8, i9))
                                        test(args_tup=(i0, i1, i2, i3, i4, i5, i6, i7, i8, i9))
                                        index += 1
"""

"""
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
                                        print(index, (i0, i1, i2, i3, i4, i5, i6, i7, i8, i9))

                                        #print((i0, i1, i2, i3, i4, i5, i6, i7, i8, i9))
                                        test(args_tup=(i0, i1, i2, i3, i4, i5, i6, i7, i8, i9))
                                        index += 1
"""

"""
for i in range(0, 40):
    print(i)
    
    t0 = adt_dict.get("0")
    t1 = adt_dict.get("1")
    t2 = adt_dict.get("2")
    t3 = adt_dict.get("3")
    t4 = adt_dict.get("4")
    t5 = adt_dict.get("5")
    t6 = adt_dict.get("6")
    t7 = adt_dict.get("7")
    t8 = adt_dict.get("8")
    t9 = adt_dict.get("9")

    i0 = t0[i % len(t0)]
    i1 = t1[i % len(t1)]
    i2 = t2[i % len(t2)]
    i3 = t3[i % len(t3)]
    i4 = t4[i % len(t4)]
    i5 = t5[i % len(t5)]
    i6 = t6[i % len(t6)]
    i7 = t7[i % len(t7)]
    i8 = t8[i % len(t8)]
    i9 = t9[i % len(t9)]

    test(args_tup=(i0, i1, i2, i3, i4, i5, i6, i7, i8, i9))
"""

"""
index = 0
for i0 in adt_dict.get("0"):
    for i1 in adt_dict.get("1"):
        for i2 in adt_dict.get("2"):
            for i3 in adt_dict.get("3"):
                for i4 in adt_dict.get("4"):
                    for i5 in adt_dict.get("5"):
                        for i6 in adt_dict.get("6"):
                            i7 =adt_dict.get("7")[0]
                            i8 = adt_dict.get("8")[0]
                            i9 = adt_dict.get("9")[0]
                            print(index)

                            # print((i0, i1, i2, i3, i4, i5, i6, i7, i8, i9))
                            test(args_tup=(i0, i1, i2, i3, i4, i5, i6, i7, i8, i9))
                            index += 1
"""

"""
index = 0
for i0 in adt_dict.get("0"):
    for i1 in adt_dict.get("1"):
        for i2 in adt_dict.get("2"):
            for i3 in adt_dict.get("3"):
                for i4 in adt_dict.get("4"):
                    for i5 in adt_dict.get("5"):
                        for i6 in adt_dict.get("6"):
                            i7 =adt_dict.get("7")[0]
                            i8 = adt_dict.get("8")[0]
                            i9 = adt_dict.get("9")[0]
                            print(index)

                            # print((i0, i1, i2, i3, i4, i5, i6, i7, i8, i9))
                            test(file="system_test2.txt", args_tup=(i0, i1, i2, i3, i4, i5, i6, i7, i8, i9))
                            index += 1
"""

test(file="system_test2.txt")
