l = list()
while True:
    n = str(input('nome: '))
    i = int(input('idade: '))
    s = str(input('sexo: '))

    l.append([n, i, s])
    
    r = str(input('Adicionar novo cadastro? [S/N]'))
    if r in 'N':
        break
print('-='*30)
print(f'{"No.":<4}{"Nome":<10}')
print('-'*60)
for i, a in enumerate(l):
    print(f'{i:<4}{a[0]:<10}')
while True: 
    print('-'*60)
    cont = int(input('Insira o n° do desbravador para abrir seus dados (999 encerra o programa)'))
    if cont == 999:
        print('Fim dos cadastros')
        break
    if cont <= len(l)-1:
        print(f'os dados de {l[cont][0]} são que ele tem {l[cont][1]} anos e seu sexo é {l[cont][2]}')
print('<<<Volte sempre>>>')
    