#***Exe. 04 - Happy Number***
"""Escreva um algoritmo para determinar se um número `n` é feliz.

Um número feliz é um número definido pelo seguinte processo:
- Começando com qualquer número inteiro positivo, substitua o número pela soma dos quadrados de seus dígitos.
- Repita o processo até que o número seja igual a 1 (onde ele permanecerá), ou ele fará um loop infinito em um ciclo que não inclui 1.
- Aqueles números para os quais este processo termina em 1 são felizes.

Retorna verdadeiro se n for um número feliz e falso se não for. 
"""
import random

numero_ran = random.randint(1,100)
print(numero_ran)

lst_numeros_exp = [numero_ran]
while numero_ran != 1:
  numero_ran = sum([int(n_aux)**2 for n_aux in str(numero_ran)])
  if numero_ran == 1:
    print('Verdadeiro')
  if numero_ran in lst_numeros_exp:
    print('Falso')
    break
  lst_numeros_exp.append(numero_ran)
  



#print('O numero {0} {1} feliz.'.format(numero_ran, 'é' if numero_feliz == True else "não é"))