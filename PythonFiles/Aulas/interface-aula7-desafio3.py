# Conversor de tempo segundos em horas e segundos em minutos
from tkinter import *


def minutos(segundos):
    segundos = int(segundos)
    rMinutos = str(segundos // 60)
    rSegundos = str(segundos % 60)
    return f'{segundos} segundos = {rMinutos} minutos e {rSegundos} segundos'


class ConversorDeTempo:
    def __init__(self):
        self.janela = Tk()

        self.fonte = ('Arial', '12', 'bold')

        # Frames
        self.frameTitulo = Frame(self.janela)
        self.frameTitulo.pack()

        self.frame0 = Frame(self.janela)
        self.frame0.pack()

        self.frame1 = Frame(self.janela)
        self.frame1.pack()

        self.frame2 = Frame(self.janela)
        self.frame2.pack()

        # Labels Entry segundos
        self.labelEntrySegundos = Label(
            self.frame0,
            text='Digite a quantidade em segundos:',
            fg='white', bg='green',
            font=self.fonte)
        self.labelEntrySegundos.pack(side=LEFT)

        self.entrySegundos = Entry(self.frame0, font=self.fonte, fg='white', bg='gray')
        self.entrySegundos.pack(side=LEFT, pady=10, padx=10)


        # labels para armazenar e mostrar os valores convertidos
        self.DinamicLabel = StringVar()

        self.showHoras = Label(self.frame1,
                                 textvariable=self.DinamicLabel,
                                 font=self.fonte, bg='gray', fg='cyan')
        self.showHoras.pack(pady=12)

        # Label de Título e Explicação
        self.titulo = Label(self.frameTitulo,
                            text='Conversor de tempo',
                            font=('Calibri', '18', 'bold'),
                            bg='yellow', fg='Violet')
        self.titulo.pack()

        self.explane = Label(self.frame2,
                            text='Pressione a tecla Enter para ver o resultado',
                            font=('Verdana', '10'),
                            bg='yellow',)
        self.explane.pack()

        # botão
        self.entrySegundos.bind('<Return>', self.minutos_horas)

        mainloop()

    def minutos_horas(self, event):
        rMminutos = int(self.entrySegundos.get()) // 60
        rMSegundos = int(self.entrySegundos.get()) % 60

        rHHoras = int(self.entrySegundos.get()) // 3600
        rHMinutos = int(self.entrySegundos.get()) % 3600 // 60
        rHSegundos = int(self.entrySegundos.get()) % 3600 % 60

        self.DinamicLabel.set(f'{self.entrySegundos.get()} segundos = {rHHoras} horas, {rHMinutos} minutos e {rHSegundos} segundos')



tela = ConversorDeTempo()

