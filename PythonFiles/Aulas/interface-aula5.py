# from tkinter import *
#
#
# def tratador_evento(event):
#     print('Você clicou na posição:', event.x, event.y)
#
#
# janela_principal = Tk()
# meuFrame = Frame(janela_principal, width=100, height=100, bg='black')
# meuFrame.bind("<Button-1>", tratador_evento)
# meuFrame.pack()
#
# janela_principal.mainloop()


from tkinter import *
from tkinter import messagebox


class EntryTeste(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.pack()
        self.master.title('<Return> teste')
        self.master.geometry('300x50')
        self.frame = Frame(self, bg='black')
        self.frame.pack(pady=5)

        self.caixa = Entry(self.frame, name='caixa')
        self.caixa.bind('<Return>', self.exibe)
        self.caixa.pack(side=LEFT, padx=5)

        self.mainloop()

    def exibe(self, event):
        nomeCaixa = event.widget.winfo_name()
        conteudoCaixa = event.widget.get()
        messagebox.showinfo('Texto na caixa', 'Nome widget: ' + nomeCaixa + '\nconteudo: ' + conteudoCaixa)

#
# from tkinter import *
#
# from tkinter import messagebox
#
#
# class EntryTeste(Frame):
#
#     def __init__(self):
#         Frame.__init__(self, bg='cyan')
#         self.pack(expand=YES, fill=BOTH)
#         self.master.title('componente de  entrada')
#         self.master.geometry('325x100')
#         self.frame = Frame(self)
#         self.frame.pack(pady=5)
#
#         self.caixa = Entry(self.frame, name='caixa1')
#         self.caixa.bind('<Return>', self.exibe)
#         self.caixa.pack(side=LEFT, padx=5)
#
#         self.caixa2 = Entry(self.frame, name='caixa2')
#         self.caixa2.insert(INSERT, "Digite um texto aqui")
#         self.caixa2.bind('<Return>', self.exibe)
#         self.caixa2.pack(side=LEFT, padx=5)
#
#         self.frame2 = Frame(self)
#         self.frame2.pack(pady=5)
#
#         self.caixa3 = Entry(self.frame2, name='caixa3')
#         self.caixa3.insert(INSERT, 'Texto não editavel')
#         self.caixa3.config(state=DISABLED)
#         self.caixa3.bind('<Return>', self.exibe)
#         self.caixa3.pack(side=LEFT, padx=5)
#
#         self.caixa4 = Entry(self.frame2, name='caixa4')
#         self.caixa4.insert(INSERT, 'Texto escondido')
#         self.caixa4.bind('<Return>', self.exibe)
#         self.caixa4.pack(side=LEFT, padx=5)
#
#         self.mainloop()
#
#     def exibe(self, event):
#         nomeCaixa = event.widget.winfo_name()
#         conteudoCaixa = event.widget.get()
#         messagebox.showinfo('Texto na caixa', 'Nome widget: ' + nomeCaixa + '\nconteudo: ' + conteudoCaixa)

bala = EntryTeste()
#


# from tkinter import *
#
# from tkinter import messagebox
#
#
# class ButtonEvent(Frame):
#
#     def __init__(self):
#         Frame.__init__(self, bg='cyan')
#         self.pack()
#         self.master.title('Botão')
#         self.master.geometry('120x40')
#
#         self.botao = Button(self, text='Clique aqui', command=self.apertou)
#         self.botao.bind('<Enter>', self.passou_por_cima)
#         self.botao.bind('<Leave>', self.saiu_de_cima)
#         self.botao.pack(side=LEFT, padx=5, pady=5)
#
#         self.mainloop()
#
#     def apertou(self):
#        messagebox.showinfo('Message', "você apertou o botão")
#
#     def passou_por_cima(self, event):
#         event.widget.config(relief=SUNKEN)
#         # RAISED = acima da interface
#         # GROOVE = mesma altura da interface
#         # SUNKEN = abaixo da interface
#         # FLAT = sem contorno
#         # REDGE = contorno branco
#
#     def saiu_de_cima(self, event):
#         event.widget.config(relief=RAISED)

#
# from tkinter import *
#
#
# class MouseEvent(Frame):
#
#     def __init__(self):
#         Frame.__init__(self, bg='cyan')
#         self.pack(expand=YES, fill=BOTH)
#         self.master.title('Eventos com mouse')
#         self.master.geometry('300x200')
#
#         self.mousePosicao = StringVar()
#         self.mousePosicao.set('Mouse fora da janela')
#
#         self.positionLabel = Label(self, textvariable=self.mousePosicao)
#         self.positionLabel.pack(side=BOTTOM)
#
#         self.bind('<Button-1>', self.botaoPressionado)
#         self.bind('<ButtonRelease-1>', self.botaoLiberado)
#         self.bind('<Enter>', self.entrouJanela)
#         self.bind('<Leave>', self.saiuJanela)
#         self.bind("<B1-Motion>", self.mouseArrastado)
#
#         self.mainloop()
#
#     def botaoPressionado(self, event):
#         self.mousePosicao.set('Pressionado em [' + str(event.x) + ',' + str(event.y) + ']')
#
#     def botaoLiberado(self, event):
#         self.mousePosicao.set('Solto em [' + str(event.x) + ',' + str(event.y) + ']')
#
#     def botaoArrastado(self, event):
#         self.mousePosicao.set('Arraste até [' + str(event.x) + ',' + str(event.y) + ']')
#
#     def entrouJanela(self, event):
#         self.mousePosicao.set('Mouse na janela')
#
#     def saiuJanela(self, event):
#         self.mousePosicao.set('Mouse fora da janela')
#
#     def mouseArrastado(self, event):
#         self.mousePosicao.set('Arrastado até [' + str(event.x) + ',' + str(event.y) + ']')
#


# from tkinter import *
#
#
# class KeyboardEvent(Frame):
#
#     def __init__(self):
#         Frame.__init__(self, bg='cyan')
#         self.pack(expand=YES, fill=BOTH)
#         self.master.title('Eventos do teclado')
#         self.master.geometry('300x200')
#
#         self.mensagem = StringVar()
#         self.mensagem.set('Aperte uma tecla')
#
#         self.Label = Label(self, textvariable=self.mensagem)
#         self.Label.pack()
#
#         self.bind('<KeyPress>', self.teclaPressionada)
#         self.bind('<KeyRelease>', self.teclaLiberada)
#         self.bind('<KeyPress-Alt_L>', self.altPressionado)
#         self.bind('<KeyRelease-Alt_L>', self.altLiberado)
#
#         self.mainloop()
#
#     def teclaPressionada(self, event):
#         self.mensagem.set('Tecla pressionada: ' + event.char)
#
#     def teclaLiberada(self, event):
#         self.mensagem.set('Tecla Solta: ' + event.char)
#
#     def altPressionado(self):
#         self.mensagem.set('Alt pressionado: ')
#
#     def altLiberado(self):
#         self.mensagem.set('Alt liberado: ')


# teste da class
# minhaInterface = EntryTeste()
