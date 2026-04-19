n,w,num = 6,6,1
target_width = num % w   # 0
target_hight = num // w + 1  # 2
if target_width == 0 :
    target_hight -= 1

add_width = n % w  # 1
total_hight = n // w

layer = [total_hight for _ in range(w)]
if add_width > 0 :
    if total_hight % 2 == 0 :
        idx = 0
        for i in range(add_width) :
            layer[idx] += 1
            idx += 1
    else :
        idx = w - 1
        for i in range(add_width):
            layer[idx] += 1
            idx -= 1

if target_hight % 2 == 0 :
    if target_width == 0 :
        target_width = w
    target_idx = w - target_width
else :
    if target_width == 0 :
        target_width = w
    target_idx = target_width - 1
print(layer[target_idx] - target_hight + 1)
