# ex001 - crie um programa que diga "olá, mundo !"

#texto = 'olá, mundo!'
                        #COM VARIAVEL !
#print(texto)

#--------------------------------------------------------#

#print('Olá, Mundo !')  #SEM VARIAVEL !

#####################################################################################################################################################################

# ex002 - crie um program que de boas vindas ao usuario !

#nome = input('Qual o seu nome completo ?')

#print('seja muito bem vindo ao nosso site', nome)

#--------------------------------------------------------#

#nome = input('qual o seu primeiro nome')

#print('Seja muito bem vindo, {}!'.format(nome))

#####################################################################################################################################################################

# ex003 - Crie um programa que leia dois numeros e mostre a soma entre eles

#num1 = int(input('Digite um valor ...'))
#num2 = int(input('Digite outro valor ...'))
#res = num1+num2

#print('A soma entre {} e {} resulta em {}'.format(num1,num2,res))

#####################################################################################################################################################################

# ex004 - faça um programa que leia algo digitado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele 

#var = input('Digite um valor ...')

#print('O tipo primitivo desse valor é',type(var))
#print('é um numero ?',var.isnumeric())
#print('é alfabetico ?',var.isalpha())
#print('é alfanumerico ?',var.isalnum())
#print('esta em maiusculas ?',var.isupper())
#print('esta em minuscula ?',var.islower())
#print('esta capitalizada ?',var.istitle())
#print('so tem espaços ? ',var.isspace())

#####################################################################################################################################################################

# ex005 - Faça um programa que leia um numero inteiro e mostre na tela seu sucessor e antecessor 

#num1 = int(input('Digite um numero inteiro...'))

#print('o sucessor de {} é'.format(num1),num1+1, end=' ')
#print('e o antecessor de {} é '.format(num1),num1-1)

#n = int(input('Digite um numero inteiro ...'))

#print('Analisando o valor {}, seu antecessor é {} e o seu sucessor é {}'.format(n,n-1,n+1))

#####################################################################################################################################################################

# ex006 - Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada

#n1 = int(input('Digite um numero inteiro'))

#print('o dobro de {} é '.format(n1), n1*2)
#print('o triplo de {} é '.format(n1), n1*3)
#print('a raiz quadrada de {} é'.format(n1), n1**(1/2))

#n1 = int(input('Digite um numero inteiro ...'))
#m1 = n1*2
#m2 = n1*3
#rq = n1**(1/2)

#print('o dobro de {} é {}'.format(n1,m1))
#print('O triplo de {} é {} \ne a raiz quadrada de {} é igual a {:.2f}'.format(n1,m2,n1,rq))

#####################################################################################################################################################################

# ex007 - Desenvolva um program que leia tres notas de um aluno e calcule a sua media 

#tri1 = float(input('Digite sua nota do primeiro trimestre ...'))
#tri2 = float(input('Digite a nota do segundo trimeste ...'))
#tri3 = float(input('Digite a nota do terceiro trimestre ...'))

#rint('A média do aluno é {:.1f} '.format((tri1+tri2)/3))

#####################################################################################################################################################################

# ex008 - Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

#metro = float(input('Digite quantos metros você pretende converter ...'))
#dcm = metro*10
#cm = metro*100
#mm = metro*1000
#km = metro/1000
#hm = metro/100
#dam = metro/10


#print('A medida {} metros correponde a \n {:.0f} decametros\n{:.0f} centimetros\n{:.0f} milimetros\n{} kilometros\n{} hm \n{} dam'.format(metro,dcm,cm,mm,km,hm,dam))


#####################################################################################################################################################################

# ex009 - faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada

#n1 = int(input('Digite um numero inteiro qualquer ...'))

#print('a tabuada de {} é '.format(n1))
#print('{} x  1 ='.format(n1),n1*1)
#print('{} x  2 ='.format(n1),n1*2)
#print('{} x  3 ='.format(n1),n1*3)
#print('{} x  4 ='.format(n1),n1*4)
#print('{} x  5 ='.format(n1),n1*5)
#print('{} x  6 ='.format(n1),n1*6)
#print('{} x  7 ='.format(n1),n1*7)
#print('{} x  8 ='.format(n1),n1*8)
#print('{} x  9 ='.format(n1),n1*9)
#print('{} x 10 ='.format(n1),n1*10)

#####################################################################################################################################################################

# ex010 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar considerando o dolar atual 

#cart = float(input('Quantos reais você tem com você para que eu possa converter ?'))

#print('Como você disse que possui nesse momento R$ {} você podera comprar {:.2f} doláres'.format(cart,cart/5.57))  

#####################################################################################################################################################################

# ex011 - Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua area e a quantidadde de tinta necessaria para pinta-la. sabendo que cada litro de tinta pinta uma area de 2m²

#base = float(input('Digite o valor da base ...'))
#altura = float(input('Digite o valor da altura ...'))
#area = base*altura

#print('Como a base da sua parede é {}m e a altura é {}m a area sera {}m²'.format(base,altura,area))
#print('Sabendo que a area é {}m² você precisara de'.format(area), area/2, 'litros de tinta')


#####################################################################################################################################################################

# ex012 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

#preço = float(input('Digite um valor ...'))
#npreço = preço*(5/100)
#desc = preço-npreço

#print('este produto com 5% de desconto sai por R${:.2f} '.format(desc))

