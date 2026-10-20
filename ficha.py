<<<<<<< HEAD
import json

def salvar_personagem(personagem):
    with open("personagem.json", "w", encoding="utf-8") as arquivo:
        json.dump(personagem, arquivo, indent=4, ensure_ascii=False)

def carregar_personagem():
    try:
        with open("personagem.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print("Nenhum personagem salvo encontrado.")
        return None

def criar_ficha(dados):
    constituicao = int(dados["constituicao"])
    forcaVontade = int(dados["forcavontade"])

    personagem = {
        **dados,
        "vida": 10 + (constituicao),
        "sanidade": 5 + (forcaVontade),
        "pericias": {},

        "inventario":[]
            
        
    }

    return personagem

def calcular_mod(atributos):
    return (atributos//10)+1

def calcular_perica(modPericia):
     return (modPericia//5)+1

def fichaPersonagem():
   
    nome=input("Nome: ")
    raca=input("Raça: ")
    idade=input("Idade: ")
    linhagem=input("linhagem: ")
    oficio=input("oficio: ")


    forca=int(input("Força: "))
    destreza=int(input("Destreza: "))
    agilidade=int(input("Agilidade: "))
    percepcao=int(input("Percepção: "))
    carisma=int(input("Carisma: "))
    forcaVontade=int(input("Força de Vontade: "))
    constituicao=int(input("Constituição: "))

    vida= 10+ (calcular_mod(constituicao))
    sanidade= 5 + (calcular_mod(forcaVontade))

    personagem = {
        "nome":nome,
        "raca":raca,
        "idade":idade,
        "linhagem":linhagem,
        "oficio":oficio,
        "forca":forca,
        "destreza":destreza,
        "agilidade":agilidade,
        "percepcao":percepcao,
        "carisma":carisma,
        "forcaVontade":forcaVontade,
        "constituicao":constituicao,
        "vida":vida,
        "sanidade":sanidade,
        "pericias": {}
        }
    return personagem



def mostrarFicha(personagem):
    print("\n ===== Ficha de personagem =====")
    print("\n Dados Basicos")

    print (f"Nome: {personagem['nome']}")
    print (f"Raça: {personagem['raca']}")
    print (f"Idade: {personagem['idade']}")
    print (f"linhagem: {personagem['linhagem']}")
    print (f"oficio: {personagem['oficio']}")

    print("\n ===== Atributos =====")



    print(f"Força: {personagem['forca']} (Mod: + {calcular_mod(personagem['forca'])})")
    print(f"Destreza: {personagem['destreza']} (Mod: +{calcular_mod(personagem['destreza'])})")
    print(f"Agilidade: {personagem['agilidade']} (Mod: +{calcular_mod(personagem['agilidade'])})")
    print(F"Percepção: {personagem['percepcao']} (Mod: +{calcular_mod(personagem['percepcao'])})")
    print(f"Carisma: {personagem['carisma']} (Mod: +{calcular_mod(personagem['carisma'])})")
    print(F"Força de Vontade: {personagem['forcaVontade']} (Mod: +{calcular_mod(personagem['forcaVontade'])})")
    print(f"Constituição: {personagem['constituicao']} (Mod: +{calcular_mod(personagem['constituicao'])})")

    print("\n ===== Status =====")

    print(F"Vida: {personagem['vida']}")
    print(F"Sanidade: {personagem['sanidade']}")

def adicionarPericias(personagem):
    while True:

        adiciarPericia = input(" Adicionar nova pericia? (sim/não)").lower()
        

        if adiciarPericia == "sim":
                novaPericia=str(input("Nome da nova Pericia: "))

                try:
                    nivelPericia=int(input("Nivel da nova Pericia: "))
                    personagem["pericias"][novaPericia] = nivelPericia

                except ValueError:
                    print("Digite um valor Valido!!!")

        elif adiciarPericia in ["não" , "nao"]:
            break

        else:
            print("Responda apenas com 'sim' ou 'não'")
        


def mostrarPericias(personagem):
    print("\n Pericias")
    for nome_pericia,nivel in personagem ["pericias"].items():
        modpericia=calcular_perica(nivel)
        print(f"{nome_pericia} {nivel} Mod: + {modpericia}")

def removerPericia(personagem):

    if not personagem:
        print("Crie um personagem primeiro!!")
        return

    nome = input("Nome da pericia para remover: ")
    
    if  nome in personagem["pericias"]:

        del personagem["pericias"][nome]

        print("Pericia removida!")

    else:
        print("Pericia nao encontrada")

def editarPericias(personagem):
    nome = input("Nome da pericia para editar: ")

    if nome in personagem ["pericias"]:
        novoNivel=(int(input("Novo nivel: ")))

        personagem ["pericias"][nome] = novoNivel
        print("Pericia atualizada")
    else:
        print("Pericia nao foi encontrada")
        
        
personagem=None

if __name__ == "__main__":

    while True:

        print("\n ========Menu========")
        print("1 - Criar personagem")
        print("2 - Mostrar Ficha")
        print("3 - Adicionar pericias")
        print("4 - Mostrar pericias")
        print("5 - editar pericias")
        print("6 - Remover pericias")
        print("7 - Salvar personagem")
        print("8 - Carregar personagem")
        print("9 - sair ")
        

        opcao = input("Escolha: ")

        if opcao == "1":
            personagem = fichaPersonagem()

        elif opcao == "2":

            if personagem:
                mostrarFicha(personagem)
            else:
                print("Crie um personagem primeiro!")
        elif opcao == "3":
            if personagem:
                adicionarPericias(personagem)
            else:
                print("Crie o primeiro personagem!!")

        elif opcao =="4":
            if personagem:
                if personagem ["pericias"]:
                    mostrarPericias(personagem)
                else:
                    print("Adicione a primeira pericia")
            else:
                print("Crie um personagem primeiro!")
        elif opcao =="5":
            if personagem:
                editarPericias(personagem)
            else:
                print("Crie um personagem primeiro!")

        elif opcao =="6":
            if personagem:
                removerPericia(personagem)
            else:
                print("Crie um personagem primeiro!")

        elif opcao == "7":
            if personagem:
                salvar_personagem(personagem)
                print("Personagem salvo!")
            else:
                print("Crie um personagem primeiro!")

        elif opcao == "8":
            loaded = carregar_personagem()
            if loaded:
                personagem = loaded


        elif opcao == "9":
            break

        else:
            print("Opção inválida, digite novamente!!")
            
=======
import json

def salvar_personagem(personagem):
    with open("personagem.json", "w", encoding="utf-8") as arquivo:
        json.dump(personagem, arquivo, indent=4, ensure_ascii=False)

def carregar_personagem():
    try:
        with open("personagem.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print("Nenhum personagem salvo encontrado.")
        return None

def calcular_mod(atributos):
    return (atributos//10)+1

def calcular_perica(modPericia):
     return (modPericia//5)+1

def fichaPersonagem():
   
    nome=input("Nome: ")
    raca=input("Raça: ")
    idade=input("Idade: ")
    linhagem=input("linhagem: ")
    oficio=input("oficio: ")


    forca=int(input("Força: "))
    destreza=int(input("Destreza: "))
    agilidade=int(input("Agilidade: "))
    percepcao=int(input("Percepção: "))
    carisma=int(input("Carisma: "))
    forcavontade=int(input("Força de Vontade: "))
    constituicao=int(input("Constituição: "))

    vida= 10+ (calcular_mod(constituicao))
    sanidade= 5 + (calcular_mod(forcavontade))

    personagem = {
        "nome":nome,
        "raca":raca,
        "idade":idade,
        "linhagem":linhagem,
        "oficio":oficio,
        "forca":forca,
        "destreza":destreza,
        "agilidade":agilidade,
        "percepcao":percepcao,
        "carisma":carisma,
        "forcavontade":forcavontade,
        "constituicao":constituicao,
        "vida":vida,
        "sanidade":sanidade,
        "pericias": {}
        }
    return personagem



def mostrarFicha(personagem):
    print("\n ===== Ficha de personagem =====")
    print("\n Dados Basicos")

    print (f"Nome: {personagem['nome']}")
    print (f"Raça: {personagem['raca']}")
    print (f"Idade: {personagem['idade']}")
    print (f"linhagem: {personagem['linhagem']}")
    print (f"oficio: {personagem['oficio']}")

    print("\n ===== Atributos =====")



    print(f"Força: {personagem['forca']} (Mod: + {calcular_mod(personagem['forca'])})")
    print(f"Destreza: {personagem['destreza']} (Mod: +{calcular_mod(personagem['destreza'])})")
    print(f"Agilidade: {personagem['agilidade']} (Mod: +{calcular_mod(personagem['agilidade'])})")
    print(F"Percepção: {personagem['percepcao']} (Mod: +{calcular_mod(personagem['percepcao'])})")
    print(f"Carisma: {personagem['carisma']} (Mod: +{calcular_mod(personagem['carisma'])})")
    print(F"Força de Vontade: {personagem['forcavontade']} (Mod: +{calcular_mod(personagem['forcavontade'])})")
    print(f"Constituição: {personagem['constituicao']} (Mod: +{calcular_mod(personagem['constituicao'])})")

    print("\n ===== Status =====")

    print(F"Vida: {personagem['vida']}")
    print(F"Sanidade: {personagem['sanidade']}")

def adicionarPericias(personagem):
    while True:

        adiciarPericia = input(" Adicionar nova pericia? (sim/não)").lower()
        

        if adiciarPericia == "sim":
                novaPericia=str(input("Nome da nova Pericia: "))

                try:
                    nivelPericia=int(input("Nivel da nova Pericia: "))
                    personagem["pericias"][novaPericia] = nivelPericia

                except ValueError:
                    print("Digite um valor Valido!!!")

        elif adiciarPericia in ["não" , "nao"]:
            break

        else:
            print("Responda apenas com 'sim' ou 'não'")
        


def mostrarPericias(personagem):
    print("\n Pericias")
    for nome_pericia,nivel in personagem ["pericias"].items():
        modpericia=calcular_perica(nivel)
        print(f"{nome_pericia} {nivel} Mod: + {modpericia}")

def removerPericia(personagem):

    if not personagem:
        print("Crie um personagem primeiro!!")
        return

    nome = input("Nome da pericia para remover: ")
    
    if  nome in personagem["pericias"]:

        del personagem["pericias"][nome]

        print("Pericia removida!")

    else:
        print("Pericia nao encontrada")

def editarPericias(personagem):
    nome = input("Nome da pericia para editar: ")

    if nome in personagem ["pericias"]:
        novoNivel=(int(input("Novo nivel: ")))

        personagem ["pericias"][nome] = novoNivel
        print("Pericia atualizada")
    else:
        print("Pericia nao foi encontrada")
        
        
personagem=None

while True:

    print("\n ========Menu========")
    print("1 - Criar personagem")
    print("2 - Mostrar Ficha")
    print("3 - Adicionar pericias")
    print("4 - Mostrar pericias")
    print("5 - editar pericias")
    print("6 - Remover pericias")
    print("7 - Salvar personagem")
    print("8 - Carregar personagem")
    print("9 - sair ")
    

    opcao = input("Escolha: ")

    if opcao == "1":
        personagem = fichaPersonagem()

    elif opcao == "2":

        if personagem:
            mostrarFicha(personagem)
        else:
            print("Crie um personagem primeiro!")
    elif opcao == "3":
        if personagem:
            adicionarPericias(personagem)
        else:
            print("Crie o primeiro personagem!!")

    elif opcao =="4":
        if personagem:
            if personagem ["pericias"]:
                mostrarPericias(personagem)
            else:
                print("Adicione a primeira pericia")
        else:
            print("Crie um personagem primeiro!")
    elif opcao =="5":
        if personagem:
            editarPericias(personagem)
        else:
            print("Crie um personagem primeiro!")

    elif opcao =="6":
        if personagem:
            removerPericia(personagem)
        else:
            print("Crie um personagem primeiro!")

    elif opcao == "7":
        if personagem:
            salvar_personagem(personagem)
            print("Personagem salvo!")
        else:
            print("Crie um personagem primeiro!")

    elif opcao == "8":
        loaded = carregar_personagem()
        if loaded:
            personagem = loaded


    elif opcao == "9":
        break

    else:
        print("Opção inválida, digite novamente!!")
        
>>>>>>> origin/main
