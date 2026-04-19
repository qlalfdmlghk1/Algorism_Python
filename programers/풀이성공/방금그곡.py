m, musicinfos = "ABC",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]

def solution(m, musicinfos):
    answer_list = []
    musics = []
    def replaces(s) :
        replace_dic = {'A#':'H', 'B#':'I', 'C#':'J', 'D#':'K', 'E#':'L', 'F#':'M', 'G#':'N'}
        for old,new in replace_dic.items() :
            s = s.replace(old,new)
        return s
    # m = m.replace('A#', 'H')
    # m = m.replace('B#', 'I')
    # m = m.replace('C#', 'J')
    # m = m.replace('D#', 'K')
    # m = m.replace('E#', 'L')
    # m = m.replace('F#', 'M')
    # m = m.replace('G#', 'N')
    m = replaces(m)

    for idx,musicinfo in enumerate(musicinfos) :
        music = musicinfo.split(',')
        musics.append(music)  # 시작 시간, 끝나는 시간, 음악 제목, 악보 정보
        for music in musics :
            hour1,minute1 = music[0].split(':')
            hour2,minute2 = music[1].split(':')
            time = int(hour2) * 60 + int(minute2) - (int(hour1) * 60 + int(minute1))  # 전체 시간
            music[3] = replaces(music[3])
            # music[3] = music[3].replace('A#', 'H')
            # music[3] = music[3].replace('B#', 'I')
            # music[3] = music[3].replace('C#', 'J')
            # music[3] = music[3].replace('D#', 'K')
            # music[3] = music[3].replace('F#', 'L')
            # music[3] = music[3].replace('G#', 'M')
            # music[3] = music[3].replace('E#', 'N')


            if time > len(music[3]) :
                music[3] = music[3] * ((time // len(music[3])) + 1)
            music[3] = music[3][:time]
            # print(music[3])
            if m in music[3] :
                answer_list.append((time,idx,music[2]))

    if not answer_list :
        answer = '(None)'
    else :
        answer_list.sort(key=lambda x : (-x[0], x[1]))
        answer = answer_list[0][2]

    return answer

print(solution(m, musicinfos))