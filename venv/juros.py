# -*- coding: utf-8 -*-
from tkinter import *
from calc import Calculos

def calcular():
    tipo=option.get()
    tTaxa=option2.get()
    P=ed1.get()
    i=ed2.get()
    n=ed3.get()
    M=ed4.get()
    print()




janela = Tk()
janela.title("Calculadora Super Bolada 3000")
janela.geometry("600x500")

lb = Label(janela, width=25, text="Informe os \ncampos abaixo", font=("Verdana", 30))
lb.place(x=0, y=0)


option = StringVar()
rd1 = Radiobutton(janela, text="Juros Composto", fg="black", font=("Verdana", 12), variable=option, value=1, tristatevalue=0)
rd1.place(x=250, y=140)
rd2 = Radiobutton(janela, text="Juros Simples", fg="black", font=("Verdana", 12), variable=option, value=2, tristatevalue=0)
rd2.place(x=250, y=170)

lb = Label(janela, text="Capital inicial:", font=("Verdana", 12))
lb.place(x=100, y=200)
ed1 = Entry(janela, width=20, fg="black")
ed1.place(x=250, y=203)

lb2 = Label(janela, text="Taxa de juros:", font=("Verdana", 12))
lb2.place(x=100, y=230)
ed2 = Entry(janela, width=20, fg="black")
ed2.place(x=250, y=233)

option2 = StringVar()
rd3 = Radiobutton(janela, text="% a.m.", fg="black", font=("Verdana", 12), variable=option2, value=1, tristatevalue=0)
rd3.place(x=250, y=252)
rd4 = Radiobutton(janela, text="% a.a.", fg="black", font=("Verdana", 12), variable=option2, value=2, tristatevalue=0)
rd4.place(x=250, y=275)


lb3 = Label(janela, text="Período (meses):", font=("Verdana", 12))
lb3.place(x=100, y=320)
ed3 = Entry(janela, width=20, fg="black")
ed3.place(x=250, y=323)

lb4 = Label(janela, text="Montante final:", font=("Verdana", 12))
lb4.place(x=100, y=350)
ed4 = Entry(janela, width=20, fg="black")
ed4.place(x=250, y=353)

bt = Button (janela, text="Calcular", command=calcular)
bt.place(x=250, y=400)


janela.mainloop()
