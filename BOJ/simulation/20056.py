import sys
sys.stdin = open('20056.txt', 'r')

def get_answer(N, K, balls):
    total = 0

    Dr = [-1, -1, 0, 1, 1, 1, 0, -1]
    Dc = [0, 1, 1, 1, 0, -1, -1, -1]

    def move(ball):
        # 좌표 이동
        r, c, m, s, d = ball
        nr = (r + Dr[d] * s) % N
        nc = (c + Dc[d] * s) % N
        key = str(nr) + ' ' + str(nc)
        if key not in B:
            # 질량, 개수, 속도, 방향1, 방향2
            # if 방향1 == -2 : odd
            B[key] = [0, 0, 0, 0, -1]

        pos = B[key]

        # 질량
        pos[0] += m

        # 개수
        pos[1] += 1

        # 속도
        pos[2] += s

        # 방향
        if pos[4] == -1:
            pos[4] = d
            pos[3] = d % 2

        elif pos[3] == -2:
            pass

        elif pos[3] != d % 2:
            pos[3] = -2

        return

    def get_balls(B):
        balls = []
        for key in B.keys():
            balls = split_ball(key, balls)
        return balls


    def split_ball(key, balls):
        r, c = map(int, key.split())
        m, count, s, d1, d2 = B[key]

        if count < 2:
            balls.append([r, c, m, s, d2])

        else:
            m //= 5
            if m:
                s //= count
                d_list = [1, 3, 5, 7] if d1 == -2 else [0, 2, 4, 6]
                for d in d_list:
                    balls.append([r, c, m, s, d])

        return balls

    for _ in range(K):
        B = {}
        for ball in balls:
            move(ball)
        balls = get_balls(B)

    for ball in balls:
        total += ball[2]

    return total

N, M, K = map(int, input().split())
balls = [map(int, input().split()) for _ in range(M)]
answer = get_answer(N, K, balls)

print(answer)