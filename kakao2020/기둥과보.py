
def solution(n, build_frame):

    def is_safe_beam(x, y):
        if P[x][y - 1] or P[x + 1][y - 1]:
            return True
        elif B[x - 1][y] and B[x + 1][y]:
            return True
        else:
            return False

    def is_safe_pillar(x, y):
        if y == 0 or P[x][y - 1] or B[x][y] or B[x - 1][y]:
            return True
        else:
            return False

    answer = []
    N = n + 1
    P = [[0] * N for _ in range(N)]
    B = [[0] * N for _ in range(N)]

    for x, y, beam, install in build_frame:
        if install:
            if beam and is_safe_beam(x, y):
                B[x][y] = 1
            elif not beam and is_safe_pillar(x, y):
                P[x][y] = 1
        else:
            if beam:
                B[x][y] = 0
                is_valid = True
                if B[x - 1][y] and not is_safe_beam(x - 1, y):
                    is_valid = False
                if B[x + 1][y] and not is_safe_beam(x + 1, y):
                    is_valid = False
                if P[x][y] and not is_safe_pillar(x, y):
                    is_valid = False
                if P[x + 1][y] and not is_safe_pillar(x + 1, y):
                    is_valid = False
                if not is_valid:
                    B[x][y] = 1
            else:
                P[x][y] = 0
                is_valid = True
                if B[x][y + 1] and not is_safe_beam(x, y + 1):
                    is_valid = False
                if B[x - 1][y + 1] and not is_safe_beam(x - 1, y + 1):
                    is_valid = False
                if P[x][y + 1] and not is_safe_pillar(x, y + 1):
                    is_valid = False
                if not is_valid:
                    P[x][y] = 1

    for x in range(N):
        for y in range(N):
            if P[x][y]:
                answer.append([x, y, 0])
            if B[x][y]:
                answer.append([x, y, 1])

    return answer






b = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
ans = [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]
print(solution(5, b))
print(ans)