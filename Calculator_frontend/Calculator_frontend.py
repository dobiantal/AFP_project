import tkinter as tk
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from Operators.Addition import Addition
from Operators.sqrt import negyzetgyok
from Operators.multiplicate import multiplicate
from Operators.div import div
from Operators.subtraction import subtract
"""*A főablak implementálása."""
window = tk.Tk()
window.title("Calculator")
Width: int = 600
Height: int = 600
From_top_left: int = 500
From_top: int = 200
window.geometry(f'{Width}x{Height}+{From_top_left}+{From_top}')

"""*A kijelző mező"""
Display = tk.Entry(font=("Times New Roman",25))
Display.focus_force()
Display.place(relwidth=0.7, relheight=0.15, relx=0.15, rely=0.1)

"""Globális vátozók melyek a kapott számokat tárolják."""
OPERANDUS_A: int = 0
OPERATOR: str = ""
OPERANDUS_B: int = 0

"""
*Az alábbi kód implementálja a fő ablakon a funkció gombokat és a kattintási methodusokat.
"""
def ZeroC():
    Display.insert("end","0")
Zero = tk.Button(text=0, bg='#065ef9', font=("Times New Roman",25),command=lambda:ZeroC())
Zero.place(relwidth=0.15, relheight=0.15, relx=0.25, rely=0.75)
def OneC():
    Display.insert("end","1")
One = tk.Button(text=1, bg='#065ef9', font=("Times New Roman",25),command=lambda:OneC())
One.place(relwidth=0.15, relheight=0.15, relx=0.1, rely=0.6)
def TwoC():
    Display.insert("end","2")
Two = tk.Button(text=2, bg='#065ef9', font=("Times New Roman",25),command=lambda:TwoC())
Two.place(relwidth=0.15, relheight=0.15, relx=0.25, rely=0.6)
def ThreeC():
    Display.insert("end","3")
Three = tk.Button(text=3, bg='#065ef9', font=("Times New Roman",25),command=lambda:ThreeC())
Three.place(relwidth=0.15, relheight=0.15, relx=0.4, rely=0.6)
def FourC():
    Display.insert("end","4")
Four = tk.Button(text=4, bg='#065ef9', font=("Times New Roman",25),command=lambda:FourC())
Four.place(relwidth=0.15, relheight=0.15, relx=0.1, rely=0.45)
def FiveC():
    Display.insert("end","5")
Five = tk.Button(text=5, bg='#065ef9', font=("Times New Roman",25),command=lambda:FiveC())
Five.place(relwidth=0.15, relheight=0.15, relx=0.25, rely=0.45)
def SixC():
    Display.insert("end","6")
Six = tk.Button(text=6, bg='#065ef9', font=("Times New Roman",25),command=lambda:SixC())
Six.place(relwidth=0.15, relheight=0.15, relx=0.4, rely=0.45)
def SevenC():
    Display.insert("end","7")
Seven = tk.Button(text=7, bg='#065ef9', font=("Times New Roman",25),command=lambda:SevenC())
Seven.place(relwidth=0.15, relheight=0.15, relx=0.1, rely=0.30)
def EightC():
    Display.insert("end","8")
Eight = tk.Button(text=8, bg='#065ef9', font=("Times New Roman",25),command=lambda:EightC())
Eight.place(relwidth=0.15, relheight=0.15, relx=0.25, rely=0.30)
def NineC():
    Display.insert("end","9")
Nine = tk.Button(text=9, bg='#065ef9', font=("Times New Roman",25),command=lambda:NineC())
Nine.place(relwidth=0.15, relheight=0.15, relx=0.4, rely=0.30)


"""
*Itt találhatóak az operátor gombok leképezései. 
*Minden funkciógomb első leütésre eltárolja az OPERANDUS_A változóba az első számértéket a mi a művelethez kell.
"""
def SumOp():
    global OPERANDUS_A
    global OPERATOR
    OPERATOR = "+"
    OPERANDUS_A = Display.get()
    Display.delete(0,'end')
