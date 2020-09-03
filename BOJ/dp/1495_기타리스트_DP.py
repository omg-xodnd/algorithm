
# 매번 곡을 시작하기 전에 볼륨을 바꾸려고 함
# if not 0 <= Volume <= M : answer = -1
# 마지막 곡을 연주할 수 있는 볼륨 중 최대값 구하기

# N : the number of songs
# S : Start Volume
# M : Max Volume

# 새로운 곡을 할 때 Volume diffs의 값만큼 + / - 할 수 있음

# DFS & Backtracking 으로 접근했지만 시간초과
# 연산 횟수는 똑같은 것 같은데 재귀보다 더 time saving 하다고 봐야할지?
# 연산 횟수가 똑같지 않음


import sys
sys.stdin = open('1495.txt', 'r')

N, S, M = map(int, input().split())
Volume_diffs = list(map(int, input().split()))
ans = -1

memo = [[0] * (M+1) for _ in range(N+1)]

# 0번째 곡에서 volume = S 가능여부
memo[0][S] = 1

for song in range(1, N+1):

    # 여기에 비효율이 있다
    # set으로 저장
    for vol in range(M+1):
        if not memo[song-1][vol] :
            continue

        plus = vol + Volume_diffs[song-1]
        minus = vol - Volume_diffs[song-1]

        if plus <= M :
            memo[song][plus] = 1
        if minus >= 0 :
            memo[song][minus] = 1

        for r in memo :
            print(r)
        print()

for k in range(M, -1, -1):
    if memo[N][k] :
        ans = k
        break

print(ans)
