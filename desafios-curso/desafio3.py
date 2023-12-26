# 1 - Crie uma lista para cada informação a seguir:
# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomes = ['João', 'Gabriel', 'Paulo', 'Vinicius']
anos = [2001, 2023]

for numero in numeros:
    print(numero)

for nome in nomes:
    print(nome)

for ano in anos:
    print(ano)

# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma_impares = 0

for numero in numeros:

    if (numero % 2) != 0:
        soma_impares = soma_impares + numero

print(f'A soma dos nº impares 1 a 10: {soma_impares}')

# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in reversed(numeros):
    print(numero)

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

numero_tabuada = int(input("Digite o número para saber a tabuada: "))
multiplicador = 1

for tabuada in range(1, 11, 1):

    multiplicacao = numero_tabuada * multiplicador
    print(f'{numero_tabuada} X {tabuada} = {multiplicacao}')
    multiplicador = multiplicador + 1

# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

numeros = [10, 20, 30, 40, 50, 'str', 60, 70, 80, 90, 100, 'str']
soma_numeros = 0

for numero in numeros:
    try:
        soma_numeros = soma_numeros + numero
    except TypeError:
        #print('Erro: Tipo inválido!')
        continue

print(soma_numeros)

# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

valores = [5, 0, 10, 20, 47, 22, 11, 7]
soma_valores = 0

for valor in valores:
    try:
        soma_valores = soma_valores + valor
        media_valores = soma_valores/len(valores)

    except ZeroDivisionError:
        print('Erro: Divisão por zero!')
    
print(round(media_valores, 2))
