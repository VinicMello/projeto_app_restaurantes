# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

pessoas = [{
    'nome': 'Vinicius',
    'idade': 22,
    'cidade': 'Curitiba'
}]

print(pessoas)

# 2 - Utilizando o dicionário criado no item 1:

# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
# Adicione um campo de profissão para essa pessoa;
# Remova um item do dicionário.

pessoas[0]['idade'] = 23
print(pessoas)

pessoas[0]['profissão'] = 'software engineer'
print(pessoas)

del pessoas[0]['profissão']
print(pessoas)

# 3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.

numeros_ao_quadrado = {
    1: 1,
    2: 4,
    3: 9,
    4: 16,
    5: 25
}

numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)

# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

#retirar o del do exercício 2

if 'profissão' in pessoas[0]:
    print("A chave 'profissão' existe no dicionário")
else:
    print("A chave 'profissão' não existe no dicionário")

# 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
    
palavras = 'TESTETESTETESTE'
freq = {}

for letra in palavras:     

    if letra in freq:
        freq[letra] = freq[letra] + 1
    else:
        freq[letra] = 1

print(freq)