#preço = float(input('Digite o valor do produto ...'))
#desconto = preço - (preço*5/100)

#print('R${:.2f} com 5% de desconto sai por R${:.2f}'.format(preço,desconto))
#####################################################################################################################################################################

# ex013 - Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento

#salario = float(input('Digite o seu salario ...'))
#salaumt = salario*(15/100)
#aument = salario+salaumt

#print('Seu novo salario agora é R${:.2f}'.format(aument))

#salario = float(input('Digite seu salário ...'))
#aumento = salario + (salario*15/100)

#print('Com o aumento de 15% seu salário agora é R${:.2f}'.format(aumento))

#####################################################################################################################################################################

# ex014 - Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit(35 °C × 9/5) + 32 = 95 °F


#celsius = float(input('Digite a temperatura em graus Celsius ...'))
#fahrenheit = (celsius * 9/5) + 32

#print('{} C° é igual {} F°'.format(celsius,fahrenheit))

#fahrenheit = float(input('Digite a temperatura em fahrenheit ...'))
#celsius = ((fahrenheit - 32)*5/9)

#print('{} F°  é igual {} C°'.format(fahrenheit,celsius))


#####################################################################################################################################################################

# ex015 -  Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

#dias = int(input('Quantos dias você ficou com o carro ?'))
#kmp = float(input('Quantos kilometros você rodou com o carro ?'))
#total = (dias*60) + (kmp*0.15)

#print('Como você utilizou o carro por {} dias e rodou {:.2f} km o total a pagar será R${:.2f}'.format(dias,kmp,total))

#####################################################################################################################################################################

# ex016 -  Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porção inteira

#import  math
#num = float(input('Digite um numero qualquer ...'))
#int = math.floor(num)

#print('O numero {} tem a parte inteira {}'.format(num,int))

#import math 
#real= float(input('Digite um numero real ...'))
#inteiro = math.trunc(real)

#print('O numero real {} tem a parte inteira {}'.format(real,inteiro))

#from math import trunc
#real = float(input('Digite um numero real ...'))
#inteiro = trunc(real)

##print('O numero real {} tem a parte inteira {}'.format(real,inteiro))'''

#from math import trunc

#num = float(input('Digite um numero Real ...'))
#print('O numero {} tem a sua parte inteira {}'.format(num,trunc(num)))

#####################################################################################################################################################################

# ex017 -  Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e moste o comprimento da hipotenusa

#from math import hypot

#x = float(input('Digite o valor do cateto oposto ...'))
#y = float(input('Digite o valor do cateto adjacente ...'))

#print('Sendo o cateto oposto {} e o adjacente {} a hipotenusa é {:.2f}'.format(x,y,hypot(x,y)))


#####################################################################################################################################################################

# ex018 -  Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo  

#import math

#ang = int(input('Digite um ângulo qualquer ...'))
#seno = math.sin(ang)
#cos = math.cos(ang)
#tan = math.tan(ang)

#print('O ângulo digitado foi {}° sendo assim o seno desse ângulo é {}, o cosseno é {} e a tangente é {} ...'.format(ang,seno,cos,tan))

#from math import sin,cos,tan,radians

#ang = float(input('Digite um ângulo qualquer ...'))

#print('O ângulo digitado foi {}° sendo assim o seno desse ângulo é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f} ...'.format(ang,sin(radians(ang)),cos(radians(ang)),tan(radians(ang))))

#####################################################################################################################################################################

# ex019 -  faça um programa que leia o nome de quatro alunos e escolha um deles para ajudar o professor 

#from random import choice 

#aluno1 = input('Digite o nome do primeiro aluno ...')
#aluno2 = input('Digite o nome do segundo aluno ....')
#aluno3 = input('Digite o nome do terceiro aluno ...')
#aluno4 = input('Digite o nome do quarto aluno ...')
#escolhido = choice([aluno1,aluno2,aluno3,aluno4])

#print('Na lista de alunos o escolhido foi {}'.format(escolhido))

#####################################################################################################################################################################

# ex020 -  O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

#from random import sample

#a1 = str(input('Digite o nome do primeiro aluno ...'))
#a2 = str(input('Digite o nome do segundo aluno ...'))
#a3 = str(input('Digite o nome do terceiro aluno ...'))
#a4 = str(input('Digite o nome do quarto aluno ...'))
#seq = sample([a1,a2,a3,a4], k=4)

#print('A ordem de apresentação escolhida foi {}'.format(seq))

#from random import shuffle

#a1 = str(input('Digite o nome do primeiro aluno ...'))
#a2 = str(input('Digite o nome do segundo aluno ...'))
#a3 = str(input('Digite o nome do terceiro aluno ...'))
#a4 = str(input('Digite o nome do quarto aluno ...'))
#sorteio = [a1,a2,a3,a4]
#shuffle(sorteio)

#print('A ordem de aprensentação sera {}'.format(sorteio))

#####################################################################################################################################################################

# ex021 -  Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

#import pygame
#pygame.init()
#pygame.mixer.music.load('ex21r.mp3')
#pygame.mixer.music.play()
#pygame.event.wait()

#####################################################################################################################################################################

# ex022 -   

#####################################################################################################################################################################

# ex023 -  

#####################################################################################################################################################################

# ex024 -  

#####################################################################################################################################################################

# ex025 -  

#####################################################################################################################################################################

# ex026 -  