Sum = tk.Button(text="+", bg='#065ef9', font=("Times New Roman",25),command=lambda: SumOp())
Sum.place(relwidth=0.15, relheight=0.15, relx=0.55, rely=0.6)
def SubOp():
    global OPERANDUS_A
    global OPERATOR
    OPERATOR = "-"
    OPERANDUS_A = Display.get()
    Display.delete(0,'end')
Sub = tk.Button(text="-", bg='#065ef9', font=("Times New Roman",25),command=lambda: SubOp())
Sub.place(relwidth=0.15, relheight=0.15, relx=0.7, rely=0.6)
def MultiOp():
    global OPERANDUS_A
    global OPERATOR
    OPERATOR = "*"
    OPERANDUS_A = Display.get()
    Display.delete(0,'end')
Multip = tk.Button(text="*", bg='#065ef9', font=("Times New Roman",25),command=lambda: MultiOp())
Multip.place(relwidth=0.15, relheight=0.15, relx=0.55, rely=0.45)
def DivOp():
    global OPERANDUS_A
    global OPERATOR
    OPERATOR = "/"
    OPERANDUS_A = Display.get()
    Display.delete(0,'end')
Div = tk.Button(text="/", bg='#065ef9', font=("Times New Roman",25),command=lambda: DivOp())
Div.place(relwidth=0.15, relheight=0.15, relx=0.7, rely=0.45)
def EvomOp():
    global OPERANDUS_A
    global OPERATOR
    OPERATOR = "√"
    OPERANDUS_A = Display.get()
    Display.delete(0, 'end')
    Display.insert(0, negyzetgyok(OPERANDUS_A))
    OPERANDUS_A = 0
    OPERATOR = ""
Evo = tk.Button(text="√", bg='#065ef9', font=("Times New Roman",25),command=lambda: EvomOp())
Evo.place(relwidth=0.15, relheight=0.15, relx=0.7, rely=0.30)
def EqOp():
    global OPERANDUS_B
    global OPERATOR
    global OPERANDUS_A
    OPERANDUS_B = Display.get()
    Display.delete(0,'end')
    """
    *Egy elágazás rendszerben kiválasztjuk melyik operátor leütés történt annak megfelelően hívjuk meg,
    az álltalatok írt methodusokat a két operandussal.
    """
    if OPERATOR == "+":
        Display.insert(0, Addition(OPERANDUS_A,OPERANDUS_B))
    elif OPERATOR == "-":
        Display.insert(0, subtract(OPERANDUS_A,OPERANDUS_B))
    elif OPERATOR == "*":
        Display.insert(0, multiplicate(OPERANDUS_A,OPERANDUS_B))
    elif OPERATOR == "/":
        Display.insert(0, div(OPERANDUS_A, OPERANDUS_B))
    else:
        Display.insert(0,"Err")
    """A gyökvonás művelet mivel egy operandussal dolgozik ezért a képernyőre 
    írás a saját függvényénél van meghívva."""
    OPERANDUS_A = 0
    OPERATOR = ""
    OPERANDUS_B = 0
def EqOp_BR(event):
    EqOp()
Eq = tk.Button(text="=", bg='#065ef9', font=("Times New Roman",25),command=lambda: EqOp())
Eq.bind("<Return>", EqOp_BR)
Eq.place(relwidth=0.15, relheight=0.15, relx=0.7, rely=0.75)

"""
*Törlő methodus letörli a képernyőt a CE gomb lenyomására. 
"""
def Clear_display():
    Display.delete(0,'end')
CE = tk.Button(text="CE", bg='#065ef9', font=("Times New Roman",25),command=lambda: Clear_display())
CE.place(relwidth=0.15, relheight=0.15, relx=0.55, rely=0.30)
window.mainloop()