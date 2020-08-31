import sys
sys.stdin = open('14425.txt', 'r')

N, M = map(int, input().split())

S = set()
answer = 0

for _ in range(N):
    S.add(input())

for _ in range(M):
    word = input()
    if word in S:
        answer += 1

print(answer)