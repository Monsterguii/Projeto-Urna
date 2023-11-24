#Iniciando o Menu
def menu():
    print('''
                          +++++++ MENU - SIMULADOR DO SISTEMA DE VOTAÇÃO +++++++

                                   1. Cadastrar Candidatos 
                                   2. Cadastrar Eleitores 
                                   3. Votar 
                                   4. Apurar Resultados
                                   5. Relatório e Estatísticas
                                   6. Encerrar''')
    opção = int(input('                                   Digite a opção escolhida: '))
    return opção

#iniciando a função de verficação de posição na lista
def procurar_elemento(lista, string):
    posicoes = 0
    for indice, elemento in enumerate(lista):
        if elemento == string:
            posicoes = indice
    return posicoes
  
#Fazendo ranking
def ranking_candidatos(lista, string):
    voto_mano = 0
    for indice, elemento in enumerate(lista):
        if elemento == string:
            voto_mano += 1
        ordem_decrescente.append(voto_mano)
    return voto_mano

#Iniciando a função de escolha:
def escolha():                                   
    opcao = input('Digite sim ou não: ')
    opcao = opcao.upper()
    while opcao != 'SIM' and opcao != 'NÃO': 
        opcao = input('Por favor digite apenas sim ou não: ')
        opcao = opcao.upper()
    return opcao

#definindo variaveis
contagem_prefeitos = 0
contagem_governadores = 0
contagem_presidentes = 0
contagem_votos = 0
contagem_eleitores = 0
contagens_voto_ps = 0
c = 0 
f = 1
w = 1
h = 0
j = 0
votos_branco = 0
votos_nulo = 0 
lst_votos_prefeito = []
lst_votos_governador = []
lst_votos_presidente = []
lst_nomeeleitor = []
lst_CPFeleitor = []
ordem_decrescente = []
lst_nomepresidente = []
lst_numeropresidente = []
lst_partidopresidente = []
lst_nomegovernador = []
lst_numerogovernador = []
lst_partidogovernador = []
lst_nomeprefeito = []
lst_numeroprefeito = []
lst_partidoprefeito = []
lst_nomepresidente_crescente = []
lst_num_presidentes = []
#inicio codigo    

while True: 
    opção = menu()
    if opção == 1:
        i = 1
        while i == 1:
            cargo = input("Digite o cargo do candidato, sendo os disponiveis presidente, governador e prefeito: ")
            cargo = cargo.upper()
            if cargo == 'PRESIDENTE':
                nome_presidente = input('Digite o nome do presidente: ')
                contagem_presidentes += 1
                lst_nomepresidente.append(nome_presidente)
                numero_presidente = input('Digite o número do presidente: ')
                lst_numeropresidente.append(numero_presidente) 
                partido_presidente = input('Digite o partido do presidente: ')
                lst_partidopresidente.append(partido_presidente)
            elif cargo == 'GOVERNADOR':
                nome_governador = input('Digite o nome do governador: ')
                contagem_governadores += 1
                lst_nomegovernador.append(nome_governador)
                numero_governador = input('Digite o número do governador ')
                lst_numerogovernador.append(numero_governador)
                partido_governador = input('Digite o partido do governador: ')
                lst_partidogovernador.append(partido_governador)
            elif cargo == 'PREFEITO':
                nome_prefeito = input('Digite o nome do prefeito: ')
                contagem_prefeitos += 1
                lst_nomeprefeito.append(nome_prefeito)
                numero_prefeito = input('Digite o número do prefeito: ')
                lst_numeroprefeito.append(numero_prefeito) 
                partido_prefeito = input('Digite o partido do prefeito: ')
                lst_partidoprefeito.append(partido_prefeito)
            print(''' 
                                    Deseja cadastrar outro candidato? ''')
            opcao = escolha()
            if opcao == 'SIM':
                True
            if opcao == 'NÃO':
                volta = input('Deseja voltar ao menu ou encerrar? digite menu ou encerrar: ')
                volta = volta.upper()
                if volta == 'ENCERRAR':
                    print('Obrigado!')
                    break
                else:
                    i += 2 
                                
    elif opção == 2:
        m = 1
        while m == 1:
            contagem_eleitores += 1 
            nome_eleitor=  input('Digite o nome do eleitor: ')
            lst_nomeeleitor.append(nome_eleitor)
            CPF_eleitor = int(input('Digite o CPF do eleitor: '))
            lst_CPFeleitor.append(CPF_eleitor)
            print(''' 
                                       Deseja cadastrar outro eleitor ? ''')
            opcao = escolha()
            if opcao == 'SIM':
                m == 1
            if opcao == 'NÃO':
                m += 2
                
    
    elif opção == 3:
