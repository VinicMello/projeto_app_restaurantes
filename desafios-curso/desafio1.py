# 1 - Imprima a frase: Python na Escola de Programação da Alura.

print('Python na Escola de Programação da Alura')

# 2 - Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores armazenados em variáveis.

nome = 'Vinicius'
idade = 22

# 3 - Imprima a palavra: ‘ALURA’ de modo que cada letra fique em uma linha, como mostrado a seguir:

##interpolação de str
print('Meu nome é',nome,'e tenho',idade,'anos.')
print(f'Meu nome é {nome} e tenho {idade} anos')
print('Meu nome é {} e tenho {} anos.'.format(nome,idade))
print('Meu nome é %s e tenho %i anos.'%(nome,idade))


# 4 - Imprima a frase: O valor arredondado de pi é: {pi_arredondado} em que o valor de pi precisa ser armazenado em uma variável e arredondado para apenas duas casas decimais. Para facilitar, utilize:

print('A\nL\nU\nR\nA')
print('A','L','U','R','A',sep='\n')

pi = 3.1415926535
pi_arredondado = round(pi,2)

print(f'O valor arredondado de pi é: {pi_arredondado}')



