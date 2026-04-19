scores = [[4, 0], [2, 5], [5, 3], [2, 6]]

def solution(scores):
   wanho = scores[0]
   wanho_sum = wanho[0] + wanho[1]
   scores.sort(reverse=True, key = lambda x : (x[0],-x[1]))
   rank = [0] * len(scores)

   max_work,max_peer = 0,0
   for index,score in enumerate(scores) :
      if score[1] < max_peer :
         rank[index] = -1
         if score[0] == wanho[0] and score[1] == wanho[1]:
            return -1
      else :
         max_peer = max(score[1],max_peer)
         rank[index] = score[0] + score[1]

   rank.sort(reverse=True)
   for r in rank :
      return rank.index(wanho_sum) + 1

print(solution(scores))