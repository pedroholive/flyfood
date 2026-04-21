from itertools import permutations
import time

def calculo(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def resolucao(caminho_arquivo):
    with open(caminho_arquivo, 'r') as f:
        linha_dimensoes = f.readline().split()
        if not linha_dimensoes:
            return
        n = int(linha_dimensoes[0])
        lines = f.read().splitlines()

    cord = {}
    pontos_delivery = []

    for i in range(n):
        line = lines[i].split()
        for col_idx, j in enumerate(line):
            if j != '0':
                cord[j] = (i, col_idx)
                if j != 'R':
                    pontos_delivery.append(j)

    todos_pontos = ['R'] + pontos_delivery
    dist = {}
    for a in todos_pontos:
        for b in todos_pontos:
            dist[(a, b)] = calculo(cord[a], cord[b])

    menor_caminho = float('inf')
    rota_final = []

    inicio = time.perf_counter()

    for k in permutations(pontos_delivery):
        atual_caminho = 0
        atual_caminho += dist[('R', k[0])]
        if atual_caminho >= menor_caminho:
            continue

        for i in range(len(k) - 1):
            atual_caminho += dist[(k[i], k[i+1])]
            if atual_caminho >= menor_caminho:  # Abandona a rota cedo
                break
        else:
            atual_caminho += dist[(k[-1], 'R')]
            if atual_caminho < menor_caminho:
                menor_caminho = atual_caminho
                rota_final = list(k)

    fim = time.perf_counter()

    print(' '.join(rota_final))
    print(f"Distância total: {menor_caminho}")
    print(f"Tempo gasto: {fim - inicio:.4f} segundos")

resolucao('matriz11.txt')