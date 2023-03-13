from ProtoType import Reservatiesysteem
import os


def test(**kwargs):
    if "file" in kwargs:
        r = Reservatiesysteem.Reservatiesysteem(display_mode="print", path=f"../testfiles/{kwargs['file']}")
    else:
        for file in os.listdir("../testfiles"):
            if file.endswith(".txt"):
                print(f"running {file}")
                print()
                r = Reservatiesysteem.Reservatiesysteem(display_mode="print", path=f"../testfiles/{file}")
                print()
                print()
                print()

                print("-" * 50)

test(file="system_test1.txt")