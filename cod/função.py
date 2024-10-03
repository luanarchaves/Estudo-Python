listraProd = [1500, 1000, 800, 3000]

def calcularImposto(preco):

    if preco <= 2000:
        impostoIr = 0.2 * preco
    else:
        impostoIr = 0.3 * preco
    importoIss = 0.15 * preco
    impostoCsll = 0.05 * preco
    impostoTotal = impostoIr + impostoCsll + importoIss
    return impostoTotal


for preco in listraProd:

    impostoTotal = calcularImposto(preco)
    print(impostoTotal)


#o loop for em py nãp tem a sintaze normal, e não tem o <= ou >=, se quiser ver
#ver o numero até 100 tem que escrever 101.

for i in range(2, 102, 2):
    print(i)

#função definida
def soma(a, b):
    return a + b  

print(soma(15, 17))  