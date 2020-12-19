import sys
sys.stdin = open('14499.txt', 'r')


R, C, r, c, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(R)]
orders = list(map(int, input().split()))
answer = []

top, up, right = 1, 2, 3
dice = [0] * 7

dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]

for d in orders:
    nr = r + dr[d]
    nc = c + dc[d]

    if 0 <= nr < R and 0 <= nc < C:
        r, c = nr, nc

        if d == 1:
            top, right = 7-right, top

        elif d == 2:
            top, right = right, 7-top

        elif d == 3:
            top, up = 7-up, top

        else:
            top, up = up, 7-top


        if not B[r][c]:
            B[r][c] = dice[7 - top]

        else:
            dice[7 - top] = B[r][c]
            B[r][c] = 0

        print(dice[top])
