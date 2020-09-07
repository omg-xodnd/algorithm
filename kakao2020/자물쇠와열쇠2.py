def solution(key, lock):

    def get_key_pos():
        pos = []
        for r in range(M):
            for c in range(M):
                if key[r][c]:
                    pos.append((r, c))
        return pos

    def get_hole_cnt():
        cnt = 0
        for r in range(N):
            for c in range(N):
                if not lock[r][c]:
                    cnt += 1
        return cnt

    def is_match(temp_key_pos):
        match_cnt = 0

        for r, c in temp_key_pos:
            if 0 <= r < N and 0 <= c < N:
                if lock[r][c]:
                    return False

                match_cnt += 1

        if match_cnt == hole_cnt:
            return True


    M, N = len(key), len(lock)
    key_pos, hole_cnt = get_key_pos(), get_hole_cnt()

    for _ in range(4):
        for dr in range(1-M, N):
            for dc in range(1-M, N):
                if is_match([(r+dr, c+dc) for r, c in key_pos]):
                    return True

        # 회전
        key_pos = [(c, M-r-1) for r, c in key_pos]

    return False



key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key, lock))
