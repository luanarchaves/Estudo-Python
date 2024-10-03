import os
from tkinter.filedialog import askdirectory 

nome_pasta = askdirectory()
print(nome_pasta)

listra_arquivos = os.listdir(nome_pasta)
print(listra_arquivos)