def solution(w):
    if not w: return ""
    is_correct = True
    balance = 0
    for i, b in enumerate(w):
        balance += 81 - (ord(b) * 2)

        if balance < 0:
            is_correct = False

        if not balance:
            u, v = w[:i + 1], w[i + 1:]
            if is_correct: return u + solution(v)
            return "(" + solution(v) + ")" + "".join(list(map(lambda x : chr(81 - ord(x)), u[1:-1])))