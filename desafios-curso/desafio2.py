# 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

numero = int(input("Digite um número: "))

if numero % 2 == 0:
     print(f'O {numero} é par')
else:
    print(f'O {numero} é impar')

# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.
    
idade = int(input("Digite sua idade: "))

if 0 < idade <= 12:
    print(f'Pela sua idade "{idade}", você é criança')
elif 13 <= idade <= 18:
    print(f'Pela sua idade "{idade}", você é adolescente')
else:
    print(f'Pela sua idade "{idade}", você é adulto')

# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

id = 'admin'
password = 'admin'

login = input("Digite seu login: ")
senha = input("Digite sua senha: ")

if login == id and senha == password:
    print("Conta acessada com sucesso!")
elif login != id and senha == password:
    print("Seu login não corresponde com o que foi cadastrado")
elif login == id and senha != password:
    print("Sua senha está errada")
else:
    print("Login e Senha errados")

# 4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

# Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# Caso contrário: o ponto está localizado no eixo ou origem.

print("--Descubra em qual quadrante as cordenadas estão--")
x = int(input("Digite a coordenada de x: "))
y = int(input("Digite a coordenada de y: "))

if x > 0 and y > 0:
    print("Está no 1º Quadrante")
elif x < 0 and y > 0:
    print("Está no 2º Quadrante")
elif x < 0 and y < 0:
    print("Está no 3º Quadrante")
elif x > 0 and y < 0:
    print("Está no 4º Quadrante")
else:
    print("O ponto está sobre um eixo ou na origem.")