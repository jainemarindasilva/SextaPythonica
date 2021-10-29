"""***Exe. 05 - Treasure Island***
Faça seu próprio jogo "Escolha sua própria aventura". Use declarações condicionais como if, else e elif para definir a lógica e o caminho da história em seu programa.
Escrever o código de acordo com a história descrita [aqui](https://app.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload) ou crie sua própria história! :monocle_face:

Dito isso, se você quiser continuar com o exemplo, sinta-se à vontade para usar os trechos de texto abaixo...
- 'Você está em uma encruzilhada. Onde você quer ir? Digite "esquerda" ou "direita" '
- Você chegou a um lago. Existe uma ilha no meio do lago. Digite "esperar" para esperar por um barco. Digite "nadar" para atravessar a nado. '
- "Você chega à ilha ileso. Tem uma casa com 3 portas. Uma vermelha, uma amarela e uma azul. Qual cor você escolhe?"
- "É uma sala cheia de fogo. Fim do jogo."
- "Você encontrou o tesouro! Você venceu!"
- "Você entra em uma sala de feras. Fim do jogo."
- "Você escolheu uma porta que não existe. Fim do jogo."
- "Você é atacado por uma truta furiosa. Fim do jogo."
- "Você caiu em um buraco. Fim do jogo."
"""

print('Bem vindo a Tresure Island. Sua missão é encontrar o tesouro.\n')
direcao = input('Você está em uma encruzilhada. Onde você quer ir? Digite "esquerda" ou "direita".\n')

if direcao == 'direita': 
  print('Você caiu em um buraco. Fim do jogo.')
else:
  acao = input('Você chegou a um lago. Existe uma ilha no meio do lago. Digite "esperar" para esperar por um barco. Digite "nadar" para atravessar a nado.\n' )
  if acao != 'nadar':
    porta = input('Você chega à ilha ileso. Tem uma casa com 3 portas. Uma vermelha, uma amarela e uma azul. Qual cor você escolhe?\n')
    if porta == 'vermelha': 
      print('É uma sala cheia de fogo. Fim do jogo.')
    elif porta == 'azul': 
      print('Você é comido por feras. Fim do jogo.')
    else: 
      print('Você encontrou o tesouro! Você venceu!')
  else: 
    print('Você é atacado por uma truta furiosa. Fim do jogo.')