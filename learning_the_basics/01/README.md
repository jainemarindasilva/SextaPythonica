
# Learning the basics - 01

#### O que aprender...

- [x] Sintaxe básica
- [x] Variáveis e tipos de dados: strings, numbers, booleans
- [x] Condicionais

#### Material de apoio...

- https://docs.python.org/pt-br/3/tutorial/introduction.html
- https://docs.python.org/pt-br/3/tutorial/introduction.html#strings
- https://docs.python.org/pt-br/3/tutorial/inputoutput.html
- https://docs.python.org/pt-br/3/tutorial/introduction.html#numbers
- https://docs.python.org/pt-br/3/tutorial/controlflow.html#if-statements
- https://www.youtube.com/watch?v=k9TUPpGqYTo&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=3
- https://www.youtube.com/watch?v=khKv-8q7YmY&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=4
- https://www.youtube.com/watch?v=DZwmZ8Usvnk&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=7
- http://devfuria.com.br/python/sintaxe-basica/
- https://github.com/pythonprobr/pypratico/raw/master/academia/py_sintaxe.pdf

 
#### Exercícios... 

 ***Exe. 01 - Band Name Generator***
- [ ] Crie um programa que gere um nome de banda.

Instruções:
- Crie uma saudação para o seu programa.
- Pergunte ao usuário a cidade em que ele cresceu.
- Peça ao usuário o nome de um animal de estimação.
- Combine o nome da cidade e o animal de estimação e mostre o nome da banda.
:+1: Certifique-se de deixar um espaço entre os nomes, de que a primeira letra dos nomes estão em maiúsculas e o resto do nome esteja em minúsculas.

***Exe. 02 - StringInfo***
- [ ] Crie um programa que, a partir de uma string digitada pelo usuário, imprima:
1. O número de caracteres da string.
2. A string com todas suas letras em maiúsculo.
3. O número de vogais da string.
4. Se a string digitada começa com “INS” (ignorando maiúsculas/minúsculas).
5. Se a string digitada termina com “AIS” (ignorando maiúsculas/minúsculas).
6. O número de dígitos (0 a 9) da string.
       
***Exe. 03 - Tip Calculator***
- [ ] Crie uma calculadora de gorjetas. 

Instruções:
- Crie uma saudação para o seu programa.
- Pergunte quanto foi o total da conta.
- Pergunte quanta gorjeta será dada.
- Pergunte quantas pessoas vão dividir a conta.
- Mostre quanto cada pessoa deve pagar.

Exemplo: 
Se a conta fosse R$ 150,00, divida entre 5 pessoas, com 12% de gorjeta.
Cada pessoa deve pagar (150,00 / 5) * 1,12 = 33,60. 
Assim, a participação de todos na conta total é de R$30,00 mais uma gorjeta de R$3,60.

Dica: Existem 2 maneiras de arredondar um número. Talvez você precise pesquisar no Google para resolver isso.💪

***Exe. 04 - Happy Number***
- [ ] Escreva um algoritmo para determinar se um número `n` é feliz.

Um número feliz é um número definido pelo seguinte processo:
- Começando com qualquer número inteiro positivo, substitua o número pela soma dos quadrados de seus dígitos.
- Repita o processo até que o número seja igual a 1 (onde ele permanecerá), ou ele fará um loop infinito em um ciclo que não inclui 1.
- Aqueles números para os quais este processo termina em 1 são felizes.

Retorna verdadeiro se n for um número feliz e falso se não for. Exemplo: 

![image](https://user-images.githubusercontent.com/52661791/139443633-1d79eafe-f9cc-4950-a313-165fe007aadd.png)

***Exe. 05 - Treasure Island***
- [ ] Faça seu próprio jogo "Escolha sua própria aventura". Use declarações condicionais como if, else e elif para definir a lógica e o caminho da história em seu programa.

Instruções:

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

*Exercícios retirados de:*
https://leetcode.com/
https://www.udemy.com/course/100-days-of-code/
