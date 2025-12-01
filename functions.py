from datetime import date

def menu(colecao):
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
            criar_tarefa(colecao)
        elif opcao == '2':
            listar_tarefas(colecao)
        elif opcao == '3':
            busca_avancada(colecao)
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


def criar_tarefa(colecao):
    print("--- NOVA-TAREFA ---")

    titulo_in = input("Titulo: ")
    descricao_in = input("Descricao: ")
    tag_in = input("Tags: ")
    lista_tag = [tag.strip() for tag in tag_in.split(",")]
    nova_tarefa = {
        "titulo":titulo_in,
        "descricao":descricao_in,
        "status":"pendente",
        "data_criacao":str(date.today()),
        "tags":lista_tag
    }

    colecao.insert_one(nova_tarefa)
    print("Tarefa Inserida com Sucesso !")

def listar_tarefas(colecao):
    print("--- LISTA DE TAREFAS ---")
    for t in colecao.find():
                print(f"ID: {t['_id']}")
                print(f"Título: {t['titulo']}")
                print(f"Descrição: {t['descricao']}")
                print(f"Status: {t['status']}")
                print(f"Data: {t['data_criacao']}")
                print(f"Tags: {t.get('tags', 'Sem tags')}")
                print("-" * 30)

def busca_avancada(colecao):
        print("\n=== TO-DO LIST MONGODB ===")
        print("1. Buscar pela Tag")
        print("2. Buscar pela Data")
        print("3. Buscar pelo Status")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            tarefas = input

        elif opcao == '2':
            data = input("Qual a data da tarefa yy-mm-dd: ")
            for t in colecao.find({"data_criacao":data}):
                print(f"\nID: {t['_id']}")
                print(f"Título: {t['titulo']}")
                print(f"Descrição: {t['descricao']}")
                print(f"Status: {t['status']}")
                print(f"Data: {t['data_criacao']}")
                print(f"Tags: {t.get('tags', 'Sem tags')}")
                print("-" * 30)

        elif opcao == '3':
            status = input("Qual Status: ")
            for t in colecao.find({"status":status}):
                print(f"\nID: {t['_id']}")
                print(f"Título: {t['titulo']}")
                print(f"Descrição: {t['descricao']}")
                print(f"Status: {t['status']}")
                print(f"Data: {t['data_criacao']}")
                print(f"Tags: {t.get('tags', 'Sem tags')}")
                print("-" * 30)