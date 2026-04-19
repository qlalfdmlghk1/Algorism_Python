bridge_length = 100
weight = 100
truck_weights =	[10,10,10,10,10,10,10,10,10,10]

from collections import deque

q = deque([0] * bridge_length)
truck_weights = deque(truck_weights)
cur_weight = 0
time = 0

while truck_weights :
    # print(q)
    time += 1
    cur_weight -= q.popleft()
    if cur_weight + truck_weights[0] <= weight :
        cur_weight += truck_weights[0]
        q.append(truck_weights.popleft())

    else :
        q.append(0)

time += bridge_length
print(time)