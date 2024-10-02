'''1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;'''


valor = int(input("Digite um número: "))
anterior1 = 1
anterior2 = 0
for sequencia in range(1, valor + 1, 1):
    atual = anterior1 + anterior2
    anterior1 = anterior2 
    anterior2 = atual

    if valor == atual:
        print ("Esse número pertence a sequência. Parabéns!")
        break
    elif valor < atual:
        print ("Esse número não pertence a sequência. Tente novamente!")
        
       