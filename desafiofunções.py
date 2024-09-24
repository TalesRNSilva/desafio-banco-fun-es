#Essa é uma resolução do desafio empregando datas para contagem de saques.
#O extrato agora é uma tupla (data, salod, valor)
#A checagem de saques é feita contra o número de saques do dia.

import datetime as dt

def formatoHora(data):
    return data.strftime("%d/%m/%y %H:%M:%S")

def saquesHoje(hoje, extrato):
    i = 0
    for valor in extrato:
        if valor[0].date() == hoje: #tem que pegar a data na tupla de cada linha do extrato
            i += 1
    return i

def deposito(*, saldo, valor, extrato, limite = 500, transacoes, hoje = dt.date.today()):
    extrato = extrato
    saldo = saldo
    if saquesHoje(hoje, extrato) >= transacoes:
            print(f"Operação não realizada: excedeu o número diário de transações ({transacoes}).")

    elif valor > 0:
            saldo += valor
            data = dt.datetime.now()
            #extrato.append((f"Depósito: R$ {valor:.2f} (R$ {saldo:.2f})", data))
            extrato.append((data, saldo, valor))

            print(f"{formatoHora(dt.datetime.now())} Depósito de R$ {valor:.2f} realizado. Seu saldo agora é: RS {saldo:.2f}.")

    else:
            print("Operação não autorizada. Informe um valor maior que zero.")
    return saldo, extrato

def saque(*, saldo, valor, extrato, limite = 500, transacoes, hoje = dt.date.today()):
    saldo = saldo
    extrato = extrato

    if valor > limite:
            print("Operação não realizada: excedeu o limite de saque.")
    elif saquesHoje(hoje, extrato) >= transacoes:
            print(f"Operação não realizada: excedeu o número diário de transações ({transacoes}).")
    elif valor > saldo:
            print("Operação não realizada: saldo insuficiente.")
    elif valor > 0:
            saldo -= valor
            data = dt.datetime.now()
            #extrato.append((f"Saque: R$ {valor:.2f} (R$ {saldo:.2f})", data))
            extrato.append((data, saldo, -valor))
            print(f"{formatoHora(dt.datetime.now())} Você sacou R$ {valor:.2f}. Seu saldo agora é R$ {saldo:.2f}.")
    else:
            print("Valor inválido. Por favor, informe um valor maior que zero.")
    return saldo, extrato

def linhaExtrato(*, linha, indice, larguraDisplay):
    data, saldo, valor = linha
    tipo = ''
    if valor > 0:
        tipo = "Depósito"
    else:
        tipo = "Saque"
    
    return f"{formatoHora(data)} {indice}. {tipo}: R$ {abs(valor):.2f}. (R$ {saldo:.2f})"

def mostrarExtrato(*, extrato, larguraDisplay, maxLinhas, saldo):
    print("| Extrato |".center(larguraDisplay, '-'))
        
    if extrato:
        if len(extrato) < maxLinhas:
            for linha in range(len(extrato)):
                print(linhaExtrato(linha = extrato[linha], indice = linha+1, larguraDisplay=larguraDisplay))
        else: 
            for linha in range(maxLinhas):
                print(linhaExtrato(linha = extrato[-maxLinhas-linha], indice = (-(-maxLinhas-linha)+1), larguraDisplay=larguraDisplay))
        print('')
    else:
        print("Sem movimentações.".center(larguraDisplay))
        
    print(f"Saldo: R$ {saldo:.2f}".center(larguraDisplay))
    print("-".center(larguraDisplay, '-'))

