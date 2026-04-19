info,edges = [0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]

def solution(info, edges):
    tree = [[] for _ in range(len(info))]
    for parent,child in edges :
        tree[parent].append(child)
    answer = 0

    # DFS
    def dfs(sheep, wolf, candidates) :
        nonlocal answer
        answer = max(answer,sheep)

        for i in range(len(candidates)) :
            node = candidates[i]
            new_sheep = sheep + (1 - info[node])
            new_wolf = wolf + info[node]

            if new_sheep > new_wolf:
                new_candidates = candidates[:i] + candidates[i+1:] + tree[node]
                dfs(new_sheep, new_wolf, new_candidates)

    dfs(1,0,tree[0])
    return answer