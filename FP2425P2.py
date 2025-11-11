# ----------------------------- POSICOES ---------------------------------
def cria_posicao(coluna, linha):
    """ Retorna uma posição com as coordenadas recebidas
        Args:
            coluna(str): string de indentificação da coluna
            linha(int): inteiro de identificação da linha
            
        Returns:
            posicao(tuple): tuplo com as coordenadas da posicao    
    """
    colunas_possiveis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    if type(coluna) != str or type(linha) != int:
        raise ValueError("cria_posicao: argumentos invalidos")
    if linha > 10 or linha < 1 or coluna not in colunas_possiveis:
        raise ValueError("cria_posicao: argumentos invalidos")
    
    posicao = (coluna, linha)   #TAD representado por tuplo da forma (coluna da posicao, linha da posicao)
    return posicao

def obtem_pos_col(pos):
    """ Retorna a coluna da posição recebida
        Args:
            pos(posicao): posicao a obter a coluna
            
        Returns:
            coluna(str): coluna da posicao recebida
    """
    coluna = pos[0]
    return coluna

#FUNCAO AUXILIAR
def obtem_index_col(coluna):
    """ Retorna o index da coluna recebida
        Args:
            coluna(str): coluna a checar o index
            
        Returns:
            index(int): index da coluna recebida
    """
    colunas_possiveis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    index = colunas_possiveis.index(coluna) # Obtem index da coluna para facilitar em calculos que
    return index                            # precisem utilizar a coluna

def int_para_col(num):
    """ Retorna a coluna do index recebido
        Args:
            num(int): inteiro que representa o index da coluna a obter
            
        Returns:
            coluna(str): coluna correspondete ao index recebido
    """
    colunas_possiveis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    coluna = colunas_possiveis[num]
    return coluna

def obtem_pos_lin(pos):
    """ Retorna a linha da posicao recebida
        Args:
            pos(posicao): posicao a obter linha
            
        Returns:
            linha(int): linha da posicao recebida
    """
    linha = pos[1]
    return linha
    

def eh_posicao(pos):
    """ Retorna se a posicao recebida é uma posição
        Args:
            pos(posicao): posicao a verificar
            
        Returns:
            boolean: True se é uma posição, False caso contrário
    """
    if type(pos) == tuple:
        linha = obtem_pos_lin(pos)
        coluna = obtem_pos_col(pos)
        return type(linha) == int and type(coluna) == str and linha > 0 and linha <= 10 and len(coluna) == 1

def posicoes_iguais(p1, p2):
    """ Retorna se as posições recebidas são iguais
        Args:
            p1(posicao): primeira posição a comparar
            p2(posicao): segunda posição a comparar
            
        Returns:
            boolean: True se são posições iguais, Falso caso contrário
    """
    return eh_posicao(p1) and eh_posicao(p2) and p1 == p2   # Se p1 e p2 forem posicoes e forem iguais, 
                                                            # são a mesma posicao

def posicao_para_str(pos):
    """ Converte a posicao recebida para uma só string
        Args:
            pos(posicao): posicao a converter para string
            
        Returns:
            pos_str(str): posicao em formato de string
    """
    linha = obtem_pos_lin(pos)
    coluna = obtem_pos_col(pos)
    pos_str = coluna + str(linha) 
    return pos_str

def str_para_posicao(string):
    """ Converte a posicao recebida como string para uma posicao
        Args:
            string(str): posicao em string a ser convertida para posicao
            
        Returns:
            posicao(posicao): representação da string recebida mas como TAD posicao
    """
    posicao = ()
    for char in string:
        if char.isdigit():  # Verifica se o caractere é um número ou uma letra
            posicao += (int(char),)
        else:
            posicao += (char,)
    return posicao

def eh_posicao_valida(p, n):
    """ Verifica se a posicao recebida pertence à um tabuleiro com n orbitas
        Args:
            string(str): posicao em string a ser convertida para posicao
            
        Returns:
            posicao(posicao): representação da string recebida mas como TAD posicao
    """
    if eh_posicao(p) and n >= 2 and n <= 5:
        if obtem_pos_col(p) not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']:
            return False
        coluna = obtem_index_col(obtem_pos_col(p)) + 1
        linha = obtem_pos_lin(p)
        return linha <= 2 * n and coluna <= 2 * n
    raise ValueError("eh_posicao_valida: argumentos invalidos")
    
