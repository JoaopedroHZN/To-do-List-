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
            atualizar_tarefa(colecao)
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
            tag = input("Qual a Tag:")
            for t in colecao.find({"tags":tag}):
                print(f"\nID: {t['_id']}")
                print(f"Título: {t['titulo']}")
                print(f"Descrição: {t['descricao']}")
                print(f"Status: {t['status']}")
                print(f"Data: {t['data_criacao']}")
                print(f"Tags: {t.get('tags', 'Sem tags')}")
                print("-" * 30)
                
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

def atualizar_tarefa(colecao):
    print("--- ATUALIZAR-TAREFA ---")
    print("1- Titulo")
    print("2- Descricao")
    print("3- Status")
    print("4- Tags")
    opcao = input("Escolha uma opcao para Atualizar: ")
    if opcao == '1' :
        titulo_ant = input("Titulo Antigo: ");
        novo_titulo = input("Novo Titulo: ")
        filtro = ({"titulo":titulo_ant})
        novo_dado = ({"$set": {"titulo": novo_titulo}})
        colecao.update_one(filtro,novo_dado)
        print(f"Tarefa {titulo_ant} mudou para {novo_titulo}")

    elif opcao == '2':
        descricao_ant = input("Descricao Antigo: ")
        descricao_nova = input("Nova Descricao: ")
        filtro = ({"descricao":descricao_ant})
        novo_dado = ({"$set": {"descricao": descricao_nova}})
        colecao.update_one(filtro,novo_dado)
        print(f"Tarefa {descricao_ant} mudou para {descricao_nova}")

    elif opcao == '3':
        titulo_in = input("Titulo da Tarefa: ")
        status_ant = input("Status Ant: ")
        status_novo = input("Status Novo:")
        filtro = {
            "titulo":titulo_in,
            "status":"pendente"}
        novo_dado = ({"$set": {"status":status_novo}})
        colecao.update_one(filtro,novo_dado)
        print(f"Tarefa: Titulo: {titulo_in} com o Status {status_ant} mudou para {status_novo}")
    
    elif opcao == '4':
        titulo_in = input("Titulo da Tarefa: ")
        tag_ant = input("Tag antigo:")
        tag_novo = input("Tag Novo:")
        filtro = {
            "titulo":titulo_in,
            "tags":tag_ant
        }
        novo_dado = ({"$set": {"tags.$":tag_novo}})
        colecao.update_one(filtro,novo_dado)
        print(f"Tarefa: Titulo: {titulo_in} com a Tag {tag_ant} mudou para {tag_novo}")