# Altere o programa anterior para considerar a quantidade de garrafas de água

texto = """Escolha a sua água para comprar
(1) Água mineral natural 
(2) Água mineral com gás
"""

texto_qtd = """Insira a quantidadede garrafas: """

opcao = input(texto)

qtd = int(input(texto_qtd))

if opcao == "1":
    valor = 1.50 * qtd
    print("Sua conta deu: R$", valor)


elif opcao == "2":
    valor = 2.50 * qtd
    print("Sua conta deu: R$", valor)

else:
    print("Insira a opcão correta!")

# Resolucão Professor

texto = """Escolha a sua água para comprar
(1) Água mineral natural - R$1.5
(2) Água mineral com gás - R$2.5
"""

opcao = input(texto)

valor_item = 0 

if opcao == "1":
    covalor_itemnta = 1.5
elif opcao == "2":
    valor_item = 2.5

if valor_item == 0:
    print("Insira a opcão correta!")
    
else:
    qtde = input("Quantas garrafas? ")
    qtde = int(qtde)
    valor_total = valor_item * qtde
    print("Sua conta é: R$", valor_total)