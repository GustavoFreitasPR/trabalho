#exercicio 1

meu_conjunto = {1,2,3,4,5,6,7,8,9,10}
print(meu_conjunto)

#EXERCICIO 2
meu_conjunto1 = {1,2,3,4,5}
meu_conjunto2 = {3,4,5,6,7}

uniao = meu_conjunto1.union(meu_conjunto2)
print(uniao)

#EXERCICIO 3 
vogais = {'a', 'e', 'i', 'o', 'u'}

palavra = input("Digite uma palavra: ")

vogais_na_palavra = []
for letra in palavra:
    
    if letra in vogais and letra not in vogais_na_palavra:
        vogais_na_palavra.append(letra)


print("Vogais na palavra:", ", ".join(vogais_na_palavra))


#EXERCICIO 4
frutas = {'abacate', 'laranja','abacaxi'}
frutas2 = {'abacate','banana','laranja'}

intersecao = frutas.intersection(frutas2)
print(intersecao)

#EXERCICIO 5
import random


numeros_aleatorios = set(random.sample(range(1, 101), 10))  

maior_numero = max(numeros_aleatorios)
menor_numero = min(numeros_aleatorios)

print("Conjunto de números aleatórios:", numeros_aleatorios)
print("Maior número:", maior_numero)
print("Menor número:", menor_numero)



#EXERCICIO 6
cores = {'vermelho', 'laranja', 'amarelo', 'verde',
'azul', 'anil', 'violeta'}

palavra = input("Digite uma cor: ")

if palavra in cores:
    print(f"A cor {palavra} esta no conjunto de cores do arco-iris")
else:
    print(f"A cor {palavra} nao esta no conjunto arco-iris")


#EXERCICIO 7
dias = {'segunda','terca','quarta','quinta','sexta','sabado','domingo'}

dias.remove('segunda')
dias.remove('sexta')
print(dias)


#EXERCICIO 8
numeros = set(range(1, 21))

numeros_pares = set(range(2, 11, 2))

diferenca = numeros - numeros_pares
print("Diferença entre os conjuntos:", diferenca)

#EXERCICIO 9
notas_input = input("Digite as notas do aluno separadas por vírgula: ")

notas = [float(nota) for nota in notas_input.split(',')]

media = sum(notas) / len(notas)

if media >= 7:
    resultado = "Aprovado"
else:
    resultado = "Reprovado"

print(f"O aluno está {resultado} com média {media:.2f}")


#EXERCICIO 10
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


numeros_primos_1_a_20 = set(numero for numero in range(1, 21) if is_prime(numero))

numero_digitado = int(input("Digite um número: "))

if numero_digitado in numeros_primos_1_a_20:
    print(f"O número {numero_digitado} é primo e está no conjunto!")
else:
    print(f"O número {numero_digitado} não é primo ou não está no conjunto.")
 



