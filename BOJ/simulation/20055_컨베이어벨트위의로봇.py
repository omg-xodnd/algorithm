import sys
sys.stdin = open('20055.txt', 'r')


def main(N, K, D):
    count = 0
    broken = 0
    belt = [0] * (N * 2)
    load, unload = 0, N - 1
    max_idx = (N * 2) - 1

    def check_idx(idx):
        if idx < 0:
            idx = max_idx
        elif idx > max_idx:
            idx = 0
        return idx

    def unload_robot():
        if belt[unload]:
            belt[unload] = 0


    while broken < K:
        count += 1

        # rotate
        unload_robot()

        load = check_idx(load - 1)
        unload = check_idx(unload - 1)

        # move robot
        unload_robot()

        before = unload
        for i in range(N):
            current = check_idx(before - 1)
            next = before

            if belt[current] and not belt[next] and D[next]:
                belt[current] = 0
                belt[next] = 1
                D[next] -= 1
                if not D[next]:
                    broken += 1

            before = current

        # load robot
        if not belt[load] and D[load]:
            belt[load] = 1
            D[load] -= 1
            if not D[load]:
                broken += 1

    return count

for i in range(4):
    N, K = map(int, input().split())
    D = list(map(int, input().split()))

    answer = main(N, K, D)
    print(answer)