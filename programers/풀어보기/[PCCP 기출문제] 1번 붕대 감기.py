# bandage = [시전 시간, 초당 회복량, 추가 회복량]
# attacks[i]는 [공격 시간, 피해량]
# 모든 공격이 끝난 직후 남은 체력을 return, 캐릭터의 체력이 0 이하가 되어 죽는다면 -1을 return
bandage,health,attacks = [3, 2, 7],	20,	[[1, 15], [5, 16], [8, 6]]  # result = 5

time = 0
cur_health = health
max_time = attacks[-1][0]
bandage_count = 0
dic = {}
for attack in attacks :
    dic[attack[0]] = attack[1]

while time <= max_time :
    if time in dic :
        cur_health -= dic[time]
        bandage_count = 0
        if cur_health <= 0 :
            print(-1)

    elif cur_health < health :
        cur_health += bandage[1]
        bandage_count += 1
        if bandage_count == bandage[0] :
            cur_health += bandage[2]
            bandage_count = 0
        if cur_health > health :
            cur_health = health
    time += 1
print(cur_health)

# time = 0
# cur_health = health
# for attack in attacks :
#     health_count = 0
#     while time < attack[0] :
#         if cur_health < health :
#             while health_count <= bandage[0] and cur_health <= health:
#                 health_count += 1
#                 cur_health += bandage[1]
#                 time += 1
#                 if health_count == bandage[0] :
#                     cur_health += bandage[2]
#                     health_count = 0
#             if cur_health > health :
#                 cur_health = health
#         else :
#             time += 1
#     cur_health -= attack[1]
#     time += 1
#     if cur_health < 0:
#         print(-1)
#         break
# print(cur_health)
