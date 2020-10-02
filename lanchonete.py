#!/usr/bin/python
#coding: utf-8

lanches = [
	[
		"1",
		"Xis Carne",
		12.5
	],
	[
		"2",
		"Xis Salada",
		11.0
	],
	[
		"3",
		"Cachorro Quente",
		14.5
	]
];

bebidas = [
	[
		"1",
		"Coca Cola 600ml",
		6.0
	],
	[
		"2",
		"Fanta Laranja",
		5.0
	],
	[
		"3",
		"Agua",
		4.0
	]
];

pedidos = [];

def adicionaPedido( arrayUsado, opcaoSelecionada ):
	adicionou = 0;
	achouProduto = 0;
	for arrayU in arrayUsado:

		if(arrayU[0] == opcaoSelecionada):
			achouProduto = 1;
			for pedido in pedidos:
				if(pedido[1] == arrayU[1]):
					pedido[0] += 1
					adicionou = 1

			if(adicionou == 0):

				pedidos.append([1,arrayU[1],arrayU[2]])

	if(achouProduto == 0):
		print "Informe um produto valido!"

	return ;

terminou = 0;
print "Informe o codigo da opcao desejada para lanches:"
while (terminou != 1):	

	for lanche in lanches: 

		print "Codigo: ",lanche[0]," | ",lanche[1]," - R$ ",lanche[2]

	inputUser = raw_input();

	adicionaPedido(lanches, inputUser);
	
	print "Voce gostaria de selecionar algum lanche (S / N)?"
	inputUser = raw_input()

	if(inputUser == "N" or inputUser == "n"):
		terminou = 1

terminou = 0;
print "Informe o codigo da opcao desejada para bebidas:"
while (terminou != 1):	

	for bebida in bebidas: 

		print "Codigo: ",bebida[0]," | ",bebida[1]," - R$ ",bebida[2]

	inputUser = raw_input();

	adicionaPedido(bebidas, inputUser);
	
	print "Voce gostaria de selecionar alguma bebida (S / N)?"
	inputUser = raw_input()

	if(inputUser == "N" or inputUser == "n"):
		terminou = 1


print "Segue o seu pedido:"
valorTotalPedido = 0;

for pedido in pedidos:
	valorParc = pedido[2]*pedido[0]
	valorTotalPedido += valorParc
	print pedido[0],"x " + pedido[1].ljust(20) + " Valor Unitario: R$", pedido[2] , " Total: R$", valorParc

print "Valor total do pedido: R$", valorTotalPedido

