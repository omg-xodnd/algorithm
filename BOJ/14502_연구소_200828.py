import sys
sys.stdin = open('14502.txt', 'r')

def find_location():
    empty, virus = [], []
    for r in range(R):
        for c in range(C):
            if B[r][c] == 0:
                empty.append((r, c))
            if B[r][c] == 2:
                virus.append((r, c))

    return empty, virus

def get_combi_3(N):
    combi_list = []
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                combi_list.append((i, j, k))

    return combi_list

def simulate(walls, virus, min_infected):
    visited = [[False] * C for _ in range(R)]
    infected = 0
    finished = True

    for r, c in walls:
        B[r][c] = 1

    Dr = [1, -1, 0, 0]
    Dc = [0, 0, -1, 1]

    stack = virus[:]
    while stack:
        if min_infected <= infected:
            finished = False
            break

        r, c = stack.pop()

        for i in range(4):
            Nr = r + Dr[i]
            Nc = c + Dc[i]

            if 0 <= Nr < R and 0 <= Nc < C and B[Nr][Nc] == 0 and not visited[Nr][Nc]:
                infected += 1
                visited[Nr][Nc] = True
                stack.append((Nr, Nc))

    for r, c in walls:
        B[r][c] = 0

    return infected, finished

def get_max_safe(R, C, B):
    max_safe = 0
    min_infected = R * C

    empty, virus = find_location()
    L = len(empty)

    for combi in get_combi_3(L):
        walls = []
        for x in combi:
            walls.append(empty[x])

        infected, finished = simulate(walls, virus, min_infected)

        if finished:
            max_safe = L - infected - 3
            min_infected = infected

    return max_safe


R, C = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(R)]

answer = get_max_safe(R, C, B)
print(answer)