from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database

db = Database("funcionarios.db")
janela_principal = Tk()
janela_principal.title("Sistema de gerenciamento de funcionários")
janela_principal.geometry("1920x1080+0+0")
janela_principal.configure(bg="#2c3e50")
janela_principal.state("zoomed")

nome = StringVar()
idade = IntVar()
dataN = StringVar()
genero = StringVar()
email = StringVar()
telefone = StringVar()
endereco = StringVar()

frame1 = Frame(janela_principal, bg="#5d5c68")
frame1.pack(side=TOP, fill=X)
titulo = Label(frame1, text='Sistema de gerenciamento de funcionários', font=('Calibri', '18', 'bold'), bg="#5d5c68",
               fg="white")
titulo.grid(row=0, columnspan=2, pady=10, padx=10, sticky="w")

labelNome = Label(frame1, text='Nome', font=('Calibri', '16'), bg="#5d5c68", fg='white')
labelNome.grid(row=1, column=0, padx=10, pady=10, sticky="w")
txtNome = Entry(frame1, textvariable=nome, font=('Calibri', '16'))
txtNome.grid(row=1, column=1, padx=10, pady=10, sticky="w")

labelIdade = Label(frame1, text='Idade', font=('Calibri', '16'), bg="#5d5c68", fg='white')
labelIdade.grid(row=1, column=2, padx=10, pady=10, sticky="w")
txtIdade = Entry(frame1, textvariable=idade, font=('Calibri', '16'))
txtIdade.grid(row=1, column=3, padx=10, pady=10, sticky="w")

labelData = Label(frame1, text='Data de nascimento', font=('Calibri', '16'), bg="#5d5c68", fg='white')
labelData.grid(row=2, column=0, padx=10, pady=10, sticky="w")
txtData = Entry(frame1, textvariable=dataN, font=('Calibri', '16'))
txtData.grid(row=2, column=1, padx=10, pady=10, sticky="w")

labelEmail = Label(frame1, text='Email', font=('Calibri', '16'), bg="#5d5c68", fg='white')
labelEmail.grid(row=2, column=2, padx=10, pady=10, sticky="w")
txtEmail = Entry(frame1, textvariable=email, font=('Calibri', '16'))
txtEmail.grid(row=2, column=3, padx=10, pady=10, sticky="w")

labelGenero = Label(frame1, text='Genero', font=('Calibri', '16'), bg="#5d5c68", fg='white')
comboGenero = ttk.Combobox(frame1, textvariable=genero, font=('Calibri', '16'), state="readonly")
labelGenero.grid(row=3, column=0, padx=10, pady=10, sticky="w")
comboGenero['values'] = ('Masculino', "Feminino")
comboGenero.grid(row=3, column=1, padx=10, pady=10, sticky="w")

labelTelefone = Label(frame1, text='Telefone', font=('Calibri', '16'), bg="#5d5c68", fg='white')
labelTelefone.grid(row=3, column=2, padx=10, pady=10, sticky="w")
txtTelefone = Entry(frame1, textvariable=telefone, font=('Calibri', '16'))
txtTelefone.grid(row=3, column=3, padx=10, pady=10, sticky="w")

labelEndereco = Label(frame1, text='Endereço', font=('Calibri', '16'), bg="#5d5c68", fg='white')
labelEndereco.grid(row=4, column=0, padx=10, pady=10, sticky="w")
txtEndereco = Text(frame1, font=('Calibri', '16'), width=72, height=5)
txtEndereco.grid(row=5, column=0, columnspan=4, padx=10, pady=10, sticky="w")


def getData(event):
    # pega a linha da tabela onde o ponteiro do mouse está
    selected_row = tv.focus()  # linha em que o mouse está encima
    # pega o item(funcionario que está na linha da tabela
    data = tv.item(selected_row)
    global row
    row = data['values']
    nome.set(row[1])
    idade.set(row[2])
    dataN.set(row[3])
    email.set(row[4])
    genero.set(row[5])
    telefone.set(row[6])
    txtEndereco.delete(1.0, END)
    txtEndereco.insert(END, row[7])


def displayAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert('', END, values=row)


