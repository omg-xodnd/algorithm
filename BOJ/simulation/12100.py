import sys
sys.stdin = open('12100.txt', 'r')

N = int(input())
B = [list(map(int, input().split())) for _ in range(N)]

def move_line(line, d):
    moved = []
    temp = 0

    if not d % 2:
        for n in line:
            if not n:
                continue

            if not temp:
                temp = n

            elif temp == n:
                moved.append(n << 1)
                temp = 0

            else:
                moved.append(temp)
                temp = n
        if temp:
            moved.append(temp)

        diff = N - len(moved)
        if diff:
            moved += ([0] * diff)

    # 하 우
    else:
        for i in range(N-1, -1, -1):
            n = line[i]

            if not line[i]:
                continue

            if not temp:
                temp = n

            elif temp == n:
                moved.insert(0, n << 1)
                temp = 0

            else:
                moved.insert(0, temp)
                temp = n

        if temp:
            moved.insert(0, temp)

        diff = N - len(moved)
        if diff:
            moved = [0] * diff + moved

    return moved


def move(d):
    # 상 하
    if d < 2:
        for c in range(N):
            line = []
            for r in range(N):
                line.append(B[r][c])
            moved = move_line(line, d)

            for r in range(N):
                B[r][c] = moved[r]

    # 좌 우
    else:
        for r in range(N):
            moved = move_line(B[r], d)
            for c in range(N):
                B[r][c] = moved[c]

def deep_copy(arr):
    return [arr[r][:] for r in range(len(arr))]

def dfs(depth = 0):
    global B, answer
    if depth == 5:
        for r in range(N):
            for c in range(N):
                answer = max(answer, B[r][c])
        return

    snapshot = deep_copy(B)
    for d in range(4):
        move(d)
        dfs(depth + 1)
        B = deep_copy(snapshot)

answer = 0
dfs()
print(answer)