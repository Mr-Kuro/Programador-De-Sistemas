# Descrição: O botão “confirmar” deverá acionar um método (utilizando o command)
# que adquira o nome inserido no campo de entrada
# e o imprima em um label, com a mensagem ‘olá’ + nome_Inserido.

from tkinter import *


class ImprimeNome:
    def __init__(self):
        self.janela = Tk()

        self.fonte = ('Arial', '11')

        self.frame0 = Frame(self.janela)
        self.frame0.pack()

        self.frame1 = Frame(self.janela)
        self.frame1.pack()

        self.frame2 = Frame(self.janela)
        self.frame2.pack()

        self.titulo = Label(self.frame0,
                            text='ImprimeNome',
                            width=12,
                            font=('Calibri', '15', 'bold'))
        self.titulo.pack(side=TOP)

        self.labelNome = Label(self.frame1,
                               text='Digite seu nome',
                               width=12,
                               font=self.fonte)
        self.labelNome.pack(side=LEFT, padx=5, pady=8)

        self.entryNome = Entry(self.frame1, width=12, font=self.fonte)
        self.entryNome.pack(side=LEFT, padx=5)

        self.botao = Button(
            self.frame1,
            text='Print',
            bg='green',
            foreground='white',
            relief=GROOVE,
            width=10,
            font=self.fonte,
            command=self.print)
        self.botao.pack(side=LEFT, padx=5)

        self.dinamicNomeLabel = StringVar()
        self.printNomeLabel = Label(
            self.frame2,
            textvariable=self.dinamicNomeLabel,
            width=12, font=self.fonte)
        self.printNomeLabel.pack()

        mainloop()

    def print(self):
        self.dinamicNomeLabel.set('Olá ' + self.entryNome.get())


tela = ImprimeNome()
