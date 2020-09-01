def my_zip(s, n):
    i = 0
    count = 1
    answer = ''
    unit = s[i:i + n]

    while i < len(s):
        test = s[i + n:i + (2 * n)]
        if unit == test:
            count += 1
        else:
            if count == 1:
                answer += unit
            else:
                answer += str(count) + unit
            count = 1
            unit = test
        i += n

    return len(answer)


def solution(s):
    answer = len(s)

    for n in range(1, 1+len(s) // 2):
        answer = min(my_zip(s, n), answer)

    return answer