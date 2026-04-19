today = "2020.04.16"
terms = ["A 36", "S 4"]
privacies = ["2017.04.17 A", "2014.04.16 S"]

answer = []
dic = {}
todays = [int(today[0:4]), int(today[5:7]),int(today[8:10])]

for term in terms :
    a,b = term.split()
    dic[a] = int(b)

for index,privacie in enumerate(privacies) :
    end = []
    day,al = privacie.split()
    if al in dic :
        year = int(privacie[0:4])
        month = int(privacie[5:7]) + dic[al]
        while month > 12 :
            month -= 12
            year += 1
        end = [year, month, int(privacie[8:10])]

        # end = [int(privacie[0:4]), int(privacie[5:7]) + dic[al], int(privacie[8:10])]

    print(end)
    print(todays)
    if end[0] < todays[0] :
        answer.append(index+1)
    elif end[0] == todays[0] :
        if end[1] < todays[1] :
            answer.append(index+1)
        elif end[1] == todays[1] :
            if end[2] <= todays[2] :
                answer.append(index+1)

print(answer)