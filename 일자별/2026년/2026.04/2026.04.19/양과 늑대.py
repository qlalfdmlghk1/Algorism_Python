info,edges = [0,1,0,1,1,0,1,0,0,1,0],[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]

def solution(info,edges) :
    tree = [[] for _ in range(len(info))]
    for edge in edges : 
        u,v = edge
        tree[u].append(v)
    answer = 0

    def dfs(sheep,wolf,candidates) : 
        nonlocal answer

        answer = max(answer,sheep)
        for idx,candidate in enumerate(candidates) :
            cur_sheep = sheep + (1-info[candidate])
            cur_wolf = wolf + info[candidate]
            
            if cur_sheep > cur_wolf :
                new_candidates = candidates[:idx] + candidates[idx+1:] + tree[candidate]
                dfs(cur_sheep,cur_wolf,new_candidates) 

    dfs(1,0,tree[0])

    return answer

print(solution(info,edges))