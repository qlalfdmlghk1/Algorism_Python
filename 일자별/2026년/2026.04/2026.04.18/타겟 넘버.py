numbers,target = [1,1,1,1,1],3

from collections import deque
def solution(numbers, target) :
    answer = 0
    q = deque()
    q.append((numbers[0],0))
    q.append((-numbers[0],0))
    while q : 
        cur_num,cur_idx = q.popleft()
        nex_idx = cur_idx + 1 
        for i in range(2) :
            if i == 0 :
                nex_num = cur_num + numbers[nex_idx]
            else :
                nex_num = cur_num - numbers[nex_idx]
            
            if nex_idx < len(numbers) - 1 :
                q.append((nex_num,nex_idx))
            else :
                if nex_num == target :
                    answer += 1 
    
    return answer

print(solution(numbers,target))