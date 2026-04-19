info = [[3, 3], [3, 3]]
n,m = 6,1

from collections import defaultdict
def solution(info, n, m):
    dp ={0:0}  # key: A누적, value: B누적
    for a_trace, b_trace in info :
        next_dp = dict()  # 새로운 상태들을 저장할 dict

        for a_total, b_total in dp.items() :
            # A가 훔치는 경우
            new_a = a_total + a_trace  # A흔적 증가
            if new_a < n and b_total < m :
                # 만약 new_a가 아직 저장되지 않았거나, 이전보다 B의 흔적을 더 적게 썼다면 갱신
                if new_a not in next_dp or next_dp[new_a] > b_total :
                    next_dp[new_a] = b_total

            # B가 훔치는 경우
            new_b = b_total + b_trace  # B의 흔적 증가
            if a_total < n and new_b < m:  # A, B 둘 다 안 잡혔을 때만 저장
                # 현재 a_total을 그대로 유지한 채 B만 증가한 케이스
                if a_total not in next_dp or next_dp[a_total] > new_b:
                    next_dp[a_total] = new_b
        # 만약 가능한 상태가 아예 없으면, 두 도둑 모두 잡힐 수밖에 없음
        if not next_dp:
            return -1

        # 다음 단계로 진행할 준비
        dp = next_dp

    # 마지막까지 살아남은 상태 중 A의 흔적이 최소인 값 리턴
    return min(dp.keys())