def obtem_posicoes_adjacentes(p, n, d):
    """ Retorna as posições adjacentes à posição recebida
        Args:
            p(posicao): posicao a verificar posicoes adjacentes
            n(int): numero de orbitas do tabuleiro
            d(boolean): True se for par aobter todas as posições adjacentes, Falso para obter só as ortogonais
            
        Returns:
            posicoes_adjacentes(tuple): tuplo com todas as posições adjacentes à posição recebida
    """
    if n >= 2 and n<= 5 and eh_posicao_valida(p, n) and d in (True, False):
        posicoes_adjacentes = ()
        coluna = obtem_index_col(obtem_pos_col(p)) + 1
        coluna_letra = obtem_pos_col(p)
        linha = obtem_pos_lin(p)
        dimensao = 2 * n
        if d:
            if linha > 1:           # Adiciona a posicao acima da pos inicial caso exista
                pos_i = cria_posicao(coluna_letra, linha - 1)
                posicoes_adjacentes += (pos_i,)
            if coluna < 2 * n:      # Adiciona a coluna a direita da pos inicial caso exista
                for l in range(linha - 1, linha + 2):
                    if l > 0 and l <= 2*n:
                        posicoes_adjacentes += (cria_posicao(int_para_col(coluna), l),)
            if linha < 2 * n:       # Adiciona pos abaixo da pos inicial caso exista
                posicoes_adjacentes += (cria_posicao(coluna_letra, linha + 1),)
            if coluna > 1:          # Adiciona a coluna a esquerda da pos inicial caso exista
                for l in range(linha + 1, linha - 2, -1):
                    if l > 0 and l <= 2*n:
                        posicoes_adjacentes += (cria_posicao(int_para_col(coluna - 2), l),)
            
            return posicoes_adjacentes
    
        # Caso d seja False, retorna as posicoes adjacentes ortogonais, caso existam
        if linha > 1:
            posicoes_adjacentes += ((coluna_letra, linha - 1),)
        if coluna > 1:
            posicoes_adjacentes += ((int_para_col(coluna - 2), linha),)
        if coluna < 2 * n:
            posicoes_adjacentes += ((int_para_col(coluna), linha),)
        if linha < 2 * n:
            posicoes_adjacentes += ((coluna_letra, linha + 1),)
        
        return posicoes_adjacentes    

def ordena_posicoes(t, n):
    """ Retorna as posições ordenadas
        Args:
            t(tuple): tuplo com as posicoes a ordenar
            n(int): numero de orbitas do tabuleiro
            
        Returns:
            posicoes_adjacentes(tuple): tuplo com todas as posições adjacentes à posição recebida
    """
    if all(eh_posicao_valida(p, n) for p in t):
        posicoes = ()
        posicoes_ordenadas = ()
        for pos in t:
            coluna = obtem_index_col(obtem_pos_col(pos)) + 1
            linha = obtem_pos_lin(pos)
            distancia = max(abs(coluna - n - .5), abs(linha - n - .5))  # Calcula a distancia da posicao
                                                                        # ao centro do tabuleiro
            dist_borda = min(coluna - 1, linha - 1, abs(2 * n - coluna), abs(2 * n - linha))
             # ^^ Calcula a distancia da posicao à borda mais próxima (posicoes com mesma distancia à borda mais
            # proxima pertencem à mesma órbita)
            
            posicoes += ((pos, distancia -.5, dist_borda),)

        for dist_b in range(n, -1, -1):
            lista = list(filter(lambda x: x[2] == dist_b, posicoes))    # Filtra as posicoes por orbita
            for dist_c in range(0, n + 1):
                posicoes_nessa_dist = list(filter(lambda x: x[1] == dist_c, lista))
                # ^^ Filtra as posicoes por distancia ao centro do tabuleiro
                for l in range(1, 2*n + 1):
                    for el in posicoes_nessa_dist:
                        if obtem_pos_lin(el[0]) == l:
                            posicoes_ordenadas += (el[0],)

        return posicoes_ordenadas
    else:
        raise ValueError("ordena_posicoes: argumentos invalidos")
        
# ------------------------------ PEDRA -----------------------------------
# TAD pedra tem como representação um tuplo contendo uma string com o tipo da pedra

def cria_pedra_branca():
    pedra = ("branca",)
    return pedra

def cria_pedra_preta():
    pedra = ("preta",)
    return pedra

def cria_pedra_neutra():
    pedra = ("neutra",)
    return pedra

#FUNCAO AUXILIAR
def obtem_jogador(pedra):
    return pedra[0]

def eh_pedra(arg):
    """ Verifica se o argumento recebido é uma pedra
        Args:
            arg(any): argumento a verificar se é uma pedra
            
        Returns:
            booleano: True se o argumento recebido for uma pedra, False caso contrário
    """
    if isinstance(arg, tuple):
        if (obtem_jogador(arg) == "branca" or obtem_jogador(arg) == "preta" or obtem_jogador(arg) == "neutra") and (len(arg) == 1 or len(arg) == 3):
            return True
    return False

def eh_pedra_branca(pedra):
    return obtem_jogador(pedra) == "branca"

def eh_pedra_preta(pedra):
    return obtem_jogador(pedra) == "preta"

def str_para_pedra(str_p):
    """ Transforma uma string recebida em pedra
        Args:
            str_p(string): string a ser convertida em posicao
            
        Returns:
            pedra(pedra): retorna a pedra correspondente à string recebida
    """
    if str_p == "X":
        return cria_pedra_preta()
    elif str_p == "O":
        return cria_pedra_branca()
    else:
        return cria_pedra_neutra()

def pedra_para_str(pedra):
    """ Transforma a pedra recebida em uma string
        Args:
            pedra(pedra): pedra a ser convertida em string
            
        Returns:
            str(string): string com a representação da pedra recebida
    """
    if eh_pedra_branca(pedra):
        return "O"
    elif eh_pedra_preta(pedra):
        return "X"
    return " "

