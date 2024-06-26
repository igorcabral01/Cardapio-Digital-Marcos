# Importa a biblioteca "os" para manipular arquivos e execução de comandos do sistema operacional
import os
import time

from Idioma_navegacao import get_mensagem_navegacao
from Idioma_pratos import get_informacoes_prato

# Define idioma padrão
idioma_atual = 'pt'  

# Cria variavel global codigo_prato
codigo_prato = "000"
cardapio = "000"
logado = False

# Definição global das listas que conterão personaliação de pratos
ingredientes_retirados = []
ingredientes_adicionados = []

# Cria a tela base do programa
def mostra_tela_titulo():
    os.system("cls" if os.name == 'nt' else "clear")  # Limpa a tela, compatível com Windows e Unix
    print('''\033[34m
░█████╗░███████╗░██████╗░█████╗░██████╗░  ██████╗░██╗░██████╗████████╗██████╗░░█████╗░
██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗  ██╔══██╗██║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗
██║░░╚═╝█████╗░░╚█████╗░███████║██████╔╝  ██████╦╝██║╚█████╗░░░░██║░░░██████╔╝██║░░██║
██║░░██╗██╔══╝░░░╚═══██╗██╔══██║██╔══██╗  ██╔══██╗██║░╚═══██╗░░░██║░░░██╔══██╗██║░░██║
╚█████╔╝███████╗██████╔╝██║░░██║██║░░██║  ██████╦╝██║██████╔╝░░░██║░░░██║░░██║╚█████╔╝
░╚════╝░╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝  ╚═════╝░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░\033[0m''')

# 1ª Tela - Função para escolher o idioma
def escolher_idioma():
    global idioma_atual
    print("\nEscolha o idioma / Choose language :")
    print("\n1 - Português (pt)")
    print("2 - Inglês (en)")
    print("3 - Espanhol (es)")
    escolha = input("\nOpção / Option / opción : ")
    if escolha == '1':
        idioma_atual = 'pt'
    elif escolha == '2':
        idioma_atual = 'en'
    else:
        idioma_atual = 'es'

# 2ª Tela - Função de boas vindas e Login
def bemvindo():
    mostra_tela_titulo()
    print(get_mensagem_navegacao(idioma_atual, 'bemvindo'))
    print(get_mensagem_navegacao(idioma_atual, 'mensagem_boas_vindas'))
    print(get_mensagem_navegacao(idioma_atual, "pergunta_fazer_login"))
    print(get_mensagem_navegacao(idioma_atual, "login"))
    print(get_mensagem_navegacao(idioma_atual, "va_cardapio"))
    print(get_mensagem_navegacao(idioma_atual, "3 - voltar"))

    choice = input(get_mensagem_navegacao(idioma_atual, 'escolha'))
    if choice == '1':
        efetua_login()
    elif choice == '2':
        escolhe_cardapio()
    elif choice == '3':
        mostra_tela_titulo()
        escolher_idioma()
    else:
        pass

# 3ª Tela - Função opcional de efetuar login
def efetua_login():
    mostra_tela_titulo()
    email = input(get_mensagem_navegacao(idioma_atual, 'informe_email'))
    if email:
        senha = input(get_mensagem_navegacao(idioma_atual, 'informe_senha'))
        if senha:
            if email == 'admin' and senha == 'admin':
                print(get_mensagem_navegacao(idioma_atual, 'login_sucesso'))
                global logado
                logado = True
                time.sleep(2)
                escolhe_cardapio()
            else:
                print("\nUsuário ou senha inválidos. Tente novamente.")
                time.sleep(2)
                efetua_login()

# 4ª Tela - Função para acessar o menu principal
def escolhe_cardapio():
    global cardapio
    mostra_tela_titulo()
    print(get_mensagem_navegacao(idioma_atual, "escolhe_cardapio"))
    print(get_mensagem_navegacao(idioma_atual, "1 - Geral"))
    print(get_mensagem_navegacao(idioma_atual, "2 - Diabetico"))
    print(get_mensagem_navegacao(idioma_atual, "3 - Vegetariano"))
    print(get_mensagem_navegacao(idioma_atual, "4 - Sem Lactose"))
    print(get_mensagem_navegacao(idioma_atual, "5 - Sem Gluten"))
    print(get_mensagem_navegacao(idioma_atual, "6 - Sazonal"))
    if logado:
        print(get_mensagem_navegacao(idioma_atual, "7 - Personalizado"))
        print(get_mensagem_navegacao(idioma_atual, "8 - voltar"))
    else:
        print(get_mensagem_navegacao(idioma_atual, "7 - voltar"))

    try:
        cardapio = int(input(get_mensagem_navegacao(idioma_atual, 'escolha')))
        if (logado == True and cardapio == 8) or (logado == False and cardapio == 7):
            mostra_tela_titulo()
            bemvindo()
        else:
            lista_pratos_cardapio_escolhido(cardapio)

    except ValueError:
        print('Por favor, digite um número válido.')
        time.sleep(2)
        mostra_tela_titulo()
        acessar_menu

