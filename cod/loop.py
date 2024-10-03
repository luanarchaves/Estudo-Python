listra = [500, 1000, 500, 1500, 2000, 2300]

meta = 1200
porcentualBonus = 0.1

vendas = 1000

for vendas in listra:
    if vendas >= meta:
        bonus = porcentualBonus * vendas
    else:
        bonus=0
    print(bonus)
