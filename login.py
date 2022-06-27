from os import system 
from colorama import init, Fore, Back, style 
from getpass import getpass

from numpy import logical_not
from sqlalchemy import true 
import stdiomask 
from time import sleep 
init(autoreset=True) 

# Criar-o menu- de opções 

def exibir_menu(): 
    print(Fore.GREEN +  '''Bem-vindos  ao Projeto  
          Sistema de login 
    Escolha uma Opção:
    [1] Cadastrar novo usuário 
    [2] fazer Login 
    [3] sair 
    ''')
        opçao = init(input('Digite sua opação:'))
        return(opçao)
    
    # Fazer login com nome e senha do usuário 

def fazer_login():
    login = input('Nome: ')
    senha = stdiomask.getpass(prompt='Senha: ', mask='')
        return(login, senha)
        # senha = stdiomask.getpass(prompt='senha:',mask='*')

        # Pesquisar no arquivo usuarios.txt


 def buscar_usuario(login, senha):
    usuario=[]
    try: 
       with open('usuarios.txt', 'r+', enconding='UTF-8', newline'') as
                for linha in aquivo:
                    linha = linha.strip(",")
                    
                    
                    
                    
while True: 
    system('cls')
    opçao = exibir_menu()
    
        if opçao == 1:
            # Cadastrar novo usuário
            login, senha = fazer_login()
            if login == senha:
                print('Sua senha deve ser diferente do login.')
                senha = getpass('senha: ')
                user = buscar_usuario(login, senha)
                if  user == True:
                    print( Fore.RED+'Usuário já existe!')
                    sleep(2)
                    #exite () 
                else:
                    with open('usuarios.tx.', 'a+', enconding='UTF-8', newline='') as aquivo:
                        arquivo.writelines(f'{login}:{senha}\n')
                        print(Fore.CYAN + 'Cadastro aprovado!')
                        exit()
                        
             elif opçao == 2:
                 # fazer o login do usuário
                 login, senha = fazer_login()
                 user= buscar_usuario(login, senha) 
                 if user == True:
                     print(fore.CYAN + 'lOGIN realizado com sucesso!')
                     sleep(1)
                     exit () 
                 else:
                     print(
                         Fore.RED+ 'Você deve ter digitado seu nome usuário ou a senha errado. \n Por favor verificar ')
                     sleep(2) 
                     
               else: 
                   system('cls')
                   print (fore.LIGHTMAGENTA_EX+'Goodbay!')
                   break