# 5ª Tela - Função para escolher o cardápio
def lista_pratos_cardapio_escolhido(cardapio):
    mostra_tela_titulo()
    global codigo_prato

    if cardapio == 1:
        print(get_mensagem_navegacao(idioma_atual, "CARDAPIO_GERAL"))
        ler_arquivo_pratos('./Cardapios/geral.txt')
        print(get_mensagem_navegacao(idioma_atual, "4 - voltar"))
        choice = input(get_mensagem_navegacao(idioma_atual, 'escolha'))
        if choice == '1':
            codigo_prato = '001'
        elif choice == '2':
            codigo_prato = '002'
        elif choice == '3':
            codigo_prato = '003'
        elif choice == '4':
            escolhe_cardapio()
        apresenta_prato_escolhido(codigo_prato)        
        time.sleep(2)
        escolhe_cardapio()

    elif cardapio == 2:
        print(get_mensagem_navegacao(idioma_atual, "CARDAPIO_DIABETICO"))
        ler_arquivo_pratos('./Cardapios/diabetico.txt')
        print(get_mensagem_navegacao(idioma_atual, "4 - voltar"))
        choice = input(get_mensagem_navegacao(idioma_atual, 'escolha'))
        if choice == '1':
            codigo_prato = '004'
        elif choice == '2':
            codigo_prato = '005'
        elif choice == '3':
            codigo_prato = '006'
        elif choice == '4':
            escolhe_cardapio()
        apresenta_prato_escolhido(codigo_prato)        
        time.sleep(2)
        escolhe_cardapio()
     
    elif cardapio == 3:
        print(get_mensagem_navegacao(idioma_atual, "CARDAPIO_VEGETARIANO"))
        ler_arquivo_pratos('./Cardapios/vegetariano.txt')
        print(get_mensagem_navegacao(idioma_atual, "4 - voltar"))
        choice = input(get_mensagem_navegacao(idioma_atual, 'escolha'))
        if choice == '1':
            codigo_prato = '007'
            apresenta_prato_escolhido(codigo_prato)        
        elif choice == '2':
            codigo_prato = '008'
            apresenta_prato_escolhido(codigo_prato)        
        elif choice == '3':
            codigo_prato = '009'
            apresenta_prato_escolhido(codigo_prato)        
        elif choice == '4':
            mostra_tela_titulo()
            escolhe_cardapio()          
    elif cardapio == 4:
        print(get_mensagem_navegacao(idioma_atual, "CARDAPIO_SEM_LACTOSE"))
        ler_arquivo_pratos('./Cardapios/sem_lactose.txt')
        print(get_mensagem_navegacao(idioma_atual, "4 - voltar"))
        choice = input(get_mensagem_navegacao(idioma_atual, 'escolha'))
        if choice == '1':
            codigo_prato = '007'
            apresenta_prato_escolhido(codigo_prato)        
        elif choice == '2':
            codigo_prato = '008'
            apresenta_prato_escolhido(codigo_prato)        
        elif choice == '3':
            codigo_prato = '009'
            apresenta_prato_escolhido(codigo_prato)        
        elif choice == '4':
            mostra_tela_titulo()
            escolhe_cardapio() 
        time.sleep(2)
        escolhe_cardapio()

    elif cardapio == 5:
        print(get_mensagem_navegacao(idioma_atual, "CARDAPIO_SEM_GLUTEN"))
        ler_arquivo_pratos('./Cardapios/sem_gluten.txt')
        print(get_mensagem_navegacao(idioma_atual, "4 - voltar"))
        choice = input(get_mensagem_navegacao(idioma_atual, 'escolha'))
        if choice == '1':
            codigo_prato = '010'
            apresenta_prato_escolhido(codigo_prato)        
        elif choice == '2':
            codigo_prato = '011'
            apresenta_prato_escolhido(codigo_prato)        
        elif choice == '3':
            codigo_prato = '012'
            apresenta_prato_escolhido(codigo_prato)        
        elif choice == '4':
            mostra_tela_titulo()
            escolhe_cardapio() 
    elif cardapio == 6:
        print(get_mensagem_navegacao(idioma_atual, "CARDAPIO_SAZONAL"))
        ler_arquivo_pratos('./Cardapios/sazonal.txt')
        print(get_mensagem_navegacao(idioma_atual, "4 - voltar"))
        choice = input(get_mensagem_navegacao(idioma_atual, 'escolha'))
        if choice == '1':
            codigo_prato = '013'
            apresenta_prato_escolhido(codigo_prato)        
        elif choice == '2':
            codigo_prato = '014'
            apresenta_prato_escolhido(codigo_prato)        
        elif choice == '3':
            codigo_prato = '015'
            apresenta_prato_escolhido(codigo_prato)        
        elif choice == '4':
            mostra_tela_titulo()
            escolhe_cardapio()

    elif cardapio == 7:
        print(get_mensagem_navegacao(idioma_atual, "CARDAPIO_PERSONALIZADO"))
        time.sleep(2)
        escolhe_cardapio()

    elif cardapio == 8:
        mostra_tela_titulo()
        escolhe_cardapio()
    else:
        print('\nDigite um Numero Válido')
        time.sleep(2)
        mostra_tela_titulo()
        escolhe_cardapio()

