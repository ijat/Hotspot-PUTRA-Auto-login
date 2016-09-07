#!/usr/bin/python3

from tkinter import *
import webbrowser, time
from datetime import datetime

guiVer = "2.0.0.2"


class App:
    def __init__(self):
        self.root = Tk()

        self.root.title("Hotspot@UPM Auto Login")
        self.root.resizable(width=False, height=False)
        self.root.iconbitmap("res/icon.ico")
        self.root.minsize(300, 300)

        img = PhotoImage(file="res/upm.png")  # reference PhotoImage in local variable
        img_on = PhotoImage(file="res/on.png")
        img_off = PhotoImage(file="res/off.png")
        img_alert = PhotoImage(file="res/alert.png")

        menubar = Menu(self.root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Get Latest Version (Current version: {0})".format(guiVer), command=self.GoWeb2)
        filemenu.add_command(label="Visit Official Site", command=self.GoWeb)
        menubar.add_cascade(label="by Ijat.my", menu=filemenu)

        logo = Label(self.root, image=img, height=145, width=280)
        logo.grid(sticky=W, row=0, column=0, padx=10)

        Label(self.root, text="Matric No: ", font=(None, 10), width=16).grid(row=1, column=0, sticky=W, pady=5)

        self.e1 = Entry(self.root, bd=2, justify=CENTER, width=22)
        self.e1.grid(row=1, column=0, sticky=E, padx=15)

        Label(self.root, text="Password: ", font=(None, 10), width=16).grid(row=2, column=0, sticky=W)

        self.e2 = Entry(self.root, bd=2, justify=CENTER, show="*", width=22)
        self.e2.grid(row=2, column=0, sticky=E, padx=15)

        CheckVar1 = IntVar()
        c1 = Checkbutton(self.root, text="Remember Me", variable=CheckVar1,
                         onvalue=1, offvalue=0, width=14)
        c1.grid(row=3, column=0, sticky=E)

        self.b1Text = StringVar()
        b1 = Button(self.root, textvariable=self.b1Text, width=40)
        b1.grid(row=4, column=0, sticky=N, pady=13)
        self.b1Text.set("Connect")

        self.statusText = StringVar()

        Label(self.root, image=img_alert, font=(None, 8)).grid(row=5, column=0, sticky=W, padx=3)
        self.statusText.set("[" + time.strftime("%H:%M:%S") + "] Enter your credentials")

        Label(self.root, textvariable=self.statusText, font=(None, 9)).grid(row=5, column=0, sticky=W, padx=40)

        self.root.config(menu=menubar)
        self.root.mainloop()

    def userType(self, event):
        print(self.e1.get())

    def passType(self, event):
        print(self.e2.get())

    def GoWeb(self):
        webbrowser.open("https://ijat.my", new=0, autoraise=True)

    def GoWeb2(self):
        webbrowser.open("https://ijat.my/hotspotputra-auto-login", new=0, autoraise=True)


def Run():
    app = App()
