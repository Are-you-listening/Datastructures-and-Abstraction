"""
Deze ADT wordt gebruikt om de gegeven file uit te lezen en te initialiseren
voor het reservatiesysteem
"""


class InstructionParser:
    def __init__(self, reservatie_systeem, use_adt, **kwargs):
        """
        Maakt een InstructionParser object aan
        Alle commandos dat door dit object wordt aangeroepen moet publiek zijn

        Precondities: Er wordt een geldige ADT gegeven die dezelfde tableinstructies heeft als een queue.
                      Ook wordt er een reference gegeven naar het reservatiesysteem vanwaar deze klasse opgeroepen
                      wordt.
                      Deze klasse mag enkel opgeroepen worden vanuit een reservatiesysteem
                      Via de **kwargs wordt een bestaand path naar een file doorgegeven die aan het juiste file format
                      voldoet.
                      Indien via **kwargs geen path gegeven is, moet het default path bestaan
                      De file moet het juiste file-format bevatten

        :param reservatie_systeem: reference naar reservatiesysteem
        :param use_adt: de adt (queue) dat gebruikt wordt om de toekomstige orders (in tupel vorm) te between
                        volgens format (timestamp, order)
        :param kwargs:kan de key "path" bevatten die een relatief path geeft naar de file die uitgelezen moet worden

        preconditie: de bovenstaande parameters worden correct gegeven
        postcondities: een InstructionParser wordt geinitialiseerd
        """

        """setup default var"""
        self.reservatie_systeem = reservatie_systeem
        self.init_mode = False
        self.start_mode = False
        self.use_adt = use_adt

        self.reservaties_waiting = 0
        self.last_reservatie_time = 0

        """kan custom path"""
        if "path" in kwargs:
            self.path = kwargs["path"]
        else:
            self.path = "../testfiles/system.txt"

    def read_file(self):
        """
        functie om de file uit te lezen
        de init instructions worden ineens uitgevoerd
        de tijd gerelateerde instructies worden bewaard in de gegeven ADT
        precondities: De file voldoet aan het gevraagde format en bevat geen onbekende instructies
                      De file bevat alle instructies chronologisch
                      Indien de line begint met 'zaal', zal het gevolgd worden door 2 integers
                      Indien de line begint met 'film', zal het gevolgd worden door 1 integer, 1 string en 1 rating in
                      deze volgorde.
                      Als de string een spatie bevat, zal de string tussen aanhalingstekens geplaatst worden
                      Indien de line begint met 'vertoning', zal het gevolgd worden door 3 integer, string(datum volgens
                      format jaar-maand-dag), 2 integers.
                      Indien de line begint met 'gebruiker, zal het gevolgd worden door 1 integer, 3 strings
                      Indien een line na de line 'start' voorkomt zal het beginnen met een datum gevolgd door de
                      tijd (uur:minuten)
                      nadien komt het commando argument.
                      Indien dit argument 'reserveer' is, wordt het gevolgd door 3 integers
                      Indien dit argument 'ticket' is, wordt het gevolgd door 2 integers

        postcondities: de instructies worden geinitialiseerd/ klaargezet op hun juiste locatie
        de testfile mag niet het teken dat overeenkomt met \u1000 bevatten
        """

        """set not reading behaviour"""
        with open(self.path, 'rt') as f:
            for line in f.readlines():
                if line[0] == "#":
                    continue

                """verwijder useless data"""
                line = line.replace("\n", "")
                line = line.replace("\u1000", "")
                line = line.replace("\u2028", "")
                line = line.replace("â€¨", "")

                """zorg dat aanhalingstekens bij elkaar blijven"""
                line_tup = self.__split(line, '"')
                for i in range(1, len(line_tup)-1):
                    token = line_tup[i]
                    token_adapt = token.replace(" ", "_\u1000")
                    line = line.replace(f'"{token}"', token_adapt)

                """breng de verdwenen spaties terug"""
                arguments = self.__split(line, " ")
                """
                for i, arg in enumerate(arguments):
                    arguments[i] = arg.replace("_\u1000", " ")
                """

                """replace tokens van string naar spatie"""
                arguments = tuple(arg.replace("_\u1000", " ") for arg in arguments)

                """indien lege line, continue"""
                if arguments[0] == '':
                    continue

                """indien init fase, run init functies"""
                if self.init_mode:
                    self.__init_commands(arguments)

                """indien start fase, start setup (store in queue)"""
                if self.start_mode:
                    self.__setup_commands(arguments)

                if arguments[0] == "init":
                    self.init_mode = True
                    self.start_mode = False

                if arguments[0] == "start":
                    self.start_mode = True
                    self.init_mode = False

    @staticmethod
    def __split(string, split_string):
        """
        splits string door een split_string.
        Equivalent van string.split(''), maar dan zonder python list te gebruiken, maar een tuple te maken
        """
        amount = string.count(split_string)
        if amount == 0:
            return (string,)
        tup = ()
        for j in range(1, amount+2):
            if j < amount+1:
                s_index = string.index(split_string)
                first_part = string[:s_index]
            else:
                first_part = string
                s_index = 0

            tup_len = len(tup)
            t_tup = tuple((tup[i] if tup_len > i else first_part) for i in range(j))
            tup = t_tup
            string = string[s_index+len(split_string):]

        return tup

    def __init_commands(self, args):
        """
        commands die uitgevoerd worden tijdens de initiasie fase
        """
        """
        format zoals in inputfile gegeven
        """
        if args[0] == "zaal":
            """
            0: 'zaal' order
            1: zaalnummer
            2: plaatsen
            """
            self.reservatie_systeem.maak_zaal(int(args[1]), int(args[2]))
        elif args[0] == "film":
            """
            0: 'film' order
            1: filmid
            2: titel
            3: rating
            """
            self.reservatie_systeem.maak_film(int(args[1]), args[2], float(args[3]))
        elif args[0] == "vertoning":
            """
            0: 'vertoning' order
            1: vertoning id
            2: zaal
            3: slot
            4: datum
            5: filmid
            6: aantal plaatsen
            """
            self.reservatie_systeem.maak_vertoning(int(args[1]), int(args[2]), int(args[3]),
                                                   args[4], int(args[5]), int(args[6]))
        elif args[0] == "gebruiker":
            """
            0: 'gebruiker' order
            1: gebruiker id
            2: voornaam
            3: achternaam
            4: e-mail
            """
            self.reservatie_systeem.maak_gebruiker(int(args[1]), args[2], args[3], args[4])

    def __setup_commands(self, args):
        """
        commands die moeten worden uitgevoerd (in volgorde) op hun juiste tijdstip

        """
        datum = args[0]
        time = args[1]

        hour = int(self.__split(time, ":")[0])
        minutes = int(self.__split(time, ":")[1])
        time = self.reservatie_systeem.convert_date(datum, hour, minutes, 0)
        args = tuple(a if i != 1 else time for i, a in enumerate(args))

        tup = (args[1])
        if args[2] == "reserveer":
            tup = (args[1], args[2], args[3], args[4], args[5])
        elif args[2] == "ticket":
            tup = (args[1], args[2], args[3], args[4])
        elif args[2] == "log":
            tup = (args[1], args[2])

        self.use_adt.tableInsert(tup)

    def __check_queue(self, time):
        """
        Checked dat de tijd matched, indien ja, voert instructie uit
        precondities: de tijd dat gegeven wordt is een integer
        postconditie: indien de tijd matched wordt de instructie uitgevoerd
        """
        tup = self.use_adt.tableFirst()[0]
        instruction = tup[1]

        """zet de tijd in het reservatiesysteem naar de gegeven tijd"""

        if self.last_reservatie_time != time and self.reservaties_waiting > 0:
            self.reservatie_systeem.lees_reservatie()

            self.reservaties_waiting -= 1
            return

        self.reservatie_systeem.set_time(time)

        self.last_reservatie_time = time
        """
        new format: datetime, order, args 
        """

        if tup[0] == time:
            if instruction == "reserveer":
                """
                0: datetime
                1: 'reserveer' order
                2: user id
                3: vertoning id
                4: aantal plaatsen
                """
                self.reservatie_systeem.maak_reservatie(int(tup[3]), int(tup[4]), tup[0], int(tup[2]))
                self.reservaties_waiting += 1
            elif instruction == "ticket":
                """
                0: datetime
                1: 'ticket' order
                2: vertoning id
                3: aantal plaatsen
                """
                self.reservatie_systeem.lees_ticket(int(tup[2]), int(tup[3]))
            elif instruction == "log":
                """
                0: datetime
                1: 'log' order
                """
                self.reservatie_systeem.log()

            """haal element weg uit de queue"""
            self.use_adt.tableDelete()

    def __get_time(self):
        """
        ontvang de tijd van het eerste element in de queue
        """
        if self.use_adt.tableIsEmpty():
            return None
        else:
            return self.use_adt.tableFirst()[0][0]

    def main_thread(self):
        """
        preconditie: wordt 1 keer opgeroepen vanuit hetzelfde reservatiesysteem dat ook werd doorgegeven in de
                     constructor.
        postconditie: alle instructies worden chronologisch uitgevoerd
        """
        time = self.__get_time()
        while time is not None:
            self.__check_queue(time)
            time = self.__get_time()
