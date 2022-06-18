from tkinter import *


class Tela:
    # criando janela
    janela_principal = Tk()

    # mudar titulo da janela
    janela_principal.title('Cadastro de Clientes')

    # variaveis para armazenar os dados dos usuários
    txtNome = StringVar()
    txtSobrenome = StringVar()
    txtEmail = StringVar()
    txtCPF = StringVar()

    # labels para sinalizar cada caixa de texto
    labelNome = Label(janela_principal, text='Nome')
    labelSobrenome = Label(janela_principal, text='Sobrenome')
    labelEmail = Label(janela_principal, text='Email')
    labelCPF = Label(janela_principal, text='CPF')

    # entrys para cada dado digitado
    entNome = Entry(janela_principal, textvariable=txtNome)
    entSobrenome = Entry(janela_principal, textvariable=txtSobrenome)
    entEmail = Entry(janela_principal, textvariable=txtEmail)
    entCPF = Entry(janela_principal, textvariable=txtCPF)

    # componentes para listas de clientes
    listClientes = Listbox(janela_principal, width=100)

    # area de texto para junto do listbox
    scrollClientes = Scrollbar(janela_principal)

    # Criando os botões do sistema
    verTodos = Button(janela_principal, text='Ver todos')
    buscar = Button(janela_principal, text='Buscar')
    inserir = Button(janela_principal, text='Inserir')
    atualizar = Button(janela_principal, text='Atualizar selecionado')
    deletar = Button(janela_principal, text='Deletar selecionados')
    fechar = Button(janela_principal, text='Fechar')

    # adicionar os componentes (widgets)
    labelNome.grid(row=0, column=0)
    labelSobrenome.grid(row=1, column=0)
    labelEmail.grid(row=2, column=0)
    labelCPF.grid(row=3, column=0)

    entNome.grid(row=0, column=1)
    entSobrenome.grid(row=1, column=1)
    entEmail.grid(row=2, column=1)
    entCPF.grid(row=3, column=1)

    listClientes.grid(row=0, column=2, rowspan=10)

    scrollClientes.grid(row=0, column=6, rowspan=10)

    verTodos.grid(row=4, column=0, columnspan=2)

    buscar.grid(row=5, column=0, columnspan=2)
    inserir.grid(row=6, column=0, columnspan=2)
    atualizar.grid(row=7, column=0, columnspan=2)
    deletar.grid(row=8, column=0, columnspan=2)
    fechar.grid(row=9, column=0, columnspan=2)

    # associando a scrollbar com o listbox
    listClientes.configure(yscrollcommand=scrollClientes.set)
    scrollClientes.configure(command=listClientes.yview)

    # criando variaveis para definir o padding e largura dos componentes
    x_pad = 5
    y_pad = 3
    width_entry = 30

    # adicionando beleza na interface

    for child in janela_principal.winfo_children():
        widget_class = child.__class__.__name__
        if widget_class == 'Button':
            child.grid_configure(sticky='ew', padx=x_pad, pady=y_pad)
        elif widget_class == 'Listbox':
            child.grid_configure(padx=0, pady=0, sticky='ns')
        elif widget_class == 'Scrollbar':
            child.grid_configure(padx=0, pady=0, sticky='ns')
        else:
            child.grid_configure(padx=x_pad, pady=y_pad, sticky='n')

    def executar(self):
        Tela.janela_principal.mainloop()  # vai chamar depois
