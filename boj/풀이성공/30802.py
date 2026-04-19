n = int(input())  # 참가자 수
tshirts = map(int,input().split())  # 사이즈 별 개수
t_size, p_size = map(int,input().split())

t_cnt = 0

for t in tshirts :
    if t % t_size == 0 :
        t_cnt += t // t_size
    else :
        t_cnt += t // t_size + 1

print(t_cnt)
print(n//p_size, n%p_size)