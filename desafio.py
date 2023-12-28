from datetime import datetime
import textwrap

def horas():
    data_hora = datetime.now()
    dt_hr_format = "%d-%m-%Y %H:%M:%S"
    dt_hr_formatada = data_hora.strftime(dt_hr_format)
    return dt_hr_formatada

def menu():
    menu = """\n
    ======================== MENU ============================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    >>> """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0 :
        extrato=str(extrato)
        tip = type(saldo)
        if saldo == '' :
            saldo = float(0)
        elif  type(saldo) == tip:
            saldo = float(saldo)
        saldo += valor
        print('TIpo do extrato: ', type(extrato))
        dt_hr_formatada = horas() 
        print(f"\nDeposito Realizado com sucesso, as {dt_hr_formatada}")
        
        extrato += str(f""" 
    Saldo de: R${saldo:.2f}
    {dt_hr_formatada} - Realizado Deposito no valor de: R$ {valor:.2f}""")
        
    else:
        print("Somente valores superiores a zero")
        
    return saldo, extrato
        
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    
    if (numero_saques < limite_saques and numero_saques >= 0) and (valor <= limite and valor > 0) and (saldo != 0):
        saldo -= valor
        numero_saques += 1
        print("\nSaque realizado com sucesse!")
        
        dt_hr_formatada = horas()
        extrato+=str(f"""
    Saldo de: R${saldo:.2f}
    {dt_hr_formatada} - Realizado Saque no valor de: R$ {valor:.2f}""")
    else:
        if (valor > saldo):
            saldo = 0
            print("\nSaldo insuficiente")
        elif numero_saques == limite_saques:
            print("\nLimite diario de saque diario excedido") 
        elif valor > limite:
            print("\nLimite de saque é de R$ 500.00 por saque")
        print('fui mlk')
    def oi():
        exceu_saldo = valor > saldo
        exceu_limite = valor > limite
        execedeu_saques = numero_saques >= limite_saques
        
        if exceu_saldo:
            print("\nSaldo insuficiente")
        elif exceu_limite:
            print("\nLimite de saque é de R$ 500.00 por saque")
        elif execedeu_saques:
            print("\nLimite diario de saque diario excedido")
        elif valor > 0 :
            saldo -= valor
            numero_saques += 1
            print("\nSaque realizado com sucesse!")
        else:
            print('Falha')
            
            dt_hr_formatada = horas()
            extrato+=(f"""
    Saldo de: R${saldo:.2f}
    {dt_hr_formatada} - Realizado Saque no valor de: R$ {valor:.2f}""")
    
    return saldo,extrato


def ixibir_extrato(saldo, /,*, extrato):
    print('\n======================= EXTRATO ===========================')
    print('Sem movimentação' if not extrato else extrato)
    

def criar_usuarios(usuarios):
    
    cpf = int(input("Digite seu CPF: "))
    
    usuario = filtrar_user(cpf, usuarios)
    
    if usuario:
        print('\nUser já cadastrado!')
        return
    
    nome = input('Digite seu nome: ')
    data_nascimento = input('Digite sua data de nascimento: ')
    endereco = input ('Digite seu endereço: ')
    
    
    usuarios.append({
            'Nome': nome,
            'data_nascimento' : data_nascimento,
            'CPF': cpf,
            'endereco' : endereco
        })


def filtrar_user(cpf, usuarios):
    
    user_filtrado = [usuario for usuario in usuarios if usuario['CPF'] == cpf ]
    return user_filtrado[0] if user_filtrado else None

def  criar_conta (agencia, numero_conta, usuarios):
    cpf = int(input('Informe o CPF: '))
   
    usuarios = filtrar_user(cpf, usuarios)
    
    
    if usuarios:
        print('\nConta criada com sucesso')
        return {'agencia': agencia,  'numero_conta': numero_conta, 'usuario': usuarios}
    print('\nUsuario não encontrado!!')
    
def listar_conta(contas):
    for conta in contas:
        linha = f"""
            Agencia:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['Nome']}
            """
        print("="*100)
        print(textwrap.dedent(linha))
        

def main():
    
    LIMITES_SAQUES = 3
    AGENCIA = '0001'
    
    saldo  = 0
    limite = 500 
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
   
    while True:
        
        opcao = menu()
        
        if opcao == 'd':
            valor = float(input("Digite o valor a ser depositada: "))
            
            saldo, extrato = depositar(saldo, valor, extrato)
            print(type(saldo))
        elif opcao == "s":
            
            valor_saq = float(input("Digite o valor a ser sacado: "))
            
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor_saq,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITES_SAQUES
            )
            
        elif opcao == "e":
            ixibir_extrato(saldo , extrato=extrato)
            
        elif opcao == 'nu':
            criar_usuarios(usuarios)
        
        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta (AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
        
        elif opcao ==  'lc':
            listar_conta(contas)
            
        elif opcao == 'q':
            break
        
main()        
        