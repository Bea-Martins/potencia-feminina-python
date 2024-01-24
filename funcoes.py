# FUNÇÕES - aula 02

def soma(): # definição da função soma
	cálculo = 10 + 2
	print(f'O resultado da soma é: {cálculo}')

def subtracao(): 
	sub = 10 - 2
	print(f'O resultado da subtração é: {sub}')
	multiplicacao() # chamada a função dentro de uma função

def multiplicacao(): 
	mult = 10 * 2
	print(f'O resultado da multiplicação é: {mult}') 

soma() # chamada da função
subtracao()


# FUNÇÕES - aula 03

def soma(num1,num2): 
	cálculo = num1 + num2
	print(f'O resultado da soma é: {cálculo}')

def subtracao(num1,num2): 
	sub = num1 - num2
	print(f'O resultado da subtração é: {sub}')

def multiplicacao(num1,num2): 
	mult = num1 * num2
	print(f'O resultado da multiplicação é: {mult}') 

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

soma(num1,num2)
subtracao(num1,num2)
multiplicacao(num1,num2)


# FUNÇÕES - aula 04, 05 e 06

file = 'arquivo.txt'

# Abertura de arquivo

# open somente para escrita
arquivo_escrita = open(file,'w')
arquivo_escrita.write('Texto a ser escrito') # logo após open
leitura = arquivo_escrita.read() # erro
arquivo_escrita.close() # sempre fechar após abrir


# open somente para leitura
arquivo_leitura = open(file,'r') 
arquivo_leitura.write('Texto a ser escrito') # erro
leitura = arquivo_escrita.read() # OK após abrir o file
print(leitura)
arquivo_leitura.close()

# open arquivos binários
arquivo_binario = open(file,'wb')


# FUNÇÕES - aula 07

def divisao(a,b):
	try:
		resultado = a/b
		print(resultado)
	except ZeroDivisionError:
		print('Erro: Impossível dividir um valor por 0')

divisao(10,0) # erro