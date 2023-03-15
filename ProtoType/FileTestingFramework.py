from ProtoType import Reservatiesysteem
import os

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
                                        print((i0, i1, i2, i3, i4, i5, i6, i7, i8, i9))


def test(**kwargs):
    if "file" in kwargs:
        r = Reservatiesysteem.Reservatiesysteem(display_mode="print", path=f"../testfiles/{kwargs['file']}")
    else:
        for file in os.listdir("../testfiles"):
            if file.endswith(".txt") and not file == "ADTFiles.txt":
                print(f"running {file}")
                print()
                r = Reservatiesysteem.Reservatiesysteem(display_mode="print", path=f"../testfiles/{file}")
                print()
                print()
                print()

                print("-" * 50)

test(file="system_test1.txt")