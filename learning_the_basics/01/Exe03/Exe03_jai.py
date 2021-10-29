# ***Exe. 03 - Tip Calculator***

#Crie uma saudação para o seu programa.
print('Bem vindo ao Tip Calculator! \n')

#Pergunte quanto foi o total da conta.
total = float(input('Informe o valor total da conta: \n'))
#Pergunte quanta gorjeta será dada.
gorgeta = float(input('Informe o valor desejado da gorjeta: \n'))
#Pergunte quantas pessoas vão dividir a conta.
pessoas_divisao = int(input('Informe a quantidade de pessoas para dividir: \n'))

#Mostre quanto cada pessoa deve pagar.
total_por_pessoa = (total + gorgeta) / pessoas_divisao
print('Cada um deve pagar: R$ {:.2f}'.format(total_por_pessoa))