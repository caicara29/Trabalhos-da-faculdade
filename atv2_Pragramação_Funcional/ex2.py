def exercicio_02():
    # a) Ler gabarito e respostas dos candidatos
    # Ex.: gabarito = "A C D B A" -> ["A", "C", "D", "B", "A"] -> "ACDBA"
    gabarito = input("Gabarito oficial da prova (ex.: A C D B A):\n").strip().split()
    gabarito = ''.join(gabarito)  # Transforma em string contínua (ex.: "ACDBA")
    
    # Ex.: candidatos = "Ana:ACDBA Bruno:ACDCA Carla:ACABA"
    entrada_candidatos = input("Lista de candidatos (ex.: Ana:ACDBA Bruno:ACDCA ...):\n").strip().split()
    # Converte em lista de tuplas
    candidatos = [
        (nome, respostas)
        for nome, respostas in (c.split(':') for c in entrada_candidatos)
    ]

    # b) 
    def avaliador(gab):
        """Retorna uma função lambda que compara as respostas do candidato 
           com o gabarito e computa a nota (máx. 10)."""
        total_questoes = len(gab)
        pontos_por_questao = 10 / total_questoes  # Nota máxima é 10
        
        return lambda respostas: (
            sum(
                1 
                for i in range(min(len(respostas), total_questoes)) 
                if respostas[i] == gab[i]
            ) 
            * pontos_por_questao
        )

    # c) Avaliar todos os candidatos com map()
    avaliar = avaliador(gabarito)
    notas = list(map(lambda x: (x[0], avaliar(x[1])), candidatos))
    

    # d) Filtrar aprovados (nota >= 7)
    aprovados = list(filter(lambda x: x[1] >= 7, notas))

    # e) Exibir resultados
    print("\Lista de candidatos e suas respectivas notas:")
    for nome, nota in notas:
        print(f"{nome}: {nota:.1f}")

    print("\Lista de aprovados (nota ≥ 7):")
    for nome, nota in aprovados:
        print(f"{nome}: {nota:.1f}")

    # Candidato com maior nota (em caso de empate, exibimos todos)
    if notas:
        maior_nota = max(notas, key=lambda x: x[1])[1]
        melhores = [nome for nome, nota in notas if nota == maior_nota]
        print(f"\Candidato(s) com maior nota: {', '.join(melhores)} - {maior_nota:.1f}")
    else:
        print("\Não há candidatos cadastrados.")

if __name__ == "__main__":
    exercicio_02()
