N = int(input("Digite o tamanho da matriz: "))

if N % 2 != 0:
    x, y = map(int, input("Digite a coordenada do patinador: ").split())

    if (x == N // 2 or y == N // 2) and x != y:
        print("cuidado faixa amarela")
    elif x == N // 2 and y == N // 2:
        print("continue no centro")

    else:
        if x > N // 2 and y > N // 2:
            print("rumo diagonal principal")
            if x > y:
                print(f"patine {x - y} metros")
            if y > x:
                print(f"patine {y - x} metros")
            print("deslize para cima ao centro")

        elif x > N // 2 and y < N // 2:
            print("rumo diagonal secundária")
            if x > y:
                print(f"patine {x - (N - 1 - y)} metros")
            if y > x:
                print(f"patine {(x - (N - 1 - y)) * (-1)} metros")
            print("deslize para baixo ao centro")

        elif x < N // 2 and y > N // 2:
            print("rumo diagonal secundária")
            if x > y:
                print(f"patine {x - (N - 1 - y)} metros")
            if y > x:
                print(f"patine {(x - (N - 1 - y)) * (-1)} metros")
            print("deslize para cima ao centro")

        elif x < N // 2 and y < N // 2:
            print("rumo diagonal principal")
            if x > y:
                print(f"patine {x - y} metros")
            else:
                print(f"patine {y - x} metros")
            print("deslize para baixo ao centro")

else:
    print("Tamanho da matriz inválido")