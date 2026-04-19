# 단순한 문자 코드 순이 아닌, 파일명에 포함된 숫자를 반영한 정렬 기능을 저장소 관리 프로그램에 구현하기로 했다.
# 파일명은 우선 HEAD 부분을 기준으로 사전 순으로 정렬
# HEAD 부분이 대소문자 차이 외에는 같을 경우, NUMBER의 숫자 순으로 정렬
# HEAD 부분과, NUMBER의 숫자도 같을 경우, 원래 입력에 주어진 순서 유지
files = ["img012k012.png", "img12.png", "img010.png", "img10.png"] # ["img010.png","img10.png","img000012.png","img12.png"]
pq = []
answer = []
dic_num = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
for index, file in enumerate(files):
    words = ''
    num = ''
    for index2, word in enumerate(file):
        if word in dic_num:
            num += word
            if len(num) == 5 :
                break
        else:
            if file[index2 - 1] in dic_num:
                break
            else:
                words += word.upper()
    if num != '':
        num = int(num)
    pq.append([words, num, index])

pq.sort(key=lambda x: (x[0], x[1], x[2]))
print(pq)

for i in pq:
    answer.append(files[i[2]])
print(answer)