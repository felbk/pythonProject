import random
n1 = input('aluno1')
n2 = input('aluno2')
n3 = input('aluno3')
n4 = input('aluno4')
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print('a ordem será {}'.format(lista))