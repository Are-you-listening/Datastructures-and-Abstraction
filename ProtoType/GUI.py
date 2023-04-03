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
        b = Button(self.main_dashboard, text="maak vertoning", font=font.Font(size=20))
        b.pack(side=BOTTOM, anchor=SW)

        b = Button(self.main_dashboard, text="maak zaal", font=font.Font(size=20))
        b.pack(side=BOTTOM, anchor=SW)

        b = Button(self.main_dashboard, text="maak film", font=font.Font(size=20))
        b.pack(side=BOTTOM, anchor=SW)

        b = Button(self.main_dashboard, text="maak gebruiker", font=font.Font(size=20))
        b.pack(side=BOTTOM, anchor=SW)

    def start(self):
        self.screen.mainloop()


r = Reservatiesysteem(display_mode="print")
v = GUI(r)
v.start()
