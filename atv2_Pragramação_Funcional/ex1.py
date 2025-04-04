def exercicio_01():
   
    def ler_entrada():
        # a) Ler entrada e transformar em lista de tuplas
        # Exemplo de entrada (numa só linha): "Ana:júnior:3000 Bruno:pleno:5500 Carla:sênior:9000"
        entrada = input("Digite o nome, o cargo e o salário dos funcionários em uma só linha:\n").strip().split()
        return [(nome, cargo, float(salario))
                for (nome, cargo, salario) in (item.split(':') for item in entrada)]

    def criar_aumento_percentual():
        # b) 
        def aumentar_percentual(porcentagem):
            return lambda salario: salario * (1 + porcentagem / 100.0)
        return aumentar_percentual

    def aplicar_aumentos(profissionais, aumentar_percentual):
        # c) Aplicar aumentos usando map()
        aumentos = {
            "júnior": aumentar_percentual(10),
            "junior": aumentar_percentual(10),  
            "pleno": aumentar_percentual(7),
            "sênior": aumentar_percentual(5),
            "senior": aumentar_percentual(5)   
        }
        
        # Função que aplica o aumento ao salário de cada profissional
        def aplicar(tupla):
            nome, cargo, salario = tupla
            cargo_lower = cargo.lower()
            if cargo_lower in aumentos:
                novo_salario = aumentos[cargo_lower](salario)
                # padroniza o nome do cargo 
                if "júnior" in cargo_lower:
                    cargo = "júnior"
                elif "pleno" in cargo_lower:
                    cargo = "pleno"
                elif "sênior" in cargo_lower:
                    cargo = "sênior"
                return (nome, cargo, novo_salario)
            else:
                # Caso não seja um cargo reconhecido, não altera o salário
                return (nome, cargo, salario)

        return list(map(aplicar, profissionais))

    def encontrar_maiores_salarios(novos_salarios):
        # d) 
        salarios_ordenados = sorted(novos_salarios, key=lambda x: x[2], reverse=True)
        
        # Garante que não dê erro se houver apenas 1 funcionário
        if len(salarios_ordenados) == 1:
            return salarios_ordenados[0], None
        
        return salarios_ordenados[0], salarios_ordenados[1]

    profissionais = ler_entrada()
    aumentar = criar_aumento_percentual()
    novos_salarios = aplicar_aumentos(profissionais, aumentar)

    # Exibir a lista completa de salários atualizados
    print("\nLista de funcionários com salários atualizados:")
    for nome, cargo, salario in novos_salarios:
        print(f"{nome} ({cargo}) - R$ {salario:.2f}")

    # Encontra o maior e o segundo maior salário
    maior, segundo = encontrar_maiores_salarios(novos_salarios)

    if maior:
        print(f"\nMaior salário após aumento: {maior[0]} - R$ {maior[2]:.2f}")
    if segundo:
        print(f"Segundo maior salário após aumento: {segundo[0]} - R$ {segundo[2]:.2f}")

if __name__ == "__main__":
    exercicio_01()
