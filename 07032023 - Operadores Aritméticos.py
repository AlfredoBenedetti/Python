import os

# Variáveis
a1 = 10
a2 = 2

# Operação de Adição
# Em Python, + é o operador de adição. É usado para adicionar 2 valores.
soma = a1 + a2

# Operação de Subtração
# Em Python, - é o operador de subtração.
# É usado para subtrair o segundo valor do primeiro valor.
subtracao = a1 - a2

# Operação de Multiplicação
# Em Python, * é o operador de multiplicação.
# É usado para encontrar o produto de 2 valores.
multiplicacao = a1*a2

# Operação de Divisão
# Em Python, / é o operador de divisão.
# É usado para encontrar o quociente quando o primeiro operando
# é dividido pelo segundo.
divisao = a1 / a2

# Operação de Módulo
# Em Python, % é o operador de módulo.
# É usado para encontrar o resto quando o primeiro operando
# é dividido pelo segundo.
modulo = a1 % a2

# Operador de exponenciação
# Em Python, ** é o operador de exponenciação.
# É usado para elevar o primeiro operando à potência de segundo.
exponenciacao = a1 ** a2

# Divisão do piso:
# Em Python, // é usado para conduzir a divisão do piso.
# É usado para encontrar o piso do quociente quando o primeiro operando é
# dividido pelo segundo.
piso = a1 // a2

os.system('cls')
print('Operação de Adição')
print('O resultado da Adição de ', a1, 'e', a2, 'é: ', str(soma))
print('')
print('Operação de Subtração')
print('O resultado da Subtração é: ', str(subtracao))
print('')
print('Operação de Multiplicação')
print('O resultado da Multiplicação é: ', str(multiplicacao))
print('')
print('Operação de Divisão')
print('O resultado da Divisão é: ', str(divisao))
print('')
print('Operação de Módulo')
print('O resultado do Módulo é: ', str(modulo))
print('')
print('Operação de Exponenciação')
print('O resultado da Exponenciação é: ', str(exponenciacao))
print('')
print('Operação de Piso')
print('O Resultado do Piso de ', a1, 'e', a2, 'é ', str(piso))