def pedras_iguais(p1, p2):
    """ Verifica se duas pedras são iguais
        Args:
            p1(pedra): primeira pedra a comparar
            p2(pedra): segunda pedra a comparar
            
        Returns:
            boolean: True se as pedras forem iguais, False caso contrario
    """
    if eh_pedra(p1) and eh_pedra(p2):
        return p1 == p2

def eh_pedra_jogador(pedra):
    """ Verifica se a pedra é de algum jogador
        Args:
            pedra(pedra): pedra a verificar
            
        Returns:
            boolean: True se a pedra for de algum jogador, False caso contrário
    """
    if not eh_pedra(pedra):
        raise ValueError("eh_pedra_jogador: argumentos invalidos")
    return eh_pedra_branca(pedra) or eh_pedra_preta(pedra)

def pedra_para_int(pedra):
    """ Converte uma pedra pra sua representação em inteiro
        Args:
            pedra(pedra): pedra a converter
            
        Returns:
            inteiro: representação da pedra recebida como inteiro
    """
    if not eh_pedra(pedra):
        raise ValueError("pedra_para_int: argumentos invalidos")
    if eh_pedra_branca(pedra):
        return -1
    elif eh_pedra_preta(pedra):
        return 1
    return 0

#FUNCAO AUXILIAR
def int_para_pedra(num):
    """ Converte um inteiro pra sua representação como pedra
        Args:
            inteiro: representação da pedra como inteiro
            
        Returns:
            pedra(pedra): pedra a converter
    """
    if num == -1:
        return pedra_para_str(cria_pedra_branca())
    elif num == 1:
        return pedra_para_str(cria_pedra_preta())
    elif num == 0:
        return pedra_para_str(cria_pedra_neutra())
    

    
# ----------------------------- TABULEIRO --------------------------------
# TAD representado por uma lista de listas, cada uma contendo 2 * nr de orbitas de elementos, que variam entre -1, 0, 1
def cria_tabuleiro_vazio(n):
    """ Cria um tabuleiro vazio com n orbitas
        Args:
            n(int): numero de orbitas do tabuleiro vazio
            
        Returns:
            tab(tabuleiro): tabuleiro vazio com n orbitas
    """
    if type(n) != int or n < 2 or n > 5:
        raise ValueError("cria_tabuleiro_vazio: argumento invalido")
    tab = []
    for orbita in range(1, 2 * n + 1):
        linha = []
        for pos in range(1, 2 * n + 1):
            linha += [0,]   # Adiciona uma pedra neutra em formato de numero pra cada elemento de cada
                            # linha do tabuleiro
        tab += [linha,]
    return tab
    
def cria_tabuleiro(n, tp, tb):
    """ Cria um tabuleiro com as posicoes das pedras brancas e pretas marcadas
        Args:
            n(int): numero de orbitas do tabuleiro vazio
            tp(tuple): tuplo com as posicoes das pedras pretas
            tb(tuple): tuplo com as posicoes das pedras brancas
            
        Returns:
            tab(tabuleiro): tabuleiro com n orbitas com as posicoes das pedras brancas e pretas marcadas
    """
    if type(n) != int or n < 2 or n > 5 or type(tb) != tuple or type(tp) != tuple \
        or not all(eh_posicao_valida(p, n) for p in (tp + tb)):
        raise ValueError("cria_tabuleiro: argumentos invalidos")
    tab = cria_tabuleiro_vazio(n)
                
    linha_contador = 1
    tabuleiro_final = []
    for pos in tp:
        coluna = obtem_index_col(obtem_pos_col(pos))
        linha = obtem_pos_lin(pos)  # Adiciona ao tab vazio uma pedra preta em formato de numero
        tab[linha - 1][coluna] = 1
    for pos in tb:
        coluna = obtem_index_col(obtem_pos_col(pos))
        linha = obtem_pos_lin(pos)  # Adiciona ao tab vazio uma pedra branca em formato de numero
        tab[linha - 1][coluna] = -1
        
        linha_contador += 1
    
    return tab

                    
def cria_copia_tabuleiro(tab):
    """ Cria uma copia de um tabuleiro
        Args:
            tab(tabuleiro): tabuleiro a ser copiado
            
        Returns:
            tab_final(tabuleiro): tabuleiro copiado
    """
    if eh_tabuleiro(tab):
        tab_final = []
        for linha in tab:
            linha_nova = []
            for el in linha:
                linha_nova += [el]  # Copia cada elemento de cada linha do tab inicial para o novo tab
            tab_final += [linha_nova,]
        return tab_final

    
def obtem_numero_orbitas(tab):
    """ Obtem o numero de orbitas de um tabuleiro
        Args:
            tab(tabuleiro): tabuleiro a ser verificado
            
        Returns:
            inteiro: numero de orbitas do tabuleiro recebido
    """
    return len(tab) // 2

def obtem_pedra(tab, pos):
    """ Obtem a pedra na posicao do tabuleiro recebido
        Args:
            tab(tabuleiro): tabuleiro a ser verificado
            pos(posicao): posicao a obter pedra
            
        Returns:
            pedra(pedra): pedra contida na posição recebida
    """
    index_coluna = obtem_index_col(obtem_pos_col(pos))
    index_linha = obtem_pos_lin(pos) - 1
    jog = tab[index_linha][index_coluna]
    return int_para_pedra(jog)



