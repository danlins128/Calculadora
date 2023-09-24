# Calculadora
import os
from math import sqrt
total = 0 
# Funções
def limpar_console():
    sistema = os.name
    if sistema == 'posix': # Para linux
        os.system('clear')
    elif sistema == 'nt': # Para windows
        os.system('cls')
    else:
        pass


def criar_barra():
    print('-' * 32)


def soma(a, b):
    resultado = a + b
    return resultado

def subtração(a, b):
    resultado = a - b
    return resultado

def divisão(a, b):
    resultado = a / b
    return resultado

def multiplicação(a, b):
    resultado = a * b
    return resultado

def potencia(base_num, elevado):
    resultado = 0
    for c in range(elevado):
        resultado = base_num * base_num
    return resultado

def porcentagem(a, b):
    resultado = (a * b) / 100
    return resultado

# Cabeçalho

criar_barra()
print('Bem vindo à calculadora 3.0')
criar_barra()

# Pedindo Número para operar
while True:
    try:
        num1_str = input('Digite o primeiro número: ')

        try: 
            num1 = float(num1_str)
        except ValueError:
            limpar_console()
            criar_barra()
            print('Valor inválido.... Digite um número inteiro ou com "." ')
            criar_barra()
            continue # Volta para o início do loop

        
        # Menu

        criar_barra()
        print('[+] Soma')
        print('[-] Subtração')
        print('[/] Divisão')
        print('[*] Multiplicação')
        print('[**] Potência')
        print('[%] Porcentagem')
        print('[R] Raiz²')
        criar_barra()

# Validando operador

        escolha = input(': ')

        if escolha.lower() == 'r':
            limpar_console()
            print(f'{sqrt(num1):.2f}')

        elif escolha == '+':
            num2_str = input('Digite o segundo número: ')
            try:
                num2 = float(num2_str)
                limpar_console()
                print(f'{soma(num1, num2)}')
                criar_barra()
            except ValueError:
                limpar_console()
                print('Valor inválido para o segundo número.')

        elif escolha == '-':
            num2_str = input('Digite o segundo número: ')
            try:
                limpar_console()
                num2 = float(num2_str)
                print(f'{subtração(num1, num2)}')
                criar_barra()
            except ValueError:
                limpar_console()
                print('Valor inválido para o segundo número.')
                      
        elif escolha == '/':
            num2_str = input('Digite o segundo número: ')
            try:
                limpar_console()
                num2 = float(num2_str)
                print(f'{divisão(num1, num2)}')
                criar_barra()
            except ValueError:
                limpar_console()
                print('Valor inválido para o segundo número.')

        elif escolha == '*':
            num2_str = input('Digite o segundo número: ')
            try:
                limpar_console()
                num2 = float(num2_str)
                print(f'{multiplicação(num1, num2)}')
                criar_barra()
            except ValueError:
                limpar_console()
                print('Valor inválido para o segundo número.')

        elif escolha == '**':
            num2_str = input('Digite o segundo número: ')
            try:
                limpar_console()
                num2 = float(num2_str)
                print(f'{potencia(num1, num2)}')
                criar_barra()
            except ValueError:
                limpar_console()
                print('Valor inválido para o segundo número.')

        elif escolha == '%':
            num2_str = input('Digite o segundo número: ')
            try:
                limpar_console()
                num2 = float(num2_str)
                print(f'{porcentagem(num1, num2)}')
                criar_barra()
            except ValueError:
                limpar_console()
                print('Valor inválido para o segundo número.')


    except KeyboardInterrupt:
        limpar_console()
        print("\nEncerrando o programa.")
        
        break  # Sai do loop quando o usuário pressiona Ctrl+C
