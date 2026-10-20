import customtkinter as ctk
from ficha import calcular_mod, calcular_perica, criar_ficha

#confuguracoes visuais
ctk.set_appearance_mode("dark") #ativa o modo escuro.
ctk.set_default_color_theme("dark-blue") #define a cor padrão de botões e outros elementos compatíveis.


personagens = []

def novo_personagem():
    titulo_ficha.configure(text="Criar Personagem")
    detalhes_personagem.pack_forget()
    formulario.pack(fill="both", expand=True, padx=20, pady=10)

def criar_campo(pai,texto,dica,linha):
    rotulo=ctk.CTkLabel(
        pai,
        text=texto,
        font=("Georgia",14,"bold"),
        text_color="#d6b477"
    )
    rotulo.grid(row=linha, column=0, padx=10, pady=10)

    campo = ctk.CTkEntry(
        pai,
        placeholder_text=dica,
        font=("Georgia",14),
        width=300,
        height=35
    )
    campo.grid(row=linha, column=1, padx=10, pady=10)

    return campo

def criar_personagem():
    
    dados = {
        "nome": nome_personagem.get().strip(),
        "raca": raca_personagem.get().strip(),
        "idade": idade_personagem.get().strip(),
        "linhagem": linhagem_personagem.get().strip(),
        "oficio": oficio_personagem.get().strip(),
        "forca": int(forca_personagem.get()),
        "destreza": int(destreza_personagem.get()),
        "agilidade": int(agilidade_personagem.get()),
        "percepcao": int(percepcao_personagem.get()),
        "carisma": int(carisma_personagem.get()),
        "forcavontade": int(forcaVontade_personagem.get()),
        "constituicao": int(constituicao_personagem.get())   
    }


    personagem = criar_ficha(dados)
    personagens.append(personagem)
    
    atualizar_lista_personagens()
    mostra_personagem(personagem)
    print(personagem)

    nome_personagem.delete(0,"end")
    raca_personagem.delete(0,"end")
    idade_personagem.delete(0,"end")
    linhagem_personagem.delete(0,"end")
    oficio_personagem.delete(0,"end")
    forca_personagem.delete(0,"end")
    destreza_personagem.delete(0,"end")
    agilidade_personagem.delete(0,"end")
    percepcao_personagem.delete(0,"end")
    carisma_personagem.delete(0,"end")
    forcaVontade_personagem.delete(0,"end")
    constituicao_personagem.delete(0,"end")

def atualizar_lista_personagens():
    for componente in lista_botoes.winfo_children():
        componente.destroy()
    for personagem in personagens:
        nome = personagem["nome"]

        botao_personagem = ctk.CTkButton(
            lista_botoes,
            text=nome,
            fg_color="transparent",
            hover_color="#49302F",
            text_color="#F5E9DC",
            anchor="w",
            command=lambda p=personagem:mostra_personagem(p)
        )

        botao_personagem.pack(
            fill="x",
            padx=10,
            pady=5
        )

def mostra_personagem(personagem):
    titulo_ficha.configure(text=personagem["nome"])

    formulario.pack_forget()
    print(personagem)

    texto=(
    f"Nome:  {personagem['nome']}\n" +
    f"Raça:  {personagem['raca']}\n" +
    f"Idade:  {personagem['idade']}\n"+
    f"Linhagem:  {personagem['linhagem']}\n"+
    f"Oficio:  {personagem['oficio']}\n"+
    f"Vida: {personagem['vida']}\n"+
    f"Sanidade: {personagem['sanidade']}"

    )

    detalhes_personagem.configure(text=texto)
    detalhes_personagem.pack(pady=20)

    recolher_lista_personagem()

def alternar_lista_personagem():
    if lista_personagem.winfo_ismapped(): #winfo verifica se a condicao e true ou false 
        recolher_lista_personagem()

    else:
        mostrar_lista_personagem()

def recolher_lista_personagem():
    lista_personagem.pack_forget()

def mostrar_lista_personagem():
    lista_personagem.pack(side="left", fill="y", before=conteudo)
    

#Criar janela principal
janela=ctk.CTk()

#configurando a janela
janela.title("Ficha de RPG")
janela.geometry("1000x650")

menu=ctk.CTkFrame(
    janela, 
    width=220, 
    fg_color="#202024"
) #cria o painel dentro da janela.
menu.pack(side="left",fill="y")



lista_personagem=ctk.CTkFrame(
    janela,
    width=220,
    fg_color="#202024"
)

lista_personagem.pack(side="left",fill="y")
lista_personagem.pack_propagate(False)

titulo_lista=ctk.CTkLabel(
    lista_personagem,
    text="Personagem",
    font=("Georgia", 18,"bold"),
    text_color="#D6B477"
)
titulo_lista.pack(pady=20)

novo_personagem_btn=ctk.CTkButton(
    lista_personagem,
    text="+ Novo Personagem",
    width=180,
    height=35,
    fg_color="#49302f",
    hover_color="#69413D",
    text_color="#F5E9DC",
    font=("Georgia", 13),
    command=novo_personagem
)
novo_personagem_btn.pack(pady=10)