#Iniciando os votos, primeiramento o de prefeito       
        j = 2
        l = 0
        k = 0
        while j == 2:
            voto_prefeito = input('Digite o número do canditado a prefeito, ou -1 ou -2 para votar em branco ou em nulo: ')
            voto_prefeito = str(voto_prefeito)
            lst_votos_prefeito.append(voto_prefeito)
            if voto_prefeito == '-1':
                branco = input('Você realmente deseja votar em branco? Digite sim ou não: ')
                branco = branco.upper()
                if branco == 'SIM':
                    votos_branco += 1
                    j += 3
                elif branco == 'NÃO':
                    volta = input('Deseja voltar ao menu ou votar novamente? digite menu ou votar: ')
                    volta = volta.upper()
                    if volta == 'VOTAR':
                        j == 2
                    else:
                        j += 3
            if voto_prefeito == '-2':
                nulo = input('Você realmente deseja votar nulo? Digite sim ou não: ')
                nulo = branco.upper()
                if nulo == 'SIM':
                    votos_nulo += 1
                    j += 3
                elif nulo == 'NÃO':
                    volta = input('Deseja voltar ao menu ou votar novamente? digite menu ou votar: ')
                    volta = volta.upper()
                    if volta == 'VOTAR':
                        j == 2
                    else:
                        j += 3
            else: 
                procurar_elemento(lst_numeroprefeito, voto_prefeito)
                posições = procurar_elemento(lst_numeroprefeito, voto_prefeito)
                print("Você deseja votar no " + lst_nomeprefeito[posições] + ",do partido " + lst_partidoprefeito[posições] + " para prefeito?")
                Confirmação_prefeito = input('Digite sim ou não: ')
                Confirmação_prefeito = Confirmação_prefeito.upper()
                if Confirmação_prefeito == 'SIM':
                    j += 3
                    contagem_votos += 1
#esse k += 3 é para ser usado para começar os votos do governador, somente a partir daqui que começa    
                    k += 3
                else:
                    volta = input('Então, voltar ao menu ou votar novamente? digite menu ou votar: ')
                    volta = volta.upper()
                    if volta == 'VOTAR':
                        j == 2
                    else:
                        j += 3
 #Agora os votos para governador       
        while k == 3:
            voto_governador = input('Digite o número do canditado a governador, ou -1 ou -2 para votar em branco ou em nulo: ')
            voto_governador = str(voto_governador)
            lst_votos_governador.append(voto_governador)
            if voto_governador == '-1':
                branco = input('Você realmente deseja votar em branco? Digite sim ou não: ')
                branco = branco.upper()
                if branco == 'SIM':
                    votos_branco += 1
                    k += 4
                elif branco == 'NÃO':
                    volta = input('Deseja voltar ao menu ou votar novamente? digite menu ou votar: ')
                    volta = volta.upper()
                    if volta == 'VOTAR':
                        k == 3
                    else:
                        k += 4
            if voto_governador == '-2':
                nulo = input('Você realmente deseja votar nulo? Digite sim ou não: ')
                nulo = nulo.upper()
                if nulo == 'SIM':
                    votos_nulo += 1
                    k += 4
                elif nulo == 'NÃO':
                    volta = input('Deseja voltar ao menu ou votar novamente? digite menu ou votar: ')
                    volta = volta.upper()
                    if volta == 'VOTAR':
                        k == 3
                    else:
                        k += 4
            else: 
                procurar_elemento(lst_numerogovernador, voto_governador)
                posiciones = procurar_elemento(lst_numerogovernador, voto_governador)
                print('Você deseja votar no ' + lst_nomegovernador[posiciones] + ',do partido ' + lst_partidogovernador[posiciones] + ' para governador?')
                Confirmação_governador = input('Digite sim ou não para confirmar: ')
                Confirmação_governador = Confirmação_governador.upper()
                if Confirmação_governador == 'SIM':
                    k += 4
                    l += 4
                    contagem_votos += 1
                else:
                    volta = input('Então, voltar ao menu ou votar novamente? digite menu ou votar: ')
                    volta = volta.upper()
                    if volta == 'VOTAR':
                        k == 3
                    else:
                        k += 4
