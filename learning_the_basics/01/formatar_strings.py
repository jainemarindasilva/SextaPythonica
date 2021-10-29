# A função print concatena strings com um espaço entre elas.
print("Admirável", "Mundo", "Novo") # 'Admirável Mundo Novo'

# A função print converte números para strings.
print(1984, "George Orwell") # '1984 George Orwell'

# As strings somadas com + são concatenadas sem espaços entre elas.
print("#" + "Programando" + "Em" + "Python") # '#ProgramandoEmPython'

# Forma mais avançada de formatação de strings
frase = 'Um triângulo de base igual a {0} e altura igual a {1} possui área igual a {2}.'.format(3, 4, 12)
print(frase) # 'Um triângulo de base igual a 3 e altura igual a 4 possui área igual a 12.'

#### Formatação de strings com f-strings
linguagem = "Python"
frase = f"Programando em {linguagem}"
print(frase) # 'Programando em Python'

# Fomatação de floats 
# Utilizar ':QTD_NUM_TOTAL.QTD_NUM_DEPOIS_PONTOf'
print('R$ {:.2f}'.format(4.5))   #R$ 4.50
print('R$ {:.5f}'.format(4.5))   #R$ 4.50000
print('R$ {:3.2f}'.format(4.5))  #R$ 4.50
print('R$ {:05.2f}'.format(7.5)) #R$ 07.50
print('R$ {:07.2f}'.format(7.5)) #R$ 0007.50
print('R$ {:07.3f}'.format(7.5)) #R$ 007.500

# Fomatação de numeros
# Utilizar: ':QTD_NUM_TOTALd'
print('R$ {:5d}'.format(4))   #R$     4
print('R$ {:05d}'.format(4))  #R$ 00004
print('Hoje é dia {:02d}/{:02d}/{:04d}'.format(24,9,2021)) #Hoje é dia 24/09/2021
