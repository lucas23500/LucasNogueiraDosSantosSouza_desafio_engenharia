"""
Loggi Turma de Estágio 2022 - Dessafio Técnico de Engenharia
Nome: Lucas Nogueira dos Santos Souza
Universidade: IFAM
Curso: Tecnologia em Análise e Desenvolvimento de Sistemas
Semestre Atual: 3 Período

Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
"""

cd_lista = ['288355555123888', '335333555584333', '223343555124001', '002111555874555', '111188555654777',
            '111333555123333', '432055555123888', '079333555584333', '155333555124001', '333188555584333',
            '555288555123001', '111388555123555', '288000555367333', '066311555874001', '110333555123555',
            '333488555584333', '455448555123001', '022388555123555', '432044555845333', '034311555874001']

# Lista de Destino dos Pacotes
ld_sud = []
ld_sul = []
ld_co = []
ld_nord = []
ld_nort = []

# Lista de Pacotes Válidos e Inválidos
l_valido = []
l_invalido = []

# Produtos Que a Loggi Envia
tipos_produtos = [1, 111, 333, 555, 888]

# Dicionário listando os produtos vendidods por vendedor
vendedores = {}

# Lista para Solucionar a Questão 3
q3_pacotes = []

# Dicionário Usado para Gerar o Relatório da Questão 6
q6_relatorio = {'Sudeste': {'Joias': [], 'Livros': [], 'Eletronicos': [], 'Bebidas': [], 'Brinquedos': []},
                'Sul': {'Joias': [], 'Livros': [], 'Eletronicos': [], 'Bebidas': [], 'Brinquedos': []},
                'Centro-Oeste': {'Joias': [], 'Livros': [], 'Eletronicos': [], 'Bebidas': [], 'Brinquedos': []},
                'Nordeste': {'Joias': [], 'Livros': [], 'Eletronicos': [], 'Bebidas': [], 'Brinquedos': []},
                'Norte': {'Joias': [], 'Livros': [], 'Eletronicos': [], 'Bebidas': [], 'Brinquedos': []}}

# Dicionário Usado para Gerar o Relatório da Questão 6
q7_truck = {'Centro-Oeste': [], 'Norte': []}


# Função para remover dados repetidos. E ajudar na transição de um pacote válido -> Inválido
def remove_dados(lista, codigo):
    if codigo in lista:
        lista.remove(codigo)


for i, j in enumerate(cd_lista):
    origem = int(j[:3])
    destino = int(j[3:6])
    loggi = int(j[6:9])
    vendedor = int(j[9:12])
    produto = int(j[12:])

    # Inserção dos Pacotes nas listas de Destinos e validação dos pacotes
    if 1 <= destino <= 99:
        l_valido.append(j)
        ld_sud.append(j)
    elif 100 <= destino <= 199:
        l_valido.append(j)
        ld_sul.append(j)
    elif 201 <= destino <= 299:
        l_valido.append(j)
        ld_co.append(j)
    elif 300 <= destino <= 399:
        l_valido.append(j)
        ld_nord.append(j)
    elif 400 <= destino <= 499:
        l_valido.append(j)
        ld_nort.append(j)
    else:
        l_invalido.append(j)

    # Validação dos Pacotes por produtos
    if produto not in tipos_produtos:
        remove_dados(l_valido, j)
        if j not in l_invalido:
            l_invalido.append(j)

    # Validação dos Pacotes por vendedor
    if vendedor == 367:
        remove_dados(l_valido, j)
        if j not in l_invalido:
            l_invalido.append(j)

    # Validação dos pacotes por origem do pacote com produto específico
    if not 1 <= origem <= 499:
        remove_dados(l_valido, j)
        if j not in l_invalido:
            l_invalido.append(j)

    # Terceira Questão - Indetifincando pacote origem regiao Sul e conteudo: brinquedo
    if j in l_valido and 100 <= origem <= 199 and produto == 888:
        q3_pacotes.append(j)

    # remocao de dados repetidos dentro da lista de destinos
    for a, s in enumerate(cd_lista):
        if s in l_invalido:
            remove_dados(ld_sud, s)
            remove_dados(ld_sul, s)
            remove_dados(ld_co, s)
            remove_dados(ld_nord, s)
            remove_dados(ld_nort, s)

# Inserção dos dados e controle de pacotes por vendedor
for i, j in enumerate(l_valido):
    vendedor = int(j[9:12])
    if vendedor not in vendedores:
        vendedores[vendedor] = []
    if vendedor in vendedores:
        vendedores[vendedor].append(j)

