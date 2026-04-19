def count_tails(coin, n):
    total_tails = 0
    # 각 행의 뒷면(T)의 개수를 최소화하여 합산
    for i in range(n):
        row_tails = 0
        for j in range(n):
            row_tails += coin[i][j]  # 각 행의 T 개수 계산
        # 각 행에 대해 최소값 선택 (T 개수 vs H 개수)
        total_tails += min(row_tails, n - row_tails)
    return total_tails


def turn_column(coin, col, n):
    # 특정 열의 모든 값을 뒤집음 (1 -> 0, 0 -> 1)
    for i in range(n):
        coin[i][col] ^= 1


def solution(coin):
    n = len(coin)
    min_tails = float('INF')  # 최소 뒷면 개수를 무한대로 초기화

    # 각 비트 조합마다 열을 뒤집는 경우의 수를 고려 (2^n개의 조합 탐색)
    for bit in range(1 << n):
        copy_coin = [row[:] for row in coin]  # 원본 배열 복사

        # 비트가 설정된 열만 뒤집기
        for j in range(n):
            if bit & (1 << j):  # bit의 j번째 비트가 1인지 확인
                turn_column(copy_coin, j, n)

        # 뒤집은 행렬에서 최소 뒷면(T) 개수를 계산
        min_tails = min(min_tails, count_tails(copy_coin, n))

    return min_tails


n = int(input())
coin = []
for _ in range(n):
    c = input()
    row = []
    for i in c:
        if i == 'T':
            row.append(1)  # T는 1로 처리
        else:
            row.append(0)  # H는 0으로 처리
    coin.append(row)

print(solution(coin))
