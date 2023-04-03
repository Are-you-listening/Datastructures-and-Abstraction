from tkinter import *
import threading
from tkinter import ttk


class GUI:
    def __init__(self):
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

    def __setup_console(self):
        canvas = Canvas(self.console)
        canvas.pack(side=LEFT, fill=BOTH, expand=1)

        scrollbar = ttk.Scrollbar(self.console, orient=VERTICAL, command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        self.inside_console = Frame(canvas)

        canvas.create_window((0, 0), window=self.inside_console, anchor="nw")

    def __add_console_message(self, msg):
        m = Label(self.inside_console, text=msg)
        m.pack()

    def start(self):
        self.screen.mainloop()


v = GUI()
v.start()
