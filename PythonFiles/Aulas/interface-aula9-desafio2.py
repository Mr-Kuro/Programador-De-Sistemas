# from tkinter import *
#
#
# class Interface:
#     def __init__(self):
#         self.janela = Tk()
#
#         self.entry = Entry(self.janela,)
#         self.entry.pack()
#         self.entry.bind('<Key-minus>', self.corretor)
#         self.entry.bind('<Key-period>', self.corretor)
#
#         mainloop()
#
#     def corretor(self, event):
#         copia = self.entry.get()
#         baka = len(copia) -1
#         print(copia[baka])
#         if copia[baka] == '.' or copia[baka] == '-':
#             self.entry.delete(copia)
#
#         self.janela.after(1000, self.corretor)
#
#
# tela = Interface()

from tkinter import *

class Tela:
    def __init__(self):
        self.janela = Tk()

        self.frameCima = Frame(self.janela)
        self.frameCima.pack()

        self.frameBaixo = Frame(self.janela)
        self.frameBaixo.pack()

        self.nome = Label(self.frameCima, text='Nome:', font=('Arial', '16'))
        self.nome.pack(side=LEFT, padx=10)

        self.caixaNome = Entry(self.frameCima, font=('Arial', '16'))
        self.caixaNome.pack(side=LEFT)

        self.cpf = Label(self.frameBaixo, text='CPF', font=('Arial', '16'))
        self.cpf.pack(side=LEFT)

        self.caixaCpf = Entry(self.frameBaixo, font=('Arial', '16'))
        self.caixaCpf.pack(side=LEFT, padx=10)

        self.apareceu = False

        self.caixaCpf.bind('<KeyPress>', self.retira)

        mainloop()

    def retira(self, event):
        if event.char == '.' or event.char == '-':
            self.apareceu = True
        elif self.apareceu == True:
            tamanho = len(event.widget.get())
            event.widget.delete(tamanho-1)
            self.apareceu = False


tela = Tela()
