# Crie 3 Radiobuttons, um com o texto “Python”,
# outro com o texto “Java” e o último com o texto “C++”.
# Além disso, crie um botão abaixo dos Radiobuttons com o texto “confirmar”,
# e por último um label sem nenhum texto. Quando o botão for clicado,
# deverá ser avaliado qual a escolha selecionada nos Radiobuttons pelo usuário,
# para cada linguagem, deverá ser exibida no label a sintaxe de “hello world” de cada um:

from tkinter import *


class Interface:
    def __init__(self):
        self.janela = Tk()

        self.fonte1 = ('Calibri', '13', 'bold')
        self.fonte2 = ('Verdana', '10')

        # frames
        self.frame0 = Frame(self.janela)
        self.frame0.pack()

        self.frame1 = Frame(self.janela)
        self.frame1.pack()

        self.frame2 = Frame(self.janela)
        self.frame2.pack()

        self.frame3 = Frame(self.janela)
        self.frame3.pack()

        self.frame4 = Frame(self.janela)
        self.frame4.pack()

        # explicação
        self.linguagem = Label(self.frame0, text='Linguagem', font=self.fonte1)
        self.linguagem.pack(side=LEFT)

        self.sintaxe = Label(self.frame0, text='Sintaxe', font=self.fonte1)
        self.sintaxe.pack(side=LEFT)

        # radiobuttons linguagem e sintaxe

        # primeira opção marcada inialmente
        self.radio_valor = IntVar()
        self.radio_valor.set(1)

        # python
        self.radioPyrhon = Radiobutton(self.frame1, text='Python', variable=self.radio_valor, font=self.fonte1,
                                       value=1, command=self.exibe)
        self.radioPyrhon.pack(side=LEFT, padx=0)

        self.sintaxePython = Label(self.frame1, text="print('Hello, World!')", font=self.fonte2)
        self.sintaxePython.pack(side=LEFT, padx=45)

        # Java
        self.radioJava = Radiobutton(self.frame2, text='Java', variable=self.radio_valor, font=self.fonte1, value=2, command=self.exibe)
        self.radioJava.pack(side=LEFT, padx=0)

        self.sintaxeJava = Label(self.frame2, text="System.out.println('Hello, World!')", font=self.fonte2)
        self.sintaxeJava.pack(side=LEFT, padx=10)

        # C++
        self.radioCMM = Radiobutton(self.frame3, variable=self.radio_valor, text='C++', font=self.fonte1, value=3, command=self.exibe)
        self.radioCMM.pack(side=LEFT, padx=0)

        self.sintaxeCMM = Label(self.frame3, text="std::cout<<'Hello, World!'<<std::endl", font=self.fonte2)
        self.sintaxeCMM.pack(side=LEFT, padx=0)

        # label de resposta
        self.resposta = Label(self.frame4, text='Escolha um botão', font=self.fonte1, fg='white', bg='violet')
        self.resposta.pack(pady=0)

        mainloop()

    def exibe(self):
        if self.radio_valor.get() == 1:
            self.resposta['text'] = "print('Hello, World!')"
        elif self.radio_valor.get() == 2:
            self.resposta['text'] = "System.out.println('Hello, World!')"
        elif self.radio_valor.get() == 3:
            self.resposta['text'] = "std::cout<<'Hello, World!'<<std::endl"



tela = Interface()


# resolução do professor

from tkinter import *

class Tela:
    def __init__(self):
        self.janela = Tk()

        self. valor = StringVar()

        self.rb1 = Radiobutton(
            self.janela,
            text='Python',
            variable=self.valor,
            value='Python'
        )
        self.rb1.pack()
        self.rb1.select()

        self.rb2 = Radiobutton(
            self.janela,
            text='Java',
            variable=self.valor,
            value='Java'
        )
        self.rb2.pack()

        self.rb3 = Radiobutton(
            self.janela,
            text='C++',
            variable=self.valor,
            value='C++'
        )
        self.rb3.pack()

        self.bnt = Button(
            self.janela,
            text='Confirmar',
            command=self.mostrar
        )
        self.bnt.pack()

        self.saida = Label(self.janela)
        self.saida.pack()

        mainloop()

    def mostrar(self):
        escolha = self.valor.get()
        if escolha == 'Python':
            self.saida['text'] = "print('Hello World')"
        elif escolha == 'Java':
            self.saida['text'] = "System.out.println('Hello World')"
        elif escolha == 'C++':
            self.saida['text'] = "std::cout << 'Hello World' << std::endl"

interface = Tela()

