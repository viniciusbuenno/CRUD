
def apresenteSe ():
    print('+-------------------------------------------------------------+')
    print('|                                                             |')
    print('| AGENDA PESSOAL DE ANIVERSÁRIOS E FORMAS DE CONTATAR PESSOAS |')
    print('|                                                             |')
    print('| Prof André Luís dos Reis Gomes de Carvalho                  |')
    print('|                                                             |')
    print('| Versão 1.0 de 12/abril/2024                                 |')
    print('|                                                             |')
    print('+-------------------------------------------------------------+')

def umTexto (solicitacao, mensagem, valido):
    digitouDireito=False
    while not digitouDireito:
        txt=input(solicitacao)

        if txt not in valido:
            print(mensagem,'- Favor redigitar...')
        else:
            digitouDireito=True

    return txt

def opcaoEscolhida (mnu):
    print ()

    opcoesValidas=[]
    posicao=0
    while posicao<len(mnu):
        print (posicao+1,') ',mnu[posicao],sep='')
        opcoesValidas.append(str(posicao+1))
        posicao+=1

    print()
    return umTexto('Qual é a sua opção? ', 'Opção inválida', opcoesValidas)


def ondeEsta (nom,agd):
    inicio=0
    final =len(agd)-1

    while inicio<=final:
        meio=(inicio+final)//2

        if nom.upper()==agd[meio][0].upper():
            return [True,meio]
        elif nom.upper()<agd[meio][0].upper():
            final=meio-1
        else: # nom.upper()>agd[meio][0].upper()
            inicio=meio+1

    return [False,inicio]

def incluir (agd):
    digitouDireito=False
    while not digitouDireito:
        nome=input('\nNome.......: ')

        resposta=ondeEsta(nome,agd)
        achou   = resposta[0]
        posicao = resposta[1]

        if achou:
            print ('Pessoa já existente - Favor redigitar...')
        else:
            digitouDireito=True

    aniversario=input('Aniversário: ')
    endereco   =input('Endereço...: ')
    telefone   =input('Telefone...: ')
    celular    =input('Celular....: ')
    email      =input('e-mail.....: ')

    contato=[nome,aniversario,endereco,telefone,celular,email]

    agd.insert(posicao,contato)
    print('Cadastro realizado com sucesso!')

def procurar (agd):
  
    parar = False
    while parar == False:


        procura = input("Digite o nome da pessoa que você busca ou 'sair' para parar: ")


        encontrouAlguem = False
        i = 0

        if procura.upper() == 'sair'.upper():
            break


        """ Usando a função ondeEsta()

        achou = ondeEsta(procura, agd)[0]
        achouIndex = ondeEsta(procura, agd)[1]
        if achou == False:
            print("Ninguém com esse nome foi encontrado!")
        else:
            print(f"Pessoa encontrada!\nNome: {agd[achouIndex][0]}\nAniversário: {agd[achouIndex][1]}\nEndereço: {agd[achouIndex][2]}\nTelefone: {agd[achouIndex][3]}\nCelular: {agd[achouIndex][4]}\nE-mail: {agd[achouIndex][5]}")
        """


        #Procurando usando função própria
        for item in agd:
            if procura.upper() == item[0].upper():
                print(f"Pessoa encontrada!\nNome: {agd[i][0]}\nAniversário: {agd[i][1]}\nEndereço: {agd[i][2]}\nTelefone: {agd[i][3]}\nCelular: {agd[i][4]}\nE-mail: {agd[i][5]}")
                encontrouAlguem = True
                break          
            i =+ 1

        if encontrouAlguem == False:
            print("Ninguém com esse nome foi encontrado!")








