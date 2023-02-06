from time import sleep
print("=" * 80)
r = '9'
n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
while r != '5':
    print('''
    [1] somar os números
    [2] multiplicar os números
    [3] qual o maior
    [4] colocar outros números
    [5] terminar programa
    ''')
    r = str(input("Qual a sua escolha? "))
    if r == '1':
        soma = n1 + n2
        print("A soma desses números é {}. ".format(soma))
    elif r == '2':
        mul = n1 * n2
        print("A multiplicação desses números é {}.".format(mul))
    elif r == '3':
        lista = [n1, n2]
        if n1 == n2:
            print("Os dois números são iguais.")
        else:
            print("O maior número entre eles dois é {}.".format(max(lista)))
    elif r == '4':
        print("Digite outro(s) número(s)")
        n1 = int(input("Primeiro número: "))
        n2 = int(input("Segundo número: "))
    elif r == '5':
        print("Ok")
        sleep(2)
    else:
        print("Opção inválida, digite novamente.")
    print("-  " * 30)
print("Programa finalizado.")
print("=" * 80)
