### Notes 
"""
Estruturas Condicionais: if, else, elif

Estruturas Lógicas: AND, NOT, OR, IS

Operadores unários:
    - not 
Operadores Binários: 
    - and, or, is

Regras de Funcionamento
- and -> Ambos valores precsiam ser True
- or -> Um ou outro precisa ser True
- not -> O valore do booleano é invertido
- is -> Compara se o valor é o esperado
""" 
### Example


idade = 0

if idade < 18:
    print('Menor de idade')
elif idade == 18:
    print('Tem 18 anos')
elif idade == 26:
    print('Tem 26 anos')
else:
    print('Maior de idade')


ativo = False
logado = False 

if not ativo:
    print('Você precisa ativar sua conta. Por Favor, cheque seu e-mail')
else:
    print('Bem-vindo usuário!')

### Exercise

#1. Faça um programa que receba dois números inteiros e mostre qual deles é o maior.

print('Insira dois numeros inteiros:')
number1 = int(input("Insira o primeiro numero: "))
number2 = int(input("Insira o segundo numero: "))

if number1 == number2:
    print('Os numeros são iguais')
else: 
    print('Os numeros não são iguais')

#  2. Faça um programa que leia um número inteiro fornecido pelo usuário. 
# Se esse número for positivo, calcule a raiz quadrada do número e apresente-a. 
# Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.

number1 = int(input("Insira um numero inteiro: "))

if number1 > 0:
    result_1 = number1 ** 2
    print('Raiz quadrada do numero: ', result_1)
else: 
    print('Numero invalido')

# 3. Faça um programa que recebe um número inteiro e informe se este número é par ou ímpar.

number1 = int(input("Insira um numero inteiro: "))

result_1 = number1 % 2

if result_1 == 0:
    print('Numero Par')
else:
    print('Numero Impar')