def ler_arquivo_pratos(menu_escolhido):
    with open(menu_escolhido, 'r') as arquivo:
        dados = arquivo.readlines()
        for dado in dados:
            print(dado.strip())

# 6ª tela - Lista as opções do menu principal usando dicionario de idiomas
def apresenta_prato_escolhido(codigo_prato):    
    mostra_tela_titulo()
    print(get_informacoes_prato(codigo_prato, idioma_atual, 'prato') + ": " + get_informacoes_prato(codigo_prato, idioma_atual, 'descricao'))
    print(get_informacoes_prato(codigo_prato, idioma_atual, 'lista_ingredientes'))
    print(get_informacoes_prato(codigo_prato, idioma_atual, 'preco_tempo'))

    print(get_mensagem_navegacao(idioma_atual, 'pedir_este_prato'))
    print(get_mensagem_navegacao(idioma_atual, 'nutricional'))
    print(get_mensagem_navegacao(idioma_atual, 'personalize'))
    print(get_mensagem_navegacao(idioma_atual, 'video'))
    print(get_mensagem_navegacao(idioma_atual, '5 - voltar'))
    print(get_mensagem_navegacao(idioma_atual, 'finalizar_pedido'))

    if ingredientes_retirados:
        print(get_mensagem_navegacao(idioma_atual, 'lista_ingredientes_retirados'), ingredientes_retirados)
    if ingredientes_adicionados:
        print(get_mensagem_navegacao(idioma_atual, 'lista_ingredientes_adicionados'), ingredientes_adicionados)
    while True:
        choice = input(get_mensagem_navegacao(idioma_atual, 'escolha'))
        # Escolheu Pedir este Prato
        if choice == '1':
            rotina_em_desenvolvimento()
        # Escolheu opção 2 (Informação Nutricional, Valor calórico e alergênicos)
        if choice == '2':
            mostra_tela_titulo()
            lista_informaçoes_nutricionais()
            mostra_tela_titulo()
            apresenta_prato_escolhido(codigo_prato)
        # Escolheu opção 3 (Personalize seu prato)
        elif choice == '3':
            mostra_tela_titulo()
            personalizar_prato()
                
        # Escolheu opção 4 (Vídeo de apresentação do prato)
        elif choice == '4':
            print(get_mensagem_navegacao(idioma_atual, 'aguarde'))
            reproduz_video_prato()
            mostra_tela_titulo()
            lista_pedido_prato(codigo_prato)
        # Escolheu opção 5 (voltar)
        elif choice == '5':
            mostra_tela_titulo()
            lista_pratos_cardapio_escolhido(cardapio)
        elif choice == '6':
            finalizar_app()
            break
        else:
            pass

# 7ª tela - Mostra as informações nutricionais do prato
def lista_informaçoes_nutricionais():
    print(get_informacoes_prato(codigo_prato, idioma_atual, 'info_nutricional'))
    print(get_informacoes_prato(codigo_prato, idioma_atual, 'calorias'))
    print(get_informacoes_prato(codigo_prato, idioma_atual, 'carboidratos'))
    print(get_informacoes_prato(codigo_prato, idioma_atual, 'proteinas'))
    print(get_informacoes_prato(codigo_prato, idioma_atual, 'gorduras'))
    print(get_informacoes_prato(codigo_prato, idioma_atual, 'saturadas'))
    print(get_informacoes_prato(codigo_prato, idioma_atual, 'trans'))
    print(get_informacoes_prato(codigo_prato, idioma_atual, 'fibra'))
    print(get_informacoes_prato(codigo_prato, idioma_atual, 'sodio'))
    print(get_informacoes_prato(codigo_prato, idioma_atual, 'base_dieta'))
    print(get_informacoes_prato(codigo_prato, idioma_atual, 'atencao_lactose'))
    input(get_mensagem_navegacao(idioma_atual, 'aperte_enter'))