def mudarDisplay(*, maxLinhas = 10, larguraDisplay = 50):
    muda = input("""[t] Mudar o número de transações exibidas.
[l] Mudar a largura da tela de extrato.
""")
            
    if muda == 't':
        valor = int(input("Qual o número de transações que gostaria de exibir? (Entre 1 e 30)\n"))
        if valor > 0 and valor <= 30:
            maxLinhas = valor
            print(f"Alterado com sucesso. Agora o extrato exibirá {valor} linhas.")
        else:
            print("Valor inválido. Por favor, insira um valor entre 25 e 50")

    elif muda == "l":
        valor = int(input("Qual a largura desejada da exibição do extrato? (Entre 30 e 70)\n"))
        if valor >= 30 and valor <= 70:
            larguraDisplay = valor
            print(f"Alterado com sucesso. Agora o extrato terá a largura de {valor} caracteres.")
        else:
            print("Valor inválido. Por favor, insira um valor entre 30 e 70.")
    else: 
        print("Comando inválido.")
    return maxLinhas, larguraDisplay

def pegarData():
    while True:
        ano = int(input("Informe o ano de seu nascimento:\n"))
        if ano >= 1900 and ano < 2024:
            break
        else:
            print("Por favor, informe um ano válido.")

    while True:
        mes = int(input("Informe o mês de seu nascimento:\n"))
        if mes >= 1 and mes <= 12:
            break
        else:
            print("Por favor, informe um mês válido.")

    while True:
        dia = int(input("Informe o dia de seu nascimento:\n"))
        if dia >= 1 and dia <= 31:
            break
        else:
            print("Por favor, informe um dia válido.")
    return dt.date(ano,mes,dia)

def pegarCpf(clientes):
    ok = False
    while not ok:
        cpf = int(input("Por favor, informe seu número de CPF:\n"))
        if not isinstance(cpf, int) and cpf < 0:
            print("Por favor, informe um número de CPF válido.")
        else:
            for item in clientes:
                if cpf == item['CPF']:
                    print("CPF já cadastrado.")
                    break
                ok = True
    return cpf

def pegarNome():
    while True:
        nome = input("Informe seu nome completo:\n")
        if not isinstance(nome, str):
            print("Informe um nome válido, por favor.")
        else:
            break
    return nome

def pegarEndereço():
    endereço = ''
    while True:
        rua = input("Informe a rua onde mora:\n")
        num = input("Informe o número de sua residência:\n")
        bairro = input("Informe o seu bairro:\n")
        cidade = input("Informe sua cidade:\n")
        estado = input("Informe a sigla de seu estado:\n")
        endereço = f'{rua}, {num} - {bairro} - {cidade}/{estado}'
        print(f"Seu endereço é: {endereço}.")
        correto = input("Está correto? (s/n) ")
        if correto == 's':
            break
    return endereço

def confiraCadastro(*, cpf, nome, nascimento, endereço, clientes):
    while True:
        print("Confira suas informações:")
        print(f"""Nome: {nome}
CPF: {cpf}
Data de Nascimento: {nascimento}
Endereço: {endereço}""")
        correto = input("Está tudo correto? s/n\n")
        if correto == 's':
            return {'nome': nome, 'data de nascimento':nascimento, 'CPF':cpf, 'endereço':endereço}
        else:
            while True:
                opcao = input("O que gostaria de alterar?\n[1] Nome\n[2] CPF\n[3] Data de Nascimento\n[4]Endereço\n")
                if opcao == '1':
                    nome = pegarNome()
                    break
                elif opcao == '2':
                    cpf = pegarCpf(clientes = clientes)
                    break
                elif opcao == '3':
                    nascimento = pegarData()
                    break
                elif opcao == '4':
                    endereço = pegarEndereço()
                    break
                else:
                    print("Por favor, escolha uma opção válida.")

def cadastrarCliente(*, clientes):
    clientes = clientes
    cpf = pegarCpf(clientes)
    nome = pegarNome()
    nascimento = pegarData()
    endereço = pegarEndereço()
    
    cadastro = confiraCadastro(cpf = cpf, nome = nome, nascimento = nascimento, endereço = endereço, clientes = clientes)
    
    return cadastro

