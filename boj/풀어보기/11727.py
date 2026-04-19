while True :
    words = input()
    if words == "#" :
        exit()
    words = words.split()
    for word in words :
        print(word[::-1], end=" ")
    print()