def add_funcionario():
    if (txtNome.get() == '' or txtIdade.get() == 0 or
            txtData.get() == "" or txtEmail.get() == "" or
            comboGenero == '' or
            txtTelefone.get() == '' or
            txtEndereco.get(1.0, END) == ""):
        messagebox.showerror('Erro na entrada', 'Por favor preencha todos os campos')
    else:
        db.insert(txtNome.get(), txtIdade.get(),
                  txtData.get(), txtEmail.get(),
                  comboGenero.get(), txtTelefone.get(), txtEndereco.get(1.0, END))
        messagebox.showinfo('Sucesso', 'Funcionário cadastrado!')
        clearAll()
        displayAll()

def edit_funcionario():
    if (txtNome.get() == '' or txtIdade.get() == 0 or
            txtData.get() == "" or txtEmail.get() == "" or
            comboGenero == '' or
            txtTelefone.get() == '' or
            txtEndereco.get(1.0, END) == ""):
        messagebox.showerror('Erro na entrada', 'Por favor preencha todos os campos')
    else:
        db.update(row[0], txtNome.get(), txtIdade.get(), txtData.get(), txtEmail.get(), comboGenero.get(),
                  txtTelefone.get(), txtEndereco.get(1.0, END))
        messagebox.showinfo('Sucesso', 'Cadastrado do Funcionáio atualizado com sucesso!')
        clearAll()
        displayAll()


def del_funcionario():
    db.remove(row[0])
    clearAll()
    displayAll()

def clearAll():
    nome.set('')
    idade.set(0)
    dataN.set('')
    genero.set('')
    email.set('')
    telefone.set('')
    txtEndereco.delete(1.0, END)


frame2 = Frame(frame1, bg="#5d5c68")
frame2.grid(row=6, column=0, columnspan=4, pady=10, padx=10, sticky="w")

btnAdd = Button(frame2, command=add_funcionario, text="Adicionar", width=15, font=('Calibri', '16', 'bold'),
                bg="#16a085", fg='#fff')
btnAdd.grid(row=0, column=0, padx=10)

btnEdit = Button(frame2, command=edit_funcionario, text="Editar", width=15, font=('Calibri', '16', 'bold'),
                 bg="#2980b9", fg='#fff')
btnEdit.grid(row=0, column=1, padx=10)

btnDel = Button(frame2, command=del_funcionario, text="Deletar", width=15, font=('Calibri', '16', 'bold'), bg="#c0392b",
                fg='#fff')
btnDel.grid(row=0, column=2, padx=10)

btnClear = Button(frame2, command=clearAll, text="Limpar campo", width=15, font=('Calibri', '16', 'bold'), bg="#f39c12",
                  fg='#fff')
btnClear.grid(row=0, column=3, padx=10)

frame3 = Frame(janela_principal, bg='#ecf0f1')
frame3.place(x=0, y=480, width=1980, height=520)

# o estilo da tabela que será criada
stile = ttk.Style()
stile.configure('mystyle.Treeview', font=('Calibri', 18), rowheight=50)
stile.configure('mystyle.Treeview.Heading', font=('Calibri', 18))

# criando a tabela de fato
tv = ttk.Treeview(frame3, columns=(1, 2, 3, 4, 5, 6, 7, 8), style='mystyle.Treeview')
tv.heading("1", text='ID')
tv.column('1', width=45, stretch=NO)
tv.heading('2', text='Nome')
tv.column('2', width=305, stretch=NO)
tv.heading('3', text='Idade')
tv.column('3', width=90, stretch=NO)
tv.heading('4', text='Data de Nascimento')
tv.column('4', width=220, stretch=NO)
tv.heading('5', text='Email')
tv.column('5', width=210, stretch=NO)
tv.heading('6', text='Genero')
tv.column('6', width=160, stretch=NO)
tv.heading('7', text='Telefone')
tv.column('7', width=160, stretch=NO)
tv.heading('8', text='Endereço')
tv.column('8', width=160, stretch=NO)
tv['show'] = 'headings'
tv.bind('<ButtonRelease-1>', getData)
tv.pack(fill=X)

displayAll()

janela_principal.mainloop()
