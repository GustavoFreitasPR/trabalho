
#EXERCICIO 1
numeros_tupla = (1, 2, 3, 4, 5)


print(numeros_tupla)
#EXERCICIO 2

paises = ('brasil','chile','franca')

print(paises[1])

#EXERCICIO 3
valor_refeicao = 35
valor_servico = 7
valor_total = valor_refeicao + valor_servico

conta_restalrante = (valor_servico,valor_refeicao,valor_total)


print(conta_restalrante)

#EXERCICO 4
nomes = ('joao','iago','darlin','gabriel','pedro')

numero = int(input("digite um numero de 1 a 5:"))

if 1 <= numero <= 5:
    nome1 = nomes[numero - 1]
    print(f"o nome corespondente e:{nome1} ")
else:
    print("numero nao valido")


#EXERCICIO 5
notas = (8.5,7.0,5.0,9.0)

media = sum(notas) / len(notas)

print("sua media e :", media)

#exercicio 6
'''
tuplas6 = ('Vermelho','laranja', 'amarelo', 'verde',
'azul', 'anil', 'violeta')

cor = input("Digite o nome de uma cor: ")

if cor in tuplas6:
  print(f"A cor {cor} digitada está na tupla")

else:
  print(f"A cor {cor} digitada não está na tupla")
'''
'''
#exercicio 7
tuplas7 = (27,30,25,14,16,18,28)
print("A temperatura mais alta da semana foi 30 graus")
print("A temperatura minima da semana foi 14 graus")
'''
#exercicio 8
'''
tuplas8 = ('Morango:vermelho','uva:roxa','pitaya:rosa','limao:verde','banana:amarelo')

print(tuplas8)
'''
#exercicio 9
'''
tupla9 = tuple(range(1, 11))
tupla10 = tuple(range(5, 16))

intersecao = tuple(set(tupla9) & set(tupla10))

print(intersecao)
'''
#exercicio 10
alfabeto = tuple('abcdefghijklmnopqrstuvwxyz')
vogais = tuple('aeiou')

conjunto_alfabeto = set(alfabeto)
conjunto_vogais = set(vogais)

diferenca = tuple(conjunto_alfabeto - conjunto_vogais)

print(diferenca)
