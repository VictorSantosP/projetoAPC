'''salario, taxa = map(float, input(). split())
aumento = (salario * (1 + taxa/100)) - salario
salario += aumento

print(salario, aumento)'''

'''dist, velm = map(float, input().split())
tempo = dist/velm
print(tempo)'''

'''c = float(input())
f = (9 * c) / 5 + 32
print(f)'''
'''a, b = map(int, input().split())
if a > b:
    print('O primeiro número é maior!')
if b > a: 
    print('O segundo número é maior!')'''

'''vel = float(input())
multa = 0
if vel > 80:
    exc = vel - 80
    multa = exc * 5
print(multa) '''

################################# Código importante ##########################################
'''
salario = float(input())
base = salario
imposto = 0
if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35)
    base = 3000
if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)
    
print(f'Salário: {salario} Imposto a pagar: {imposto}') '''
#########################################################################################

'''a, b, c = map(int, input().split())
maior = 0
menor = 0
if a > b and a > c and b < c:
    maior = a
    menor = b
elif b > a and b > c and c < a:
    maior = b
    menor = c
elif c > a and c > b and a < b:
    maior = c
    menor = a
elif c > a and c > b and b < a:
    maior = c
    menor = b
else:
    maior = b
    menor = a

print(maior, menor)'''

'''dist = float(input())
if dist <= 200:
    preco = dist * 0.5
else:
    preco = dist * 0.45

print(preco)'''

'''num1, num2 = map(float, input().split())
ope = input()
if ope == '+':
    print(num1 + num2)
elif ope == '-':
    print(num1 - num2)
elif ope == '*':
    print(num1 * num2)
elif ope == '/':
    print(num1 / num2) '''

'''pcasa, salario = map(float, input().split())
anos = int(input())
meses = anos * 12
prest = pcasa / meses
salarioperm = salario * 0.3
if prest > salarioperm:
    print('Não aprovado, prestação superior a 30 por cento do salário')
else:
    print('Aprovado')'''

'''energia = float(input())
inst = input()
vf = 0
if inst == 'R':
    if energia <= 500:
        preco = 0.4
        vf = energia * preco
    else:
        preco = 0.65
        vf = energia * preco

elif inst == 'C':
    if energia <= 1000:
        preco = 0.55
        vf = energia * preco
    else:
        preco = 0.6
        vf = energia * preco
elif inst == 'I':
    if energia <= 5000:
        preco = 0.55
        vf = energia * preco
    else:
        preco = 0.6
        vf = energia * preco
    
print(vf)'''

'''x = 10
while x >= 0:
    print(x, end=' ')
    if x == 0:
        print('e Fogo!')
    x -= 1'''

'''dep = float(input())
taxa = float(input())
dep_mensal = float(input())
x = 0
soma = dep
juros = 0
while x < 24:
    soma *= (1 + taxa / 100)
    soma += dep_mensal
    print(f'{soma:.2f}')
    
    x += 1
juros = soma - dep - (dep_mensal * 24)
print(f'{juros:.2f}')
'''
'''divida_inicial = float(input("Digite o valor da dívida inicial: "))
juros_mensal = float(input("Digite a taxa de juros mensal (em %): "))
pagamento_mensal = float(input("Digite o valor do pagamento mensal: "))
adevolver = 0
# Inicialização das variáveis
saldo_devedor = divida_inicial
total_pago = 0
total_juros = 0
meses = 0

# Loop para calcular a dívida mês a mês
while saldo_devedor > 0:
    meses += 1  # Incrementa o contador de meses

    # Calcula os juros do mês sobre o saldo devedor
    juros = saldo_devedor * (juros_mensal / 100)
    total_juros += juros  # Acumula o total de juros

    # Atualiza o saldo devedor: aplica juros e subtrai o pagamento mensal
    saldo_devedor = saldo_devedor + juros - pagamento_mensal

    # Se o saldo devedor for menor que zero, ajusta para zero (dívida quitada)
    if saldo_devedor <= 0:
        saldo_devedor = 0

    # Acumula o total pago
    total_pago += pagamento_mensal
ardevolve = total_pago - total_juros - divida_inicial
# Exibe os resultados finais

print(f"Numero de meses para quitar a dívida: {meses}")
print(f"Total pago: R$ {total_pago:.2f}")
print(f"Total de juros pagos: R$ {total_juros:.2f}")
print(f'Valor a ser devolvido: R$ {adevolver:.2f}')  '''     

'''n = 1
cont = 0
soma = 0
while n != 0:
    cont +=1
    n = int(input())
    soma += n
print(soma)
print(soma / (cont-1))'''

'''codigo = 1
preco = 0
soma = 0
while True:
    codigo = int(input())
    if codigo == 0:
        break
    qnt = int(input())
    if codigo != 1 and codigo != 2 and codigo != 3 and codigo != 5 and codigo != 9 and codigo != 0:
        print('Código inválido.')
    if codigo == 1:
        preco = 0.50
        soma += preco * qnt
    elif codigo == 2:
        preco = 1.00
        soma += preco * qnt
    elif codigo == 3:
        preco = 4.00
        soma += preco * qnt
    elif codigo == 5:
        preco = 7.00
        soma += preco * qnt
    elif codigo == 9:
        preco = 8.00
        soma += preco * qnt
print(f'soma:.2f')'''
################################# REVISAR AMANHÃ #############################################
'''valor = int(input('Digite o valor a pagar: '))
cedulas = 0
atual = 50
apagar = valor
while True:                         ###Entendi###
    if atual <= apagar:
        apagar -= atual
        cedulas += 1
    else:
        print(f'{cedulas} cédula(s) de R$ {atual}')
        if apagar == 0:
            break
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        cedulas = 0'''

#############################################################################################

'''tabuada = 1
while tabuada <= 10:
    numero = 1
    while numero <= 10:
        print(f'{tabuada} x {numero} = {tabuada * numero}')
        numero += 1
    tabuada += 1'''

'''n = int(input())
i = 2
cont = 0
while cont < n:
    j = 2
    if i % j == 0:
        j += 1
    else:
        print(i)
        cont += 1
    i += 1'''

'''n = int(input())
p = 1
b = 2
while abs(p ** 2 - n) > 0.0001:
    p = (b +(n/b))/2
    b = p
print(p)'''

'''a, b = map(int, input().split())
soma = 0
while True:
    if soma > a:
        soma -= b
        break
    else:
        soma += b

dif = a - soma
print(dif)'''

'''n = input()
i = 0
j = len(n)
dif = 0
while i < len(n) // 2:
    if n[i] != n[j-1]:
        dif += 1
    j -= 1
    i += 1
if dif > 0:
    print('Não é palíndromo')
else:
    print('É palíndromo')'''
'''menu = ''
while menu != 'sair':
    menu = input('adição, subtração, divisão, multiplicação e sair: ')
    if menu == 'multiplicação':
        tabuada = 1
        while tabuada <= 10:
            numero = 1
            while numero <= 10:
                print(f'{tabuada} x {numero} = {tabuada * numero}')
                numero += 1
            tabuada += 1
    elif menu == 'divisão':
        tabuada = 10
        while tabuada >= 1:
            numero = 10
            while numero >=1:
                print(f'{tabuada} / {numero} = {tabuada * numero}')
                numero -= 1 
            tabuada -= 1'''

