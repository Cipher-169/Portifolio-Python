meses = ['janeiro','fevereiro','março','abril','maio','junho',
    'julho','agosto','setembro','outubro','novembro','dezembro']

def data(usu):
    datac = verificador(usu)
    if datac is None:
        print(f"Não passou na verificação")
        return
    if datac[1] == 2:
        if ((datac[2] % 4 == 0 and not datac[2] % 100 == 0) or datac[2] % 400 == 0):
            if datac[0] > 29:
                print('Digite uma data valida')
            else:
                print(f'{datac[0]} de {meses[datac[1]-1]} de {datac[2]}')
        elif datac[0] > 28:
                print('Digite uma data valida')
        else:
            print(f'{datac[0]} de {meses[datac[1]-1]} de {datac[2]}')
    elif datac[1] in [1,3,5,7,8,10,12] and datac[0] > 31:
            print('Digite uma data valida')
    elif datac[1] in [4,6,9,11] and datac[0] > 30:
        print('Digite uma data valida')
    elif datac[0] == 0 or datac[1] == 0 or datac[2] == 0:
        print('Digite uma data valida')
    else:
        print(f'{datac[0]} de {meses[datac[1]-1]} de {datac[2]}')

def verificador(a):
    t = input(a).split('/')
    if len(t) != 3:
        return None
    
    elif not t[0].isnumeric() or not t[1].isnumeric() or not t[2].isnumeric():
        return None
    
    for i in range(3): t[i] = int(t[i])

    if t[0] < 1 or t[0] > 31 or t[1] < 1 or t[1] > 12:
        return None
    else:
        return t

data('Digite uma data no formato (DD/MM/AAAA): ') 
