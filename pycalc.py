from tkinter import GROOVE, Button, Frame, IntVar, Label, Tk

window = Tk()

utregning = IntVar(window)
tall = ""


def klikk(x):
    global tall
    tall += str(x)
    utregning.set(int(tall))
    display.config(text=utregning.get())


display = Label(window, text=utregning.get(), width=25, relief=GROOVE)
display.grid(row=0, column=0)

rad1 = Frame(window)
rad1.grid(row=1, column=0)
rad2 = Frame(window)
rad2.grid(row=2, column=0)
rad3 = Frame(window)
rad3.grid(row=3, column=0)
rad4 = Frame(window)
rad4.grid(row=4, column=0)

button7 = Button(rad1, text=7, width=5, command=lambda: klikk(7))
button7.grid(row=1, column=0)
button8 = Button(rad1, text=8, width=5, command=lambda: klikk(8))
button8.grid(row=1, column=1)
button9 = Button(rad1, text=9, width=5, command=lambda: klikk(9))
button9.grid(row=1, column=2)
buttonaddition = Button(rad1, text="+", width=5)
buttonaddition.grid(row=1, column=3)

button4 = Button(rad2, text=4, width=5, command=lambda: klikk(4))
button4.grid(row=2, column=0)
button5 = Button(rad2, text=5, width=5, command=lambda: klikk(5))
button5.grid(row=2, column=1)
button6 = Button(rad2, text=6, width=5, command=lambda: klikk(6))
button6.grid(row=2, column=2)
buttonsubtraction = Button(rad2, text="-", width=5)
buttonsubtraction.grid(row=2, column=3)

button1 = Button(rad3, text=1, width=5, command=lambda: klikk(1))
button1.grid(row=3, column=0)
button2 = Button(rad3, text=2, width=5, command=lambda: klikk(2))
button2.grid(row=3, column=1)
button3 = Button(rad3, text=3, width=5, command=lambda: klikk(3))
button3.grid(row=3, column=2)
buttonmultiplication = Button(rad3, text="*", width=5)
buttonmultiplication.grid(row=3, column=3)

button0 = Button(rad4, text=0, width=5, command=lambda: klikk(0))
button0.grid(row=4, column=0)
buttonc = Button(rad4, text="C", width=5)
buttonc.grid(row=4, column=1)
buttonequal = Button(rad4, text="=", width=5)
buttonequal.grid(row=4, column=2)
buttondivision = Button(rad4, text="/", width=5)
buttondivision.grid(row=4, column=3)

window.mainloop()
