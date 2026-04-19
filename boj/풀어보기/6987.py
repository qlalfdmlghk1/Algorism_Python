for _ in range(4) :
    games,matches = [],[]
    arr = list(map(int, input().split()))

    for i in range(6):
        for j in range(i + 1, 6):
            matches.append((i,j))

    for i in range(6):
        games.append(arr[3 * i:3 * (i + 1)])

    def is_possible(idx) :
        if idx == 15 :
            for g in games :
                if g != [0,0,0] :
                    return False
            return True

        else :
            a_team, b_team = matches[idx]
            # a팀이 b팀을 이기는 경우
            games[a_team][0] -= 1
            games[b_team][2] -= 1
            if games[a_team][0] >= 0 and games[b_team][2] >= 0 :
                if is_possible(idx + 1):
                    return True
            games[a_team][0] += 1
            games[b_team][2] += 1

            # a팀 b팀으 비기는 경우
            games[a_team][1] -= 1
            games[b_team][1] -= 1
            if games[a_team][1] >= 0 and games[b_team][1] >= 0 :
                if is_possible(idx+1) :
                    return True
            games[a_team][1] += 1
            games[b_team][1] += 1

            # a팀이 b팀에 지는 경우
            games[a_team][2] -= 1
            games[b_team][0] -= 1
            if games[a_team][2] >= 0 and games[b_team][0] >= 0 :
                if is_possible(idx + 1):
                    return True
            games[a_team][2] += 1
            games[b_team][0] += 1

        return False

    if is_possible(0) :
        print(1)
    else :
        print(0)
