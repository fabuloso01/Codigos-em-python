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

'''
# Exemplo 1 - Declarando a lista
l1 = [2, 6, 4, 5, 7]
print(l1)
# Substituindo os valores
l1[2] = 3
print(l1)

l1[0:2] = [0,1]
print(l1)
'''
'''
Dada as listas e tuplas abaixo:
preco = (10.9, 5.40, 8.30, 3.40)
qtdComprada = [0, 3, 2, 4]
Calcule e mostre para o usuário o valor total da compra dele sendo que
o valor total será a soma da multiplicação do preço do produto pela quantidade comprada.
'''


'''
preco = (10.9, 5.40, 8.30, 3.40)
qtdComprada = [0, 3, 2, 4]

preco = (10.9, 5.40, 8.30, 3.40)
lista = sum(preco)
print(f" O valor total do preço da compra é R$ {lista:.2f}")


qtdComprada = [0, 3, 2, 4]
lista = sum(qtdComprada)
print(f" O valor total do quantidade de compra é R$ {lista:.2f}")

total = somar*lista

print(f" O valor total da compra é R$ {total:.2f}")
'''
'''
#Exercício 1 - Declarando dicionário
cardapio = {"X-Tudo" : 10.9,
            "Batata" : 5.5,
            "Refri" : 3.9}
# 1. Mostrando cardápio:
print("=" * 35)
print(" " * 12, "CARDÁPIO")
print("=" * 35)
for lanche, valor in cardapio.items():
  print(f"{lanche:.<25} R${valor:.2f}")
print("=" * 35)

# 2. Pergunta e Calcula:
qtd = {}
subTotal = {}
total = 0

for chave, valor in cardapio.items():
  qtd[chave] = int(input(f"Quantos {chave} você quer? "))
  subTotal[chave] = cardapio[chave] * qtd[chave]
  total += subTotal[chave]
#print(qtd)
#print(subTotal)
#print(f"{total:.2f}")

# 3. Recibo
print("=" * 35)
print(" " * 12, "RECIBO")
print("=" * 35)
for chave, valor in qtd.items():
  print(f"[{qtd[chave]}] R${chave:.<22} {subTotal[chave]:.2f}")
print(f"TOTAL A PAGAR:............. R${total:.2f}")
print("=" * 35)

'''
'''
#Exemplo 1 - Lista:

#Dicionário equivalente.

lista = ['Fulano', 40, 'Minas Gerais']
dicio = {'nome': 'Fulano', 
        'idade': 40, 
       'cidade': 'Minas Gerais'}
print(lista)
print(dicio)
print(dicio.values())
print(dicio.keys())
'''
'''
#Exemplo 2 - Declarando dicionários

# Imprimindo
dic1 = {}
dic2 = dict()
dic3 = {
      'key1' : 'value1',
      'key2' : 'value2',
      'key3' : 'value3'
     }

print(dic1)
print(dic2)
print(dic3)
'''
'''
#Exemplo 3 - Declarando dicionário:

# Acessando os valores:

pessoa = {"nome"  : "Fulano",
          "idade" :  40, 
          "cidade": "Minas Gerais"}
print(dicio.values())
'''
'''
#Exemplo 3 - Declarando dicionário:
pessoas = {"nome"  : "Fulano",
          "idade" :  40, 
          "cidade": "Minas Gerais"}
# Acessando os valores:
print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
print(pessoas['cidade'])
'''

'''
#Exemplo 4 - Modificando o valor:

# Imprimindo valores:
pessoas = {"nome"  : "Fulano",
          "idade" :  40, 
          "cidade": "Minas Gerais"}

pessoas["cidade"] = 'São Paulo'

print(pessoas)
'''
'''
#Exemplo 5 - Criando uma chave:

# Imprimindo valores:
pessoas = {"nome"  : "Fulano",
          "idade" :  40, 
          "cidade": "Minas Gerais"}
pessoas["peso"] = 65

print(pessoas)
'''
'''
#Exemplo 6 - Criando uma chave:
 
# Imprimindo valores:
pessoas = {"nome"  : "Fulano",
          "idade" :  40, 
          "cidade": "Minas Gerais"}

pessoas["Cidade"] = 'São Paulo'

print(pessoas)
'''
'''
#Exemplo 7 - Deletando uma chave:
pessoas = {"nome"  : "Fulano",
          "idade" :  40, 
          "cidade": "Minas Gerais"}

pessoas["cidade"] = 'São Paulo'
del pessoas["cidade"] 

print(pessoas)
'''
'''
#Exemplo 8 - Imprimindo valores
dicio = {"nome"  : "Fulano",
          "idade" :  40, 
          "cidade": "Minas Gerais"}
print(dicio)          #dicionário completo
print(dicio.values())  #somente os valores do dicionário
print(dicio.keys())   #somente as chaves do dicionário
print(dicio.items())
'''
'''
#Exemplo 9 - Imprimindo valores
pessoas = {"nome"  : "Fulano",
          "idade" :  40, 
          "cidade": "Minas Gerais"}
for valor in pessoa.values():
  print(valor)

'''
'''
#Exemplo 10 - Imprimindo chaves
pessoas = {"nome"  : "Fulano",
          "idade" :  40, 
          "cidade": "Minas Gerais"}
for valor in pessoa.keys():
  print(valor)
'''
'''
#Exemplo 11 - Imprimindo chaves e valores
pessoas = {"nome"  : "Fulano",
          "idade" :  40, 
          "cidade": "Minas Gerais"}

for chave, valor in pessoas.items():
  print(chave, valor)
'''
'''
# math
import math
print(math.factorial(5))
print(math.sqrt(49))

from math import sqrt
print(sqrt(49))

from math import sqrt as raiz
print(raiz(49))
*/

'''
'''
# Area de um circulo
from math import pi

raio = 4

area = pi * (raio * raio)

print(area)
'''
'''
# datetime
import datetime

datetime.date.today()
print(datetime.date.today())
print(datetime.date.today().day)
print(datetime.date.today().month)
print(datetime.date.today().year)
'''
'''
# from datetime
from datetime import date
dia = date.today().day
mes = date.today().month
ano = date.today().year
print(f"{dia}/{mes}/{ano}")
'''



