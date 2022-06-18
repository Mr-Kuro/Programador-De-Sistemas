# programa que caucula o IMC (Índice de Massa Corporal)
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

        self.frame4 = Frame(self.janela_principal, bg='white')
        self.frame4.pack()

        self.frame5 = Frame(self.janela_principal, bg='white')
        self.frame5.pack()

        # titulo
        self.labelTitulo = Label(self.frame1, text='Calculador de IMC (Índice de Massa Corporal)', font=('Calibri', '18', 'bold'), bg='white')
        self.labelTitulo.pack(pady=15, padx=25)

        # entrada de dados peso
        self.labelEntradaPeso = Label(self.frame2, text='Digite Seu peso:', font=self.fonte, bg='white')
        self.labelEntradaPeso.pack(side=LEFT, padx=8, pady=10)

        self.entryEntradaPeso = Entry(self.frame2, font=self.fonte)
        self.entryEntradaPeso.pack(padx=16,  pady=10)

        # entrada de dados altura
        self.labelEntradaAltura = Label(self.frame3, text='Digite sua altura:', font=self.fonte, bg='white')
        self.labelEntradaAltura.pack(side=LEFT, padx=5)

        self.entryEntradaAltura = Entry(self.frame3, font=self.fonte)
        self.entryEntradaAltura.pack(padx=13)

        # saida da resposta

        self.labelResposta = Label(self.frame4, font=self.fonte, fg='violet', bg='white')
        self.labelResposta.pack(pady=15)

        # tratando entradas
        self.botao = Button(self.frame5, text='CALCULAR IMC', command=self.calcular, font=('ARIAL', '8', "bold"), fg='white', bg='gray')
        self.botao.pack(pady=15)

        mainloop()

    def calcular(self):
        imc = float(float(self.entryEntradaPeso.get()) / (float(self.entryEntradaAltura.get()) ** 2))
        if imc < 18.5:
            self.labelResposta['text'] = f'Com um IMC de {imc:.1f}, sua situação é de Magresa.'
        elif 24.9 >= imc >= 18.5:
            self.labelResposta['text'] = f'Com um IMC de {imc:.1f}, sua situação é Normal.'
        elif 29.9 >= imc > 24.9:
            self.labelResposta['text'] = f'Com um IMC de {imc:.1f}, sua situação é de Sobrepeso.'
        elif 39.9 >= imc > 29.9:
            self.labelResposta['text'] = f'Com um IMC de {imc:.1f}, sua situação é de Obesidade.'
        elif 40 <= imc:
            self.labelResposta['text'] = f'Com um IMC de {imc:.1f}, sua situação é de Obesidade Grave.'

        print(imc)

        self.entryEntradaAltura.delete(0, END)
        self.entryEntradaPeso.delete(0, END)


interface = MediaAritimetica()
