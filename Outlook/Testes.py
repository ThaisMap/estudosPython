import win32com.client

subpastas = []


def principal():
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    caixas = get_caixas_de_email(outlook)
    for i in range(0, len(caixas)):
        print(i, caixas[i])

    caixa_escolhida = int(input("Qual caixa? "))
    get_subpastas(outlook.Folders[caixas[caixa_escolhida]].Folders, 0)
    index = 0
    for subfold in subpastas:
        print(index, subfold.Name, len(subfold.Items))
        index += 1
    pasta_selecionada = int(input("Qual pasta? "))
    duplicidades = indices_com_duplicados(subpastas[pasta_selecionada])
    print("Encontradas {} duplicidades".format(len(duplicidades)))
    if len(duplicidades) > 0:
        apagar = input("Apagar agora? ")
        if apagar == "s":
            apagar_emails(subpastas[pasta_selecionada], duplicidades)


def apagar_emails(folder, indices):
    while len(indices) > 0:
        folder.Items[indices.pop(-1)].Delete()


def indices_com_duplicados(folder):
    chaves_distintas = {}
    indices = []
    i = 0
    for item in folder.Items:
        chave = "{0} {1} {2} {3} {4}".format(item.SenderEmailAddress, item.Subject, item.To, item.CC, item.SentOn)
        if chave in chaves_distintas:
            indices.append(i)
            print(i)
        else:
            chaves_distintas[chave] = i
        i += 1
    return indices


def get_subpastas(folders, indent):
    ignorar_pastas = {"Itens Excluídos", "Caixa de Saída", "Itens Enviados", "Contatos Sugeridos", "Lixo eletrônico",
                      "Configurações de Ação de Conversa", "Configurações de Etapa Rápida", "Rascunhos", "Calendário",
                      "Contatos", "Diário", "Anotações", "Tarefas", "RSS Feeds", "News Feed", "Lembretes",
                      "IM Contact List", "Contatos Rápidos", "Arquivo Morto",
                      "ao arquivo para que as modificações feitas no arquivo sejam refletidas no item."}
    for i in range(0, folders.Count):
        folder = folders[i]
        if folder.Name not in ignorar_pastas:
            subpastas.append(folder)
        get_subpastas(folder.Folders, indent + 1)


def get_caixas_de_email(outlook):
    caixas = outlook.Folders
    nomes = []
    for fold in caixas:
        nomes.append(fold.name)
    return nomes


if __name__ == "__main__":
    principal()
