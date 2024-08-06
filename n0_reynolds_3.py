#Objetivos deste programa: Calcular o número de Reynolds automaticamente.Como?
#Re =ρVD/μ ou Re = VD/v
#onde:
#ρ : massa específica (kg/m³);
#V: velocidade (m/s);
#D: Diâmetro da tubulação (m);
#μ: viscosidade dinâmica (Pa*s ou N*s/m²)
#v: viscosidade cinemática (m²/s)
#Sendo que: v = μ/ρ

#Classificação do Escoamento dado pelo número de Reynolds:
#Re <= 2000: Escoamento laminar;
#2000 <= Re <= 4000: Escoamento transitório;
#Re >= 4000:  

#Solução:

while True is True:

        #Etapa 01: Inserindo os dados para o cálculo do Numero de Reynolds.
    
        print('\nCaso alguma informação não esteja disponível para inserção, deixe-a em branco: \n')
        V = input('\nInsira a velocidade desejada, (em m/s): ')
        D = input('\nInsira o Diâmetro da Tubulação desejado, em (m): ')
        Q = input('\nInsira a Vazão da Tubulação desejada, em (m³/s):')

        #Tratando os erros nesta etapa: O usuário pode não inserir dados importantes...

        if  len(D) < 1: #Se o usuário não digitou a informação do diâmetro da tubulação...
             print('\nPara a correta execução deste programa, é necessário inserir o valor do Diâmetro da tubulação.')
             if len (V) < 1 and len (Q) < 1: #Se, em adição, o valor V e Q estão em branco.
                  print('\nAlém disso, também é necessário inserir o valor da Velocidade ou Vazão do fluido.') 
             continue
        elif len(V) < 1 and len(Q) <1: #se o usuário não digitou nem a informação da velocidade e nem da vazão...
             print('\nPara a correta execução deste programa, é necessário também inserir o valor da velocidade ou da vazão.')
             continue 
        
        #Os erros foram tratados. Caso não haja um erro, o programa continua normalmente.
        
        if len(V) < 1: #se o usuário não digitou a informação da velocidade...
                try: #Tentando executar o código...Sem erros, o código funcionará bem.
                    D_float = float(D)
                    Q_float = float(Q)
                    A_float = 3.14*D_float**2/4 #cálculo da área da seção transversal da tubulação.
                    V_float = Q_float/A_float #em m/s
                except: #Se houver algum erro no código acima, então o usuário digitou alguma informação incorreta.
                    print('\nFoi detectada a inserção de um dado incorreto: por favor, verifique os dados e reinsira-os novamente:\n')
                    continue  #O programa volta a ler a primeira linha do WHILE
        else: #Se o usuário tem a informação da velocidade...está tudo ok e não preciso executar nenhuma ação adicional.
            try: #Tentando executar o código...Sem erros, o código funcionará bem.
                V_float = float(V)
                D_float = float(D)
            except: #Se houver algum erro no código acima, então o usuário digitou alguma informação incorreta.
                print('\nFoi detectada a inserção de um dado incorreto: por favor, verifique os dados e reinsira-os novamente:\n')
                continue  #O programa volta a ler a primeira linha do WHILE

    
        #Etapa 02: Somente para o fluido água: μ: viscosidade dinâmica (Pa*s ou N*s/m²) e ρ : massa específica (kg/m³);
        μ = 0.001 
        ρ = 998
        print('\nInformações do fluido água:')
        print(f'\nViscosidade dinâmica (μ): {μ}  (Pa*s ou N*s/m²)')
        print(f'\nMassa específica (ρ): {ρ}  (kg/m³)')


        #Etapa 03: Cálculo do número de Reynolds
        Re = ρ*V_float*D_float/μ #Cálculo do número de reynolds.
        print(f'\nO número de Reynolds calculado é {Re:.2f}') #aqui o número de reynolds [Re] está formatado para ser exibido com somente 2 casas decimais.


        #Etapa 04: Classificar o número de Reynolds obtido:
        if Re <= 2000: #Escoamento laminar
            print('O Escoamento observado é Laminar\n')
        elif Re >= 2000 and Re <= 4000: #Escoamento transitório;
            print('O Escoamento observado é Transitório\n')
        else: #Escoamento turbulento.
            print('O Escoamento observado é Turbulento\n')
    
        #Etapa 05: O Usuário gostaria de sair ou de permanecer no programa para mais cálculos?
        sair = input('Deseja Finalizar o programa? [s]im ou [n]ão: ')
        sair_final = sair.lower()
        if sair_final.startswith('s'): #quero finalizar o programa
            print('\nO programa foi finalizado')
            break
        else: #não quero finalizar o programa
            print('\nO programa não foi finalizado\n')
            continue #o programa volta para o começo do WHILE.
   