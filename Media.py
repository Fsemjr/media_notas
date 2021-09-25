import math

media_1 = int(input('Primeira media:'))
media_2 = int(input('Segunda media:'))
media_3 = int(input('Terceira media:'))

media = (media_1 + media_2 + media_3)/3 
if media > 7:
	print('Aprovado', + media)
elif media < 7:
	print('Reprovado', + media)
