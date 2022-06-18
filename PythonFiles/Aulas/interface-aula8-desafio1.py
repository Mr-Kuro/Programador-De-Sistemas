# Relógio digital

# import datetime
#
# agora = datetime.datetime.now()
# agora.strftime('%H: %M: %S:')
# janela.after(100, self.alterarHora) #1000 segundos = 1

from tkinter import *
import datetime

class RelogioDigital:
    def __init__(self):
        self.janela = Tk()

        self.labelRelogio = Label(font=('calibri', '20', 'bold'))
        self.labelRelogio.pack(pady=10, padx=10)

        self.timeReal()

        mainloop()

    def timeReal(self):
        self.janela.after(1000, self.timeReal)
        self.labelRelogio['text'] = datetime.datetime.now().strftime('%H: %M: %S:')


tela1 = RelogioDigital()


# resolção do professor

# from tkinter import *
# import datetime
#
# class Tela:
#     def __init__(self):
#
#         self.jala_principal = Tk()
#
#         self.relogio = Label(self.jala_principal,
#                              font=('Arial', '16'),
#                              fg='blue')
#         self.relogio.pack(padx=30, pady=30)
#
#         self.alteraHora()
#
#         mainloop()
#
#     def alteraHora(self):
#         agora = datetime.datetime.now()
#
#         self.relogio['text'] = agora.strftime('%H: %M: %S:')
#
#         self.jala_principal.after(1000, self.alteraHora)
#
# interface = Tela()