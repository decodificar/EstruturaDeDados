### aula semana 1

# conferindo a execução do python

#variavel
a = 5
print("a = ", a)

a = a + 3
print("a = ", a)

############################# condicional

if a > 5:
    print('É maior')
else:
    print('é menor')


############# Estrutura de Repetição

for valor in range(0, 11):
    print('valor = ', valor)
        # 0 1 2 3 4 5 6 7
lista = [25, 32, 97, 11, 6, 18, 31, 84]
for valor in lista:
    #print(valor) maneira simples
print('lista[', lista.index(valor), '] = ', valor)

print('lista[3] = ', lista[3])
print('tamanho da lista = ', len(lista))

############################### funções

def soma(a, b):
    return a + b

def soma2(a, b):
    c = a + b
    return c

print('soma = ', soma(5, 8))
print('soma2 = ', soma2(9, 11))

################################## busca simples
#### busca usando bandeira

def busca(lista, buscado):
    Flag = False # não existe o valor buscado
    for valor in lista:
        if valor == buscado:
            Flag = True #encontrado
            print('existe')
            break

    if Flag == False:
        print('Não existe')

busca(lista, 7)
busca(lista, 11)

########################### busca retornando True/False

