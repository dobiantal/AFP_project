import tkinter as tk
"""*A főablak implementálása."""
window = tk.Tk()
Width: int = 600
Height: int = 600
From_top_left: int = 500
From_top: int = 200
window.geometry(f'{Width}x{Height}+{From_top_left}+{From_top}')

"""*A kijelző mező"""
Display = tk.Entry(font=("Times New Roman",25))
Display.focus_force()
Display.place(relwidth=0.7, relheight=0.15, relx=0.03, rely=0.1)


"""Globális vátozók melyek a kapott számokat tárolják."""
OPERANDUS_A: int = 0
OPERATOR: str = ""
OPERANDUS_B: int = 0

"""
*Az alábbi kód implementálja a fő ablakon a funkció gombokat és a kattintási methodusokat.
"""
def ZeroC():
    Display.insert("end","0")
Zero = tk.Button(text=0, font=("Times New Roman",25),command=lambda:ZeroC())
Zero.place(relwidth=0.15, relheight=0.15, relx=0.18, rely=0.75)
def OneC():
    Display.insert("end","1")
One = tk.Button(text=1,font=("Times New Roman",25),command=lambda:OneC())
One.place(relwidth=0.15, relheight=0.15, relx=0.03, rely=0.6)
def TwoC():
    Display.insert("end","2")
Two = tk.Button(text=2,font=("Times New Roman",25),command=lambda:TwoC())
Two.place(relwidth=0.15, relheight=0.15, relx=0.18, rely=0.6)
def ThreeC():
    Display.insert("end","3")
Three = tk.Button(text=3,font=("Times New Roman",25),command=lambda:ThreeC())
Three.place(relwidth=0.15, relheight=0.15, relx=0.33, rely=0.6)
def FourC():
    Display.insert("end","4")
Four = tk.Button(text=4,font=("Times New Roman",25),command=lambda:FourC())
Four.place(relwidth=0.15, relheight=0.15, relx=0.03, rely=0.45)
def FiveC():
    Display.insert("end","5")
Five = tk.Button(text=5,font=("Times New Roman",25),command=lambda:FiveC())
Five.place(relwidth=0.15, relheight=0.15, relx=0.18, rely=0.45)
def SixC():
    Display.insert("end","6")
Six = tk.Button(text=6,font=("Times New Roman",25),command=lambda:SixC())
Six.place(relwidth=0.15, relheight=0.15, relx=0.33, rely=0.45)
def SevenC():
    Display.insert("end","7")
Seven = tk.Button(text=7,font=("Times New Roman",25),command=lambda:SevenC())
Seven.place(relwidth=0.15, relheight=0.15, relx=0.03, rely=0.30)
def EightC():
    Display.insert("end","8")
Eight = tk.Button(text=8,font=("Times New Roman",25),command=lambda:EightC())
Eight.place(relwidth=0.15, relheight=0.15, relx=0.18, rely=0.30)
def NineC():
    Display.insert("end","9")
Nine = tk.Button(text=9,font=("Times New Roman",25),command=lambda:NineC())
Nine.place(relwidth=0.15, relheight=0.15, relx=0.33, rely=0.30)


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
Sum = tk.Button(text="+",font=("Times New Roman",25),command=lambda: SumOp())
Sum.place(relwidth=0.15, relheight=0.15, relx=0.48, rely=0.6)
def SubOp():
    global OPERANDUS_A
    global OPERATOR
    OPERATOR = "-"
    OPERANDUS_A = Display.get()
    Display.delete(0,'end')
Sub = tk.Button(text="-",font=("Times New Roman",25),command=lambda: SubOp())
Sub.place(relwidth=0.15, relheight=0.15, relx=0.63, rely=0.6)
def MultiOp():
    global OPERANDUS_A
    global OPERATOR
    OPERATOR = "*"
    OPERANDUS_A = Display.get()
    Display.delete(0,'end')
Multip = tk.Button(text="*",font=("Times New Roman",25),command=lambda: MultiOp())
Multip.place(relwidth=0.15, relheight=0.15, relx=0.48, rely=0.45)
def DivOp():
    global OPERANDUS_A
    global OPERATOR
    OPERATOR = "/"
    OPERANDUS_A = Display.get()
    Display.delete(0,'end')
Div = tk.Button(text="/",font=("Times New Roman",25),command=lambda: DivOp())
Div.place(relwidth=0.15, relheight=0.15, relx=0.63, rely=0.45)
def EvomOp():
    global OPERANDUS_A
    global OPERATOR
    OPERATOR = "√"
    OPERANDUS_A = Display.get()
    Display.delete(0,'end')
Evo = tk.Button(text="√",font=("Times New Roman",25),command=lambda: EvomOp())
Evo.place(relwidth=0.15, relheight=0.15, relx=0.63, rely=0.30)
def EqOp():
    global OPERANDUS_B
    OPERANDUS_B = Display.get()
    Display.delete(0,'end')
    """
    *Egy elágazás rendszerben kiválasztjuk melyik operátor leütés történt annak megfelelően hívjuk meg,
    az álltalatok írt methodusokat a két operandussal.
    """
    Display.insert(0,"A számítás végeredményét visszaírjuk a kijelzőre.")
Eq = tk.Button(text="=",font=("Times New Roman",25),command=lambda: EqOp())
Eq.place(relwidth=0.15, relheight=0.15, relx=0.63, rely=0.75)

"""
*Törlő methodus letörli a képernyőt a CE gomb lenyomására. 
"""
def Clear_display():
    Display.delete(0,'end')
CE = tk.Button(text="CE",font=("Times New Roman",25),command=lambda: Clear_display())
CE.place(relwidth=0.15, relheight=0.15, relx=0.48, rely=0.30)
window.mainloop()