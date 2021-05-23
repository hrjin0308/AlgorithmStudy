#
# 문제 설명
# 고고학자인 "튜브"는 고대 유적지에서 보물과 유적이 가득할 것으로 추정되는 비밀의 문을 발견하였습니다.
# 런데 문을 열려고 살펴보니 특이한 형태의 자물쇠로 잠겨 있었고
# 문 앞에는 특이한 형태의 열쇠와 함께 자물쇠를 푸는 방법에 대해 다음과 같이 설명해 주는 종이가 발견되었습니다.
#
# 잠겨있는 자물쇠는 격자 한 칸의 크기가 1 x 1인 N x N 크기의 정사각 격자 형태이고
# 특이한 모양의 열쇠는 M x M 크기인 정사각 격자 형태로 되어 있습니다.
#
# 자물쇠에는 홈이 파여 있고 열쇠 또한 홈과 돌기 부분이 있습니다.
# 열쇠는 회전과 이동이 가능하며 열쇠의 돌기 부분을 자물쇠의 홈 부분에 딱 맞게 채우면 자물쇠가 열리게 되는 구조입니다.
# 자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 자물쇠를 여는 데 영향을 주지 않지만,
# 자물쇠 영역 내에서는 열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확히 일치해야 하며 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안됩니다.
# 또한 자물쇠의 모든 홈을 채워 비어있는 곳이 없어야 자물쇠를 열 수 있습니다.
#
# 열쇠를 나타내는 2차원 배열 key와 자물쇠를 나타내는 2차원 배열 lock이 매개변수로 주어질 때,
# 열쇠로 자물쇠를 열수 있으면 true를, 열 수 없으면 false를 return 하도록 solution 함수를 완성해주세요.
#
# 제한사항
# key는 M x M(3 ≤ M ≤ 20, M은 자연수)크기 2차원 배열입니다.
# lock은 N x N(3 ≤ N ≤ 20, N은 자연수)크기 2차원 배열입니다.
# M은 항상 N 이하입니다.
# key와 lock의 원소는 0 또는 1로 이루어져 있습니다.
# 0은 홈 부분, 1은 돌기 부분을 나타냅니다.
# 입출력 예
# key	lock	result
# [[0, 0, 0], [1, 0, 0], [0, 1, 1]]	[[1, 1, 1], [1, 1, 0], [1, 0, 1]]	true

def rotateKey(key):
    n = len(key)
    tmpKey = [[0 for col in range(n)] for row in range(n)]
    for i, rows in enumerate(key):
        for j, value in enumerate(rows):
            tmpKey[j][(n - 1) - i] = key[i][j]
    return tmpKey

# 돌기 부분이 중복인지
def checkValid(key, lock):
    for i, rows in enumerate(key):
        for j, keyValue in enumerate(rows):
            lockValue = lock[i][j]
            # And
            if keyValue and lockValue:
                return False
    return True

# 주어진 키로 자물쇠를 열 수 있는지
def lockOpen(key, lock):
    for i, rows in enumerate(key):
        for j, keyValue in enumerate(rows):
            lockValue = lock[i][j]
            # XOR
            if not ((keyValue and (not lockValue)) or ((not keyValue) and lockValue)):
                return False
    return True

def printArray(array):
    for rows in array:
        for value in rows:
            print(value, end = " ")
        print()
    print()

def solution(key, lock):
    canOpen = False
    rotateCount = 0
    lockSize = len(lock)
    keySize = len(key)
    # printKey(key)
    # key = rotateKey(key)
    # printKey(key)

    while rotateCount < 4:
        # lock과 key의 크기가 다르기 때문에 lock 크기만큼의 2차원 배열로 key의 위치 잡아주기
        startPos = (keySize - 1, keySize - 1)
        compareKey = [[0 for col in range(lockSize)] for row in range(lockSize)]

        for i in range(lockSize + 2 * keySize - 1):
            for j in range(lockSize + 2 * keySize - 1):


        rotateCount += 1

    return canOpen

solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])

#
# 이걸 어케풀어..ㅠ
# https://velog.io/@tjdud0123/%EC%9E%90%EB%AC%BC%EC%87%A0%EC%99%80-%EC%97%B4%EC%87%A0-2020-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EA%B3%B5%EC%B1%84-python
#
# # 파이썬
# def attach(x, y, M, key, board):
#     for i in range(M):
#         for j in range(M):
#             board[x + i][y + j] += key[i][j]
#
#
# def detach(x, y, M, key, board):
#     for i in range(M):
#         for j in range(M):
#             board[x + i][y + j] -= key[i][j]
#
#
# def rotate90(arr):
#     return list(zip(*arr[::-1]))
#
#
# def check(board, M, N):
#     for i in range(N):
#         for j in range(N):
#             if board[M + i][M + j] != 1:
#                 return False;
#     return True
#
#
# def solution(key, lock):
#     M, N = len(key), len(lock)
#
#     board = [[0] * (M * 2 + N) for _ in range(M * 2 + N)]
#     # 자물쇠 중앙 배치
#     for i in range(N):
#         for j in range(N):
#             board[M + i][M + j] = lock[i][j]
#
#     rotated_key = key
#     # 모든 방향 (4번 루프)
#     for _ in range(4):
#         rotated_key = rotate90(rotated_key)
#         for x in range(1, M + N):
#             for y in range(1, M + N):
#                 # 열쇠 넣어보기
#                 attach(x, y, M, rotated_key, board)
#                 # lock 가능 check
#                 if (check(board, M, N)):
#                     return True
#                 # 열쇠 빼기
#                 detach(x, y, M, rotated_key, board)
#
#     return False