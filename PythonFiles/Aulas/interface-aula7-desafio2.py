# posicinamento dos botões
from tkinter import *


class PosicinamentoBotoes:
    def __init__(self):
        self.janela = Tk()

        self.fonte = ('Arial', '11', 'bold')

        # Frames
        self.frame0 = Frame(self.janela)
        self.frame0.pack()

        self.frame1 = Frame(self.janela)
        self.frame1.pack()

        self.frame2 = Frame(self.janela)
        self.frame2.pack()

        # BOTÕES
        # relif: RAISED, GROOV, SUNKEN, FLAT, RIDGE
        self.botao1 = Button(self.frame0, text='1', width=4, height=4, relief=SUNKEN)
        self.botao1.pack()

        self.botao2 = Button(self.frame1, text='2', width=4, height=4, relief=SUNKEN)
        self.botao2.pack(side=LEFT)

        self.botao3 = Button(self.frame1, text='3', width=4, height=4, relief=RAISED)
        self.botao3.pack(side=LEFT)

        self.botao4 = Button(self.frame2, text='4', width=4, height=4, relief=GROOVE)
        self.botao4.pack(side=LEFT)

        self.botao5 = Button(self.frame2, text='5', width=4, height=4, relief=FLAT)
        self.botao5.pack(side=LEFT)

        self.botao6 = Button(self.frame2, text='6', width=4, height=4, relief=RIDGE)
        self.botao6.pack(side=LEFT)

        mainloop()


tela = PosicinamentoBotoes()