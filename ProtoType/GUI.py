from tkinter import *
from tkinter import ttk, font
import math
import datetime
import threading
import time
from Reservatiesysteem import Reservatiesysteem


class GUI:
    def __init__(self, reservatiesysteem):
        """
        setup GUI
        precondities: Er moet een geldig reservatiesysteem meeegegeven worden
        postconditie: Er wordt een GUI die het reservatiesysteem weergeeft getoont
        """

        self.reservatiesysteem = reservatiesysteem

        """aanmaken GUI screen"""
        self.screen = Tk()
        self.screen.geometry("1920x1280")
        self.tab_manager = ttk.Notebook(self.screen)
        self.main_dashboard = Frame(self.tab_manager)

        """support voor meerdere tabs"""
        self.tab_manager.add(self.main_dashboard, text="main tab")
        self.tab_manager.pack(expand=True, fill=BOTH)

        """define de frame waar alle vertoningen worden gezet"""
        self.vertoning_frame = Frame(self.main_dashboard, width=1920, height=960)
        self.vertoning_frame.pack(side=TOP, anchor=NW)

        """
        geef de vertoningen een default row en column
        en gebruik de self.__refresh_vertoningen() om de vertoningen weer te geven
        """
        self.row_col = (0, 0)
        self.__refresh_vertoningen()

        """
        Maakt een frame aan voor de commando buttons
        """
        self.button_frame = Frame(self.main_dashboard)
        self.button_frame.pack(side=BOTTOM, anchor=SW)

        """
        bewaard de entries van een butoon
        en welke button aangeklikt is
        """
        self.entry_labels = ()
        self.entries = ()
        self.option_selected = None

        """
        boxes voor te kunnen kiezen uit een lijst
        """
        self.film_box = None
        self.zaal_box = None
        self.slots = None
        self.vertoning_box = None
        self.gebruiker_box = None

        """
        submit_button: uitvoeren van actie
        time_label: geeft de tijd weer
        """
        self.submit_button = None
        self.time_label = None

        self.loading = Label(self.main_dashboard, text="Loading...", font=font.Font(size=20))

        """
        bewaard de huidge tijd in de GUI
        """
        self.current_time = self.reservatiesysteem.get_time()

        """
        roept setup routine op
        """
        self.__setup_buttons()
        self.__setup_time()

    def __add_vertoning(self, vertoning_tup):
        """voorkomt dat de hoofdpagina volledig opgevuld wordt max 25 vertoningen worden weergegeven"""
        if self.row_col[0] > 5:
            return
        """lesst vertoning object uit"""
        vertoning_object = vertoning_tup[0]
        vertoning_frame = LabelFrame(self.vertoning_frame, text=f"vertoning {vertoning_object.get_id()}")
        vertoning_frame.grid(row=self.row_col[0], column=self.row_col[1], sticky="news")

        film_id = vertoning_object.filmid
        film_retrieve_tup = self.reservatiesysteem.films.tableRetrieve(film_id)
        if not film_retrieve_tup[1]:
            film_name = "not loaded"
        else:
            film_name = film_retrieve_tup[0].titel

        """
        Geeft info over de vertoning weer
        """
        info_frame = LabelFrame(vertoning_frame, text=f"Info")
        info_frame.grid(row=0, column=0)

        film_label = Label(info_frame, text=f"Film: {film_name}", wraplength=120)
        film_label.pack(anchor="w")

        zaalnummer = vertoning_object.zaalnummer
        zaal_label = Label(info_frame, text=f"Zaal: {zaalnummer}")
        zaal_label.pack(anchor="w")

        status = vertoning_object.status(self.reservatiesysteem.get_time())
        status_label = Label(info_frame, text=f"Status: {status}")
        status_label.pack(anchor="w")

        """
        stelt super cool cirkeldiagram op
        """
        reservaties = vertoning_object.vrije_plaatsen - vertoning_object.vrije_plaatsenVirtueel
        aanwezige = vertoning_object.vrije_plaatsenFysiek
        self.__create_vertoning_diagram(vertoning_frame, aanwezige, reservaties, vertoning_object.vrije_plaatsen)

        """
        veranderd de volgende row/column positie
        """
        if self.row_col[1] < 5:
            self.row_col = (self.row_col[0], self.row_col[1]+1)
        else:
            self.row_col = (self.row_col[0]+1, 0)

    def __create_vertoning_diagram(self, root, tickets, reservaties, plaatsen):
        """
        maakt vertoning diagram
        """

        """
        definieer de middenpositie van het diagram en de radius
        """
        canvas_mid = (100, 100)
        radius = 80

        """
        canvas wordt aangemaakt
        """
        diagram = Canvas(root, width=200, height=200)
        diagram.grid(row=0, column=1)

        """
        de grote cirkel (100%) wordt getekend
        """
        diagram.create_oval(canvas_mid[0] - radius+2, canvas_mid[1] - radius+2, canvas_mid[0] + radius-2,
                            canvas_mid[1] + radius-2, fill="gray", outline="gray")

        """
        Een deel van de cirkel wordt in het blauw ingekleurd (overeenkomstig met % reservaties)
        """
        rPCT = reservaties/plaatsen
        for i in range(round(rPCT*1000)):
            angle = 2*math.pi*i/1000-math.pi/2
            diagram.create_line(canvas_mid[0], canvas_mid[1], canvas_mid[0]+math.cos(angle)*radius, canvas_mid[1]+math.sin(angle)*radius, width=10, fill="#006AFF")

        """
        Een deel van de cirkel wordt in het groen ingekleurd (overeenkomstig met % tickets)
        """
        tPCT = tickets / plaatsen
        for i in range(round(tPCT * 1000)):
            angle = 2 * math.pi * i / 1000 - math.pi / 2
            diagram.create_line(canvas_mid[0], canvas_mid[1], canvas_mid[0] + math.cos(angle) * (radius+1),
                                canvas_mid[1] + math.sin(angle) * (radius+1), width=10, fill="#00FF00")

        """
        Kleine middencirkel wordt getekend
        """
        diagram.create_oval(canvas_mid[0]-radius/2, canvas_mid[1]-radius/2, canvas_mid[0]+radius/2,
                            canvas_mid[1]+radius/2, fill="#D9D9D9", outline='#D9D9D9')

        """
        de waardes worden in die middencirkel weergegeven
        """
        diagram.create_text(100, 90, text=f"{reservaties}/{plaatsen}")
        diagram.create_text(100, 110, text=f"{tickets}/{reservaties}")

    def __setup_buttons(self):
        self.submit_button = Button(self.button_frame, text="submit", font=font.Font(size=20), command=self.__execute_order)

        self.img_1 = PhotoImage(file="../GUI_images/vertoning.png", width=100, height=100)
        b = Button(self.button_frame, image=self.img_1, command=self.__maak_vertoning_res)
        b.grid(row=0, column=0)

        self.img_2 = PhotoImage(file="../GUI_images/zaal.png", width=100, height=100)
        b = Button(self.button_frame, image=self.img_2, command=self.__maak_zaal_res)
        b.grid(row=0, column=1)

        self.img_3 = PhotoImage(file="../GUI_images/Film.png", width=100, height=100)
        b = Button(self.button_frame, image=self.img_3, command=self.__maak_film_res)
        b.grid(row=1, column=0)

        self.img_4 = PhotoImage(file="../GUI_images/gebruiker.png", width=100, height=100)
        b = Button(self.button_frame, image=self.img_4, command=self.__maak_gebruiker_res)
        b.grid(row=1, column=1)

        self.img_5 = PhotoImage(file="../GUI_images/reserveer.png", width=100, height=100)
        b = Button(self.button_frame, image=self.img_5, command=self.__maak_reservatie_res)
        b.grid(row=0, column=2)

        self.img_6 = PhotoImage(file="../GUI_images/ticket.png", width=100, height=100)
        b = Button(self.button_frame, image=self.img_6, command=self.__maak_ticket)
        b.grid(row=1, column=2)

    def __setup_time(self):
        date_frame = LabelFrame(self.main_dashboard, text=f"Huidig tijdstip")
        date_frame.pack(side=LEFT, anchor=SW)

        time_tup = self.reservatiesysteem.convert_time(self.current_time)
        self.time_label = Label(date_frame, text=f"{time_tup[0]}, {time_tup[1]}:{'0'*(2-len(str(time_tup[2])))+str(time_tup[2])}:{'0'*(2-len(str(time_tup[3])))+str(time_tup[3])}", font=font.Font(size=20))
        self.time_label.pack()
        self.img_7 = PhotoImage(file="../GUI_images/arrow1.png", width=25, height=25)
        Button(date_frame, image=self.img_7, command=self.__speed_up_1).pack(side=LEFT)

        self.img_8 = PhotoImage(file="../GUI_images/arrow2.png", width=25, height=25)
        Button(date_frame, image=self.img_8, command=self.__speed_up_2).pack(side=LEFT)

        self.img_9 = PhotoImage(file="../GUI_images/arrow3.png", width=25, height=25)
        Button(date_frame, image=self.img_9, command=self.__speed_up_3).pack(side=LEFT)

    def __speed_up_1(self):
        time_tup = self.reservatiesysteem.convert_time(self.current_time)

        time = datetime.datetime.strptime(f"{time_tup[0]}-{time_tup[1]}-{time_tup[2]}-{time_tup[3]}", '%Y-%m-%d-%H-%M-%S')
        time += datetime.timedelta(minutes=1)

        self.__set_new_time(time)

    def __speed_up_2(self):
        time_tup = self.reservatiesysteem.convert_time(self.current_time)

        time = datetime.datetime.strptime(f"{time_tup[0]}-{time_tup[1]}-{time_tup[2]}-{time_tup[3]}",
                                          '%Y-%m-%d-%H-%M-%S')
        time += datetime.timedelta(hours=1)

        self.__set_new_time(time)

    def __speed_up_3(self):
        time_tup = self.reservatiesysteem.convert_time(self.current_time)

        time = datetime.datetime.strptime(f"{time_tup[0]}-{time_tup[1]}-{time_tup[2]}-{time_tup[3]}",
                                          '%Y-%m-%d-%H-%M-%S')
        time += datetime.timedelta(days=1)

        self.__set_new_time(time)


    def __set_new_time(self, time):
        year = str(time.year)
        month = str(time.month)
        day = str(time.day)
        year = "0" * (4 - len(year)) + year
        month = "0" * (2 - len(month)) + month
        day = "0" * (2 - len(day)) + day

        self.current_time = self.reservatiesysteem.convert_date(f"{year}-{month}-{day}", time.hour,
                                                                time.minute, time.second)
        self.reservatiesysteem.set_time(self.current_time)
        time_tup = self.reservatiesysteem.convert_time(self.current_time)
        self.time_label.config(
            text=f"{time_tup[0]}, {time_tup[1]}:{'0' * (2 - len(str(time_tup[2]))) + str(time_tup[2])}:{'0' * (2 - len(str(time_tup[3]))) + str(time_tup[3])}")

        self.__refresh_vertoningen()
    def __maak_film_res(self):
        if self.option_selected == "film":
            self.option_selected = None
            self.__reset_entries()
            return

        self.__reset_entries()
        self.option_selected = "film"

        """Titel input"""
        titel_label = Label(self.button_frame, text="Titel: ", font=font.Font(size=20))
        titel_label.grid(row=0, column=3)

        entry = Entry(self.button_frame, width=20, font=font.Font(size=20))
        entry.focus_set()
        entry.grid(row=0, column=4)

        """Rating input"""
        rating_label = Label(self.button_frame, text="Rating: ", font=font.Font(size=20))
        rating_label.grid(row=1, column=3)

        rat_entry = Scale(self.button_frame, from_=0, to=100, orient=HORIZONTAL, width=20, length=200)
        rat_entry.focus_set()
        rat_entry.grid(row=1, column=4)

        self.submit_button.grid(row=1, column=5)

        self.entry_labels = (titel_label, rating_label)
        self.entries = (entry, rat_entry)

    def __maak_zaal_res(self):
        if self.option_selected == "zaal":
            self.option_selected = None
            self.__reset_entries()
            return

        self.__reset_entries()
        self.option_selected = "zaal"

        """zaalnummer input"""
        zaal_nr_label = Label(self.button_frame, text="Zaalnummer: ", font=font.Font(size=20))
        zaal_nr_label.grid(row=0, column=3)

        entry = Entry(self.button_frame, width=20, font=font.Font(size=20))
        entry.focus_set()
        entry.grid(row=0, column=4)

        """plaatsen input"""
        plaatsen_label = Label(self.button_frame, text="Aantal plaatsen: ", font=font.Font(size=20))
        plaatsen_label.grid(row=1, column=3)

        plaatsen_entry = Entry(self.button_frame, width=20, font=font.Font(size=20))
        plaatsen_entry.focus_set()
        plaatsen_entry.grid(row=1, column=4)

        self.submit_button.grid(row=1, column=5)

        self.entry_labels = (zaal_nr_label, plaatsen_label)
        self.entries = (entry, plaatsen_entry)

    def __maak_gebruiker_res(self):
        if self.option_selected == "gebruiker":
            self.option_selected = None
            self.__reset_entries()
            return

        self.__reset_entries()
        self.option_selected = "gebruiker"

        """Voornaam input"""
        vr_label = Label(self.button_frame, text="Voornaam: ", font=font.Font(size=20))
        vr_label.grid(row=0, column=3)

        vr_entry = Entry(self.button_frame, width=20, font=font.Font(size=20))
        vr_entry.focus_set()
        vr_entry.grid(row=0, column=4)

        """achternaam input"""
        ar_label = Label(self.button_frame, text="Achternaam: ", font=font.Font(size=20))
        ar_label.grid(row=1, column=3)

        ar_entry = Entry(self.button_frame, width=20, font=font.Font(size=20))
        ar_entry.focus_set()
        ar_entry.grid(row=1, column=4)

        """e-mail input"""
        m_label = Label(self.button_frame, text="E-mail: ", font=font.Font(size=20))
        m_label.grid(row=1, column=5)

        m_entry = Entry(self.button_frame, width=20, font=font.Font(size=20))
        m_entry.focus_set()
        m_entry.grid(row=1, column=6)

        self.submit_button.grid(row=1, column=7)

        self.entry_labels = (vr_label, ar_label, m_label)
        self.entries = (vr_entry, ar_entry, m_entry)

    def __maak_vertoning_res(self):
        if self.option_selected == "vertoning":
            self.option_selected = None
            self.__reset_entries()
            return

        self.__reset_entries()
        self.option_selected = "vertoning"

        film_box_label = Label(self.button_frame, text="Film: ", font=font.Font(size=20))
        film_box_label.grid(row=0, column=3)

        self.film_box = Listbox(self.button_frame, selectmode="single", height=10, exportselection=False)
        self.film_box.grid(row=0, column=4, rowspan=2)

        self.reservatiesysteem.films.traverseTable(self.__filmbox_add)

        zaal_box_label = Label(self.button_frame, text="Zaal: ", font=font.Font(size=20))
        zaal_box_label.grid(row=0, column=5)

        self.zaal_box = Listbox(self.button_frame, selectmode="single", height=10, exportselection=False)
        self.zaal_box.grid(row=0, column=6, rowspan=2)

        self.reservatiesysteem.zalen.traverseTable(self.__zaalbox_add)

        slot_box_label = Label(self.button_frame, text="Slot: ", font=font.Font(size=20))
        slot_box_label.grid(row=0, column=7)

        self.slot_box = Listbox(self.button_frame, selectmode="single", height=10, exportselection=False)
        self.slot_box.grid(row=0, column=8, rowspan=2)

        self.reservatiesysteem.slots.traverseTable(self.__slotbox_add)

        datum_label = Label(self.button_frame, text="Datum: (format: jaar-maand-dag)", font=font.Font(size=18))
        datum_label.grid(row=0, column=9)

        datum_entry = Entry(self.button_frame, width=20, font=font.Font(size=20))
        datum_entry.focus_set()
        datum_entry.grid(row=1, column=9)

        self.submit_button.grid(row=1, column=10)

        self.entry_labels = (film_box_label, zaal_box_label, slot_box_label, datum_label)
        self.entries = (self.film_box, self.zaal_box, self.slot_box, datum_entry)

    def __maak_reservatie_res(self):
        if self.option_selected == "reservatie":
            self.option_selected = None
            self.__reset_entries()
            return

        self.__reset_entries()
        self.option_selected = "reservatie"

        gebruiker_box_label = Label(self.button_frame, text="User: ", font=font.Font(size=20))
        gebruiker_box_label.grid(row=0, column=3)

        self.gebruiker_box = Listbox(self.button_frame, selectmode="single", height=10, exportselection=False)
        self.gebruiker_box.grid(row=0, column=4, rowspan=2)

        self.reservatiesysteem.gebruikers.traverseTable(self.__gebruikerbox_add)

        vertoning_box_label = Label(self.button_frame, text="Vertoning: ", font=font.Font(size=20))
        vertoning_box_label.grid(row=0, column=5)

        self.vertoning_box = Listbox(self.button_frame, selectmode="single", height=10, exportselection=False)
        self.vertoning_box.grid(row=0, column=6, rowspan=2)

        self.reservatiesysteem.vertoningen.traverseTable(self.__vertoningbox_add)

        plaatsen_label = Label(self.button_frame, text="Plaatsen:", font=font.Font(size=18))
        plaatsen_label.grid(row=0, column=7)

        plaatsen_entry = Entry(self.button_frame, width=10, font=font.Font(size=20))
        plaatsen_entry.focus_set()
        plaatsen_entry.grid(row=1, column=7)

        self.submit_button.grid(row=1, column=8)

        self.entry_labels = (gebruiker_box_label, vertoning_box_label, plaatsen_label)
        self.entries = (self.gebruiker_box, self.vertoning_box, plaatsen_entry)

    def __maak_ticket(self):
        if self.option_selected == "ticket":
            self.option_selected = None
            self.__reset_entries()
            return

        self.__reset_entries()
        self.option_selected = "ticket"

        vertoning_box_label = Label(self.button_frame, text="Vertoning: ", font=font.Font(size=20))
        vertoning_box_label.grid(row=0, column=3)

        self.vertoning_box = Listbox(self.button_frame, selectmode="single", height=10, exportselection=False)
        self.vertoning_box.grid(row=0, column=4, rowspan=2)

        self.reservatiesysteem.vertoningen.traverseTable(self.__vertoningbox_add)

        plaatsen_label = Label(self.button_frame, text="Plaatsen:", font=font.Font(size=18))
        plaatsen_label.grid(row=0, column=5)

        plaatsen_entry = Entry(self.button_frame, width=10, font=font.Font(size=20))
        plaatsen_entry.focus_set()
        plaatsen_entry.grid(row=1, column=5)

        self.submit_button.grid(row=1, column=6)

        self.entry_labels = (vertoning_box_label, plaatsen_label)
        self.entries = (self.vertoning_box, plaatsen_entry)

    def __reset_entries(self):
        for i in range(len(self.entries)):
            self.entries[i].grid_remove()

        self.entries = ()

        for i in range(len(self.entry_labels)):
            self.entry_labels[i].grid_remove()

        self.entry_labels = ()

        self.submit_button.grid_remove()

    def __execute_order(self):
        if self.option_selected == "film":
            titel = self.entries[0].get()
            rating = self.entries[1].get()

            start_id = 0
            suc6 = True
            while suc6:
                start_id += 1
                suc6 = self.reservatiesysteem.films.tableRetrieve(start_id)[1]

            threading.Thread(target=self.reservatiesysteem.maak_film, args=(start_id, titel, rating/100)).start()

        elif self.option_selected == "zaal":
            zaal_nr = eval(self.entries[0].get())
            aantal_plaatsen = eval(self.entries[1].get())

            if isinstance(zaal_nr, int) and (aantal_plaatsen, int) and \
                    not self.reservatiesysteem.zalen.tableRetrieve(zaal_nr)[1]:

                threading.Thread(target=self.reservatiesysteem.maak_zaal, args=(zaal_nr, aantal_plaatsen)).start()
            else:
                print("error geen integer gegeven/ zaal bestaat al")

        elif self.option_selected == "gebruiker":
            vr = self.entries[0].get()
            ar = self.entries[1].get()
            m = self.entries[1].get()

            start_id = 0
            suc6 = True
            while suc6:
                start_id += 1
                suc6 = self.reservatiesysteem.gebruikers.tableRetrieve(start_id)[1]

            threading.Thread(target=self.reservatiesysteem.maak_gebruiker, args=(start_id, vr, ar, m)).start()

        elif self.option_selected == "vertoning":
            if not self.entries[0].curselection():
                print("film niet geselecteerd")
                return

            if not self.entries[1].curselection():
                print("zaal niet geselecteerd")
                return

            if not self.entries[0].curselection():
                print("slot niet geselecteerd")
                return

            filmid = self.entries[0].get(self.entries[0].curselection())[0]
            zaalid = int(self.entries[1].get(self.entries[1].curselection()).replace("Zaal ", ""))
            slot_index = int(self.entries[2].curselection()[0])+1
            datum = self.entries[3].get()

            start_id = 0
            suc6 = True
            while suc6:
                start_id += 1
                suc6 = self.reservatiesysteem.vertoningen.tableRetrieve(start_id)[1]
            threading.Thread(target=self.reservatiesysteem.maak_vertoning, args=(start_id,
                                                                                 zaalid,
                                                                                 slot_index,
                                                                                 datum,
                                                                                 filmid,
                                                                                 self.reservatiesysteem.zalen.tableRetrieve(zaalid)[0].plaatsen)).start()

            self.__refresh_vertoningen()

        elif self.option_selected == "reservatie":
            gebruikerid = self.entries[0].get(self.entries[0].curselection())[0]
            vertoningid = int(self.entries[1].get(self.entries[1].curselection()).replace("Vertoning ", ""))
            plaatsen = int(self.entries[2].get())
            threading.Thread(target=self.reservatiesysteem.maak_reservatie, args=(vertoningid, plaatsen, self.current_time, gebruikerid)).start()
            print("heo")

        elif self.option_selected == "ticket":
            vertoningid = int(self.entries[0].get(self.entries[0].curselection()).replace("Vertoning ", ""))
            plaatsen = int(self.entries[1].get())
            self.reservatiesysteem.lees_ticket(vertoningid, plaatsen)
            threading.Thread(target=self.reservatiesysteem.lees_ticket, args=(vertoningid, plaatsen)).start()
            self.__refresh_vertoningen()

        self.option_selected = None
        self.__reset_entries()
        self.current_time += 60  # add 1 minutes after every operation
        threading.Thread(target=self.__check_lees_reservatie).start()

    def __check_lees_reservatie(self):
        if not self.reservatiesysteem.reservaties.tableIsEmpty():
            self.reservatiesysteem.lees_reservatie()
            self.__refresh_vertoningen()

    def __refresh_vertoningen(self):
        for vertoning in self.vertoning_frame.winfo_children():
            vertoning.destroy()
        self.row_col = (0, 0)
        self.reservatiesysteem.vertoningen.traverseTable(self.__add_vertoning)
    def __filmbox_add(self, value):
        self.film_box.insert(self.film_box.size(), (value.get_id(), value.titel))

    def __zaalbox_add(self, value):
        self.zaal_box.insert(self.zaal_box.size(), f"Zaal {value.zaalnummer}")

    def __slotbox_add(self, value):
        tup = self.reservatiesysteem.convert_time(value)
        if tup[2] > 10:
            self.slot_box.insert(self.slot_box.size(), f"{tup[1]}:{tup[2]}")
        else:
            self.slot_box.insert(self.slot_box.size(), f"{tup[1]}:0{tup[2]}")

    def __gebruikerbox_add(self, value):
        self.gebruiker_box.insert(self.gebruiker_box.size(), (value.get_id(), f"{value.vnaam} {value.anaam}"))

    def __vertoningbox_add(self, value):
        self.vertoning_box.insert(self.vertoning_box.size(), f"Vertoning {value[0].get_id()}")

    def __check_loading(self):
        is_loading = False
        while True:
            time.sleep(1)
            if threading.active_count() > 2 and not is_loading:
                self.loading.pack(anchor=S, side=RIGHT)
                is_loading = True

            if threading.active_count() <= 2 and is_loading:
                self.loading.pack_forget()
                is_loading = False


    def start(self):
        threading.Thread(target=self.__check_loading).start()
        self.screen.mainloop()

r = Reservatiesysteem(display_mode="print", path=f"../testfiles/system_test5.txt")
v = GUI(r)
v.start()