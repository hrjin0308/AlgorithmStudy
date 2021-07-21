# 행성 터널
#
# 문제
# 때는 2040년, 이민혁은 우주에 자신만의 왕국을 만들었다.
# 왕국은 N개의 행성으로 이루어져 있다.
# 민혁이는 이 행성을 효율적으로 지배하기 위해서 행성을 연결하는 터널을 만들려고 한다.
#
# 행성은 3차원 좌표위의 한 점으로 생각하면 된다.
# 두 행성 A(xA, yA, zA)와 B(xB, yB, zB)를 터널로 연결할 때 드는 비용은 min(|xA-xB|, |yA-yB|, |zA-zB|)이다.
#
# 민혁이는 터널을 총 N-1개 건설해서 모든 행성이 서로 연결되게 하려고 한다.
# 이때, 모든 행성을 터널로 연결하는데 필요한 최소 비용을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 행성의 개수 N이 주어진다. (1 ≤ N ≤ 100,000)
# 다음 N개 줄에는 각 행성의 x, y, z좌표가 주어진다.
# 좌표는 -109보다 크거나 같고, 109보다 작거나 같은 정수이다.
# 한 위치에 행성이 두 개 이상 있는 경우는 없다.
#
# 출력
# 첫째 줄에 모든 행성을 터널로 연결하는데 필요한 최소 비용을 출력한다.
#
# 예제 입력 1
# 5
# 11 -15 -15
# 14 -5 -15
# -1 -1 -5
# 10 -4 -1
# 19 -4 19
# 예제 출력 1
# 4

# 최소 신장 트리 사용하기

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드 갯수
n = int(input())
# 노드 정보
planets = [list(map(int, input().split())) for _ in range(n)]

parent = [0] * (n + 1)  # 부모 테이블 초기화
# 부모 테이블상에서 부모를 자기자신으로 초기화
for i in range(1, n + 1):
    parent[i] = i

result = 0

# 모든 간선 구하기
edges = []
for i in range(n - 1):
    a = planets[i]
    for j in range(i + 1, n):
        b = planets[j]
        cost = min(abs(a[0] - b[0]), abs(a[1] - b[1]), abs(a[2] - b[2]))
        # 비용 순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
        edges.append((cost, i, j))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)