email_cliente = 'emailcomum@gmail.com'

#trasformar em letra maiuscula 
email_cliente = email_cliente.upper()
#print(email_cliente)

#trasformar em letra minuscula
email_cliente = email_cliente.lower()
#print(email_cliente)


condição = True
email = (input('Insira seu email: '))

#python ver todas as string como array, então pode se saber um caractere de uma palavra colocando um indice
print(email[-10:])
#todo email depois do @

print(email[:-10])
#mostra todo o texto antes do indice -10 (de tras pra frente), no caso todo o email antes do @

novoEmail = email.replace("gmail.com", "hotmail.com") #trocar uma parte do meu texto
print(novoEmail)

if email.find("@") >= 6:
    condição = True
    print('Email valido')
    print(len(email)) #ler de (lenght), ver quantidade de caractere
else:
    condição = False 
    print('Email invalido')
    print(len(email))

nome = (input('Insira seu nome:'))
print(nome.title())  #deixar a primeira letra de cada palavra em maiusculo 

emailReserva = (input("Email reserva: "))
posição = emailReserva.find("@") + 1 #pegar valor APOS o @
servidor = emailReserva[posição:] #analisar texto após o indice encontrado
print(servidor)
