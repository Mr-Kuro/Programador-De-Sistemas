# programa que soma dois inteiros

from tkinter import *


class SomaInteiros:
    def __init__(self):
        self.janela = Tk()

        self.fonte = ('Verdana', '15')

        self.titulo = Label(text="Digite os números inteiros em cada caixa", font=('Calibri', '20'))
        self.titulo.pack()

        self.num1 = Entry(width=16, font=self.fonte)
        self.num1.pack(padx=8, pady=8)

        self.num2 = Entry(width=16, font=self.fonte)
        self.num2.pack(padx=8, pady=8)

        self.labelDinamica = StringVar()
        self.labelDinamica.set('Clique-me')
        self.resposta = Label(textvariable=self.labelDinamica)
        self.resposta.pack()
        self.resposta.bind('<Button-1>', self.exibe)

        mainloop()

    def exibe(self, event):
        resposta = str(int(self.num1.get()) + int(self.num2.get()))
        self.labelDinamica.set(f'Resultado: {resposta}')



programa = SomaInteiros()


# resolução professor

class Tela:
    def __init__(self):
        self.janela_principal = Tk()

        self.frameCima = Frame(self.janela_principal)
        self.frameMeio = Frame(self.janela_principal)
        self.frameBaixo = Frame(self.janela_principal)

        self.frameCima.pack()
        self.frameMeio.pack()
        self.frameBaixo.pack()

        self.valor1 = Entry(self.frameCima, width=25)
        self.valor1.pack(side=LEFT, padx=10)

        self.valor2 = Entry(self.frameMeio, width=25)
        self.valor2.pack(side=LEFT, padx=10)

        self.labelDinamica = StringVar()
        self.labelDinamica.set('Clique aqui')

        self.result = Label(self.frameBaixo, textvariable=self.labelDinamica)
        self.result.pack()

        self.result.bind('<Button-1>', self.somar)

        mainloop()

    def somar(self, event):
        self.inteiro1 = int(self.valor1.get())
        self.inteiro2 = int(self.valor2.get())

        self.resultado = self.inteiro1 + self.inteiro2

        self.labelDinamica.set(str(self.resultado))


tela = Tela()
