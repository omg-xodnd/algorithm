import sys
sys.stdin = open('1700.txt', 'r')

N, K = map(int, input().split())
Schedule = list(map(int, input().split()))
ans = 0
Tab = [0] * N

for schedule_idx, new_device in enumerate(Schedule):
    in_tab = False
    for idx, port in enumerate(Tab):

        # 포트에 빈 자리 있는지 탐색
        if port == 0 or port == new_device:
            Tab[idx] = new_device
            in_tab = True
            break

        # 포트에 같은 장비가 사용 중인지 확인
        # 기기별 is_in_use 리스트를 만들어서 확인할 수도 있을 듯..

    # 포트에 빈 자리 없을 경우
    if not in_tab:
        max_distance = 0
        out_idx = 0

        # tab에 꽂혀있는 장비들에 대해 향후 사용여부 확인
        temp = Schedule[schedule_idx+1:]
        for idx, in_device in enumerate(Tab):

            # 앞으로 사용하지 않는 경우
            if in_device not in temp:
                out_idx = idx
                break

            # 남아있는 스케쥴에서 꽂혀있는 장비가 언제 가장 먼저 등장하는지 확인
            else :
                j = schedule_idx
                while True :
                    if Schedule[j] == in_device :
                        if j > max_distance :
                            max_distance = j
                            out_idx = idx
                        break
                    j += 1

        Tab[out_idx] = new_device
        ans += 1

print(ans)