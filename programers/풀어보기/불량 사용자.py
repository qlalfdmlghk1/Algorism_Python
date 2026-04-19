from itertools import permutations
import re
user_id	 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
new_banned = []

for banned in banned_id :
    banned = banned.replace('*','.')
    new_banned.append(banned)

answer = []
for com_user in permutations(user_id,len(banned_id)) :
    cnt = 0

    for i in range(len(new_banned)) :
        if re.match(new_banned[i],com_user[i]) and len(new_banned[i]) == len(com_user[i]):
            cnt += 1
    if cnt == len(com_user) :
        if sorted(com_user) not in answer :
            answer.append(sorted(com_user))

# print(answer)
print(len(answer))






