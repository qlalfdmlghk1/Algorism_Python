# 페인트가 칠해진 길이가 n미터인 벽
# 벽에 페인트를 칠하는 롤러의 길이는 m미터
# 다시 페인트를 칠하기로 정한 구역들의 번호가 담긴 정수 배열 section
# 롤러로 페인트칠해야 하는 최소 횟수를 return
# n	m	section	result = 8	4	[2, 3, 6]	2
# 롤러의 길이가 4미터이므로 한 번의 페인트칠에 연속된 4개의 구역을 칠할 수 있습니다.
n,m,section,result = 4,1,[1, 2, 3, 4],4
visited = [1] * n
cnt = 0
for i in section :
    visited[i-1] = 0
for index,j in enumerate(visited) :
    if visited[index] == 0 :
        cnt += 1
        for k in range(m) :
            if index+k < n :
                visited[index+k] = 1

print(cnt)