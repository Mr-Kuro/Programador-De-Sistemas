# Programa que caulcula os valores de Delta

from tkinter import *
import math


class Delta:
    def __init__(self):
        self.janela_principal = Tk()
        self.janela_principal['bg'] = ('white')
        self.fonte = ('Verdana', '10')

        # frames
        self.frame0 = Frame(self.janela_principal, bg='white')
        self.frame0.pack()

        self.frame1 = Frame(self.janela_principal, bg='white')
        self.frame1.pack()

        self.frame2 = Frame(self.janela_principal, bg='white')
        self.frame2.pack()

        self.frame3 = Frame(self.janela_principal, bg='white')
        self.frame3.pack()

        self.frame4 = Frame(self.janela_principal, bg='white')
        self.frame4.pack()

        self.frame5 = Frame(self.janela_principal, bg='white')
        self.frame5.pack()

        # titulo
        self.labelTitulo = Label(self.frame0, text='Calculadora para os valores de DELTA', font=('Calibri', '18', 'bold'), bg='white')
        self.labelTitulo.pack(pady=15, padx=25)

        # entrada de dados A
        self.labelEntradaA = Label(self.frame1, text='Digite o valor de A:', font=self.fonte, bg='white')
        self.labelEntradaA.pack(side=LEFT, padx=8, )

        self.entryEntradaA = Entry(self.frame1, font=self.fonte)
        self.entryEntradaA.pack(padx=16,  pady=10)

        # entrada de dados B
        self.labelEntradaB = Label(self.frame2, text='Digite o valor de B:', font=self.fonte, bg='white')
        self.labelEntradaB.pack(side=LEFT, padx=8, pady=10)

        self.entryEntradaB = Entry(self.frame2, font=self.fonte)
        self.entryEntradaB.pack(padx=16,  pady=10)

        # entrada de dados C
        self.labelEntradaC = Label(self.frame3, text='Digite o valor de C:', font=self.fonte, bg='white')
        self.labelEntradaC.pack(side=LEFT, padx=8)

        self.entryEntradaC = Entry(self.frame3, font=self.fonte)
        self.entryEntradaC.pack(padx=16,  pady=10)

        # saida da resposta

        self.labelResposta = Label(self.frame4, font=self.fonte, fg='violet', bg='white')
        self.labelResposta.pack(pady=15)

        # tratando entradas
        self.botao = Button(self.frame5, text='Calcular valores de DELTA', command=self.calcular, font=('ARIAL', '8', "bold"), fg='white', bg='gray')
        self.botao.pack(pady=15)

        mainloop()

    def calcular(self):

        delta = float(self.entryEntradaB.get()) ** 2 - 4 * float(self.entryEntradaA.get()) * float(self.entryEntradaC.get())

        x1 = (0- float(self.entryEntradaB.get()) + math.sqrt(delta)) / (2 * float(self.entryEntradaA.get()))
        x2 = (0 --float(self.entryEntradaB.get()) - math.sqrt(delta)) / (2 * float(self.entryEntradaA.get()))

        self.labelResposta['text'] = f'X1 = {x1}\n X2 = {x2}'

        print(f'{delta} DELTA\n{x1} X1\n{x2} X2\n{delta ** 0.5}  #RAIZ QUADRADA DE DELTA')

        self.entryEntradaA.delete(0, END)
        self.entryEntradaB.delete(0, END)
        self.entryEntradaC.delete(0, END)


interface = Delta()


# Resolução do professor

from tkinter import *


class Tela:
    def __init__(self):
        self.janela = Tk()

        self.frame1 = Frame(self.janela)
        self.frame1.pack()

        self.frame2 = Frame(self.janela)
        self.frame2.pack()

        self.frame3 = Frame(self.janela)
        self.frame3.pack()

        self.frame4 = Frame(self.janela)
        self.frame4.pack()

        self.frame5 = Frame(self.janela)
        self.frame5.pack()

        self.labelA = Label(self.frame1, text='Digite o valor de A')
        self.labelA.pack(side=LEFT)
        self.entryA = Entry(self.frame1)
        self.entryA.pack(side=LEFT)

        self.labelB = Label(self.frame2, text='Digite o valor de B')
        self.labelB.pack(side=LEFT)
        self.entryB = Entry(self.frame2)
        self.entryB.pack(side=LEFT)

        self.labelC = Label(self.frame3, text='Digite o valor de C')
        self.labelC.pack(side=LEFT)
        self.entryC = Entry(self.frame3)
        self.entryC.pack(side=LEFT)



        self.botao = Button(self.frame4, text='Caucular', command=self.equacao)
        self.botao.pack()

        self.saida = Label(self.frame5)

        mainloop()

    def equacao(self):
        a = float(self.entryA.get())
        b = float(self.entryB.get())
        c = float(self.entryC.get())

        if a == 0:
           self.saida['text'] = 'O valor de A não pode ser 0'
        else:
           delta = b * b - 4 * a * c

           x1 = (0-b + math.sqrt(delta)) / 2 * a
           x2 = (0-b - math.sqrt(delta)) / 2 * a

           print(delta)

           self.saida['text'] = f'{x1}, {x2}'


tela = Tela()