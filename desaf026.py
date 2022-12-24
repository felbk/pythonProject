n = str(input('Digite uma frase: ')).lower().strip()
print('aparições de A:', n.count('a'))
print('A primeira letra A foi encontrada na posição {}' .format(n.find('a')+1))
print('A ultima letra A foi encontrada na posição {}' .format(n.rfind('a')+1))