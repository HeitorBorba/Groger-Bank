nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))
saldo = float(input('Digite seu saldo: '))

informacoes = int(input('Digite 1 para sacar, \n'
                    '            Digite (2) para fazer depósito, \n'
                    '            Digite (3) para visualizar informaçoes, \n'
                    '            Digite qualquer outro numero para sair: '))


def fsaque():
    saque = float(input('Digite o quanto você deseja sacar: '))

    if saque > 1000 or saq > saldo:
        print('Seu saque deve ser maior que R$1000')

    else:
        print('Seu saldo agora é: ' + str(saldo - saque))


def fdeposito():
    deposito = float(input('quanto você quer depositar: '))

    if deposito > 5000:
        print('Valor errado')

    else:
        print('Seu saldo agora é: ' + str(saldo + deposito))

def finformacoes():
    print(nome )
    print(idade)
    print('R$' + str(saldo))

if informacoes == 1:
    fsaque()

elif informacoes == 2:
    fdeposito()

elif informacoes == 4:
    finformacoes()

else:
    print('Tchau, ate mais.')