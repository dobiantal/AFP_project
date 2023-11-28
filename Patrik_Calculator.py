from tkinter import *

def button_pres(num):

    global equation_text

    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equals():

    global equation_text

    try:
        total = str(eval(equation_text))

        equation_label.set(total)

        equation_text=total
    except SyntaxError:
        equation_label.set("Szintaktikai hiba!")
        equation_text=""
    except ZeroDivisionError:
        equation_label.set("Aritmetikai hiba!")
        equation_text = ""


def clear():
    global equation_text

    equation_label.set("")

    equation_text = ""

window = Tk()
window.title("Számológép")
window.geometry("500x500")

equation_text = ""

equation_label = StringVar()

label = Label(window,textvariable=equation_label, font=('consolas',20),bg="white", width=24, height=2)
label.pack()

frame=Frame(window)
frame.pack()

button1=Button(frame,text=1, height=4,width=9,font=35,
               command=lambda: button_pres(1))
button1.grid(row=0, column=0)

button2=Button(frame,text=2, height=4,width=9,font=35,
               command=lambda: button_pres(2))
button2.grid(row=0, column=1)

button3=Button(frame,text=3, height=4,width=9,font=35,
               command=lambda: button_pres(3))
button3.grid(row=0, column=2)

button4=Button(frame,text=4, height=4,width=9,font=35,
               command=lambda: button_pres(4))
button4.grid(row=1, column=0)

button5=Button(frame,text=5, height=4,width=9,font=35,
               command=lambda: button_pres(5))
button5.grid(row=1, column=1)

button6=Button(frame,text=6, height=4,width=9,font=35,
               command=lambda: button_pres(6))
button6.grid(row=1, column=2)

button7=Button(frame,text=7, height=4,width=9,font=35,
               command=lambda: button_pres(7))
button7.grid(row=2, column=0)

button8=Button(frame,text=8, height=4,width=9,font=35,
               command=lambda: button_pres(8))
button8.grid(row=2, column=1)

button9=Button(frame,text=9, height=4,width=9,font=35,
               command=lambda: button_pres(9))
button9.grid(row=2, column=2)

button0=Button(frame,text=0, height=4,width=9,font=35,
               command=lambda: button_pres(0))
button0.grid(row=3, column=0)

plus=Button(frame,text='+', height=4,width=9,font=35,
               command=lambda: button_pres('+'))
plus.grid(row=0, column=3)

minus=Button(frame,text='-', height=4,width=9,font=35,
               command=lambda: button_pres('-'))
minus.grid(row=1, column=3)

multi=Button(frame,text='*', height=4,width=9,font=35,
               command=lambda: button_pres('*'))
multi.grid(row=2, column=3)

div=Button(frame,text='/', height=4,width=9,font=35,
               command=lambda: button_pres('/'))
div.grid(row=3, column=3)

equal=Button(frame,text='=', height=4,width=9,font=35,
               command=equals)
equal.grid(row=3, column=2)

decimal=Button(frame,text='.', height=4,width=9,font=35,
               command=lambda: button_pres('.'))
decimal.grid(row=3, column=1)

clear=Button(window,text='Töröl', height=4,width=12,font=35,
               command=clear)
clear.pack()

window.mainloop()
