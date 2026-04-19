import copy
storage,requests = ["AAAAA", "ABCDA", "AGAEA", "AZAFA", "ZYAAA"],["BB", "DD", "Z", "Y", "Z", "G", "C", "E", "F"]

def solution(storage, requests):
    n,m = len(storage),len(storage[0])
    board = []
    for st in storage :
        li = []
        for s in st :
            li.append(s)
        board.append(li)

    # 외부와 연결되어 있는지 RETURN 하는 함수
    def check_border(r,c,cur_board) :
        dr = [1,-1,0,0]
        dc = [0,0,1,-1]
        if r == 0 or c == 0 or r == n-1 or c == m-1 :
            return True
        for i in range(4) :
            nex_r = r + dr[i]
            nex_c = c + dc[i]
            if 0 <= nex_r < n and 0 <= nex_c < m :
                if cur_board[nex_r][nex_c] == 0 :
                    return True
        return False

    for request in requests :
        for i in range(n) :
            for j in range(m) :
                if board[i][j] == -1 :
                    if check_border(i,j,board) :
                        board[i][j] = 0
        cur_board = copy.deepcopy(board)

        # 지게차
        if len(request) == 1 :
            for i in range(n) :
                for j in range(m) :
                    if board[i][j] == request and check_border(i,j,cur_board) :
                        board[i][j] = 0

        # 크레인
        else :
            request = request[0]
            for i in range(n) :
                for j in range(m) :
                    if board[i][j] == request :
                        if check_border(i,j,cur_board) :
                            board[i][j] = 0
                        else :
                            board[i][j] = -1

    answer = n * m
    for st in board :
        answer -= st.count(0)
        answer -= st.count(-1)

    return answer

print(solution(storage,requests))
