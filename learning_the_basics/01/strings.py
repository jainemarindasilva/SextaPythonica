#Sintaxe:
message: str = "Wello world" #ou
message = "Wello world" #ou
message: str = 'Wello world' #ou
message = 'Wello world'

#para utilizar aspas simples ou aspas duplas dentro do texto:
message = 'The "Hello World" is classic'
#ou
message = "The \"Hello World\" is classic"

#para atribuir mais de uma linha:
message = """Este texto
tem duas linhas """

#Substring / Slice:
#Sintaxe de slicing de strings é: [início:fim:salto]
s = "Olá, mundo!"
print(s[0]) # 'O'
print(s[2]) # 'á'
print(s[6]) # 'u'

#Podemos também acessar os elementos em ordem reversa usando índices negativos. Neste esquema, o último caracter de uma string está no índice −1, o penúltimo no índice −2, e assim por diante, como mostrado no exemplo abaixo.
print(s[-1]) # '!'
print(s[-2]) # 'o'
print(s[-4]) # 'n'

#Podemos também acessar fatias ou "slices" de uma string ou lista, sendo que o primeiro argunto é inclusivo, mas o segundo é exclusivo
print(s[1:3]) # 'lá'
print(s[:3])  # 'Olá'
print(s[5:])  # 'mundo!'
print(s[:])   # "Olá, mundo!"

#É possível ainda especificar um parâmetro que indica quantos caracteres devem ser processados de cada vez.
print(s[::2])  # Imprime os caracteres nos índices pares (inicia do index = 0 e pega de dois em dois)
	# Oá ud!
print(s[1::2]) # Imprime os caracteres nos índices ímpares (inicia do index = 1 e pega de dois em dois)
	# l,mno
print(s[::-1]) # Salta de um caracter por vez e começa pelo último (por causa do '-')
	# !odnum ,álO
print(s[::-2]) # Salta de dois caracter por vez e começa pelo último (por causa do '-')
	# !du áO
