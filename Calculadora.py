op = 'x'
while op != '0':
    print('Soma .................. +')
    print('Subtração ............. -')
    print('Multiplicação...........*')
    print('Divisão................./')
    print('Sair ...................0')

    op = input()
    if op != '0':
        print('Digite 2 números: ')
        n1 = float (input())
        n2 = float (input())
        if op == '+':
            print(f'Soma = {n1+n2}')
        elif op == '-':
            print(f'Subtração = {n1-n2}')
        elif op == '*':
            print(f'Multiplicação = {n1*n2}')
        elif op == '/':
            if n2 != 0:
                print(f'Divisão = {n1/n2}')
            else:
                print('Não há divisão por zero')
