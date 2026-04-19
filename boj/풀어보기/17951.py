n,k = map(int,input().split())
scores = list(map(int,input().split()))
sum_scores = [scores[0]]

# 누적합 같은데 누적합은 어떻게 푸는걸까
for s in scores[1:] :
    sum_scores.append(sum_scores[-1])