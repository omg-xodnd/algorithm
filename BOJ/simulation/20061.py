import sys
sys.stdin = open('20061.txt', 'r')

G = [[0] * 4 for _ in range(6)]
B = [[0] * 4 for _ in range(6)]
score = 0

def get_Bt(t):
    return [0, 1, 3, 2][t]

def get_Bc(t, c):
    if t == 3:
        c -= 1
    return c

def get_pos(board, t, c):

    r = 1
    while True:
        if r == 5 or board[r + 1][c]:
            break
        if t == 2 and board[r + 1][c + 1]:
            break
        r += 1

    pos = [(r, c)]

    if t == 2:
        pos.append((r, c + 1))

    elif t == 3:
        pos.append((r - 1, c))

    return pos

def put_block_on(board, pos):
    for r, c in pos:
        board[r][c] = 1
    return board

def check_full(board,score):
    r = 5
    while r > 1:
        is_full = True
        for block in board[r]:
            if not block:
                is_full = False
                break

        if is_full:
            board.pop(r)
            board.insert(0, [0, 0, 0, 0])
            score += 1
        else:
            r -= 1

    return board, score

def check_top(board):
    count = 0
    for r in range(2):
        for block in board[r]:
            if block:
                count += 1
                break

    for _ in range(count):
        board.pop()
        board.insert(0, [0, 0, 0, 0])

    return board

def count_blocks(board):
    count = 0
    for r in range(2,  6):
        for c in range(4):
            if board[r][c]:
                count += 1
    return count

N = int(input())
for _ in range(N):
    t, r, c = map(int, input().split())

    pos_G = get_pos(G, t, c)
    G = put_block_on(G, pos_G)
    G, score = check_full(G, score)
    G = check_top(G)

    pos_B = get_pos(B, get_Bt(t), get_Bc(t, 3-r))
    B = put_block_on(B, pos_B)
    B, score = check_full(B, score)
    B = check_top(B)

answer = count_blocks(G) + count_blocks(B)
print(score)
print(answer)