#por ultimo os votos para presidente      
        while l == 4:
            voto_presidente = input('Digite o número do canditado a presidente, ou -1 para votar em branco, ou -2 para votar em nulo: ')
            voto_presidente = str(voto_presidente)
            lst_votos_presidente.append(voto_presidente)
            if voto_presidente == '-1':
                branco = input('Você realmente deseja votar em branco? Digite sim ou não: ')
                branco = branco.upper()
                if branco == 'SIM':
                    votos_branco += 1
                    l += 5
                elif branco == 'NÃO':
                    volta = input('Deseja voltar ao menu ou votar novamente? digite menu ou votar: ')
                    volta = volta.upper()
                    if volta == 'VOTAR':
                        l == 4 
                    else:
                        l += 5
            if voto_presidente == '-2':
                nulo = input('Você realmente deseja votar nulo? Digite sim ou não: ')
                nulo = branco.upper()
                if nulo == 'SIM':
                    votos_nulo += 1
                    l += 5
                elif nulo == 'NÃO':
                    volta = input('Deseja voltar ao menu ou votar novamente? digite menu ou votar: ')
                    volta = volta.upper()
                    if volta == 'VOTAR':
                        l == 4
                    else:
                        l += 5
            else: 
                procurar_elemento(lst_numeropresidente, voto_presidente)
                pozições = procurar_elemento(lst_numeropresidente, voto_presidente)
                print('Você deseja votar no ' + lst_nomepresidente[pozições] + ', do partido '  + lst_partidopresidente[pozições] + ' para presidente?')
                Confirmação_presidente = input('Digite sim ou não para confirmar: ')
                Confirmação_presidente = Confirmação_presidente.upper()
                if Confirmação_presidente == 'SIM':
                    l += 5
                    contagem_votos += 1
                else:
                    volta = input('Então, voltar ao menu ou votar novamente? digite menu ou votar: ')
                    volta = volta.upper()
                    if volta == 'VOTAR':
                        l == 4
                    else:
                        l += 5
    elif opção == 4:
        print('''
                             +++++RANKING DO RESULTADO PARA PRESIDENTE++++++ 
            /        NOME        /  PARTIDO  /  TOTAL DE VOTOS /  % DE VOTOS VÁLIDOS /''')
        while f <= contagem_presidentes:
            while h <= (len(lst_numeropresidente)-1):
                contagens_voto_ps = lst_numeropresidente[h]
                ordem_decrescente = ranking_candidatos(lst_votos_presidente, contagens_voto_ps)
                h += 1
            lst_num_presidentes = [i for i, _ in sorted(enumerate(ordem_decrescente),key=lambda x: x[1])] 
            print(lst_num_presidentes)
            lst_nomepresidente_crescente = sorted(lst_nomepresidente, key=lambda x: lst_num_presidentes[lst_nomepresidente.index(x)])
            print(lst_nomepresidente_crescente)
            f += 1

    elif opção == 5:
        lst_nomeeleitor.sort()
        print ('+++++++++++++LISTA DE ELEITORES++++++++++++++')
        while w <= contagem_eleitores:
            print(w, lst_nomeeleitor[c])
            c += 1
            w += 1
        print('+++++++++++++VOTOS TOTAIS+++++++++++++')
        print(contagem_votos+ votos_branco + votos_nulo)
        print('+++++++++++++ELEITORES TOTAIS+++++++++++++')
        print(contagem_eleitores)
    elif opção == 6:
        print('Obrigado!')
        break
