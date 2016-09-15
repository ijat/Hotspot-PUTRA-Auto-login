#!/usr/bin/python3

from tkinter import *
from Network import *
import webbrowser, time
import uuid, aes, dmidecode, os
import login
from datetime import datetime

guiVer = "2.0.0.2"


class App:
    def __init__(self, u=None, p=None):
        self.status = None

        self.root = Tk()

        self.root.title("Hotspot@UPM Auto Login")
        self.root.resizable(width=False, height=False)
        self.root.iconbitmap("res/icon.ico")
        self.root.minsize(300, 300)

        img = PhotoImage(file="res/upm.png")  # reference PhotoImage in local variable
        self.img_on = PhotoImage(file="res/on.png")
        self.img_off = PhotoImage(file="res/off.png")
        self.img_alert = PhotoImage(file="res/alert.png")

        menubar = Menu(self.root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Get Latest Version (Current version: {0})".format(guiVer), command=self.GoWeb2)
        filemenu.add_command(label="Visit Official Site", command=self.GoWeb)
        menubar.add_cascade(label="by Ijat.my", menu=filemenu)

        logo = Label(self.root, image=img, height=145, width=280)
        logo.grid(sticky=W, row=0, column=0, padx=10)

        Label(self.root, text="Matric No: ", font=(None, 10), width=16).grid(row=1, column=0, sticky=W, pady=5)

        self.e1Var = StringVar()
        self.e1 = Entry(self.root, bd=2, justify=CENTER, width=22, textvariable=self.e1Var)
        self.e1.grid(row=1, column=0, sticky=E, padx=15)

        Label(self.root, text="Password: ", font=(None, 10), width=16).grid(row=2, column=0, sticky=W)

        self.e2Var = StringVar()
        self.e2 = Entry(self.root, bd=2, justify=CENTER, show="*", width=22, textvariable=self.e2Var)
        self.e2.grid(row=2, column=0, sticky=E, padx=15)

        self.c1Var = IntVar()
        self.c1 = Checkbutton(self.root, text="Remember Me", variable=self.c1Var,
                         onvalue=1, offvalue=0, width=14)
        self.c1.grid(row=3, column=0, sticky=E)

        self.b1Text = StringVar()
        self.b1Text.set("Connect")

        self.b1 = Button(self.root, textvariable=self.b1Text, width=40, command=self.b1Pressed)
        self.b1.grid(row=4, column=0, sticky=N, pady=13)

        self.statusText = StringVar()

        self.stat_icon = Label(self.root, font=(None, 8), image=self.img_alert)
        self.stat_icon.grid(row=5, column=0, sticky=W, padx=3)
        self._img = self.img_alert

        self.statusText.set("Enter your credentials")
        Label(self.root, textvariable=self.statusText, font=("Consolas", 9)).grid(row=5, column=0, sticky=N, padx=40)

        self.root.config(menu=menubar)

        (eusr, epwd) = self.user_conf()
        if (eusr) and (epwd):
            (self.u, self.p) = self.user_load(eusr, epwd)
            self.e1Var.set(self.u)
            self.e2Var.set(self.p)
            self.c1Var.set(1)
            self.remember = True
            self.statusText.set("Click Connect to start")
        else:
            self.remember = False

        self.index = 0
        self.root.mainloop()

    def userType(self, event):
        print(self.e1.get())

    def passType(self, event):
        print(self.e2.get())

    def b1Pressed(self):
        if (self.status == 0) or (self.status == 1):
            try:
                self.root.after_cancel(self.__job)
                self.__job = None
            except:
                pass
            self.b1Text.set("Connect")
            self.status = None

            # Enable options
            self.e1.configure(state=NORMAL)
            self.e2.configure(state=NORMAL)
            self.c1.configure(state=NORMAL)
            self.b1.configure(state=NORMAL)

            self.change_status_icon(2)
            self.statusText.set("Click Connect to start")

            return 0

        self.u = self.e1.get()
        self.p = self.e2.get()

        if (self.c1Var.get()):
            self.user_save(self.e1.get(), self.e2.get())
        else:
            try:
                os.remove(".user.dat")
            except:
                pass

        if self.b1Text.get() == "Connect":
            self.e1.configure(state=DISABLED)
            self.e2.configure(state=DISABLED)
            self.c1.configure(state=DISABLED)
            self.b1.configure(state=DISABLED)
            self.b1Text.set("Stop")
        else:
            self.e1.configure(state=NORMAL)
            self.e2.configure(state=NORMAL)
            self.b1Text.set("Connect")

        # Connect engine
        self.statusText.set("Connecting... #" + str(self.index + 1) + "\nLast updated on " + time.strftime("%H:%M:%S"))
        self.status = 0
        self.first = True
        self.root.after(10, self.reconnect)

    def reconnect(self):
        if (self.index > 2) and self.first:
            try:
                self.statusText.set("Failed after 3 retries\nCheck your login and password")
                self.root.after_cancel(self.__job)
                self.__job = None
                self.status = 0
                self.b1Text.set("Connect")
                self.e1.configure(state=NORMAL)
                self.e2.configure(state=NORMAL)
                self.c1.configure(state=NORMAL)
                self.b1.configure(state=NORMAL)
                self.index = 0
            except:
                pass
            finally:
                return 0

        if isUp("authenticate.upm.my"):
            if not isUp("ping.ijat.my"):
                self.user = login.HotspotUPM(self.u, self.p)
                self.root.after(1000, self.user_connect)
                self.status = 0
            else:
                self.first = False
                self.status = 1
        else:
            self.statusText.set("Not connected to Hotspot@UPM ?\nLast updated on " + time.strftime("%H:%M:%S"))
            self.change_status_icon(0)
            self.status = 0
            self.__job = self.root.after(4567, self.reconnect)
            self.b1.configure(state=NORMAL)
            return 0

        if self.status == 1:
            self.b1Text.set("Stop")
            self.statusText.set("Connected\nLast updated on " + time.strftime("%H:%M:%S"))
            self.change_status_icon(1)
            self.b1.configure(state=NORMAL)
            self.index = 0
        elif self.status == 0:
            self.statusText.set(
                "Connecting... #" + str(self.index + 1) + "\nLast updated on " + time.strftime("%H:%M:%S"))
            self.b1Text.set("Stop")
            self.change_status_icon(3)
            self.b1.configure(state=NORMAL)
            self.index += 1
        else:
            self.b1Text.set("Connect")
            return 0

        self.__job = self.root.after(15000, self.reconnect)

    def user_connect(self):
        self.user.async_connect()

    def change_status_icon(self, icon):
        if icon == 0:
            self.stat_icon.configure(image=self.img_off)
            self._img = self.img_off
        elif icon == 1:
            self.stat_icon.configure(image=self.img_on)
            self._img = self.img_on
        else:
            self.stat_icon.configure(image=self.img_alert)
            self._img = self.img_alert

    def GoWeb(self):
        webbrowser.open("https://ijat.my", new=0, autoraise=True)

    def GoWeb2(self):
        webbrowser.open("https://ijat.my/hotspotputra-auto-login", new=0, autoraise=True)

    def user_save(self, u, p):
        hwid = dmidecode.get_id()

        eusr = aes.AESCipher(hwid)
        s_eusr = eusr.encrypt(u)
        s_eusr = bytes(s_eusr).decode()

        kpswd = uuid.uuid5(uuid.NAMESPACE_DNS, s_eusr)
        kpswd = str(kpswd).replace("-", "")

        epsw = aes.AESCipher(kpswd)
        s_epsw = epsw.encrypt(p)
        s_epsw = bytes(s_epsw).decode()

        fh = open(".user.dat", "w")
        fh.write(s_eusr + "\n")
        fh.write(s_epsw + "\n")
        fh.close()

        self.user_load(s_eusr, s_epsw)

    def user_conf(self):
        try:
            fh = open(".user.dat", "r")
            eusr = fh.readline().strip()
            epsw = fh.readline().strip()
            return eusr, epsw
        except:
            return "", ""

    def user_load(self, eu, ep):
        hwid = dmidecode.get_id()
        dusr = aes.AESCipher(hwid)
        s_dusr = dusr.decrypt(eu)

        kpswd = uuid.uuid5(uuid.NAMESPACE_DNS, eu)
        kpswd = str(kpswd).replace("-", "")

        dpsw = aes.AESCipher(kpswd)
        s_dpsw = dpsw.decrypt(ep)

        return (s_dusr, s_dpsw)


def Run():
    app = App()