# Cricao do relatorio para questao 6 - Pacotes por Destino e Por tipo (Apenas válidos)
for i, j in enumerate(l_valido):
    destino = int(j[3:6])
    produto = int(j[12:])
    if 1 <= destino <= 99:
        destino = 'Sudeste'
    elif 100 <= destino <= 199:
        destino = 'Sul'
    elif 201 <= destino <= 299:
        destino = 'Centro-Oeste'
    elif 300 <= destino <= 399:
        destino = 'Nordeste'
    elif 400 <= destino <= 499:
        destino = 'Norte'

    if produto == 1:
        produto = "Joias"
    elif produto == 111:
        produto = "Livros"
    elif produto == 333:
        produto = "Eletronicos"
    elif produto == 555:
        produto = "Bebidas"
    elif produto == 888:
        produto = "Brinquedos"

    q6_relatorio[destino][produto].append(j)

# Oitava Questão
for i, j in enumerate(l_valido):
    destino = int(j[3:6])
    produto = int(j[12:])
    contco = 0
    if 201 <= destino <= 299:
        destino = 'Centro-Oeste'
        if produto == 1:
            q7_truck[destino].insert(0, j)
        else:
            q7_truck[destino].append(j)
        # Vai ser o ponto de referência para inserir o os pacotes que irao para o norte
        contco += 1
    if 400 <= destino <= 499:
        destino = 'Norte'
        if produto == 1:

            q7_truck[destino].insert(contco, j)
        else:
            q7_truck[destino].append(j)

# Apresentação do Resultado

print("\n\n" + '=' * 100)
print("=== Questão 1 ===")
print("Identificar a região de destino de cada pacote, com totalização de pacotes (soma região)\n")
print(f"Sudeste: {len(ld_sud)} Pacotes: {ld_sud}\n")
print(f"Sul: {len(ld_sul)} Pacotes: {ld_sul}\n")
print(f"Centro-Oeste: {len(ld_co)} Pacotes: {ld_co}\n")
print(f"Nordeste: {len(ld_nord)} Pacotes: {ld_nord}\n")
print(f"Norte: {len(ld_nort)} Pacotes: {ld_nort}\n")

print("\n\n=== Questão 2 ===")
print("Saber quais pacotes possuem códigos de barras válidos e/ou inválidos\n")
print(f"Pacotes Válidos: {len(l_valido)}")
print(f"Pacotes Inválidos: {len(l_invalido)}")
print(f"Pacotes Válidos: {l_valido}")
print(f"Pacotes Inválidos: {l_invalido}")

print("\n\n=== Questão 3 ===")
print("Identificar os pacotes que têm como origem a região Sul e Brinquedos em seu conteúdo\n")
print(f"Número de Pacotes: {len(q3_pacotes)}")
print(f"Pacotes: {q3_pacotes}")

print("\n\n=== Questão 4 ===")
print("Listar os pacotes agrupados por região de destino (Considere apenas pacotes válidos)\n")
print(f"Sudeste: {ld_sud}")
print(f"Sul: {ld_sul}")
print(f"Centro-Oeste: {ld_co}")
print(f"Nordeste: {ld_nord}")
print(f"Norte: {ld_nort}")

print("\n\n=== Questão 5 ===")
print("Listar o número de pacotes enviados por cada vendedor (Considere apenas pacotes válidos)\n")
for key, value in vendedores.items():
    print(f"Vendedor: {key} Pacotes: {value}")

print("\n\n=== Questão 6 ===")
print("Gerar o relatório/lista de pacotes por destino e por tipo (Considere apenas pacotes válidos)\n")

for chave, valor in q6_relatorio.items():
    print(f"Destino: {chave}")
    for key, value in q6_relatorio[chave].items():
        print(f"Tipo de Produto: {key} Pacotes: {value}")
    print('\n')

print("\n\n=== Questão 7 ===")
print("""Se o transporte dos pacotes para o Norte passa pela Região
Centro-Oeste, quais são os pacotes que devem ser despachados no
mesmo caminhão?
\n""")
for chave, valor in q7_truck.items():
    for i, j in enumerate(q7_truck[chave]):
        print(f" {i + 1}. Pacote: {j}")
    print('\n')

print("\n\n=== Questão 8 ===")
print("""Se todos os pacotes fossem uma fila qual seria a ordem de carga
para o Norte no caminhão para descarregar os pacotes da Região
Centro Oeste primeiro;
\n""")

for chave, valor in q7_truck.items():
    for i, j in enumerate(q7_truck[chave]):
        print(f" {i + 1}. Pacote: {j}")
    print('\n')

print("\n\n=== Questão 9 ===")
print("""No item acima considerar que as jóias fossem sempre as primeiras a
serem descarregadas\n""")

for chave, valor in q7_truck.items():
    for i, j in enumerate(q7_truck[chave]):
        print(f" {i + 1}. Pacote: {j}")
    print('\n')

print("\n\n=== Questão 10 ===")
print("""Listar os pacotes inválidos\n""")
print(f"Pacotes Inválidos: {l_invalido}")