titulo = ctk.CTkLabel(
    menu,
    text="Grimorio",
    font=("Georgia", 22,"bold"),
    text_color="#D6B477"
)
titulo.pack(pady=20)

personagem_btn = ctk.CTkButton(
    menu,
    text="Personagem",
    width=180,
    height=40,
    fg_color="#49302F",
    hover_color="#69413D",
    text_color="#F5E9DC",
    font=("Georgia", 14)
)
personagem_btn.pack(pady=10)

abrir_lista_btn = ctk.CTkButton(
    menu,
    text="☰",
    width=40,
    height=35,
    fg_color="#49302F",
    hover_color="#69413D",
    text_color="#F5E9DC",
    font=("Georgia", 20),
    command=alternar_lista_personagem
)

abrir_lista_btn.pack(pady=10)

lista_botoes=ctk.CTkFrame(
    lista_personagem,
    fg_color="#202024"
)
lista_botoes.pack(fill="both", expand=True)

conteudo=ctk.CTkFrame(
    janela,
    fg_color= "#171719"
)
conteudo.pack(side="left", fill="both", expand=True, padx=10, pady=10)

titulo_ficha=ctk.CTkLabel(
    conteudo,
    text="Ficha do Personagem",
    font=("Georgia",26, "bold"),
    text_color="#f1e6d5"
)
titulo_ficha.pack(anchor="w", padx=20, pady=20)

detalhes_personagem=ctk.CTkLabel(
    conteudo,
    text="Selecione um Personagem da lista",
    font=("Georgia", 14),
    text_color="#F5E9DC",
    justify="left",
    anchor="nw"
)
detalhes_personagem.pack(fill="x", padx=20, pady=10)


formulario = ctk.CTkScrollableFrame(
    conteudo,
    fg_color="#202024"
)
formulario.pack(fill="both", expand=True, padx=20, pady=10)
formulario.pack_forget()
#Faz ficar oculto ate ser apertado


nome_personagem = criar_campo(
    formulario, "Nome:", "Digite o nome...", 0
)

raca_personagem = criar_campo(
    formulario, "Raça:", "Digite a raça...", 1
)

idade_personagem = criar_campo(
    formulario, "Idade:", "Digite a idade...", 2
)

linhagem_personagem = criar_campo(
    formulario, "Linhagem:", "Digite a linhagem...", 3
)

oficio_personagem = criar_campo(
    formulario, "Oficio:", "Digite o oficio...", 4
)


titulo_atributos = ctk.CTkLabel(
    formulario,
    text="Atributos",
    font=("Georgia", 20, "bold"),
    text_color="#D6B477"
)
titulo_atributos.grid(
    row=5,
    column=0,
    columnspan=2,
    padx=10,
    pady=(25, 10),
    sticky="w"
)

forca_personagem = criar_campo(
    formulario, "Força:", "Digite a força...", 6
)

destreza_personagem = criar_campo(
    formulario, "Destreza:", "Digite a destreza...", 7
)

agilidade_personagem = criar_campo(
    formulario, "Agilidade:", "Digite a agilidade...", 8
)

percepcao_personagem = criar_campo(
    formulario, "Percepção:", "Digite a percepção...", 9
)

carisma_personagem = criar_campo(
    formulario, "Carisma:", "Digite o carisma...", 10
)

forcaVontade_personagem = criar_campo(
    formulario, "Força de Vontade:", "Digite a força de vontade...", 11
)

constituicao_personagem = criar_campo(
    formulario, "Constituição:", "Digite a constituição...", 12
)



botao_criar=ctk.CTkButton(
    formulario,
    text="Criar Personagem",
    font=("Georgia",14,"bold"),
    command=criar_personagem,
    fg_color="#49302F",
    hover_color="#69413D",
    text_color="#F5E9DC",
    width=200,
    height=40
)
botao_criar.grid(
    row=16,
    column=0,
    columnspan=2,
    padx=10,
    pady=20
)

nome=nome_personagem.get()
print(nome)
raca=raca_personagem.get()
print(raca)
idade=idade_personagem.get()
print(idade)
linhagem=linhagem_personagem.get()
print(linhagem)
forca=forca_personagem.get()
print(forca)
destreza=destreza_personagem.get()
print(destreza)
agilidade=agilidade_personagem.get()
print(agilidade)
percepcao=percepcao_personagem.get()
print(percepcao)
carisma=carisma_personagem.get()
print(carisma)
forcaVontade=forcaVontade_personagem.get()
print(forcaVontade)
constituicao=constituicao_personagem.get()
print(constituicao)


inventario=[]
item={

    "nome": "Poção de cura",
    "quantidade": 3

}
inventario.append(item)
print(inventario)

item2={

    "nome":"diario de medicina",
    "quantidade":1
}
inventario.append(item2)
print(inventario)

for item in inventario:
        print(f"{item['nome']} - {item['quantidade']}")
#mantem a janela aberta
janela.mainloop()