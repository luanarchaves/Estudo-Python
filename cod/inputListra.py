
vendas = [100, 50, 14, 20, 30, 700]

totalVendas = sum(vendas)
#somar todos elementos da listra
print(totalVendas)

quantidadeVendas = len(vendas)
#ver quantidade de elementos
print(quantidadeVendas)

print(max(vendas)) #ver maior valor da listra
print(min(vendas)) #ver menor valor da listra

print(vendas[1])
print(vendas[-1]) #ultimo valor

listraProduto = ['iphone', 'airpode', 'ipad', 'macbook', 'iphone', 'airpode', 'ipad', 'macbook']

produto_procurado = input("Qual produto esta procurando? ")

print(produto_procurado.lower() in listraProduto) #se nao tiver é false e se tiver é true

newProduct = input('Qual valor adicionar a listra? ')
listraProduto.append(newProduct) #colocando novo elemento na listra

listraProduto.remove('iphone') #remover elemento da listra
listraProduto.pop(2) #remover elemento indice 2
listraProduto.sort() #ordena a listra em ordem alfabetica

print(listraProduto)