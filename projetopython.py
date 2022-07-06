#print("Olá mundo!")
'''
a = float(input())
area = 3.14159 * a  ** 2
print("Área do círculo = %.4f "% area)
print("Área do círculo = {:.4f}".format(area))
print(f"Área do círculo =  {area:.4f}")
'''
'''
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))
media =(n1 + n2 + n3 + n4) / 4
if media >= 6.5:
    print('Aprovado!')
if media < 6.5:
    print('Reprovado!')
'''
'''
valor_salario = float(input("Informe o sálario: "))
valor_aumento_porcentagem = float(input("Informe o aumento do sálario: "))
valor_com_reajuste = valor_salario * valor_aumento_porcentagem / 100 + valor_salario
print(f"O valor do sálario com reajuste é R$ {valor_com_reajuste:.2f}")
'''

'''
lista = [1, 2, 3, 4, 5]

for item in lista:
    print(item, end=" ")
'''

'''
sequencia = [1, 2, 3]
for item in sequencia:
    print(item, end=" ")
else:
    print('Todos os items foram exibidos com sucesso')
'''
'''
computador = ['Processador', 'Teclado', 'Mouse']

for item in computador:
    print(item, end= ",")
else:
    print('Todos os items foram exibidos com sucesso')
'''
'''
for caractere in 'Python':
    print(caractere, end=" ")
'''
'''
notas = {
    'Potuguês': 7, 
    'Matemática': 9, 
    'Lógica': 7, 
    'Algoritmo': 7
}

for chave, valor in notas.items():
    print(f"{chave}: {valor}")
    '''
'''
contador = 0

while contador < 10:
    print(f'Valor do contador é {contador}')
    contador += 1
'''
'''
contador = 0

while contador < 10:
    contador += 1
    print(f'Valor do contador é {contador}')    
else:
    print(f'Fim do while e o valor do contador é {contador}')
'''
'''
for num in range(10):
    # Se o número for igual a = 5, devemos parar o loop
    if num == 5:
        # Break faz o loop finalizar
        break
    else:
        print(num, end=" ")
     
   '''
'''
num = 0
while num < 5:
    num += 1

    if num == 3:
        break
        
    print(num)
    '''
'''
lojas = ['Rio de Janeiro', 'São Paulo']

for loja in lojas:
    print(loja)
print("Acabou o For")
'''
'''
# Verificando as variáveis
variavel = "junior"

if variavel.isalpha() == True:
  print("é um texto")
elif variavel.isnumeric() == True:
  print("é um numero")
elif variavel.isalnum() == True:
  print("é uma alpha numerico")
elif variavel.isascii() == True:
  print("é especial")
else:
  print("Formato não reconhecido")
  '''
'''
tabuada=int(input("Tabuada do numero: "))

print("+-"*10)
print("   Tabuada de 10")
print("+-"*10)

for count in range(10):
    print("{ } x { } = { }" % (tabuada, count+1, tabuada*(count+1)) )
'''
'''

soma = 0
num = 0

while soma < 20:
    num = int(input("Informe um múmero: "))
    soma += num
print(f"A soma total é {soma}")
'''
'''
soma = 0

while True:
    num = int(input("Informe um múmero: "))
    soma += num

    if soma > 20:
        break
 '''   

'''
while True:
    num = input("Digite um número: ")
    if num.isnumeric() == True:
        print("Você digitou um número válido: ")
        break
        print("Você não digitou um número válido")
print("Fim!")
'''
'''

while True:
    try:
       n = int(input("Digite um número inteiro: "))
    if n == 0:
    break
soma = soma + n
quantidade = quantidade + 1
print("Quantidade de números digitados:", quantidade)
print("Soma: ", soma)
except:
    print("Erro.")

'''

'''
pedido = ("Pizza", 2, 59.90, True)

print(type(pedido))
print(type(pedido[0]))
print(type(pedido[1]))
print(type(pedido[2]))
print(type(pedido[3]))
'''
'''
# 1. Declare as Tuplas acima
t1 = ('Arroz', 'Feijão', 'Batata')
t2 = (0, 6, 4, 2, 8, 6, 4)
t3 = (1, 3, 3, 5, 3, 5, 7)
'''
'''
# 2. Calcule o tamanho das tuplas: t1 e t2
tamanhoT1 = len(t1)
tamanhoT2 = len(t2)

print(tamanhoT1)
print(tamanhoT2)
'''
'''
# 3. Imprima as tuplas ordenadas: t1 e t2 e depois reimprima-as
t1 = ('Arroz', 'Feijão', 'Batata')
t2 = (0, 6, 4, 2, 8, 6, 4)

print(t1)
print(sorted(t1))
print("-" * 30)
print(t2)
print(sorted(t2))
'''
'''
# 4. Conte quantas vezes aparecem o valor 3 na t3
t3 = (1, 3, 3, 5, 3, 5, 7)
print(t3.count(3))
'''
# Exemplo 1 - Declarando a lista
l1 = [2, 6, 4, 5, 7]
print(l1)
# Substituindo os valores
l1[2] = 3
print(l1)

l1[0:2] = [0,1]
print(l1)




