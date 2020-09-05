def solution(key, lock):
    M, N = len(key), len(lock)
    key_pos = get_key_position(key, M)
    hole_cnt = get_hole_cnt(lock, N)

    for _ in range(4):
        for dr in range(1-M, N):
            for dc in range(1-M, N):
                temp_key_pos = [(r+dr, c+dc) for r, c in key_pos]

                if is_match(temp_key_pos, lock, N, hole_cnt):
                    return True

        key_pos = rotate(key_pos, M)

    return False


def get_key_position(arr, M):
    pos = []
    for r in range(M):
        for c in range(M):
            if arr[r][c]:
                pos.append((r, c))
    return pos

def get_hole_cnt(lock, N):
    cnt = 0
    for r in range(N):
        for c in range(N):
            if not lock[r][c]:
                cnt += 1
    return cnt

def rotate(pos, M):
    return [(c, M-1-r) for r, c in pos]


def is_match(key_pos, lock, N, hole_cnt):
    match_cnt = 0

    for r, c in key_pos:
        if 0<= r < N and 0<= c < N:
            if lock[r][c]:
                return False

            match_cnt += 1

    if match_cnt == hole_cnt:
        return True


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key, lock))
