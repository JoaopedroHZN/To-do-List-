def menu():
    while True:
        print("\n=== TO-DO LIST MONGODB ===")
        print("1. Adicionar Tarefa")
        print("2. Listar Todas")
        print("3. Buscar (Status ou Tags)")
        print("4. Atualizar Tarefa")
        print("5. Adicionar Comentário")
        print("6. Excluir Tarefa")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            criar_tarefa()
        elif opcao == '2':
            listar_tarefas()
        elif opcao == '3':
            buscar_avancada()
        elif opcao == '4':
            atualizar_tarefa()
        elif opcao == '5':
            adicionar_comentario()
        elif opcao == '6':
            excluir_tarefa()
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

