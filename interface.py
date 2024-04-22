import conexao
from customtkinter import *


def adicionar_item():
    nome = nome_entry.get()
    quantidade = quantidade_entry.get()
    preco = preco_entry.get()
    local = onde_entry.get()
    if quantidade == "":
        quantidade = "0"
    if preco == "":
        preco = "0.0"
    if local == "Escolha um local" or local == "":
        local = "-"
    conexao.Adicionar(nome, quantidade, preco, local)
    lista_atualiza()

def editar_item():
    nome = nome_entry.get()
    quantidade = quantidade_entry.get()
    preco = preco_entry.get()
    local = onde_entry.get()
    conexao.Editar(nome, quantidade, preco, local)
    lista_atualiza()

def apagar_item():
    nome = nome_entry.get()
    conexao.Apagar(nome)
    lista_atualiza()

def lista_atualiza():
    global saida
    saida = ""
    resultado = conexao.obter_lista()
    if resultado:
        for item in resultado:
            saida += f'{item}\n'
        lista.configure(text=saida)
    else:
        lista.configure(text='Nenhum item encontrado')

def fechar_janela():
    janela.destroy()

# Converter preço em float e quantidade em inteiro
def float_only_input(char):
    return char.isdigit() or (char == "." and "." not in preco_entry.get())
def int_only_input(char):
    return char.isdigit() or (char == "-" and len(preco_entry.get()) == 0)

# Configurações da Janela
set_appearance_mode("dark")
set_default_color_theme("dark-blue")
janela = CTk()
janela.geometry("500x600")
janela.resizable(False, False)
janela.iconbitmap('MarketCart.ico')
janela.title("Lista de Compras")

# Aviso no Topo da Janela(Header)
header = CTkLabel(janela, text="Adicione, Modifique ou Apague os items da sua lista de compras.")
header.pack(padx=10, pady=15)

# Campos de preenchimento - Cima
nome = CTkLabel(janela, text="Nome do Produto:")
nome.place(relx=0.12, rely=0.1)

nome_entry = CTkEntry(janela, width=120, height=25, placeholder_text="-")
nome_entry.place(relx=0.33, rely=0.1)

quantidade = CTkLabel(janela, text="Quantidade:")
quantidade.place(relx=0.62, rely=0.1)

quantidade_entry = CTkEntry(janela, width=56, height=25, placeholder_text="")
quantidade_entry.place(relx=0.77, rely=0.1)
quantidade_entry.configure(validate="key", validatecommand=(janela.register(int_only_input), "%S"))

# Campos de preenchimento - Baixo
preco = CTkLabel(janela, text="Preço:")
preco.place(relx=0.13, rely=0.15)

preco_entry = CTkEntry(janela, width=59, height=25, placeholder_text=".")
preco_entry.place(relx=0.21, rely=0.15)
preco_entry.configure(validate="key", validatecommand=(janela.register(float_only_input), "%S"))

onde = CTkLabel(janela, text="Onde comprar:")
onde.place(relx=0.42, rely=0.15)

locais_compra = ["Atacadão", "Assaí", "Carrefour", "Compre Bem", "Dia", "Extra", "Itambé", "Nagumo", "Pão de Açúcar", "Semar", "Shibata", "Tenda"]
onde_entry = CTkComboBox(janela, values=locais_compra)
onde_entry.set("-")
onde_entry.place(relx=0.6, rely=0.15)

# Botões
adicionar = CTkButton(janela, text="Adicionar", command=adicionar_item, fg_color="#2ecc71", text_color="#1a1a1a")
adicionar.pack(side=LEFT, padx=15, pady=5)
adicionar.place(relx=0.05, rely=0.25)

editar = CTkButton(janela, text="Editar", command=editar_item, fg_color="#4dd0e1", text_color="#1a1a1a")
editar.pack(side=LEFT, padx=10, pady=5)
editar.place(relx=0.35, rely=0.25)

apagar = CTkButton(janela, text="Apagar", command=apagar_item, fg_color="#ed1c24")
apagar.pack(side=LEFT, padx=10, pady=5)
apagar.place(relx=0.65, rely=0.25)

fechar = CTkButton(janela, text="Fechar", command=fechar_janela)
fechar.pack(pady=(0, 20), side=BOTTOM)

# Aviso no Meio da Janela
footer = CTkLabel(janela, text="Explicações:\n\n• Para adicionar items, é preciso apenas o nome do Produto.\n• Caso vá editar algum item, você precisa colocar todos os items.\n• Para apagar, basta colocar exatamente o nome do item no campo nome.")
footer.pack(padx=0, pady=140)

# Lista de Compras Atualizada
lista = CTkLabel(janela, text="")
lista.pack(pady=(0, 30), side=BOTTOM)
lista_atualiza()

# Loop da Janela
janela.mainloop()
