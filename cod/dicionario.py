listraPorudtos = ['airpode', 'ipad', 'iphone', 'macbook']
precos = [2000, 9000, 6000, 11000]
#no dicionario só pode ter 1 elemento com a mesma chave

dic_produtos = {'airpode': 2000, 'ipad': 9000} 
#dicionario, une informações de duas listras em uma

print(dic_produtos['airpode']) 
#o indice do dicionario é o nome do rotulo(chave)

dic_produtos['airpode'] = int(dic_produtos['airpode'] * 1.3)
print(dic_produtos)

print(len(dic_produtos))

#dic_produtos.pop('airpode') #o indice do dicionario é a chave
#print(dic_produtos)

dic_produtos['apple watch'] = 2500 #adicionar novo elemento
print(dic_produtos)

if 9000 in dic_produtos.values():
    print('existe')
else:
    print('não existe')

#nomeProduto = input('nome do produto')
#precoProduto = float(input('preço do produto'))

#nomeProduto = nomeProduto.lower()

#dic_produtos[nomeProduto] = precoProduto
#print(dic_produtos)


produto = 'ipad'
print(dic_produtos)

#automaticamente a variavel 'item' se refere a chave do dicionario
for item in dic_produtos:  
    novoPreco = int(dic_produtos[produto] * 1.1)
    dic_produtos[produto] = novoPreco

print(dic_produtos)
