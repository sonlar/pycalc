from tkinter import GROOVE, Button, Frame, Label, Tk


class Kalkulator(Tk):
    tall1 = ""
    tall2 = ""
    tegnsjekk = False
    addisjonsjekk = False
    subtraksjonsjekk = False
    multiplikasjonsjekk = False
    divisjonsjekk = False

    def klikk(self, num):
        if self.tegnsjekk is False:
            self.tall1 += str(num)
            self.skjerm.config(text=self.tall1)
        else:
            self.tall2 += str(num)
            self.skjerm.config(text=self.tall2)

    def addisjon(self):
        self.skjerm.config(text="+")
        self.tegnsjekk = True
        self.addisjonsjekk = True

    def subtraksjon(self):
        self.skjerm.config(text="-")
        self.tegnsjekk = True
        self.subtraksjonsjekk = True

    def multiplikasjon(self):
        self.skjerm.config(text="*")
        self.tegnsjekk = True
        self.multiplikasjonsjekk = True

    def divisjon(self):
        self.skjerm.config(text="/")
        self.tegnsjekk = True
        self.divisjonsjekk = True

    def likhet(self):
        if self.addisjonsjekk is True:
            resultat = int(self.tall1) + int(self.tall2)
            self.addisjonsjekk = False
        elif self.subtraksjonsjekk is True:
            resultat = int(self.tall1) - int(self.tall2)
            self.subtraksjonsjekk = False
        elif self.multiplikasjonsjekk is True:
            resultat = int(self.tall1) * int(self.tall2)
            self.multiplikasjonsjekk = False
        elif self.divisjonsjekk is True:
            resultat = int(self.tall1) / int(self.tall2)
            self.divisjonsjekk = False
        self.skjerm.config(text=resultat)
        self.tall1 = ""
        self.tall2 = ""
        self.tegnsjekk = False

    def clear(self):
        self.tall1 = ""
        self.tall2 = ""
        self.skjerm.config(text=0)

    # layout
    def __init__(self):
        super().__init__()
        self.skjerm = Label(self, text=0, width=25, relief=GROOVE)
        self.skjerm.grid(row=0, column=0)

        rad_1 = Frame(self)
        rad_1.grid(row=1, column=0)
        rad_2 = Frame(self)
        rad_2.grid(row=2, column=0)
        rad_3 = Frame(self)
        rad_3.grid(row=3, column=0)
        rad_4 = Frame(self)
        rad_4.grid(row=4, column=0)

        knapp_7 = Button(rad_1, text=7, width=5, command=lambda: self.klikk(7))
        knapp_7.grid(row=1, column=0)
        knapp_8 = Button(rad_1, text=8, width=5, command=lambda: self.klikk(8))
        knapp_8.grid(row=1, column=1)
        knapp_9 = Button(rad_1, text=9, width=5, command=lambda: self.klikk(9))
        knapp_9.grid(row=1, column=2)
        knapp_addisjon = Button(rad_1, text="+", width=5, command=self.addisjon)
        knapp_addisjon.grid(row=1, column=3)

        knapp_4 = Button(rad_2, text=4, width=5, command=lambda: self.klikk(4))
        knapp_4.grid(row=2, column=0)
        knapp_5 = Button(rad_2, text=5, width=5, command=lambda: self.klikk(5))
        knapp_5.grid(row=2, column=1)
        knapp_6 = Button(rad_2, text=6, width=5, command=lambda: self.klikk(6))
        knapp_6.grid(row=2, column=2)
        knapp_subtraksjon = Button(rad_2, text="-", width=5, command=self.subtraksjon)
        knapp_subtraksjon.grid(row=2, column=3)

        knapp_1 = Button(rad_3, text=1, width=5, command=lambda: self.klikk(1))
        knapp_1.grid(row=3, column=0)
        knapp_2 = Button(rad_3, text=2, width=5, command=lambda: self.klikk(2))
        knapp_2.grid(row=3, column=1)
        knapp_3 = Button(rad_3, text=3, width=5, command=lambda: self.klikk(3))
        knapp_3.grid(row=3, column=2)
        knapp_multiplikasjon = Button(
            rad_3, text="*", width=5, command=self.multiplikasjon
        )
        knapp_multiplikasjon.grid(row=3, column=3)

        knapp_0 = Button(rad_4, text=0, width=5, command=lambda: self.klikk(0))
        knapp_0.grid(row=4, column=0)
        knapp_c = Button(rad_4, text="C", width=5, command=self.clear)
        knapp_c.grid(row=4, column=1)
        knapp_likhet = Button(rad_4, text="=", width=5, command=self.likhet)
        knapp_likhet.grid(row=4, column=2)
        knapp_divisjon = Button(rad_4, text="/", width=5, command=self.divisjon)
        knapp_divisjon.grid(row=4, column=3)


if __name__ == "__main__":
    root = Kalkulator()
    root.mainloop()
