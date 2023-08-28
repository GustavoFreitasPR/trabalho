#exercicio 1
'''
dicionario1 = {}
dicionario1['Nome'] = 'Gustavo'
dicionario1['idade'] = 18
print(dicionario1)
'''
#exercicio 2 
'''
dicionario2 = {'Nome':'Gustavo de Freitas','Idade':18,'Cidade':'Candoi'}
print(dicionario2)
'''
#exercicio 3
'''
dicionario3 = {'Pastel':8.99,'Coca-cola':5,'Suco de laranja':9.99}
print(dicionario3)
'''
#exercicio 4
'''
dicionario4 = {'Parana':'Curitiba','Sao Paulo':'Sao paulo','Santa catarina':'Florianopolis'}

estado = input("Digite o nome do estado que queira saber a capital :")
if estado in dicionario4:
    capital = dicionario4[estado]
    print(f"A capital do estado {estado} é {capital}")
else:
    print(f"O estado não encontrado")
'''
#exercicio 5
'''
dicionario5 = {'Guarapuava':200000,'Candoi':15000,'Foz do Jordao':17000,'Copel':1000,'Cachoeira':1500}

print(f"A cidade com a maior população é Guarapuava com 200000 habitantes")
'''
#exercicio 6
'''
dicionario6 = {'Pastel':500,'Coca-cola':276,'Suco de laranja':56}
alimento = input("Digite o nome do alimento que queira saber a quantidade de calorias :")
if alimento in dicionario6:
    caloria = dicionario6[alimento]
    print(f"A quantidade de calorias que tem no alimento {alimento} é {caloria} calorias.")
else:
    print(f"O alimento nao foi encontrado.")
'''
#exercicio 7
'''
dicionario7 = {'Passaro':'ave','Leao':'mamifero','Tubarao':'peixe','Cobra':'reptil','Pinguim':'ave'}
animal = dicionario7.keys()
print(animal)
'''
#exercicio 8
'''
dicionario8 = {'Brasil':'Verde, amarelo, azul, branco','Japao':'Vermelho, branco','Franca':'Azul, branco, vermelho','Alemanha':'Preto, vermelho, doado','Russia':'Branco, azul, vermho'}
Pais = dicionario8.keys()
print(Pais)
'''
#exercicio 9 
'''
dicionario9 = {'Banana':'amarelo','Morango':'Vermelho','Laranja':'Laranja','Uva':'Roxo','Limao':'Verde'}
print(dicionario9)
'''
#exercicio 10
dicionario10 = {'Futebol':11,'Xadrez':2,'Poker':2}
Jogo = input("Digite o nome do Jogo que queira saber a quantidade de Jogadores necessários :")
if Jogo in dicionario10:
    Jogadores = dicionario10[Jogo]
    print(f"A quantidade de Jogadores que é necessária para uma partida de {Jogo} é {Jogadores} Jogadores.")
else:
    print(f"O Jogo nao foi encontrado.")