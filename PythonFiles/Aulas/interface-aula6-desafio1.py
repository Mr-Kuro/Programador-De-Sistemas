from tkinter import *


# class Interface:
#
#     def __init__(self):
#
#         self.janela = Tk()
#
#         self.font = ('Verdana', '15')
#
#         self.n = Frame(self.janela,)
#         self.n.pack()
#
#         self.l = Frame(self.janela,)
#         self.l.pack()
#
#         self.s = Frame(self.janela,)
#         self.s.pack()
#
#         self.label1 = Label(self.n, text='Label', height=3, width=20, font=self.font)
#         self.label1.pack()
#
#         self.labe2 = Label(self.s, text='Labe2', height=3, width=20, font=self.font)
#         self.labe2.pack()
#
#         self.labe3 = Label(self.l, text='Labe3', height=3, width=20, font=self.font)
#         self.labe3.pack(side=LEFT)
#
#         self.labe4 = Label(self.l, text='Labe4', height=3, width=20, font=self.font)
#         self.labe4.pack(side=RIGHT,)
#
#         mainloop()
#
#
# interface = Interface()


# resolução do professor

class Tela:
    def __init__(self):
        self.jaanela = Tk()

        self.fonte = ('Arial', '16')

        self.label1 = Label(self.jaanela, text='Label 1', font=self.fonte)
        self.label1.pack()

        self.label2 = Label(self.jaanela, text='Label 2', font=self.fonte)
        self.label2.pack(side=BOTTOM)

        self.label3 = Label(self.jaanela, text='Label 3', font=self.fonte)
        self.label3.pack(side=LEFT)

        self.label4 = Label(self.jaanela, text='Label 3', font=self.fonte)
        self.label4.pack(side=RIGHT)


        mainloop()


tela = Tela()