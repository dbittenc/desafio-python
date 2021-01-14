from time import sleep
print('.°'*15, 'Desbrava Bank', '°.'*15)
m = 0
while m != 5:
    print(f'{"1 - Cadastrar desbravador":<4}')
    print(f'{"2 - Listar desbravadores":<4}')
    print(f'{"3 - Alterar cadastro de desbravador":<4}')
    print(f'{"4 - Deletar um cadastro":<4}')
    print(f'{"5 - Sair":<4}')
    m = int(input('escolha uma das opções: '))

    if m == 1:
        print('-='*15, 'Novos cadastros','-='*15)
        print('_'*20, 'Preencha as informações solicitadas', '_'*20)
        l = list()
        while True:
            n = str(input('nome: '))
            i = int(input('idade: '))
            s = str(input('sexo: '))

            l.append([n, i, s])
        
            r = str(input('Adicionar novo cadastro? [S/N]'))
            if r in 'N' or r in 'n':
                break
        print('-='*30)
        print(f'{"No.":<4}{"Nome":<10}')
        print('-'*60)
        for i, a in enumerate(l):
            print(f'{i:<4}{a[0]:<10}')
        while True: 
            print('-'*60)
            cont = int(input('Insira o n° do desbravador para abrir seus dados (999 volta ao menu principal)'))
            if cont == 999:
                print('-='*11, 'Fim dos cadastros', '-='*11)
                print('°'*63)
                print('-='*11, 'Menu Princiapal', '-='*12)
                break
            if cont <= len(l)-1:
                print(f'{l[cont][0]} Tem {l[cont][1]} anos e é do sexo {l[cont][2]}')
    if m == 2:
        print('-='*30)
        print(f'{"No.":<4}{"Nome":<10}')
        print('-'*60)
        for i, a in enumerate(l):
            print(f'{i:<4}{a[0]:<10}')
        while True: 
            print('-'*60)
            cont = int(input('Insira o n° do desbravador para abrir seus dados (999 encerra o programa)'))
            if cont == 999:
                print('-='*11, 'Fim dos cadastros', '-='*11)
                print('°'*63)
                print('-='*11, 'Menu Princiapal', '-='*12)
                break
            if cont <= len(l)-1:
                print(f'{l[cont][0]} Tem {l[cont][1]} anos e é do sexo {l[cont][2]}')
            
    if m == 3:
        print('-='*30)
        print(f'{"No.":<4}{"Nome":<10}')
        print('-'*60)
        for i, a in enumerate(l):
            print(f'{i:<4}{a[0]:<10}')
        while True: 
            print('-'*60)
            cont = int(input('Insira o n° do desbravador que deseja alterar os dados (999 encerra o programa)'))
            if cont == 999:
                print('-='*11, 'Fim dos cadastros', '-='*11)
                print('°'*63)
                print('-='*11, 'Menu Princiapal', '-='*12)
                break
            if cont <= len(l)-1:
                print(f'os dados de {l[cont][0]} são que ele tem {l[cont][1]} anos e seu sexo é {l[cont][2]}')
                print('1 - Nome')
                print('2 - Idade')
                print('3 - Sexo')
                ax = int(input('o que deseja alterar? '))
                
                if ax == 1:    
                    l[cont][0] = str(input('qual é o novo dado: '))
                if ax == 2:
                    l[cont][1] = str(input('qual é o novo dado: '))
                if ax == 3:
                    l[cont][2] = str(input('qual é o novo dado: '))
                    print('-='*30)
                print(f'{"No.":<4}{"Nome":<10}')
                print('-'*60)
                for i, a in enumerate(l):
                    print(f'{i:<4}{a[0]:<10}')
                    

    if m == 4:
        print('-='*30)
        print(f'{"No.":<4}{"Nome":<10}')
        print('-'*60)
        for i, a in enumerate(l):
            print(f'{i:<4}{a[0]:<10}')
        while True: 
            print('-'*60)
            cont = int(input('Insira o n° do desbravador que deseja apagar do sistema (999 encerra o programa)'))
            if cont == 999:
                print('-='*11, 'Fim dos cadastros', '-='*11)
                print('°'*63)
                print('-='*11, 'Menu Princiapal', '-='*12)
                break
            if cont <= len(l)-1:
                l.pop(cont)
            print('-='*30)
            print(f'{"No.":<4}{"Nome":<10}')
            print('-'*60)
            for i, a in enumerate(l):
                print(f'{i:<4}{a[0]:<10}')
            
    if m == 5:
        print('Finalizando...')
        sleep(1)
        print('.°'*10, 'Obrigado por usar o Desbrava brank', '°.'*10)