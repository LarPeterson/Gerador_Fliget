import pyfiglet
import random

def mostrar_menu():
    print("\n--- Gerador de ASCII Art com PyFiglet ---")
    print("1. Criar uma palavra em ASCII Art")
    print("2. Trocar a fonte")
    print("3. Sair")

fonte_atual = "standard"

while True:
    mostrar_menu()
    escolha = input("Escolha uma opção (1/2/3): ")
    
    if escolha == "1":
        texto = input("Digite a palavra ou frase: ")
        
        try:
            resultado = pyfiglet.figlet_format(texto, font=fonte_atual)
            print(resultado)
        except pyfiglet.FontNotFound:
            print("Fonte não encontrada. Tente novamente!")
    
    elif escolha == "2":
        fontes_disponiveis = random.sample(pyfiglet.FigletFont.getFonts(), min(10, len(pyfiglet.FigletFont.getFonts())))
        print("Escolha uma das fontes abaixo:")
        for i, fonte in enumerate(fontes_disponiveis, 1):
            print(f"{i}. {fonte}")
        
        try:
            opcao_fonte = int(input("Digite o número da fonte desejada: "))
            if 1 <= opcao_fonte <= len(fontes_disponiveis):
                fonte_atual = fontes_disponiveis[opcao_fonte - 1]
                print(f"Fonte alterada para: {fonte_atual}")
            else:
                print("Número inválido!")
        except ValueError:
            print("Digite um número válido.")
    
    elif escolha == "3":
        print("Saindo... ")
        break
    
    else:
        print("Opção inválida. Tente novamente!")