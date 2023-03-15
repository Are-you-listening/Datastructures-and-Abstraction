from ADT import *
import Reservatiesysteem


class log:
    def __init__(self, reservatiesysteem, use_ADT):
        self.resSYS = reservatiesysteem
        self.resSYS.vertoningen.traverseTable(self.add_to_info)

        self.header_string = ""
        self.text_string = ""
        self.sorting_tree = use_ADT
        self.current = (0, 0, -1, 1)

    def log(self):  # Public

        """
        self.vertoningen.traverseTable(self.add_to_info)
        stringlist = MyCircularLinkedChainAnas.LCTable()

        stringlist.tableInsert(stringlist.tableGetLength()+1,"<thead>")
        stringlist.tableInsert(stringlist.tableGetLength() + 1, "<td>Datum</td>")
        stringlist.tableInsert(stringlist.tableGetLength() + 1, "<td>Film</td>")

        #Voeg alle tijdslots toe
        for i in range(self.slots.tableGetLength()+1):
            slot = self.slots.tableRetrieve(i)[0] #Seconden van het tijdslot
            slot = int("00000000"+str(slot)) #Restore het format juist
            tijdslot = self.convert_time(slot)[1] + ":" + self.convert_time(slot)[2]
            stringlist.tableInsert(stringlist.tableGetLength() + 1, f"<td>{tijdslot}<td\>")

        stringlist.tableInsert(stringlist.tableGetLength() + 1, "</thead>") #Sluit thead
        stringlist.tableInsert(stringlist.tableGetLength() + 1, "<tbody>") #Open Body
        stringlist.tableInsert(stringlist.tableGetLength() + 1, "<tr>")

        #hier data

        stringlist.tableInsert(stringlist.tableGetLength() + 1, "</tr>")
        stringlist.tableInsert(stringlist.tableGetLength() + 1, "</tbody>")


        print(self.info.save())
        self.add_tijdslot(500099987)
        print(self.slots.save())
        #(datum,film,listt[(G,tijd)])
        """


        for i in range(1, self.slots.tableGetLength() + 1):
            slot = self.slots.tableRetrieve(i)[0]
            self.sorting_tree.tableInsert(slot, slot)
        self.sorting_tree.traverseTable(self.log_add_header)

        self.sorting_tree.clear()
        for i in range(1, self.info.tableGetLength() + 1):
            tup = self.info.tableRetrieve(i)[0]
            datum = tup[0].replace("-", "")
            filmid = tup[1]
            slot = tup[3]
            key_value = int(datum + str(filmid) + str(slot))
            self.sorting_tree.tableInsert(key_value, tup)

        self.sorting_tree.traverseTable(self.log_add_data)

        current_datum, current_tijd, current_film, current_index = self.current
        while current_index != self.slots.tableGetLength() + 1:
            self.text_string += """<td></td>"""
            current_index += 1

        result_string = """
        <html>
            <head>
                <style>
                    table {
                        border-collapse: collapse;
                    }
    
                    table, td, th {
                        border: 1px solid black;
                   }
                </style>
            </head>
            <body>
                <h1>Log op 2023-10-10 18:00</h1>
                <table>
                    <thead>
                        <td>Datum</td>
                        <td>Film</td>"""

        result_string += self.header_string

        tabs = '\t' * 5
        result_string += f"\n{tabs}</thead>"
        result_string += self.text_string
        result_string += """
                        </tr>
                    </tbody>
                </table>
            </body>
        </html>"""

        print(result_string)
        with open("../testfiles/log_test.html", 'wt') as f:
            f.write(result_string)
            f.close()

    def log_add_header(self, value):
        value = int(f"10000000{value}")  # Value = 1 slot
        minutes = str(self.convert_time(value)[2])
        tijdslot = str(self.convert_time(value)[1]) + ":" + "0" * (2 - len(minutes)) + minutes
        tabs = '\t' * 6
        self.header_string += f"\n{tabs}<td>{tijdslot}</td>"

    def add_to_info(self, value):
        current_slot = self.convert_time(self.tijdsstip)[1] * 3600 + self.convert_time(self.tijdsstip)[2] * 60
        self.info.tableInsert(1, (value[0].datum, value[0].filmid, value[0].status(current_slot), value[0].slot))

    def log_add_data(self, value):
        datum = value[0]
        datum_int = int(datum.replace("-", ""))
        tijd = value[3]
        current_datum, current_tijd, current_film, current_index = self.current
        tabs = '\t' * 6

        if (datum_int > current_datum) or (value[1] != current_film):
            if current_datum != 0:
                self.text_string += f"""\n</tr> </tbody>"""
                while current_index != self.slots.tableGetLength():
                    self.text_string += """\n<td></td>"""
                    current_index += 1

            tenp_tabs = "\t" * 5
            self.text_string += f"""\n{tenp_tabs}<tbody> <tr>"""
            self.text_string += f"\n{tabs}<td>{datum}</td>"
            self.text_string += f"\n{tabs}<td>{self.films.tableRetrieveTranverse(value[1])[0].titel}</td>"
            current_index = 1

        tijd_slot = self.slots.tableRetrieve(current_index)[0]
        while tijd_slot != tijd:
            self.text_string += f"""\n{tabs}<td></td>"""

            current_index += 1
            tijd_slot = self.slots.tableRetrieve(current_index)[0]

        self.text_string += f"\n{tabs}<td>{value[2]}</td>"
        self.current = (datum_int, tijd, value[1], current_index + 1)