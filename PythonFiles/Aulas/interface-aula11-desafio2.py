# programa que converte Celsius em F e F em C = Conversor de Temperatura
from tkinter import *
from tkinter import messagebox


class ConversorDeTemperatura:
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
        self.labelTitulo = Label(self.frame1, text='Conversor de Temperatura)', font=('Calibri', '18', 'bold'), bg='white')
        self.labelTitulo.pack(pady=15, padx=25)

        # entrada de dados F e C
        self.labelEntrada = Label(self.frame3, text='Escolha a entrada de temperatura...', font=self.fonte, bg='white')
        self.labelEntrada.pack(side=LEFT,padx=10,  pady=20)

        self.entryEntrada = Entry(self.frame3, font=self.fonte)
        self.entryEntrada.pack(padx=16,  pady=20)

        # RadioButtons
        self.opcao = StringVar()

        self.f = Radiobutton(self.frame1, text='Farenhit  >  Celsios', command=self.conversor, font=('ARIAL', '8', "bold"), bg='white', variable=self.opcao, value='F')
        self.f.pack(side=LEFT, pady=15)

        self.c = Radiobutton(self.frame1, text='Celsio  >  Farenhit', command=self.conversor, font=('ARIAL', '8', "bold"), bg='white', variable=self.opcao, value='C')
        self.c.pack(side=BOTTOM, pady=15)

        # Tratando dados
        self.entryEntrada.bind('<Return>', self.converter)

        mainloop()

    def conversor(self):
        if self.opcao.get() == 'C':
            self.labelEntrada['text'] = 'Digite a temperatura em Celsios:'

        elif self.opcao.get() == 'F':
            self.labelEntrada['text'] = 'Digite a temperatura em Farenhit:'

    def converter(self, event):
        if self.opcao.get() == 'F':
            c = float(self.entryEntrada.get())
            messagebox.showinfo('Coversor', f'{c}° Celsios são exatamente = {c * 1.8 + 32:.1f}° Farenhit.')
            print(c)

        elif self.opcao.get() == 'C':
            f = float(self.entryEntrada.get())
            messagebox.showinfo('Coversor', f'{f}º Farenhit  são exatamente = {(f - 32) / 1.8:.1f}° Celcios.')
            print(f)

        self.entryEntrada.delete(0, END)


interface = ConversorDeTemperatura()
