# Faça um programa que receba 4 alturas usando um laço de repetição 
# e realize a soma dessas alturas.

#%%
soma = 0 #Valor final
qtde_entradas = 4 #Contador de entradas

for i in range(qtde_entradas): # range(0,4)
    altura = input("Entre com a altura: ")
    altura = float(altura)
    soma += altura 

print("Soma das alturas: ", soma)

# %%
