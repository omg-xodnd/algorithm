import sys
sys.stdin = open('14891.txt', 'r')


def solution():

    # vars
    answer = 0
    W = [list(map(int, input())) for _ in range(4)]
    K = int(input())
    orders = []

    for _ in range(K):
        Si, Sd = map(int, input().split())
        orders.append((Si-1, Sd))

    # activate
    for order in orders:
        Q = [order]
        rotated = [0, 0, 0, 0, 1]
        while Q:
            i, d = Q.pop(0)
            rotated[i] = 1

            # left
            if not rotated[i-1] and W[i-1][2] != W[i][-2]:
                Q.append((i-1, -d))

            # right
            if not rotated[i+1] and W[i][2] != W[i+1][-2]:
                Q.append((i+1, -d))

            # rotate
            if d == 1:
                W[i] = [W[i][7]] + W[i][:7]
            else:
                W[i] = W[i][1:7] + [W[i][0]]

    # calc answer
    for i in range(4):
        if W[i][0]:
            answer += W[i][0] << i

    return answer

answer = solution()
print(answer)