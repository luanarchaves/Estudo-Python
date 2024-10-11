# with open("C:\\Users\\chave\\OneDrive\\Documentos\\3 - PYTHON\\Estudo-Python\\arquivos\\info.txt", "r", encoding="utf-8") as arquivo:
#     mensagem = arquivo.readlines()

# for linha in mensagem:
#     if 'e' in linha:
#         print(linha)

with open("C:\\Users\\chave\\OneDrive\\Documentos\\3 - PYTHON\\Estudo-Python\\arquivos\\novo.info.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write('sem mais perguntas')