def atualizar (agd):
  
    atualizaOpcoes = ["Aniversário", \
                      "Endereço", \
                      "Telefone", \
                      "Celular", \
                      "E-mail", \
                      "Voltar"]

    mais = True

    while mais:



        nomeDoAtualizado = str(input("Digite o nome da pessoa a ser atualizada ou 'sair' para cancelar: ")).upper()
        achou = False

        if nomeDoAtualizado == 'sair'.upper():
            break


        # Achando o atualizado usando a função ondeEsta()

        """
        nomeDoAtualizado = input("Digite o nome da pessoa que você busca ou 'sair' para parar: ")
        achou = ondeEsta(nomeDoAtualizado, agd)[0]
        achouIndex = ondeEsta(nomeDoAtualizado, agd)[1]
        if achou == False:
            print("Ninguém com esse nome foi encontrado!")
        """

        #Achando o atualizado usando função própria

        for item in agd:
            if nomeDoAtualizado == item[0].upper(): #achando o usuario a ser atualizado
                vaiAtualizar = item # vaiAtualizar é o usuário
                achou = True
            if achou == True:
                break
            else:
                print("Pessoa não encontrada, cancelando atualização!")


        if achou == True:
            opcaoAtualiza = opcaoEscolhida(atualizaOpcoes)
            qualIndex = '0'

            match(opcaoAtualiza):
                case '1':

                    qualIndex = 1

                    print(f"Atualizando o Aniversário de {vaiAtualizar[0]}") #nome do usuário
                    print(f"O Aniversário atual é {vaiAtualizar[qualIndex]}")
                    novoDado = input("Digite o novo Aniversário: ")
                    if novoDado == vaiAtualizar[qualIndex]:
                        print("O dado permaneceu igual")
                    else:
                        vaiAtualizar.pop(qualIndex)
                        vaiAtualizar.insert(qualIndex, str(novoDado))
                        print("O dado foi atualizado com sucesso!")

                case '2':

                    qualIndex = 2

                    print(f"Atualizando o Endereço de {vaiAtualizar[0]}") #nome do usuário
                    print(f"O Aniversário atual é {vaiAtualizar[qualIndex]}")
                    novoDado = input("Digite o novo Endereço: ")
                    if novoDado == vaiAtualizar[qualIndex]:
                        print("O dado permaneceu igual")
                    else:
                        vaiAtualizar.pop(qualIndex)
                        vaiAtualizar.insert(qualIndex, str(novoDado))
                        print("O dado foi atualizado com sucesso!")
                case '3':

                    qualIndex = 3

                    print(f"Atualizando o Telefone de {vaiAtualizar[0]}") #nome do usuário
                    print(f"O Aniversário atual é {vaiAtualizar[qualIndex]}")
                    novoDado = input("Digite o novo Telefone: ")
                    if novoDado == vaiAtualizar[qualIndex]:
                        print("O dado permaneceu igual")
                    else:
                        vaiAtualizar.pop(qualIndex)
                        vaiAtualizar.insert(qualIndex, str(novoDado))
                        print("O dado foi atualizado com sucesso!")
                case '4':

                    qualIndex = 4

                    print(f"Atualizando o Celular de {vaiAtualizar[0]}") #nome do usuário
                    print(f"O Aniversário atual é {vaiAtualizar[qualIndex]}")
                    novoDado = input("Digite o novo Celular: ")
                    if novoDado == vaiAtualizar[qualIndex]:
                        print("O dado permaneceu igual")
                    else:
                        vaiAtualizar.pop(qualIndex)
                        vaiAtualizar.insert(qualIndex, str(novoDado))
                        print("O dado foi atualizado com sucesso!")
                case '5':
                    qualIndex = 5

                    print(f"Atualizando o E-mail de {vaiAtualizar[0]}") #nome do usuário
                    print(f"O Aniversário atual é {vaiAtualizar[qualIndex]}")
                    novoDado = input("Digite o novo E-mail: ")
                    if novoDado == vaiAtualizar[qualIndex]:
                        print("O dado permaneceu igual")
                    else:
                        vaiAtualizar.pop(qualIndex)
                        vaiAtualizar.insert(qualIndex, str(novoDado))
                        print("O dado foi atualizado com sucesso!")
                case '6':
                    break










def listar (agd):


    if not agd:
        print("Nenhum contato cadastrado.")
    else:
        print("Lista de contatos:")
        for contato in agd:
            print("Nome:", contato[0])
            print("Aniversário:", contato[1])
            print("Endereço:", contato[2])
            print("Telefone:", contato[3])
            print("Celular:", contato[4])
            print("E-mail:", contato[5])
            print()  # Adiciona uma linha em branco entre os contatos


def excluir (agd):
    print()
    digitouDireito=False
    while not digitouDireito:
        nome=input('Nome.......: ')

        resposta=ondeEsta(nome,agd)
        achou   = resposta[0]
        posicao = resposta[1]

        if not achou:
            print ('Pessoa inexistente - Favor redigitar...')
        else:
            digitouDireito=True

    print('Aniversario:',agd[posicao][1])
    print('Endereco...:',agd[posicao][2])
    print('Telefone...:',agd[posicao][3])
    print('Celular....:',agd[posicao][4])
    print('e-mail.....:',agd[posicao][5])

    resposta=umTexto('Deseja realmente excluir? ','Você deve digitar S ou N',['s','S','n','N'])

    if resposta in ['s','S']:
        del agd[posicao]
        print('Remoção realizada com sucesso!')
    else:
        print('Remoção não realizada!')

# daqui para cima, definimos subprogramas (ou módulos, é a mesma coisa)
# daqui para baixo, implementamos o programa (nosso CRUD, C=create(inserir), R=read(recuperar), U=update(atualizar), D=delete(remover,apagar)

apresenteSe()

agenda=[]

menu=['Incluir Contato',\
      'Procurar Contato',\
      'Atualizar Contato',\
      'Listar Contatos',\
      'Excluir Contato',\
      'Sair do Programa']

opcao=666
while opcao!=6:
    opcao = int(opcaoEscolhida(menu))

    if opcao==1:
        incluir(agenda)
    elif opcao==2:
        procurar(agenda)
    elif opcao==3:
        atualizar(agenda)
    elif opcao==4:
        listar(agenda)
    elif opcao==5:
        excluir(agenda)






print('OBRIGADO POR USAR ESTE PROGRAMA!')

