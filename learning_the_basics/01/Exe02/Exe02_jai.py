#***Exe. 02 - StringInfo***

#Crie um programa que, a partir de uma string digitada pelo usuário, imprima:
alguma_string = input('Digite algo: ')

#1. O número de caracteres da string.
print('Numero de caracteres da string: {0}'.format(len(alguma_string)))

#2. A string com todas suas letras em maiúsculo.
print('A string com todas suas letras em maiúsculo: {0}'.format(alguma_string.upper()))

#3. O número de vogais da string.
vogais = ['a','e','i','o','u']
num_vogais = 0
for i in alguma_string.lower():
  if i in vogais:
    num_vogais = num_vogais + 1
# OU...
for i in vogais:
  num_vogais += alguma_string.lower().count(i)
# OU...
num_vogais = sum(alguma_string.lower().count(i) for i in vogais)
print(f'O número de vogais da string: {num_vogais}')

#4. Se a string digitada começa com “INS” (ignorando maiúsculas/minúsculas).
print('A string digitada começa com INS: ', alguma_string.lower().startswith('ins'))

#5. Se a string digitada termina com “AIS” (ignorando maiúsculas/minúsculas).
print('A string digitada termina com AIS: ', alguma_string.lower().endswith('ais'))

#6. O número de dígitos (0 a 9) da string.
digitos = [0,1,2,3,4,5,6,7,8,9]
num_digitos = 0
for i in alguma_string:
  if i.isnumeric():
    num_digitos = num_digitos + 1
print(f'O número de digitos da string: {num_digitos}')