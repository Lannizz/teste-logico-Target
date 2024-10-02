'''2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;'''

string = "Olá, mundo!"
if string.count('a') > 0 or string.count('A') > 0:
    print("A letra 'a' está presente na string!")
    print("Ela aparece {} vezes".format(string.count('a') + string.count('A')))
else:
    print("A letra 'a' não está presente na string.")