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