def obtem_linha_horizontal(tab, pos):
    """ Obtem a linha horizontal que contem a posição recebida no tabuleiro recebido
        Args:
            tab(tabuleiro): tabuleiro a obter linha
            pos(posicao): posicao a obter linha
            
        Returns:
            tup_linha(tuple): tuplo com todas as posicoes contidas na linha horizontal da posicao recebida
    """
    colunas_possiveis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    tup_linha = ()
    index_linha = obtem_pos_lin(pos) - 1
    index_coluna = 0
    for element in tab[index_linha]:
        tup_linha += (((colunas_possiveis[index_coluna], index_linha + 1), str_para_pedra(int_para_pedra(element))),)
        index_coluna += 1
    return tup_linha


def obtem_linha_vertical(tab, pos):
    """ Obtem a linha vertical que contem a posição recebida no tabuleiro recebido
        Args:
            tab(tabuleiro): tabuleiro a obter linha
            pos(posicao): posicao a obter linha
            
        Returns:
            tup_linha(tuple): tuplo com todas as posicoes contidas na linha vertical da posicao recebida
    """
    tup_coluna = ()
    index_coluna = obtem_index_col(obtem_pos_col(pos))
    linha_contador = 1
    for linha in tab:
        jogador = tab[linha_contador - 1][index_coluna]
        tup_coluna += (((obtem_pos_col(pos), linha_contador), str_para_pedra(int_para_pedra(jogador))),)
        linha_contador += 1
    return tup_coluna

def obtem_linhas_diagonais(tab, pos):
    """ Obtem as linhas diagonais que contem a posição recebida no tabuleiro recebido
        Args:
            tab(tabuleiro): tabuleiro a obter linha
            pos(posicao): posicao a obter linha
            
        Returns:
            (diagonal, antidiagonal)(tuple): tuplo com dois tuplos, sendo o primeiro o que contem as posicoes da
            linha diagonal e o segundo da linha antidiagonal, ambos que contem a posicao recebida
    """
    diagonal = ()
    antidiagonal = ()
    
    nr_coluna = obtem_index_col(obtem_pos_col(pos)) + 1
    linha = obtem_pos_lin(pos)
    menor_distancia = min(nr_coluna, linha) # Calcula a menor distancia para as bordas
                                            # esquerda e superior do tabuleiro para a posicao recebida
    nr_col_lin = obtem_numero_orbitas(tab)
    # ^^ Numero de colunas e linhas do tabuleiro (que é igual ja que o tabuleiro é quadrado)
    
    inicio_diagonal = (int_para_col(nr_coluna - menor_distancia), linha - menor_distancia + 1)
    # ^^ Calcula a primeira posição da diagonal que contém a posição recebida
    
    coluna_inicial = obtem_index_col(obtem_pos_col(inicio_diagonal)) + 1
    linha_inicial = obtem_pos_lin(inicio_diagonal)
    
    while coluna_inicial <= nr_col_lin * 2 and linha_inicial <= nr_col_lin * 2:
        diagonal += ((inicio_diagonal, str_para_pedra(int_para_pedra(tab[linha_inicial - 1][coluna_inicial - 1]))),)
        coluna_inicial += 1
        linha_inicial += 1
        # Adiciona 1 à linha e à coluna de forma a obter a posicao à diagonal inferior esquerda
        # da posicao atual
        inicio_diagonal = (int_para_col(coluna_inicial - 1), linha_inicial)
        
    menor_distancia = min(nr_coluna - 1, nr_col_lin * 2 - linha)
    # ^^ Calcula a menor distancia da posicao às bordas do tabuleiro esquerda e inferior
    
    inicio_antidiagonal = (int_para_col(nr_coluna - menor_distancia - 1), linha + menor_distancia)
    # ^^ Calcula a posição inicial da antidiagonal
    coluna_inicial = obtem_index_col(obtem_pos_col(inicio_antidiagonal)) + 1
    linha_inicial = obtem_pos_lin(inicio_antidiagonal)
    
    while coluna_inicial <= nr_col_lin * 2 and linha_inicial <= nr_col_lin * 2 and linha_inicial >= 1 and coluna_inicial > 0:
        antidiagonal += ((inicio_antidiagonal, str_para_pedra(int_para_pedra(tab[linha_inicial - 1][coluna_inicial - 1]))),)
        coluna_inicial += 1
        linha_inicial -= 1
        # Adiciona um a coluna inicial e subtrai um da linha inicial de forma a obter a posicao
        # que se encontra na diagonal superior direita da posicao atual
        inicio_antidiagonal = int_para_col(coluna_inicial - 1), linha_inicial
        
    return diagonal, antidiagonal

