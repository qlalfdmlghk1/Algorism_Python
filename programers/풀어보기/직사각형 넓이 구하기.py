dots = [[-1, -1], [1, 1], [1, -1], [-1, 1]]
dots.sort(key=lambda x : (x[0],x[1]))
print((dots[1][1] - dots[0][1]) * (dots[3][1] - dots[2][1]))