import sys
sys.stdin = open('3190.txt', 'r')

N = int(input())
K = int(input())

# 지도 및 사과 배치
B = [[0] * N for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    B[r-1][c-1] = 1

# 방향전환 정보
L = int(input())
turn_t = []
turn_d = []
turn_idx = 0

for _ in range(L):
    t, d = input().split()
    turn_t.append(int(t))
    turn_d.append(-1 if d == 'L' else 1)

# 방향
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
d = 1

# 뱀 초기정보
r, c = 0, 0
B[0][0] = 2
snake = [(0, 0)]


# 시간 초기화 및 실행
t = 0
while True:
    t += 1
    nr = r + dr[d]
    nc = c + dc[d]

    if not (0 <= nr < N and 0 <= nc < N) or B[nr][nc] == 2:
        break

    if not B[nr][nc]:
        tr, tc = snake.pop(0)
        B[tr][tc] = 0

    B[nr][nc] = 2
    snake += [(nr, nc)]
    r, c = nr, nc

    if turn_idx < L and t == turn_t[turn_idx]:
        d = (d + turn_d[turn_idx]) % 4
        turn_idx += 1

print(t)