def obtem_posicoes_pedra(tab, jog):
    """ Obtem as posicoes da pedra recebida no tabuleiro recebido
        Args:
            tab(tabuleiro): tabuleiro a verificar
            jog(pedra): pedra a verificar posicoes
            
        Returns:
            posicoes_pedra(tuple): tuplo com todas as posicoes do tabuleiro tab com a pedra jog
    """
    posicoes = ()
    linha_contador = 1
    for linha in tab:
        coluna_contador = 0
        for element in linha:
            if str_para_pedra(int_para_pedra(element)) == jog:
                posicoes += ((int_para_col(coluna_contador), linha_contador),)
            coluna_contador += 1
        linha_contador += 1
    posicoes_pedra = ordena_posicoes(posicoes, obtem_numero_orbitas(tab))
    return posicoes_pedra

def coloca_pedra(tab, pos, pedra):
    """ Coloca uma pedra na posicao recebida
        Args:
            tab(tabuleiro): tabuleiro a modificar
            pos(posicao): posicao a colocar pedra
            pedra(pedra): pedra a colocar 
            
        Returns:
            tab(tabuleiro): retorna o tabuleiro recebido mas modificado, com a pedra colocada na posicao recebida
    """
    linha = obtem_pos_lin(pos)
    coluna = obtem_pos_col(pos)
    index_coluna = obtem_index_col(coluna)
    tab[linha - 1][index_coluna] = pedra_para_int(pedra)
    
    return tab
    
def remove_pedra(tab, pos):
    """ Remove uma pedra na posicao recebida
        Args:
            tab(tabuleiro): tabuleiro a modificar
            pos(posicao): posicao a colocar pedra
            
        Returns:
            tab(tabuleiro): retorna o tabuleiro recebido mas modificado, com a pedra removida na posicao recebida
    """
    linha = obtem_pos_lin(pos)
    index_coluna = obtem_index_col(obtem_pos_col(pos))
    tab[linha - 1][index_coluna] = 0
    
    return tab

def eh_tabuleiro(tab):
    """ Verifica se o argumento recebido é um tabuleiro
        Args:
            tab(tabuleiro): tabuleiro a verificar
            
        Returns:
            boolean: True se o argumento recebido for um tabuleiro, False caso contrário
    """
    if type(tab) == list:
        if obtem_numero_orbitas(tab) >= 2 and obtem_numero_orbitas(tab) <= 5:
            if all(type(linha) == list for linha in tab):
                for linha in tab:
                    return len(linha) == obtem_numero_orbitas(tab) * 2 and all(el in [-1, 0, 1] for el in linha)
    return False
    
def tabuleiros_iguais(t1, t2):
    """ Verifica se dois tabuleiros recebidos são iguais
        Args:
            t1(tabuleiro): primeiro tabuleiro a comparar
            t2(tabuleiro): segundo tabuleiro a comparar
            
        Returns:
            boolean: True se os tabuleiros forem iguais, False caso contrário
    """
    if eh_tabuleiro(t1) and eh_tabuleiro(t2):
        return t1 == t2

def tabuleiro_para_str(tab):
    """ Converte um tabuleiro para sua representação em string
        Args:
            tab(tabuleiro): tabuleiro a converter
            
        Returns:
            tabuleiro_final(str): representacao do tabuleiro recebido em string
    """
    n = obtem_numero_orbitas(tab)
    tabuleiro_final = "    "
    tamanho_linha = obtem_numero_orbitas(tab) * 2 - 1   # Index mámixo das linhas   
    nr_colunas = 2 * n
    linha_contador = 1
    
    # For loop para adicionar o identificador de cada coluna
    for coluna in range(1, nr_colunas + 1):
            tabuleiro_final += f"{int_para_col(coluna - 1)}"
            if coluna <= tamanho_linha:
                tabuleiro_final += "   "
    tabuleiro_final += "\n"
    
    # For loop para adicionar identificador de cada linha e os valores de cada posicao delas
    for linha in tab:
        tabuleiro_final += f"{str(linha_contador).zfill(2)} "
        index_element = 0
        for element in linha:
            pedra = int_para_pedra(element)
            tabuleiro_final += f"[{pedra}]"
            if index_element < tamanho_linha:
                tabuleiro_final += "-"
            else:
                if linha_contador < 2 * obtem_numero_orbitas(tab):
                    tabuleiro_final += "\n    "
                    for num in range(1, tamanho_linha + 2):
                        tabuleiro_final += "|"
                        if num <= tamanho_linha:
                            tabuleiro_final += "   "
                        else:
                            tabuleiro_final += "\n"
                    
            index_element += 1
        linha_contador += 1
        
    return tabuleiro_final


def move_pedra(t, p1, p2):
    """ Move uma pedra de uma dada posição à outra
        Args:
            t(tabuleiro): tabuleiro a modificar
            p1(posicao): posicao original da pedra
            p2(posicao): posicao final da pedra
            
        Returns:
            t(tabuleiro): tabuleiro recebido modificado, com uma pedra em posicao diferente
    """
    if eh_tabuleiro(t):
        n = obtem_numero_orbitas(t)
        if eh_posicao_valida(p1, n) and eh_posicao_valida(p2, n):
            pedra = str_para_pedra(obtem_pedra(t, p1))
            coloca_pedra(t, p2, pedra)
            remove_pedra(t, p1)
            # Remove a pedra da posicao inicial e coloca a mesma na posicao final

            return t
    raise ValueError("move_pedra: argumentos invalidos")

