S = input()
T = input()

def solve(word) :
    if len(word) == len(S) :
        if word == S :
            return True
        else :
            return False
    
    result = False
    
    if word[-1] == "A" :
        result = result or solve(word[:-1])
        
    
    if word[0] == "B" :
        result = result or solve(word[1:][::-1])
    
    return result

if solve(T) :
    print(1)
else :
    print(0)