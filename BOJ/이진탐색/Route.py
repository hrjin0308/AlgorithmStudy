# 공유기 설치
#
# 문제
# 도현이의 집 N개가 수직선 위에 있다.
# 각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.
#
# 도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다.
# 최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치할 수 있고,
# 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.
#
# C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)이 하나 이상의 빈 칸을 사이에 두고 주어진다.
# 둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi (0 ≤ xi ≤ 1,000,000,000)가 한 줄에 하나씩 주어진다.
#
# 출력
# 첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리를 출력한다.

# 도현이는 벌써 집이 N개나 있네..부러워라...

# 문제 풀이
# 1. 집의 번호를 sort하여 첫번째 값을 start, 마지막 값을 end로 두고 시작 (거리 = mid)
# 2. 이진 탐색할 때 start와 end가 어떻게 움직일지에 대한 조건
#    2-1) start~mid 만큼 거리를 최소 거리로 했을 때 C개의 공유기가 다 설치되는지
#    2-2) 설치된다면 거리값 저장 후 mid + 1을 start로 변경
#    2-3) 설치되지 않는다면 mid - 1을 end로 변경

n, c = list(map(int, input().split()))
houses = [int(input()) for _ in range(n)]
houses.sort()
start = 0
end = n - 1
maxDistance = 0

# houses[posIdx1]~houses[posIdx2]만큼 거리를 최소 거리로 했을 때 C개의 공유기가 다 설치되는지 확인
def isSetupEnabled(posIdx1, posIdx2):
    others = houses[posIdx2 + 1:]
    # 남아있는 집 수가 설치해야 될 공유기의 수보다 적은 경우 return False
    if len(others) < c - 1:
        print("남아있는 집 수가 설치해야 될 공유기의 수보다 적은 경우 return False")
        return False

    distance = houses[posIdx2] - houses[posIdx1]
    lastHouse = houses[posIdx2]
    count = 0
    for house in others:
        print("house", house, "lastHouse", lastHouse)
        if house - lastHouse <= distance:
            continue
        count += 1
        lastHouse = house

    if count < c - 1:
        print("카운트가 공유기의 수보다 적은 경우 return False", count)
        return False
    else:
        print("카운트가 공유기의 수보다 큰 경우 return True", count)
        return True

while start < end:
    mid = (start + end) // 2
    print(start, end, mid)
    distance = houses[mid] - houses[0]
    if isSetupEnabled(start, mid):
        # 설치된다면 distance값 저장 후 mid + 1을 start로 변경
        print("isSetupEnabled True", distance)
        maxDistance = distance
        start = mid + 1
    else:
        print("isSetupEnabled False", distance)
        end = mid - 1

print(maxDistance)


