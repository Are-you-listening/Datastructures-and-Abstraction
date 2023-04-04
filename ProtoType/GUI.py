from tkinter import *
import threading
from tkinter import ttk, font
import math
from Reservatiesysteem import Reservatiesysteem


class GUI:
    def __init__(self, reservatiesysteem):

        self.reservatiesysteem = reservatiesysteem

        self.screen = Tk()
        self.screen.geometry("1920x1280")
        self.tab_manager = ttk.Notebook(self.screen)

        self.main_dashboard = Frame(self.tab_manager)
        self.time_schema = Frame(self.tab_manager)
        self.console = Frame(self.tab_manager)

        self.tab_manager.add(self.main_dashboard, text="main tab")
        self.tab_manager.add(self.time_schema, text="time schema")
        self.tab_manager.add(self.console, text="console")
        self.tab_manager.pack(expand=True, fill=BOTH)

        self.__setup_console()
        for i in range(100):
            self.__add_console_message(f"test {i}")

        self.vertoning_frame = Frame(self.main_dashboard, width=1920, height=960)
        self.vertoning_frame.pack(side=TOP, anchor=NW)

        self.row_col = (0, 0)
        self.reservatiesysteem.vertoningen.traverseTable(self.__add_vertoning)

        self.button_frame = Frame(self.main_dashboard)
        self.button_frame.pack(side=BOTTOM, anchor=SW)

        self.entry_labels = ()
        self.entries = ()
        self.option_selected = None

        self.film_box = None
        self.zaal_box = None
        self.vertoning_box = None
        self.gebruiker_box = None

        self.submit_button = None
        self.__setup_buttons()

    def __add_vertoning(self, vertoning_tup):
        """prevent filling the main page to much, add scrollwheel later"""
        if self.row_col[0] > 5:
            return
        vertoning_object = vertoning_tup[0]
        vertoning_frame = LabelFrame(self.vertoning_frame, text=f"vertoning {vertoning_object.get_id()}")
        vertoning_frame.grid(row=self.row_col[0], column=self.row_col[1])

        film_id = vertoning_object.filmid
        film_retrieve_tup = self.reservatiesysteem.films.tableRetrieve(film_id)
        if not film_retrieve_tup[1]:
            film_name = "not loaded"
        else:
            film_name = film_retrieve_tup[0].titel

        info_frame = LabelFrame(vertoning_frame, text=f"Info")
        info_frame.grid(row=0, column=0)

        film_label = Label(info_frame, text=f"Film: {film_name}")
        film_label.pack(anchor="w")

        zaalnummer = vertoning_object.zaalnummer
        zaal_label = Label(info_frame, text=f"Zaal: {zaalnummer}")
        zaal_label.pack(anchor="w")

        reservaties = vertoning_object.vrije_plaatsen - vertoning_object.vrije_plaatsenVirtueel
        aanwezige = vertoning_object.vrije_plaatsenFysiek
        self.__create_vertoning_diagram(vertoning_frame, aanwezige, reservaties, vertoning_object.vrije_plaatsen)

        if self.row_col[1] < 5:
            self.row_col = (self.row_col[0], self.row_col[1]+1)
        else:
            self.row_col = (self.row_col[0]+1, 0)

    def __create_vertoning_diagram(self, root, tickets, reservaties, plaatsen):
        canvas_mid = (100, 100)
        radius = 80

        diagram = Canvas(root, width=200, height=200)
        diagram.grid(row=0, column=1)

        diagram.create_oval(canvas_mid[0] - radius+2, canvas_mid[1] - radius+2, canvas_mid[0] + radius-2,
                            canvas_mid[1] + radius-2, fill="gray", outline="gray")

        rPCT = reservaties/plaatsen
        for i in range(round(rPCT*100)):
            angle = 2*math.pi*i/100-math.pi/2
            diagram.create_line(canvas_mid[0], canvas_mid[1], canvas_mid[0]+math.cos(angle)*radius, canvas_mid[1]+math.sin(angle)*radius, width=10, fill="#006AFF")

        tPCT = tickets / plaatsen
        for i in range(round(tPCT * 100)):
            angle = 2 * math.pi * i / 100 - math.pi / 2
            diagram.create_line(canvas_mid[0], canvas_mid[1], canvas_mid[0] + math.cos(angle) * (radius+1),
                                canvas_mid[1] + math.sin(angle) * (radius+1), width=10, fill="#00FF00")

        diagram.create_oval(canvas_mid[0]-radius/2, canvas_mid[1]-radius/2, canvas_mid[0]+radius/2,
                            canvas_mid[1]+radius/2, fill="#D9D9D9", outline='#D9D9D9')

        diagram.create_text(100, 90, text=f"{reservaties}/{plaatsen}")
        diagram.create_text(100, 110, text=f"{tickets}/{reservaties}")

    def __setup_console(self):
        canvas = Canvas(self.console)
        canvas.pack(side=LEFT, fill=BOTH, expand=1)

        scrollbar = ttk.Scrollbar(self.console, orient=VERTICAL, command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        self.inside_console = Frame(canvas)

        canvas.create_window((0, 0), window=self.inside_console, anchor=NW)

    def __add_console_message(self, msg):
        m = Label(self.inside_console, text=msg)
        m.pack()

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
        b = Button(self.button_frame, image=self.img_5)
        b.grid(row=0, column=2)

        self.img_6 = PhotoImage(file="../GUI_images/ticket.png", width=100, height=100)
        b = Button(self.button_frame, image=self.img_6)
        b.grid(row=1, column=2)

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

        self.film_box = Listbox(self.button_frame, selectmode="single", height=10)
        self.film_box.grid(row=0, column=4, rowspan=2)

        self.reservatiesysteem.films.traverseTable(self.__filmbox_add)

        self.entry_labels = (film_box_label,)
        self.entries = (self.film_box,)

        """
        needed:
        -timeslot
        -zaal
        -film
        :return:
        """

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

            start_id = 100
            suc6 = True
            while suc6:
                start_id += 1
                suc6 = self.reservatiesysteem.films.tableRetrieve(start_id)[1]

            self.reservatiesysteem.maak_film(start_id, titel, rating/100)

        elif self.option_selected == "zaal":
            zaal_nr = eval(self.entries[0].get())
            aantal_plaatsen = eval(self.entries[1].get())

            if isinstance(zaal_nr, int) and (aantal_plaatsen, int) and \
                    not self.reservatiesysteem.zalen.tableRetrieve(zaal_nr)[1]:
                self.reservatiesysteem.maak_zaal(zaal_nr, aantal_plaatsen)
            else:
                print("error geen integer gegeven/ zaal bestaat al")

        elif self.option_selected == "gebruiker":
            vr = self.entries[0].get()
            ar = self.entries[1].get()
            m = self.entries[1].get()

            start_id = 100
            suc6 = True
            while suc6:
                start_id += 1
                suc6 = self.reservatiesysteem.gebruikers.tableRetrieve(start_id)[1]

            self.reservatiesysteem.maak_gebruiker(start_id, vr, ar, m)

        self.option_selected = None
        self.__reset_entries()

    def __filmbox_add(self, value):
        self.film_box.insert(self.film_box.size(), (value.get_id(), value.titel))

    def __zaalbox_add(self, value):
        self.zaal_box.insert(self.zaal_box.size(), (value.get_id(), value.titel))

    def start(self):
        self.screen.mainloop()


r = Reservatiesysteem(display_mode="print")
v = GUI(r)
v.start()
