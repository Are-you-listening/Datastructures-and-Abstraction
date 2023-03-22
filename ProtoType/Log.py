"""
Deze ADT geeft een logsysteem weer

Data:
self.header_string: bewaard de header regel van de tabel
self.text_string: beaard alle data die in de tabel hoort te staan
self.sorting_tree: bewaard een ADT
self.current: bewaard current locaties nodig voor te detecteren in het geval van lege slots en onderscheid tussen films
self.resSYS: reference naar reservatiesysteem
"""

class Log:
    def __init__(self, reservatiesysteem, use_ADT):
        """
        precondities: Er wordt een geldige ADT gegeven die dezelfde tableinstructies heeft als een zoekboom.
                      Ook wordt er een reference gegeven naar het reservatiesysteem vanwaar deze klasse opgeroepen wordt.
                      Deze klasse mag enkel opgeroepen worden vanuit een reservatiesysteem
        postcondities: er wordt een log aangemaakt in html format

        :param: reservatiesysteem: Reservatiesysteem Object
        :param: use_ADT: een adt dat gebruikt wordt om data te sorteren
        """

        self.header_string = ""
        self.text_string = ""
        self.sorting_tree = use_ADT
        self.current = (0, 0, -1, 1)

        self.resSYS = reservatiesysteem


    def create_log(self):  # Public
        """
        maakt een log aan

        precondities: er worden geen parameters gegeven

        store alle timeslots in een sorting tree, om een gesorteerde string te vormen (header)
        die alle tijdslots chronlogisch plaatst
        """
        for i in range(1, self.resSYS.slots.tableGetLength() + 1):
            slot = self.resSYS.slots.tableRetrieve(i)[0]
            self.sorting_tree.tableInsert(slot, slot)
        self.sorting_tree.traverseTable(self.__log_add_header)
        self.sorting_tree.clear()

        """
        Gebruik dezelfde tree om alle films te sorteren zodat:
        Alle films (met dezelfde datum) hun slots bij elkaar staan
        """
        self.resSYS.vertoningen.traverseTable(self.__add_to_info)
        self.sorting_tree.traverseTable(self.__log_add_data)

        """we vullen de niet ingevulde slot aan het einde op"""
        current_datum, current_tijd, current_film, current_index = self.current
        while current_index != self.resSYS.slots.tableGetLength() + 1:
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

        """toevoeging van header"""
        result_string += self.header_string

        tabs = '\t' * 5
        result_string += f"\n{tabs}</thead>"
        """toevoeging van data"""
        result_string += self.text_string
        result_string += """
                        </tr>
                    </tbody>
                </table>
            </body>
        </html>"""

        with open("../testfiles/log_test.html", 'wt') as f:
            f.write(result_string)
            f.close()

    def __log_add_header(self, value):
        """leest value uit, convert naar string time, voeg toe aan header string"""
        value = int(value)  # Value = 1 slot
        minutes = str(self.resSYS.convert_time(value)[2])
        tijdslot = str(self.resSYS.convert_time(value)[1]) + ":" + "0" * (2 - len(minutes)) + minutes
        tabs = '\t' * 6
        self.header_string += f"\n{tabs}<td>{tijdslot}</td>"

    def __add_to_info(self, value):
        """
        leest de vertoning uit en stored die in de sorting_tree
        """
        current_slot = self.resSYS.convert_time(self.resSYS.tijdsstip)[1] * 3600 + self.resSYS.convert_time(self.resSYS.tijdsstip)[2] * 60
        tup = (value[0].datum, value[0].filmid, value[0].status(current_slot), value[0].slot)
        datum = tup[0].replace("-", "")
        filmid = tup[1]
        slot = tup[3]
        key_value = int(datum + str(filmid) + str(slot))
        self.sorting_tree.tableInsert(key_value, tup)

    def __log_add_data(self, value):
        print(value)
        """
        Leest de vertoning uit en voegt het toe aan de output string
        """
        datum = value[0]
        datum_int = int(datum.replace("-", ""))
        tijd = value[3]
        current_datum, current_tijd, current_film, current_index = self.current
        tabs = '\t' * 6

        """indien de datum/film niet matched gaan we naar een volgende regel"""
        if (datum_int > current_datum) or (value[1] != current_film):
            if current_datum != 0:
                """opvullen van huidige regel"""
                while current_index != self.resSYS.slots.tableGetLength()+1:
                    self.text_string += """\n<td></td>"""
                    current_index += 1
                self.text_string += f"""\n</tr> </tbody>"""



            tenp_tabs = "\t" * 5
            self.text_string += f"""\n{tenp_tabs}<tbody> <tr>"""
            self.text_string += f"\n{tabs}<td>{datum}</td>"
            self.text_string += f"\n{tabs}<td>{self.resSYS.films.tableRetrieveTranverse(value[1]).titel}</td>"
            current_index = 1

        """we gaan steeds een tijdslot verder totdat de tijdslot matched"""
        tijd_slot = self.resSYS.slots.tableRetrieve(current_index)[0]
        while tijd_slot != tijd:
            self.text_string += f"""\n{tabs}<td></td>"""

            current_index += 1
            tijd_slot = self.resSYS.slots.tableRetrieve(current_index)[0]

        """voeg de data toe onder de tijdslot"""
        self.text_string += f"\n{tabs}<td>{value[2]}</td>"
        self.current = (datum_int, tijd, value[1], current_index + 1)
