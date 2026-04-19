import sys
input = sys.stdin.readline
n, max_attack = map(int ,input().split())  # 방의 수, 초기 공격력
li = []
for _ in range(n):
    li.append(list(map(int,input().split())))

def game(n,max_attack,li,max_health) :
    cur_health = max_health
    cur_attack = max_attack
    for i in range(n) :
        t,a,h = li[i]
        if t == 1 :  # 공격력 a인 몬스터, 생명력 h인 몬스터 있음
            if h % cur_attack == 0 :
                attack_cnt = h // cur_attack - 1
            else :
                attack_cnt = h // cur_attack

            if cur_health - (a * attack_cnt) <= 0 :
                return False
            cur_health -= (a * attack_cnt)
        elif t == 2 :  # 공격력을 a만큼 증가, 현재 생명력을 h만큼 증가
            cur_attack += a
            cur_health += h
            if cur_health > max_health :
                cur_health = max_health
    return True

left = 1
right = int(1e18)
result = []
while left < right :
    mid = (left + right) // 2
    if game(n,max_attack,li,mid) :
        # result.append(mid)
        # result = min(result,mid)
        right = mid
    else :
        left = mid + 1
    # print(left,right)
print(left)