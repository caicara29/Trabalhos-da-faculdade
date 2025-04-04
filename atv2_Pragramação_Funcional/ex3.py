def exercicio_03():
    # a) 
    # Exemplo de entrada (em uma única linha): "1:23.5 2:24.0 3:26.0 4:25.2 5:26.5"
    entrada = input("Digite os dados de fechamento (ex.: 1:23.5 2:24.0 3:26.0):\n").strip().split()
    
    # Monta o dicionário {dia (int): preço (float)}
    precos = {
        int(dia): float(valor) 
        for dia, valor in (par.split(':') for par in entrada)
    }

    # b) Função de primeira classe que retorna lambda para testar limite
    def criar_teste_limite(limite):
        """
        Retorna uma função lambda que verifica
        se o valor de fechamento está acima do 'limite'.
        """
        return lambda valor: valor > limite

    # c) Filtrar (com filter) os dias com valores acima de R$ 25.00
    #    lembrem-se: precos.items() gera (dia, valor)
    dias_acima_25 = list(filter(lambda x: criar_teste_limite(25.0)(x[1]), precos.items()))
    
    # Ordenar os dias resultantes por dia 
    dias_acima_25 = sorted(dias_acima_25, key=lambda x: x[0])
    # Agora apenas a lista dos dias
    dias_acima_25 = [dia for dia, _ in dias_acima_25]

    print("\nDias com valor acima de R$ 25.0:")
    print(dias_acima_25)

    # d) Calcular variação percentual diária: {dia -> variação%}
    #    A variação do dia 'i' é calculada em relação ao dia imediatamente anterior
    dias_ordenados = sorted(precos.keys())
    variacao_percentual = {}
    for i in range(1, len(dias_ordenados)):
        dia_atual = dias_ordenados[i]
        dia_anterior = dias_ordenados[i - 1]
        preco_atual = precos[dia_atual]
        preco_anterior = precos[dia_anterior]
        
        # Cálculo da variação percentual
        variacao = ((preco_atual - preco_anterior) / preco_anterior) * 100
        # Armazenamos com duas casas decimais:
        variacao_percentual[dia_atual] = round(variacao, 2)

    print("\nVariação percentual diária:")
    print(variacao_percentual)

    # e) Maior alta e maior queda
    #    Se houver apenas 1 dia, variacao_percentual ficará vazio, então checamos antes de usar max/min
    if variacao_percentual:
        maior_alta = max(variacao_percentual.items(), key=lambda x: x[1])
        maior_queda = min(variacao_percentual.items(), key=lambda x: x[1])

        print(f"\nMaior alta: Dia {maior_alta[0]} - {maior_alta[1]}%")
        print(f"Maior queda: Dia {maior_queda[0]} - {maior_queda[1]}%")
    else:
        print("Não foi possível calcular variação (é preciso ao menos 2 dias).")

    # f) Calcular a média dos preços
    if precos:
        media = sum(precos.values()) / len(precos)
        print(f"\nMédia dos preços: R$ {media:.2f}")
    else:
        media = 0
        print("Não há dados de preços para calcular a média.")

    # g) Função de primeira classe para comparar com média
    def comparar_com_media(m):
        """
        Retorna uma função lambda que classifica o valor
        como "acima da média" ou "abaixo da média".
        """
        return lambda valor: "acima da média" if valor > m else "abaixo da média"

    # Gera um novo dicionário com a forma:
    # {dia: ("acima da média" ou "abaixo da média", valor), ...}
    comparar = comparar_com_media(media)
    classificacao = {
        dia: (comparar(valor), valor) 
        for dia, valor in sorted(precos.items())
    }

    print("\nClassificação de cada dia em relação à média:")
    print(classificacao)

if __name__ == "__main__":
    exercicio_03()
