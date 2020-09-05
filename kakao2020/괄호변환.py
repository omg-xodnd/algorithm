def is_correct(w):
    stack = []
    for b in w:
        if stack and b != stack[-1] and b == ")":
            stack.pop()
        else:
            stack.append(b)
    return not stack


def split_w(w):
    u, v = w, ""
    balance = 0

    for i, b in enumerate(w):
        balance += 81 - (ord(b) * 2)

        if not balance:
            u, v = w[:i + 1], w[i + 1:]
            return u, v


def DP(w):
    if not w: return ""

    u, v = split_w(w)
    if is_correct(u): return u + DP(v)

    new = ""
    for b in u[1:-1]:
        new += chr(81 - ord(b))
    return "(" + DP(v) + ")" + new


def solution(p):
    answer = DP(p)
    return answer