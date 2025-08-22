def exibir_menu():

    print('''
**-MENU-**
    
1. Adicionar nova tarefa
2. Vizualizar todas as tarefas
3. Marcar tarefa como concluída
4. Remover tarefa
5. Salvar em um arquivo .txt e sair
6. Sair sem salvar
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

    print('\n--------------------------------------------------')
    print('              LISTA DE TAREFAS')
    print('--------------------------------------------------')

    if not tarefas:
        print('Nenhuma tarefa na lista ainda.')
    else:
        for i, tarefa in enumerate(tarefas):
            print(f"{i+1}. [{tarefa['Status'].upper()}] | {tarefa['Descrição']}")

    print('--------------------------------------------------\n')

def marcar_tarefa(tarefas):

    visualizar_tarefas(tarefas)

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

    visualizar_tarefas(tarefas)

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

def salvar_tarefas(tarefas):
    nome_arquivo = 'tarefas.txt'
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            for i, tarefa in enumerate(tarefas):
                # Escreve cada tarefa em uma linha, separando status e descrição por um caractere
                arquivo.write(f'Tarefa {i+1}: {tarefa['Status']} - {tarefa['Descrição']}\n')
        print(f'\nTarefas salvas com sucesso no arquivo "{nome_arquivo}" !')
    except IOError as e:
        print(f'\nOcorreu um erro ao salvar o arquivo: {e}')

def main():

    print('''
BEM-VINDO AO GERENCIADOR DE TAREFAS!
    
Para iniciar, é necessário adicionar sua primeira tarefa.
Após criá-la, você será direcionado ao menu principal.''')
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
                    escolha = int(input('Escolha uma opção do menu: '))
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
                if not tarefas:
                    print('\nERRO: Sua lista de tarefas está vazia, não existem tarefas a serem vizualizadas!\n')
                else:
                    visualizar_tarefas(tarefas)
            case 3:
                if not tarefas:
                    print('\nERRO: Sua lista de tarefas está vazia, não existem tarefas a serem marcadas!\n')
                else:
                    tarefas = marcar_tarefa(tarefas)
            case 4:
                if not tarefas:
                    print('ERRO: Sua lista de tarefas está vazia, não existem tarefas a serem marcadas! ')
                else:
                    tarefas = remover_tarefa(tarefas)
            case 5:
                salvar_tarefas(tarefas)
                print('Saindo...')
                break
            case 6:
                print('Saindo...')
                break

main()