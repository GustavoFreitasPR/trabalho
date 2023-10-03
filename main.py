'''
1:

import random

# Listas de nomes e sobrenomes
nomes = ["Alice", "Bernardo", "Clara", "Davi", "Eduarda", "Felipe", "Gabriela", "Heitor", "Isabela", "João",
         "Lara", "Matheus", "Natália", "Otávio", "Priscila", "Rafael", "Sofia", "Thiago", "Valentina", "William"]
sobrenomes = ["Alves", "Barbosa", "Carvalho", "Dias", "Fernandes", "Gomes", "Hernandez", "Inácio", "Jorge", "Klein",
              "Lima", "Mendes", "Nunes", "Oliveira", "Pereira", "Queiroz", "Ramos", "Santos", "Teixeira", "Vieira"]

def gera_dados_aleatorios(N):
    with open("dados_pessoais.txt", "w") as arquivo:
        for _ in range(N):
            nome_completo = f"{random.choice(nomes)} {random.choice(sobrenomes)}"
            idade = random.randint(18, 60)
            altura = round(random.uniform(1.50, 2.00), 2)
            arquivo.write(f"{nome_completo}, {idade} anos, {altura} m\n")

N = int(input("Digite o número de registros a serem gerados: "))
gera_dados_aleatorios(N)
'''
'''
2:

import random

# Listas de nomes e sobrenomes
nomes = ["Alice", "Bernardo", "Clara", "Davi", "Eduarda", "Felipe", "Gabriela", "Heitor", "Isabela", "João",
         "Lara", "Matheus", "Natália", "Otávio", "Priscila", "Rafael", "Sofia", "Thiago", "Valentina", "William"]
sobrenomes = ["Alves", "Barbosa", "Carvalho", "Dias", "Fernandes", "Gomes", "Hernandez", "Inácio", "Jorge", "Klein",
              "Lima", "Mendes", "Nunes", "Oliveira", "Pereira", "Queiroz", "Ramos", "Santos", "Teixeira", "Vieira"]

def gera_dados_aleatorios(N):
    with open("dados_pessoais.txt", "w") as arquivo:
        for _ in range(N):
            nome_completo = f"{random.choice(nomes)} {random.choice(sobrenomes)}"
            idade = random.randint(18, 60)
            altura = round(random.uniform(1.50, 2.00), 2)
            arquivo.write(f"{nome_completo}, {idade} anos, {altura} m\n")

N = int(input("Digite o número de registros a serem gerados: "))
gera_dados_aleatorios(N)


def escreverNumerosAleatorios(qtdNumeros, nomeArquivo):
    arquivoNumeros = open(nomeArquivo, 'w')
    for i in range(qtdNumeros):
        nome_completo = f"{random.choice(nomes)} {random.choice(sobrenomes)}"
        idade = random.randint(18, 60)
        altura = round(random.uniform(1.50, 2.00), 2)
        arquivoNumeros.write(f"{nome_completo}, {idade} anos, {altura} m\n")
    arquivoNumeros.close()

escreverNumerosAleatorios(100, 'cadastro.txt')
'''


'''
3:

def copia_arquivo_sem_comentarios(origem, destino):
    with open(origem, "r") as arquivo_origem, open(destino, "w") as arquivo_destino:
        for linha in arquivo_origem:
            if not linha.strip().startswith("//"):
                arquivo_destino.write(linha)

copia_arquivo_sem_comentarios("arquivo_origem.txt", "arquivo_destino.txt")
'''
'''
4:


def calcular_media(notas):
    notas = [float(nota) for nota in notas.split()]
    return sum(notas) / len(notas)

def criar_arquivos():
    alunos = ["João", "Maria", "Pedro"]
    notas = ["8.5 7.0 9.5", "6.0 7.5 8.0", "9.0 8.5 9.5"]

    with open("alunos.txt", "w") as arquivo_alunos, open("notas.txt", "w") as arquivo_notas:
        for aluno, nota in zip(alunos, notas):
            arquivo_alunos.write(f"{aluno}\n")
            arquivo_notas.write(f"{nota}\n")

def gerar_arquivo_medias(nome_alunos, nome_notas, nome_resultado):
    linhas_alunos = open(nome_alunos, "r").readlines()
    linhas_notas = open(nome_notas, "r").readlines()

    with open(nome_resultado, "w") as arquivo_resultado:
        for linha_aluno, linha_notas in zip(linhas_alunos, linhas_notas):
            nome_aluno = linha_aluno.strip()
            media = calcular_media(linha_notas)
            arquivo_resultado.write(f"{nome_aluno}: {media}\n")

# Criar arquivos de exemplo
criar_arquivos()

# Gerar o arquivo de médias
gerar_arquivo_medias("alunos.txt", "notas.txt", "medias.txt")

'''
'''
5:

def alterar_nota_aluno(arquivo_notas, nome_aluno, nota_antiga, nova_nota):
    linhas = []
    with open(arquivo_notas, "r") as arquivo_leitura:
        for linha in arquivo_leitura:
            if nome_aluno in linha:
                linha = linha.replace(nota_antiga, nova_nota)
            linhas.append(linha)
    with open(arquivo_notas, "w") as arquivo_escrita:
        arquivo_escrita.writelines(linhas)

alterar_nota_aluno("notas.txt", "João", "7.5", "8.0")
'''
'''

6:

def separar_enderecos_ip(arquivo_entrada, arquivo_validos, arquivo_invalidos):
    with open(arquivo_entrada, "r") as entrada, open(arquivo_validos, "w") as validos, open(arquivo_invalidos, "w") as invalidos:
        for linha in entrada:
            endereco = linha.strip().split(".")
            if len(endereco) == 4:
                octetos_validos = True
                for octeto in endereco:
                    if not (octeto.isdigit() and 0 <= int(octeto) <= 255):
                        octetos_validos = False
                        break
                if octetos_validos:
                    validos.write(linha)
                else:
                    invalidos.write(linha)
            else:
                invalidos.write(linha)

# Exemplo de uso
separar_enderecos_ip("enderecos.txt", "validos.txt", "invalidos.txt")
'''