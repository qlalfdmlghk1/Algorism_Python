import sys
input = sys.stdin.readline

from _collections import deque

a, b, c, d = map(int, input().split())

visit = {}

def bfs():
    queue = deque()
    queue.append((0, 0))
    visit[(0, 0)] = 1

    # 목표 상태가 이미 (0, 0)일 경우 바로 반환
    if c == 0 and d == 0:
        return 0

    while queue:
        x, y = queue.popleft()

        # 물통 a를 가득 채우기 (x를 a로 설정)
        if not visit.get((a, y)):
            queue.append((a, y))
            visit[(a, y)] = visit[(x, y)] + 1

        # 물통 b를 가득 채우기 (y를 b로 설정)
        if not visit.get((x, b)):
            queue.append((x, b))
            visit[(x, b)] = visit[(x, y)] + 1

        # 물통 a를 비우기 (x를 0으로 설정)
        if not visit.get((0, y)):
            queue.append((0, y))
            visit[(0, y)] = visit[(x, y)] + 1

        # 물통 b를 비우기 (y를 0으로 설정)
        if not visit.get((x, 0)):
            queue.append((x, 0))
            visit[(x, 0)] = visit[(x, y)] + 1

        # 물통 a의 물을 b로 옮기기 (a -> b)
        if x <= b - y:
            # a의 모든 물을 b로 옮겨도 b가 넘치지 않는 경우
            if not visit.get((0, x + y)):
                queue.append((0, x + y))
                visit[(0, x + y)] = visit[(x, y)] + 1

        else:
            # a의 물 일부를 b에 채워서 b가 가득 차는 경우
            if not visit.get((x + y - b, b)):
                queue.append((x + y - b, b))
                visit[(x + y - b, b)] = visit[(x, y)] + 1

        # 물통 b의 물을 a로 옮기기 (b -> a)
        if y <= a - x:
            # b의 모든 물을 a로 옮겨도 a가 넘치지 않는 경우
            if not visit.get((x + y, 0)):
                queue.append((x + y, 0))
                visit[(x + y, 0)] = visit[(x, y)] + 1

        else:
            # b의 물 일부를 a에 채워서 a가 가득 차는 경우
            if not visit.get((a, x + y - a)):
                queue.append((a, x + y - a))
                visit[(a, x + y - a)] = visit[(x, y)] + 1

        # 목표 상태 (c, d)에 도달했는지 확인
        if visit.get((c, d)):
            if visit[(x, y)] > 0:
                return (visit[(x, y)]) # 목표 상태에 도달한 경우 이동 횟수 반환

    return -1  # 목표 상태에 도달할 수 없는 경우 -1 반환

print(bfs())