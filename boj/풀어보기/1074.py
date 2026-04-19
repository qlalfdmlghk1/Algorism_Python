import sys
# sys.setrecursionlimit(10^6)
input = sys.stdin.readline

n,r,c = map(int,input().split()) # n : 몇 승, r : 행, c : 열

def z(cur_n, cur_r, cur_c, result) :
    while cur_n > 1 :
        cur_n = cur_n // 2
        # 1영역
        if cur_r < cur_n and cur_c < cur_n :
            continue

        # 2영역
        elif cur_r < cur_n  and cur_c >= cur_n :
            result += cur_n ** 2 * 1
            cur_c -= cur_n

        # 3영억
        elif cur_r >= cur_n and cur_c < cur_n :
            result += cur_n ** 2 * 2
            cur_r -= cur_n

        # 4영역
        elif cur_r >= cur_n  and cur_c >= cur_n :
            result += cur_n ** 2 * 3
            cur_r -= cur_n
            cur_c -= cur_n
    print(result)

z(2**n,r,c,0)