#FUNCAO AUXILIAR
# Calcula a órbita de uma dada posicao a partir da distancia desta à borda do tabuleiro mais próxima
def obtem_orbita_pos(t, p):
    """ Obtem a orbita da posicao recebida
        Args:
            t(tabuleiro): tabuleiro a verificar
            p(posicao): posicao a obter orbita
            
        Returns:
            orbita(int): orbita a que pertence a posicao recebida
    """
    tamanho_tab = obtem_numero_orbitas(t) * 2
    distancia_esquerda = obtem_index_col(obtem_pos_col(p)) + 1
    distancia_direita = tamanho_tab - distancia_esquerda + 1
    distancia_cima = obtem_pos_lin(p) 
    distancia_embaixo = tamanho_tab - distancia_cima + 1
    
    orbita = min(distancia_cima, distancia_embaixo, distancia_direita, distancia_esquerda)
    
    return orbita

#FUNCAO AUXILIAR
# Obtem todas as posicoes de uma dada orbita
def obtem_posicoes_da_orbita(t, orbita):
    """ Obtem todas as posições de uma orbita
        Args:
            t(tabuleiro): tabuleiro a verificar
            orbita(int): orbita a verificar
            
        Returns:
            posicoes_orbita(tuple): todas as posições da órbita recebida
    """
    posicoes_orbita = ()
    linha_index = 1
    for linha in t:
        coluna_index = 0
        for element in linha:
            pos = (int_para_col(coluna_index), linha_index)
            if obtem_orbita_pos(t, pos) == orbita:
                posicoes_orbita += (pos,)
            coluna_index += 1
        linha_index += 1
    return posicoes_orbita
    
def obtem_posicao_seguinte(t, p, s):
    """ Obtem a posição seguinte à posicao recebida
        Args:
            t(tabuleiro): tabuleiro a verificar
            p(posicao): posicao original da pedra
            s(boolean): True para verificar em sentido horário, False para sentido anti-horario
            
        Returns:
            posicao(posicao): posicao seguinte à posicao recebida
    """
    if eh_tabuleiro(t):
        n = obtem_numero_orbitas(t)
        if eh_posicao_valida(p, n) and s in [True, False]:
            orbita = obtem_orbita_pos(t, p)
            posicoes_orbita = obtem_posicoes_da_orbita(t, orbita)
            index_posicao = posicoes_orbita.index(p)
            primeira_coluna_orbita = obtem_pos_col(posicoes_orbita[0])
            ultima_coluna_orbita = obtem_pos_col(posicoes_orbita[-1])
            ultima_linha_orbita = obtem_pos_lin(posicoes_orbita[-1])
            primeira_linha_orbita = obtem_pos_lin(posicoes_orbita[0])
            linha_pos = obtem_pos_lin(posicoes_orbita[index_posicao])
            coluna_pos = obtem_pos_col(posicoes_orbita[index_posicao])
            if s:
                if coluna_pos == primeira_coluna_orbita:
                    if linha_pos == primeira_linha_orbita:
                        return posicoes_orbita[index_posicao + 1]
                    else:
                        pos = (coluna_pos, linha_pos - 1)
                        return pos
                elif coluna_pos == ultima_coluna_orbita:
                    if linha_pos == ultima_linha_orbita:
                        return posicoes_orbita[index_posicao - 1]
                    else:
                        pos = (coluna_pos, linha_pos + 1)
                        return pos
                else:
                    if linha_pos == primeira_linha_orbita:
                        return posicoes_orbita[index_posicao + 1]
                    else:
                        return posicoes_orbita[index_posicao - 1]
            else:
                if coluna_pos == primeira_coluna_orbita:
                    if linha_pos == ultima_linha_orbita:
                        return posicoes_orbita[index_posicao + 1]
                    else:
                        pos = (coluna_pos, linha_pos + 1)
                        return pos
                elif coluna_pos == ultima_coluna_orbita:
                    if linha_pos == primeira_linha_orbita:
                        return posicoes_orbita[index_posicao - 1]
                    else:
                        pos = (coluna_pos, linha_pos - 1)
                        return pos
                else:
                    if linha_pos == primeira_linha_orbita:
                        return posicoes_orbita[index_posicao - 1]
                    else:
                        return posicoes_orbita[index_posicao + 1]
        else:
            raise ValueError("obtem_posicao_seguinte: argumentos invalidos")
            
def roda_tabuleiro(t):
    """ Roda o tabuleiro em sentido anti-horário
        Args:
            t(tabuleiro): tabuleiro a modificar
            
        Returns:
            t(tabuleiro): tabuleiro modificao, com uma rotação
    """
    if not eh_tabuleiro(t):
        raise ValueError("roda_tabuleiro: argumentos invalidos")
    
    posicoes_antes = {}
    for pos in obtem_posicoes_pedra(t, str_para_pedra(int_para_pedra(-1))):
        # Guarda posicoes que contem pedras brancas no dicionario
        posicoes_antes[pos] = -1
        remove_pedra(t, pos)
    for pos in obtem_posicoes_pedra(t, str_para_pedra(int_para_pedra(1))):
        # Guarda posicoes que contem pedras pretas no dicionario
        posicoes_antes[pos] = 1
        remove_pedra(t, pos)
    for pos in posicoes_antes:
        pedra = str_para_pedra(int_para_pedra(posicoes_antes[pos]))
        coloca_pedra(t, obtem_posicao_seguinte(t, pos, False), pedra)
        # ^^ Adiciona a pedra de cada posicao na posicao seguinte à ela
    return t

