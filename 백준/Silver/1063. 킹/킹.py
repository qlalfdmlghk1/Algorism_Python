king, rock, n = input().split()

king_r, king_c = ord(king[0]) - 65, int(king[1])-1
rock_r, rock_c = ord(rock[0]) - 65, int(rock[1])-1

def is_range(r,c) :
    if 0 <= r < 8 and 0 <= c < 8 :
       return True
    else :
       return False



for _ in range(int(n)) :
    move = input()
    if move == "R" : 
        if is_range(king_r+1, king_c) :
            if king_r+1 == rock_r and king_c == rock_c :
                if is_range(rock_r+1,rock_c) : # 왕이 이동한 지점 = 돌의 지점
                    rock_r += 1
                else :
                    king_r -= 1
            king_r += 1
    
    elif move == "L" :
        if is_range(king_r-1,king_c) :
            if king_r-1 == rock_r and king_c == rock_c :
                if is_range(rock_r-1,rock_c) : 
                    rock_r -= 1
                else :
                    king_r += 1        
            king_r -= 1

    elif move == "B" :
        if is_range(king_r,king_c-1) :
            if king_r == rock_r and king_c-1 == rock_c :
                if is_range(rock_r,rock_c-1) :
                    rock_c -= 1
                else :
                    king_c += 1        
            king_c -= 1
    
    elif move == "T" :
        if is_range(king_r,king_c+1) :
            if king_r == rock_r and king_c+1 == rock_c :
                if is_range(rock_r,rock_c+1) :
                    rock_c += 1
                else :
                    king_c -= 1
            king_c += 1

    elif move == "RT" :
        if is_range(king_r+1,king_c+1) :
            if king_r+1 == rock_r and king_c+1 == rock_c :
                if is_range(rock_r+1,rock_c+1) :
                    rock_r += 1
                    rock_c += 1
                else :
                    king_r -= 1
                    king_c -= 1        
            king_r += 1
            king_c += 1

    elif move == "LT" :
        if is_range(king_r-1,king_c+1) :
            if king_r-1 == rock_r and king_c+1 == rock_c :
                if is_range(rock_r-1,rock_c+1) :
                    rock_r -= 1
                    rock_c += 1
                else :
                    king_r += 1
                    king_c -= 1    
            king_r -= 1
            king_c += 1

    elif move == "RB" :
        if is_range(king_r+1,king_c-1) :
            if king_r+1 == rock_r and king_c-1 == rock_c :
                if is_range(rock_r+1,rock_c-1) :
                    rock_r += 1
                    rock_c -= 1
                else :
                    king_r -= 1
                    king_c += 1    
            king_r += 1
            king_c -= 1

    elif move == "LB" :
        if is_range(king_r-1,king_c-1) :
            if king_r-1 == rock_r and king_c-1 == rock_c :
                if is_range(rock_r-1,rock_c-1) :
                    rock_r -= 1
                    rock_c -= 1
                else :
                    king_r += 1
                    king_c += 1        
            king_r -= 1
            king_c -= 1
    
king,rock = '',''

# 숫자 -> 문자
def num_to_alpha(n) :
    if n == 0 : return "A"
    elif n == 1 : return "B"
    elif n == 2 : return "C"
    elif n == 3 : return "D"
    elif n == 4 : return "E"
    elif n == 5 : return "F"
    elif n == 6 : return "G"
    elif n == 7 : return "H"

king += num_to_alpha(king_r)
king += str(king_c+1)
rock += num_to_alpha(rock_r)
rock += str(rock_c+1)
print(king)
print(rock)