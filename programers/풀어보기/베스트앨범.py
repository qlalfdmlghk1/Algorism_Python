genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
# return = [4, 1, 3, 0]

musics = []
dic = {}
ind = 0
for i,j in zip(genres,plays) :
    musics.append((i,j,ind))
    if i in dic :
        dic[i] += j
    else :
        dic[i] = j
    ind += 1
# print(musics)

musics.sort(key = lambda x : x[1], reverse = True)
result = []

dic= sorted(dic, key = lambda x : x[1], reverse = True) # 왜 key값만 나오지?
print(dic)
for genre in dic :
    cnt = 0
    for music in musics :
        if genre == music[0] :
            result.append(music[2])
            cnt += 1
            if cnt == 2 :
                break
    print(result)
print(result)