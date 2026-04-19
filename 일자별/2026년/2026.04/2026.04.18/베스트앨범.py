genres,plays = ["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]

from collections import defaultdict
def solution(genres,plays) :
    answer = []
    genre_dic = defaultdict(int)
    music_dic = defaultdict(list)
    for idx,genre in enumerate(genres) :
        music_dic[genre].append((plays[idx],-idx))
        genre_dic[genre] += plays[idx]
    
    sorted_genres = sorted(genre_dic.items(), key = lambda x : x[1] ,reverse = True)

    for genre,_ in sorted_genres : 
        music_dic[genre].sort(reverse = True)
        cnt = 0
        for music in music_dic[genre] :
            answer.append(-music[1])
            cnt += 1
            if cnt == 2 :
                break

    return answer

print(solution(genres,plays))