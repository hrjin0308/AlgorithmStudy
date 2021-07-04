# 신나는 함수 실행
# 문제
# 재귀 호출만 생각하면 신이 난다! 아닌가요?
#
# 다음과 같은 재귀함수 w(a, b, c)가 있다.
#
# if a <= 0 or b <= 0 or c <= 0,
# then w(a, b, c) returns: 1
#
# if a > 20 or b > 20 or c > 20,
# then w(a, b, c) returns: w(20, 20, 20)
#
# if a < b and b < c,
# then w(a, b, c) returns: w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
#
# otherwise it returns: w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
# 위의 함수를 구현하는 것은 매우 쉽다. 하지만, 그대로 구현하면 값을 구하는데 매우 오랜 시간이 걸린다. (예를 들면, a=15, b=15, c=15)
#
# a, b, c가 주어졌을 때, w(a, b, c)를 출력하는 프로그램을 작성하시오.
#
# 입력
# 입력은 세 정수 a, b, c로 이루어져 있으며, 한 줄에 하나씩 주어진다.
# 입력의 마지막은 -1 -1 -1로 나타내며, 세 정수가 모두 -1인 경우는 입력의 마지막을 제외하면 없다.
#
# 출력
# 입력으로 주어진 각각의 a, b, c에 대해서, w(a, b, c)를 출력한다.
#
# 제한
# -50 ≤ a, b, c ≤ 50

# 예제 입력 1
# 1 1 1
# 2 2 2
# 10 4 6
# 50 50 50
# -1 7 18
# -1 -1 -1
# 예제 출력 1
# w(1, 1, 1) = 2
# w(2, 2, 2) = 4
# w(10, 4, 6) = 523
# w(50, 50, 50) = 1048576
# w(-1, 7, 18) = 1

# 위의 식으로 하면 refer복사처럼 된다... 파이썬은 이게 어려움
# 아래의 식으로 해야 값을 변화시킬때 서로 영향이 가지 않아서 제대로 된 값을 얻을 수 있다.
# d = [[[0] * 21] * 21] * 21
d = [[[0]*21 for _ in range(21)] for __ in range(21)]

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if d[a][b][c] != 0:
        return d[a][b][c]

    if a < b < c:
        d[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return d[a][b][c]

    d[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
    return d[a][b][c]

array = []

while True:
    a, b, c = list(map(int, input().split()))

    if a == -1 and b == -1 and c == -1:
        break

    array.append([a, b, c])

for a, b, c in array:
    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")
