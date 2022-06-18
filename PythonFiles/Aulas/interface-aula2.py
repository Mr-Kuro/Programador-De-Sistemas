from tkinter import *

janela = Tk()


# frame1= Frame(
#     master=janela,
#     width=200,
#     height=100,
#     bg='red'
# )
# # master = dentro de
# frame1.pack(fill=BOTH, side=LEFT, expand=TRUE)
# # fill = preencher todo o eixo
# # TOP = cima, BOTTOM = baixo, RIGHT = direita, LEFT = esquerda
#
#
# frame2 = Frame(
#     master=janela,
#     width=100,
#     bg='yellow'
# )
# frame2.pack(fill=BOTH, side=LEFT, expand=TRUE)
#
#
# frame3 = Frame(
#     master=janela,
#     width=50,
#     bg='blue'
# )
# frame3.pack(fill=BOTH, side=LEFT, expand=TRUE)
#
# # label = Label(
# #     master=frame3,
# #     text='Teste',
# #     width=200,
# #     height=200,
# #     bg='green'
# # )
# # label.pack(fill=BOTH)
# # # preencher todos os eixos


# frame = Frame(
#     master=janela,
#     width=175,
#     height=150,
#     bg='cyan'
# )
# frame.pack()
#
# label1 = Label(
#     master=frame,
#     text='Estou em 0,0',
#     bg='red'
# )
# label1.place(x=0, y=0)
# # place se utiliza da localização em pixel, mas não dá responsividade
#
# label2 = Label(
#     master=frame,
#     text='Teste',
#     bg='yellow'
# )
# label2.place(x=142, y=0)


for i in range(0, 3):
    janela.columnconfigure(i, weight=1, minsize=75)
    janela.rowconfigure(i, weight=1, minsize=50)
    for j in range(0, 3):
        frame = Frame(
            master=janela,
            relief=RAISED,
            borderwidth=3
        )
        frame.grid(row=i, column=j, padx=5, pady=5)

        label = Label(
            master=frame,
            text=f'Linha {i} \nColuna {j}'
        )
        label.pack(padx=5, pady=5)

# padding dá um preenchimento
# o grid é incrível com o for
# weight = peso no crescimento


# janela.rowconfigure(0, minsize=50)
# janela.columnconfigure([0,1,2,3], minsize=50)
#
# label1 = Label(
#     text='1',
#     bg='black',
#     fg='white'
# )
# label2 = Label(
#     text='2',
#     bg='black',
#     fg='white'
# )
# label3 = Label(
#     text='3',
#     bg='black',
#     fg='white'
# )
# label4 = Label(
#     text='4',
#     bg='black',
#     fg='white'
# )
#
# label1.grid(row=0, column=0)
# label2.grid(row=0, column=1, sticky='ew')
# label3.grid(row=0, column=2, sticky='ns')
# label4.grid(row=0, column=3, sticky='nsew')


# sticky=
# N ou n = topo centro
# E ou e = direita centro
# S ou s = baixo centro
# W ou w = esquerda centro
# NE ou ne = topo direita
# NW ou nw = topo esquerda
# SE ou se = baixo direita
# SW ou sw = baixo essquerda

# ns = força o componente(widget) a ocupar toda a cécula na vertical(eixo x)
# ew = força o componente(widget) a ocupar toda a cécula na horizontal(eixo y)
# nsew = força o componente(widget) a ocupar a cécula inteira


janela.mainloop()
