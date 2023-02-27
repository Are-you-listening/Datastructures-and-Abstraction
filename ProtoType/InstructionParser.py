
class InstructionParser:
    def __init__(self, reservatie_systeem, use_adt, **kwargs):
        """
        Maakt een InstructionParser object aan
        Alle commandos dat door dit object wordt aangeroepen moet publiek zijn

        :param reservatie_systeem: refrence naar reservatiesysteem
        :param use_adt: de adt (queue) dat gebruikt wordt om de toekomstige orders (in tupel vorm) te bewren
                        volgens format (timestamp, order)
        :param kwargs:kan de key "path" bevatten die een relatief path geeft naar de file die uitgelezen moet worden

        preconditie: de parameters worden correct gegeven, er wordt een correct path gegeven
        postcondities: een InstructionParser wordt geinitialiseerd
        """

        self.reservatie_systeem = reservatie_systeem
        self.init_mode = False
        self.start_mode = False
        self.use_adt = use_adt

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
        postcondities: de instructies worden geinitialiseerd/ klaargezet op hun juiste locatie

        """
        with open(self.path, 'rt') as f:
            for line in f.readlines():
                if line[0] == "#":
                    continue

                """verwijder useless data"""
                line = line.replace("\n", "")
                line = line.replace("\u2028", "")

                """zorg dat movies met spaties bij elkaar blijven"""
                line_array = line.split('"')
                if len(line_array) > 1:
                    movie = line_array[1]
                    movie_adapt = movie.replace(" ", "_")
                    line = line.replace(f'"{movie}"', movie_adapt)

                arguments = line.split(" ")
                if len(arguments) > 2:
                    arguments[2] = arguments[2].replace("_", " ")

                if arguments[0] == '':
                    continue

                if self.init_mode:
                    self.__init_commands(arguments)

                if self.start_mode:
                    self.__setup_commands(arguments)

                if arguments[0] == "init":
                    self.init_mode = True
                    self.start_mode = False

                if arguments[0] == "start":
                    self.start_mode = True
                    self.init_mode = False

    def __init_commands(self, args):
        """
        private instruction

        """
        if args[0] == "zaal":
            self.reservatie_systeem.maak_zaal(int(args[1]), int(args[2]))
        elif args[0] == "film":
            self.reservatie_systeem.maak_film(args[2], args[3])
        elif args[0] == "vertoning":
            self.reservatie_systeem.maak_vertoning(int(args[2]), int(args[3]), args[4], int(args[5]))
        elif args[0] == "gebruiker":
            self.reservatie_systeem.maak_gebruiker(args[2], args[3], args[4])

    def __setup_commands(self, args):
        """
        private instruction

        """
        datum = args[0]
        time = args[1]

        hour = int(time.split(":")[0])
        minutes = int(time.split(":")[1])
        time = self.reservatie_systeem.convert_date(datum, hour, minutes, 0)
        args[1] = time

        tup = tuple(args[1:])
        #print(tup)
        if tup[1] == "reserveer":
            self.reservatie_systeem.maak_reservatie(int(tup[3]), int(tup[2]), tup[0], int(tup[2]))
            tup = (args[1], "lees_reservatie")

        self.use_adt.tableInsert(tup)

    def check_queue(self, time):
        """
        Checkt dat de tijd matched, indien ja, voert instructie uit
        precondities: de tijd dat gegeven wordt is een integer
        postoconditie: indien de tijd matched wordt de instructie uitgevoerd
        """
        tup = self.use_adt.tableFront()[0]
        instruction = tup[1]

        if tup[0] == time:
            #print(tup)
            if instruction == "lees_reserveer":
                pass
            elif instruction == "ticket":
                pass
            elif instruction == "log":
                pass

            self.use_adt.tableDelete()

    def get_time(self):
        return self.use_adt.tableFront()[0][0]

    def __str__(self):
        """
        DEBUG
        REMOVE LATER
        :return:
        """

        return str(self.use_adt.tableRetrieve(None))

