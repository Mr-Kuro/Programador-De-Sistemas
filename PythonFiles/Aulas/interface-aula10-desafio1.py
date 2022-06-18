# programa que caucula a média aritimética de 3 notas recebidas
from tkinter import *


class MediaAritimetica:
    def __init__(self):
        self.janela_principal = Tk()
        self.janela_principal['bg'] = ('white')
        self.fonte = ('Verdana', '10')

        # frames
        self.frame1 = Frame(self.janela_principal, bg='white')
        self.frame1.pack()
        self.frame2 = Frame(self.janela_principal, bg='white')
        self.frame2.pack()
        self.frame3 = Frame(self.janela_principal, bg='white')
        self.frame3.pack()

        # titulo
        self.labelTitulo = Label(self.frame1, text='Calculador de média aritimética', font=('Calibri', '18', 'bold'), bg='white')
        self.labelTitulo.pack(pady=15, padx=25)

        # entrada de dados
        self.labelEntrada = Label(self.frame2, text='Digite uma nota por vez:', font=self.fonte, bg='white')
        self.labelEntrada.pack(side=LEFT, padx=5)

        self.entryEntrada = Entry(self.frame2, font=self.fonte)
        self.entryEntrada.pack(padx=13)

        # saida da resposta
        self.labelDinamicaStr = StringVar()
        self.labelDinamicaStr.set('Digitas as três notas...')

        self.labelResposta = Label(self.frame3, textvariable=self.labelDinamicaStr, font=self.fonte, fg='violet', bg='white')
        self.labelResposta.pack(pady=15)

        # tratando entradas
        self.entryEntrada.bind('<Key-Return>', self.calcular)

        # # self.aptoAMediar = False

        self.contador = 0
        self.somas = 0

        mainloop()

    def calcular(self, event):
        self.somas += int(self.entryEntrada.get())

        if self.contador < 4:
            self.contador += 1

        if self.contador == 3:
            self.labelDinamicaStr.set('A média aritimétia é: ' + str(self.somas / 3))
            self.contador += 1

        if self.contador > 3:
            self.somas = 0
            self.contador = 0

        print(self.contador, ' - ', self.somas)

        self.entryEntrada.delete(0, END)


interface = MediaAritimetica()