def tela_personalizar_prato():
    print(get_informacoes_prato(codigo_prato, idioma_atual, 'prato'))
    print(get_informacoes_prato(codigo_prato, idioma_atual, 'lista_ingredientes'))
    print(get_mensagem_navegacao(idioma_atual, 'retirar_ingrediente'))
    print(get_mensagem_navegacao(idioma_atual, 'adicionar_ingrediente'))
    print(get_mensagem_navegacao(idioma_atual, '3 - voltar'))

def personalizar_prato():
    choice = '0'
    global ingredientes_retirados 
    global ingredientes_adicionados

    tela_personalizar_prato()
    
    if ingredientes_retirados:
        print(get_mensagem_navegacao(idioma_atual, 'lista_ingredientes_retirados'), ingredientes_retirados)
    if ingredientes_adicionados:
        print(get_mensagem_navegacao(idioma_atual, 'lista_ingredientes_adicionados'), ingredientes_adicionados)

    while choice.isdigit and choice != '3':
        choice = input(get_mensagem_navegacao(idioma_atual, 'escolha'))
        if choice == '1':
            if ingredientes_retirados:
                print(get_mensagem_navegacao(idioma_atual, 'aviso_substituir_ingredientes'))
                ingredientes_retirados = []  # Limpa a lista de ingredientes retirados
            ingrediente = input(get_mensagem_navegacao(idioma_atual, 'digite_ingrediente_retirar'))
            if ingrediente:
                ingredientes_retirados.append(ingrediente)  # Adiciona o novo ingrediente retirado à lista
            else:
                print(get_mensagem_navegacao(idioma_atual, 'sem_ingredientes_retirados'))
        elif choice == '2':
            if ingredientes_adicionados:
                print(get_mensagem_navegacao(idioma_atual, 'aviso_substituir_ingredientes'))
                ingredientes_adicionados = []  # Limpa a lista de ingredientes adicionados
            ingrediente = input(get_mensagem_navegacao(idioma_atual, 'digite_ingrediente_adicionar'))
            if ingrediente:
                ingredientes_adicionados.append(ingrediente)  # Adiciona o novo ingrediente adicionado à lista
            else:
                print(get_mensagem_navegacao(idioma_atual, 'sem_ingredientes_adicionados'))

        elif choice == '3':
            mostra_tela_titulo()
            lista_pedido_prato(codigo_prato)
            break
        else:
            print(get_mensagem_navegacao(idioma_atual, 'invalido'))

# Reproduz o vídeo de apresentação do prato
def reproduz_video_prato():
    # Caminho base onde os vídeos estão armazenados
    base_path = r"C:\Cesar_School\PROJETO\CARDAPIO.MARCOS\Videos"
    # Constrói o caminho completo do arquivo de vídeo
    video_filename = f"{codigo_prato}.mp4"  # Adiciona o código do prato e a extensão .mp4
    path_video = os.path.join(base_path, video_filename)  # Usa os.path.join para construir o caminho completo

    # Verifica se o arquivo de vídeo existe
    if os.path.isfile(path_video):
        # Executa o arquivo de vídeo passando o caminho como argumento
        os.system(f"python PlayMP4Video.py \"{path_video}\"")
    else:
        print("Arquivo de vídeo não encontrado.")

def finalizar_app():
    os.system("cls" if os.name == 'nt' else "clear")  # Limpa a tela, compatível com Windows e Unix
    print("Encerrando o programa...\n", flush=True)
    time.sleep(1)

def rotina_em_desenvolvimento():
    for _ in range(3):  # Faz a frase piscar 2 vezes
        os.system("cls" if os.name == 'nt' else "clear")  # Limpa a tela, compatível com Windows e Unix
        print(get_mensagem_navegacao(idioma_atual, 'rotina_desenvolvimento'), end='', flush=True)
        time.sleep(0.5)  # Tempo com a frase visível
        os.system("cls" if os.name == 'nt' else "clear")  # Limpa a tela
        time.sleep(0.5)  # Tempo com a tela limpa

    mostra_tela_titulo()
    apresenta_prato_escolhido(codigo_prato)



    


# Função principal
def main():
    mostra_tela_titulo()
    escolher_idioma()
    bemvindo()
    efetua_login()

# Executa o programa
if __name__ == "__main__":
    main()
