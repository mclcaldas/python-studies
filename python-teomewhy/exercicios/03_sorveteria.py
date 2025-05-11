#Faça o programa de uma sorveteria, onde o usuário pode escolher:
#Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
#Sabor do sorvete: morango, creme, chocolate
#Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)
#Apresente o valor a ser pago


texto_tipo = """Escolha o tipo do sorvete:
(1) Casquinha - R$ 1,00
(2) Cascão - R$ 2,50
(3) Cestinha - R$ 4,00
"""

texto_sabor = """Escolha o sabor do sorvete:
(1) Morango
(2) Creme
(3) Chocolate
"""

texto_cobertura = """Escolha o sabor da cobertura:
(1) Caramelo - R$ 1,50
(2) Morango - R$ 1,50
(3) Chocolate - R$ 1,50
(4) Sem cobertura - R$ 0,00
"""

valor_tipo = 0
valor_cobertura = 0

opcao_tipo = input(texto_tipo)

if opcao_tipo == "1":
    valor_tipo = 1.0
elif opcao_tipo == "2":
    valor_tipo = 2.5
elif opcao_tipo == "3":
    valor_tipo = 4.0
else:
    print("Tipo inválido!")
    exit()

opcao_sabor = input(texto_sabor)

if opcao_sabor == "1" or opcao_sabor == "2" or opcao_sabor == "3":
    pass
else:
    print("Sabor inválido!")
    exit()

opcao_cobertura = input(texto_cobertura)

if opcao_cobertura == "1" or opcao_cobertura == "2" or opcao_cobertura == "3":
    valor_cobertura = 1.5
elif opcao_cobertura == "4":
    valor_cobertura = 0.0
else:
    print("Cobertura inválida!")
    exit()

valor_total = valor_tipo + valor_cobertura
print("Sua conta é: R$", valor_total)