def verifica_linha_pedras(t, p, j, k):
        """ Verifica se uma posicao esta contida em alguma linha com k pedras j consecutivas
            Args:
                t(tabuleiro): tabuleiro a verificar
                p(posicao): posicao a verificar linhas
                j(pedra): pedra a verificar
                k(int): numero de pedras seguidas
                
            Returns:
                boolean: True se há uma linha que passa em p e tem k pedras j consecutivas, False caso contrário
        """
        linha = obtem_linha_horizontal(t, p)
        coluna = obtem_linha_vertical(t, p)
        diagonal = obtem_linhas_diagonais(t, p)[0]
        antidiagonal = obtem_linhas_diagonais(t, p)[1]
        position = (p, str_para_pedra(obtem_pedra(t, p)))
        conjuntos = (linha, coluna, diagonal, antidiagonal,)
        index = 0
        for conjunto in conjuntos:
            index += 1
            idx = conjunto.index(position)
            for num in range(k):
                linha_num = conjunto[idx - num:idx + k - num]
                if len(linha_num) == k:
                    lista = [element for element in linha_num]
                    if all(element[1] == j for element in linha_num):
                        return True
        return False
        
# ------------------------- FUNCOES AUXILIARES -----------------------------
def obtem_posicoes_neutras(t):
    """ Obtem todas as posicoes neutras do tabuleiro recebido
            Args:
                t(tabuleiro): tabuleiro a verificar
                
            Returns:
                posicoes(tuple): tuplo com todas as posicoes neutras do tabuleiro recebido
        """
    posicoes = ()
    jog = pedra_para_int(cria_pedra_neutra())
    linha_contador = 1
    for linha in t:
        coluna_contador = 1
        for element in linha:
            if element == jog:
                posicoes += ((int_para_col(coluna_contador - 1), linha_contador),)
            coluna_contador += 1
        linha_contador += 1
    return posicoes

def eh_vencedor(t, j):
    """ Verifica se a pedra j é vencedora no tabuleiro t
            Args:
                t(tabuleiro): tabuleiro a verificar
                j(pedra): pedra a verificar
                
            Returns:
                boolean: True se a pedra j é vencedora, False caso contrário
    """
    posicoes_jogador = obtem_posicoes_pedra(t, j)
    k = obtem_numero_orbitas(t) * 2
    for pos in posicoes_jogador:
        if verifica_linha_pedras(t, pos, j, k):
            return True
    return False

def eh_fim_jogo(t):
    """ Verifica se é fim de jogo em dado tabuleiro t
            Args:
                t(tabuleiro): tabuleiro a verificar
                
            Returns:
                boolean: True se a pedra é fim de jogo no tabuleiro t, False caso contrário
    """
    if eh_vencedor(t, cria_pedra_preta()) or eh_vencedor(t, cria_pedra_branca()):
        return True
    elif obtem_posicoes_neutras == ():
        return True
    return False

def escolhe_movimento_manual(t):
    """ Retorna movimento manual escolhido pelo jogador
            Args:
                t(tabuleiro): tabuleiro a verificar
                
            Returns:
                posicao_escolhida(posicao): retorna a posicao escolhida
    """
    posicao_escolhida = input("Escolha uma posicao livre:")
    if str_para_posicao(posicao_escolhida) in obtem_posicoes_neutras(t):
        return str_para_posicao(posicao_escolhida)
    return escolhe_movimento_manual(t)

def escolhe_movimento_auto(t, j, lvl):
    """ Retorna movimento escolhido pelo computador
            Args:
                t(tabuleiro): tabuleiro a verificar
                j(pedra): pedra que representa o computador
                lvl(string): nivel de dificuldade do computador
                
            Returns:
                pos_final(posicao): posicao escolhida pelo computador
    """
    n = obtem_numero_orbitas(t)
    
    # Obtem a pedra do adversario
    if j == cria_pedra_preta():
        adversario = cria_pedra_branca()
    else:
        adversario = cria_pedra_preta()
    
    if lvl == "facil":
        t1 = cria_copia_tabuleiro(t)
        roda_tabuleiro(t1)
        for pos in obtem_posicoes_neutras(t1):
            if pos in [obtem_posicoes_adjacentes(p, n, True) for p in obtem_posicoes_pedra(t1, j)]:
                return pos  # Retorna a primeira posicao neutra que após a rotação do tab, se encontra adjacente à uma pedra própria
        pos = ordena_posicoes(obtem_posicoes_neutras(t), n)[0]
        return pos
    
    elif lvl == "normal":
        L_jog = []
        k = 2 * obtem_numero_orbitas(t)     # k = maximo de pedras seguidas possiveis de se fazer no tabuleiro
        posicoes_livres = obtem_posicoes_neutras(t)
        
        t1 = cria_copia_tabuleiro(t)
        t1 = roda_tabuleiro(t1)
        t2 = roda_tabuleiro(t1)
        
        # For loop para simular o maior L (numero de pedras seguidas) possiveis de se fazer apos colocar pedra em cada uma das
        # posicoes livres do tabuleiro e rotacioná-lo
        
        for pos in posicoes_livres:
            pos_seguinte = obtem_posicao_seguinte(t1, pos, False)
            coloca_pedra(t1, pos_seguinte, j)
            
            for L in range(1, 2*n + 1):
                if verifica_linha_pedras(t1, pos_seguinte, j, L):
                    L_jog += [(L, pos)]
            
            todos_os_L = [L[0] for L in L_jog ]

            if max(todos_os_L) < 2*n:
                p = obtem_posicao_seguinte(t1, pos_seguinte, False)
                for L in range(1, 2*n + 1):
                    if verifica_linha_pedras(roda_tabuleiro(t1), p, adversario, k):
                        L_jog += [(L, pos)]
                        
                        
            t1 = remove_pedra(t1, pos_seguinte)
            t2 = remove_pedra(t2, pos_seguinte)
                
        todos_os_L = [L[0] for L in L_jog ]
        L_max = max(todos_os_L) # Obtem o maior L entre o L do jogador e do adversario
        index_L = todos_os_L.index(L_max)
        pos_final = L_jog[index_L][1]
        return pos_final
        
            