def mostrarClientes(*, clientes):
    print("Lista de clientes:")
    for item in clientes:
        print(f"{item['nome']} - {item['data de nascimento']} - {item['CPF']} - {item['endereço']}")

def cadastrarConta(*, contas, clientes):
    cpf = int(input("Por favor, digite o CPF do titular da conta:\n"))
    if cpf not in [d['CPF'] for d in clientes]:
        print("Usuário não cadastrado.")
        return []
    else:
        if not contas:
            conta = "0001.1"
        else:
            conta = f'0001.{int(contas[-1]['conta'][5:])+1}'
    print(f"Sua conta foi cadastrada, sr(a) {getNameFromCPF(cpf = cpf, clientes = clientes)}. Seu número de conta é: {conta}")
    return { 'conta': conta, 'CPF' : cpf}

def getNameFromCPF(*, cpf, clientes):
    if cpf not in [d['CPF'] for d in clientes]:
        print("CPF não cadastrado.")
        return 'Null'
    else:
        for d in clientes:
            if d['CPF'] == cpf:
                return d['nome'] 

def mostrarContas(*, contas, clientes):
    print("Contas cadastradas:")
    for item in contas:
        print(f'{item['conta']}: {getNameFromCPF(cpf = item['CPF'], clientes = clientes)} - CPF: {item['CPF']}')

menu = f"""
[d] Depositar
[s] Sacar
[e] Extrato
[i] Informações

[c] Cadastrar Cliente (C para ver lista de clientes)
[k] Cadastrar Conta   (K para ver a lista de contas)

[q] Sair

[a] Alterar Exibição do Extrato
[v] Virar o dia
=> """

saldo = 0
limite = 500
extrato = [] #Extrato é uma lista de triplas (saldo, valor, data)
clientes = [ {'CPF':1, 'nome':'João', 'data de nascimento' : dt.date(1994,9,29), 'endereço': 'R Martinico Prado, 142 - Santa Cecília - São Paulo/SP'}] #Clientes é uma lista de dicionários com nome (str), data de nascimento (date), endereço (str) e cpf (int)
contas = [] #contas é uma lista de dicionários, com as chaves 'cpf' e 'conta'. 
numero_saques = 0
LIMITE_TRANSACOES = 10
larguraDisplay = 50
maxLinhas = 10
hoje = dt.date.today()

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = deposito(saldo = saldo, valor = valor, extrato = extrato, limite = limite, transacoes = LIMITE_TRANSACOES, hoje = hoje)
    
    
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato = saque(saldo = saldo, valor = valor, extrato = extrato, limite = limite, transacoes = LIMITE_TRANSACOES, hoje = hoje)
        
    elif opcao == "e":
        mostrarExtrato(extrato = extrato, larguraDisplay = larguraDisplay, maxLinhas = maxLinhas, saldo = saldo)

    elif opcao == "a":
        maxLinhas, larguraDisplay = mudarDisplay(maxLinhas = maxLinhas, larguraDisplay=larguraDisplay)

    elif opcao == 'c':
        clientes.append(cadastrarCliente(clientes = clientes))
    
    elif opcao == 'C':
        mostrarClientes(clientes = clientes)

    elif opcao == 'k':
        conta_nova = cadastrarConta(clientes = clientes, contas = contas)
        if conta_nova:
            contas.append(conta_nova)
            
    elif opcao == 'K':
        mostrarContas(contas = contas, clientes = clientes)

    elif opcao == "v":
        hoje = hoje + dt.timedelta(days = 1)
        print("Dia virado. O número de transações diárias foi resetado.")

    elif opcao == "i":
        print(f"O número máximo de transações diárias é {LIMITE_TRANSACOES}. Hoje você realizou {numero_saques} saques.")
        print(f"O limite máximo de saque é R$ {float(limite):.2f}. Seu saldo atual é R$ {saldo:.2f}.")

    elif opcao == "q":
        break

    else:
         print("Operação inváilida, por favor selecione novamente a operação desejada.")
