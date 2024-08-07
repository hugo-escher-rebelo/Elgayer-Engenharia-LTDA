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

#Dicionário com todos os fluidos disponíveis para calcular o número de Reynolds:
fluidos = [
     {'Nome': 'Hidrogenio',
      'nome': 'hidrogenio',
      'μ' : 9.05*(10**-6) ,
      'ρ' : 0.0839, } ,
      {'Nome': 'Ar',
       'nome': 'ar', 
      'μ' : 1.80*(10**-5) ,
      'ρ' : 1.20, } ,
      {'Nome': 'Gasolina',
       'nome': 'gasolina', 
      'μ' : 2.92*(10**-4) ,
      'ρ' : 680, } ,
      {'Nome': 'Agua', 
       'nome': 'agua',
      'μ' : 1*(10**-3) ,
      'ρ' : 998, } ,
      {'Nome': 'Alcool Etilico',
       'nome': 'alcool etilico', 
      'μ' : 1.20*(10**-3) ,
      'ρ' : 789, } ,
      {'Nome': 'Mercurio',
       'nome': 'mercurio',
      'μ' : 1.56*(10**-3) ,
      'ρ' : 13550, } ,
      {'Nome': 'Oleo SAE 10W', 
       'nome': 'oleo sae 10w',
      'μ' : 1.04*(10**-1) ,
      'ρ' : 870, } ,
      {'Nome': 'Oleo SAE 30W',
       'nome': 'oleo sae 30w', 
      'μ' : 2.90*(10**-1) ,
      'ρ' : 891, } ,
      {'Nome': 'Agua do Mar', 
       'nome': 'agua do mar',
      'μ' : 1.07*(10**-3) ,
      'ρ' : 1025, } ,
      {'Nome': 'Glicerina',
       'nome': 'glicerina', 
      'μ' : 1.49 ,
      'ρ' : 1260, } ,
      {'Nome': 'Gas Carbonico',
       'nome': 'gas carbonico', 
      'μ' : 1.48*(10**-5) ,
      'ρ' : 1.82, } ,
      {'Nome': 'Azeite de Oliva',
       'nome': 'azeite de oliva', 
      'μ' : 84*(10**-3) ,
      'ρ' : 890, } ,
]
#set com todos os 'nomes' dos fluidos disponíveis para a escolha pelo usuário.
nomes_fluido = {'hidrogenio', 'ar', 'gasolina', 'agua', 'alcool etilico', 'mercurio', 'oleo sae 10w', 'oleo sae 30w', 'agua do mar', 'glicerina', 'gas carbonico', 'azeite de oliva'}

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

    
        #Etapa 02: Para qualquer fluido dentro do dicionário 'fluidos': μ: viscosidade dinâmica (Pa*s ou N*s/m²) e ρ : massa específica (kg/m³);
        print('\nOs fluidos disponíveis para o cálculo do Número de Reynolds são:')
        for fluido in fluidos: #acessando cada fluido do dicionário 'fluidos'
             print()
             print(f'Nome: {fluido['Nome']}')
             print(f'μ : {fluido['μ']}')
             print(f'ρ : {fluido['ρ']}')
             print()    #Aqui, fizemos a impressão das informações de cada fluido.
        fluido_desejado = input('Insira o nome do fluido desejado (Sem acentos): ') #Inserção do fluido desejado pelo usuário.
        fluido_desejado = fluido_desejado.lower() #transformar o nome inserido em letras minusculas.
        
        if fluido_desejado in nomes_fluido: #Se o fluido desejado existe no dicionário:
             
            for fluido in fluidos: #acessando cada fluido do dicionário 'fluidos'
                if fluido_desejado == fluido['nome']: #Quando o fluido inserido for igual ao nome do fluido disponível no dicionário...
                    μ = fluido['μ'] #Aqui, definimos os valores das incognitas baseadas no fluido escolhido pelo usuário.
                    ρ = fluido['ρ']  

        else: #O fluido não existe no dicionário
            print('\nO fluido desejado não se encontra disponível na base de dados. Por favor, re-insira os dados e tente novamente:')
            continue #O programa volta a ler a primeira linha do WHILE
            

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