def orbito(n, modo, jog):
    """ Jogo orbito-n
            Args:
                n(int): numero de orbitas do tabuleiro do jogo
                modo(string): modo de jogo
                jog(pedra): pedra do jogador
                
            Returns:
                vencedor(int): retorna o numero que representa o vencedor
    """
    if n < 2 or n > 5 or modo not in ["facil", "normal", "2jogadores"] or jog not in ['X', 'O']:
        raise ValueError("orbito: argumentos invalidos")
    print(f"Bem-vindo ao ORBITO-{n}.")
    jog = str_para_pedra(jog)
    adv = str_para_pedra(int_para_pedra(-pedra_para_int(jog)))
    t = cria_tabuleiro_vazio(n)
    if modo != "2jogadores":
        print(f"Jogo contra o computador ({modo}).")
        print(f"O jogador joga com '{pedra_para_str(jog)}'.")
        
        print(tabuleiro_para_str(t))
        
        if eh_pedra_preta(jog):
            while not eh_fim_jogo(t):
                
                print("Turno do jogador.")
                pos_j = escolhe_movimento_manual(t)
                t = coloca_pedra(t, pos_j, jog)
                t = roda_tabuleiro(t)
                print(tabuleiro_para_str(t))
                if eh_fim_jogo(t):
                    break
                
                print(f"Turno do computador ({modo}):")            
                pos_c = escolhe_movimento_auto(t, adv, modo)
                t = coloca_pedra(t, pos_c, adv)
                t = roda_tabuleiro(t)
                print(tabuleiro_para_str(t))
        
        elif eh_pedra_branca(jog):
            while not eh_fim_jogo(t):
                print(f"Turno do computador ({modo}):")            
                pos_c = escolhe_movimento_auto(t, adv, modo)
                t = coloca_pedra(t, pos_c, adv)
                t = roda_tabuleiro(t)
                print(tabuleiro_para_str(t))
                if eh_fim_jogo(t):
                    break
                
                print("Turno do jogador.")
                pos_j = escolhe_movimento_manual(t)
                t = coloca_pedra(t, pos_j, jog)
                t = roda_tabuleiro(t)
                print(tabuleiro_para_str(t))
                
        
        if (eh_vencedor(t, jog) and eh_vencedor(t, adv)) or (not eh_vencedor(t, jog) and not eh_vencedor(t, adv)):
            print("EMPATE")
            return 0
        elif eh_vencedor(t, jog):
            print("VITORIA")
            return pedra_para_int(jog)
        elif eh_vencedor(t, adv):
            print("DERROTA")
            return pedra_para_int(adv)
        
    else:
        print("Jogo para dois jogadores.")
        print(tabuleiro_para_str(t))
        while not eh_fim_jogo(t):
            print("Turno do jogador 'X'.")
            pos_x = escolhe_movimento_manual(t)
            t = coloca_pedra(t, pos_x, cria_pedra_preta())
            t = roda_tabuleiro(t)
            print(tabuleiro_para_str(t))
            if eh_fim_jogo(t):
                break
            
            print("Turno do jogador 'O'.")
            pos_o = escolhe_movimento_manual(t)
            t = coloca_pedra(t, pos_o, cria_pedra_branca())
            t = roda_tabuleiro(t)
            print(tabuleiro_para_str(t))
            
        if (eh_vencedor(t, jog) and eh_vencedor(t, adv)) or (not eh_vencedor(t, jog) and not eh_vencedor(t, adv)):
            print("EMPATE")
            return 0
        elif eh_vencedor(t, jog):
            print(f"VITORIA DO JOGADOR '{pedra_para_str(jog)}'")
            return pedra_para_int(jog)
        elif eh_vencedor(t, adv):
            print(f"VITORIA DO JOGADOR '{pedra_para_str(adv)}'")
            return pedra_para_int(adv)
        