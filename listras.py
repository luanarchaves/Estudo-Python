# Atividade: Criar um sistema de registro de alunos que armazene nome, idade e nota de cada aluno em um dicionário e calcule a média da turma.

def CalcularNota(media, i, alunos):

    nome = str(input('Qual o nome completo do aluno?'))
    idade = int(input('Qual a idade do aluno?'))
    nota = float(input('Qual a nota do aluno?'))

    media[0] += nota

    if len(nome.split()) <= 1 or idade < 15 or nota > 10:
        print('\nAlguma informação foi inserida incorretamente, tente novamente')
        return 

    i += 1
    media[1] = i

    alunos['Nome_Aluno' + str(i)] = nome
    alunos['Idade_Aluno' + str(i)] = idade
    alunos['Nota_Aluno' + str(i)] = nota
    
    print(alunos)

    return media, i


media = [0, 0]
alunos = {}
i = 0

while True:
    print('\nRegistrador de alunos Ensino Médio\n')
    print('Deseja registrar um aluno?')
    option = input('Digite 1 - Sim\nDigite 2 - Não\n')

    if option == '1':
        media, i = CalcularNota(media, i, alunos)
        print(media)
        print(f'Média dos alunos: {media[0]/media[1]}')
    else:
        break


    
    

