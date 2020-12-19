import sys
sys.stdin = open('20057.txt', 'r')

# 좌하우상

def get_answer(N, B):
    r = c = N // 2
    dr = [0, 1, 0, -1]
    dc = [-1, 0, 1, 0]

    dx = 1
    d = 0

    def wind(r, c, d):
        dir = (dr[d], dc[d])

        # 좌우 / 상하
        m1, m2 = 0, 1 if not dir[0] else 1, 0





    while True:
        for i in range(2):
            for j in range(dx):
                r += dr[d]
                c += dc[d]
                if not r and not c: return
                wind(d)







            d = (d + 1) % 4
        dx += 1



    return

N = int(input())
B = [list(map(int, input().split())) for _ in range(N)]

answer = get_answer(N, B)
print(answer)
