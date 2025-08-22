def exibir_menu():

    print('''
**-MENU-**
    
1. Adicionar nova tarefa
2. Vizualizar todas as tarefas
3. Marcar tarefa como concluída
4. Remover tarefa
5. Sair
    ''')

def adicionar_tarefa():

    ds_tarefa = input('\nDigite a descrição da tarefa a ser adicionada: ')
    status_tarefa = 'Pendente'

    tarefa = {
        'Descrição':ds_tarefa,
        'Status': status_tarefa
    }

    print('\nTarefa adicionada com sucesso!')

    return(tarefa)

def visualizar_tarefas(tarefas):

    print('\n--------------------------------------------------------------------------------')
    print('LISTA DE TAREFAS')
    # Laço para exibir as tarefas
    i = 1
    while i <= len(tarefas):
        print(f'{i}. [{(tarefas[i-1]['Status']).upper()}] {tarefas[i-1]['Descrição']}')
        i+=1
    print('\n--------------------------------------------------------------------------------')

def marcar_tarefa(tarefas):

    print('\n--------------------------------------------------------------------------------')
    print('LISTA DE TAREFAS')
    # Laço para exibir as tarefas
    i = 1
    while i <= len(tarefas):
        print(f'{i}. [{(tarefas[i-1]['Status']).upper()}] {tarefas[i-1]['Descrição']}')
        i += 1
    print('\n--------------------------------------------------------------------------------')


    while True:

        # Laço que valida a escolha do menu sem ValueError
        while True:
            try:
                opcao = int(input('\nDigite o número da terfa que deseja marcar como concluída: '))
            except ValueError:
                print('Opção inválida, tente novamente.')
            else:
                break

        # Verifica se a tarefa existe
        # Se existir, break
        if opcao < 1 or opcao > len(tarefas):
            print(f'A tarefa de número {opcao} não existe! Tente novamente.')
        else:
            break

    tarefas[opcao-1]['Status'] = 'Concluída'

    print('\nTarefa marcada como concluída com sucesso!')

    return tarefas

def remover_tarefa(tarefas):

    print('\n--------------------------------------------------------------------------------')
    print('LISTA DE TAREFAS')
    #Laço para exibir as tarefas
    i = 1
    while i <= len(tarefas):
        print(f'{i}. [{(tarefas[i-1]['Status']).upper()}] {tarefas[i-1]['Descrição']}')
        i += 1
    print('\n--------------------------------------------------------------------------------')


    while True:

        # Laço que valida a escolha do menu sem ValueError
        while True:
            try:
                opcao = int(input('\nDigite o número da tarefa que deseja remover: '))
            except ValueError:
                print('Opção inválida, tente novamente.')
            else:
                break


        # Verifica se a tarefa existe
        # Se existir, break
        if opcao < 1 or opcao > len(tarefas):
            print(f'A tarefa de número {opcao} não existe! Tente novamente.')
        else:
            break

    print('\nTarefa removida com sucesso!')

    tarefas.pop(opcao-1)

    return tarefas

def main():

    print('''
BEM-VINDO AO GERENCIADOR DE TAREFAS!
    
Para iniciar, é necessário adicionar sua primeira tarefa.
Após criá-la, você será direcionado ao menu principal.
    ''')
    # Começa o programa criando uma primeira tarefa
    tarefas = []
    tarefa = adicionar_tarefa()

    tarefas.append(tarefa)

    while True:
        # Exibe o menu de opções
        exibir_menu()

        # Laço para a escolha do menu
        while True:

            # Laço que valida a escolha do menu sem ValueError
            while True:
                try:
                    escolha = int(input('\nEscolha uma opção do menu: '))
                except ValueError:
                    print('Opção inválida, tente novamente.')
                else:
                    break

            if escolha > 5 or escolha < 1:
                print('Opção inválida, tente novamente.')
            else:
                break

        match escolha:
            case 1:
                tarefa = adicionar_tarefa()
                tarefas.append(tarefa)
            case 2:
                visualizar_tarefas(tarefas)
            case 3:
                tarefas = marcar_tarefa(tarefas)
            case 4:
                tarefas = remover_tarefa(tarefas)
            case 5:
                break

main()