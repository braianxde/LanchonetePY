#!/usr/bin/python
#coding: utf-8


terminou = 0
subvalor = 0


while (terminou == 0):
	print "\nInforme o código da opção desejada para lanches: "
	print "Codigo  |  Nome            |  Valor \n 1      |  Xis Carne       |  R$12,00 \n 2      |  Xis Salada      |  R$13,00 \n 3      |  Xis Calabresa   |  R$16,00 \n 0      |  Sair  do menu Lanches \n"
	inputEscolha = raw_input()

	if(inputEscolha == "1"):
		subvalor += 12.0
	elif(inputEscolha == "2"):
		subvalor += 13.0
	elif(inputEscolha == "3"):
		subvalor += 16.0
	elif(inputEscolha == "0"):
		terminou = 1
		break
	else:
		print "\nOpção inválida\n"
		

	print "\nTu desejas sair do menu de lanche? (sim ou nao)"
	inputSair = raw_input()

	if(inputSair.lower() == "sim"):
		terminou = 1



terminou = 0;

while (terminou == 0):
	print "\nInforme o código da opção desejada para bebidas: "
	print "Codigo |  Nome   |  Valor \n 1     |  Coca   |  R$5,50 \n 2     |  Fanta  |  R$4,00 \n 3     |  Pepsi  |  R$5,00 \n 0     |  Sair do menu de Bebidas\n"
	inputEscolha = raw_input()

	if(inputEscolha == "1"):
		subvalor += 5.5
	elif(inputEscolha == "2"):
		subvalor += 4.0
	elif(inputEscolha == "3"):
		subvalor += 5.0
	elif(inputEscolha == "0"):
		terminou = 1
		break
	else:
		print "\nOpção inválida\n"

	print "\nTu desejas sair do menu de bebidas? (sim ou nao)"
	inputSair = raw_input()

	if(inputSair.lower() == "sim"):
		terminou = 1

print "O valor total do seu pedido foi ", subvalor;

