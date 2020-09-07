def solution(n, build_frame):
    def is_safe_beam(x, y):
        if (P[x][y - 1] or P[x + 1][y - 1]) or (B[x - 1][y] and B[x + 1][y]):
            return True

    def is_safe_pillar(x, y):
        if y == 0 or P[x][y - 1] or B[x][y] or B[x - 1][y]:
            return True

    answer = []
    N = n + 1
    P, B = [[0] * N for _ in range(N)], [[0] * N for _ in range(N)]

    for x, y, beam, install in build_frame:
        if install:
            if beam and is_safe_beam(x, y):
                B[x][y] = 1
            elif not beam and is_safe_pillar(x, y):
                P[x][y] = 1
        else:
            if beam:
                B[x][y] = 0

                if ((B[x - 1][y] and not is_safe_beam(x - 1, y)) or
                        (B[x + 1][y] and not is_safe_beam(x + 1, y)) or
                        (P[x][y] and not is_safe_pillar(x, y)) or
                        (P[x + 1][y] and not is_safe_pillar(x + 1, y))):
                    B[x][y] = 1

            else:
                P[x][y] = 0

                if ((B[x][y + 1] and not is_safe_beam(x, y + 1)) or
                        (B[x - 1][y + 1] and not is_safe_beam(x - 1, y + 1)) or
                        (P[x][y + 1] and not is_safe_pillar(x, y + 1))):
                    P[x][y] = 1

    for x in range(N):
        for y in range(N):
            if P[x][y]:
                answer.append([x, y, 0])
            if B[x][y]:
                answer.append([x, y, 1])

    return answer