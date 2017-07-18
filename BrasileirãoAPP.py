import sys
import os
def limpar():
    os.system("cls")
def menu_do_cliente():
     while(True):
        print("Menu")
        print("1 - Vizualizar a classificação atual do brasileirão")
        print("2 - prever o resultado")
        print("3 - Simular estatisticas")
        print("4 - Sair\n\n")
        op = input("Digite sua opção\n>")

        if(op == "1"):
            print("Tabela do Brasileirão")
        elif(op == "2"):
            print("Simular")
            #def cadastrar()
        elif(op == "3"):
            print("Simular estatisticas")
        elif(op == "4"):
            return
        else:
            print("Valor invalido!!!")
    
def menuprincipal():
    while(True):
        print("Menu")
        print("1 - Login")
        print("2 - Cadastre-se")
        print("3 - Sair\n\n")
        op = input("Digite sua opção\n>")

        if(op == "1"):
            entrar()
            limpar()
        elif(op == "2"):
            print("Cadastrando")
            limpar()
            #def cadastrar()
        elif(op == "3"):
            sys.exit(1)
        else:
            print("Valor invalido!!!")
def entrar():
    limpar()
    while(True):
        print("\n\nLogin (0 - voltar)")
        print("Email: ")
        email = input()
        if(email == "0"):
            return 0
        print("Senha: ")
        senha = input()
        if(email == "0"):
            return 0
        if((email == "admin") and (senha == "admin")):
            menu_do_cliente()
            limpar()
menuprincipal()
