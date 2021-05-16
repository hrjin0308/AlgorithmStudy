# 문제 설명
# 무인도에 갇힌 사람들을 구명보트를 이용하여 구출하려고 합니다. 구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있습니다.

# 예를 들어, 사람들의 몸무게가 [70kg, 50kg, 80kg, 50kg]이고 구명보트의 무게 제한이 100kg이라면 2번째 사람과 4번째 사람은 같이 탈 수 있지만 1번째 사람과 3번째 사람의 무게의 합은 150kg이므로 구명보트의 무게 제한을 초과하여 같이 탈 수 없습니다.

# 구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 합니다.

# 사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때, 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 무인도에 갇힌 사람은 1명 이상 50,000명 이하입니다.
# 각 사람의 몸무게는 40kg 이상 240kg 이하입니다.
# 구명보트의 무게 제한은 40kg 이상 240kg 이하입니다.
# 구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로 사람들을 구출할 수 없는 경우는 없습니다.
# 입출력 예
# people    limit    return
# [70, 50, 80, 50]    100    3
# [70, 80, 50]    100    3

# from collections import deque
#
# def solution(people, limit):
#     answer = 0
#     l = len(people)
#     p = deque(people)
#
#     while l > 0:
#         answer += 1
#         print(f"p :: {p}")
#         p1 = p.popleft()
#         print(f"p1 :: {p1}")
#         l -= 1
#
#         for _ in range(l):
#             if p1 + p[l - 1] <= limit:
#                 p.pop()
#                 l -= 1
#                 break
#             else:
#                 p.rotate(-1)
#                 print(f"p :: {p}")
#
#     return answer


# 테스트 1 〉	통과 (809.37ms, 10.2MB)
# 테스트 2 〉	통과 (662.23ms, 10.3MB)
# 테스트 3 〉	통과 (390.64ms, 10.3MB)
# 테스트 4 〉	통과 (237.86ms, 10.2MB)
# 테스트 5 〉	통과 (108.17ms, 10.2MB)
# 테스트 6 〉	통과 (57.42ms, 10.3MB)
# 테스트 7 〉	통과 (136.43ms, 10.2MB)
# 테스트 8 〉	통과 (2.15ms, 10.1MB)
# 테스트 9 〉	통과 (4.10ms, 10.2MB)
# 테스트 10 〉	통과 (402.75ms, 10.2MB)
# 테스트 11 〉	통과 (203.11ms, 10.3MB)
# 테스트 12 〉	통과 (211.86ms, 10.3MB)
# 테스트 13 〉	통과 (498.88ms, 10.2MB)
# 테스트 14 〉	통과 (919.48ms, 10.2MB)
# 테스트 15 〉	통과 (7.84ms, 10.2MB)

# 여기까지 줄였는데도 안되네...
# 테스트 1 〉	통과 (538.81ms, 10.4MB)
# 테스트 2 〉	통과 (407.12ms, 10.2MB)
# 테스트 3 〉	통과 (273.97ms, 10.2MB)
# 테스트 4 〉	통과 (211.14ms, 10.3MB)
# 테스트 5 〉	통과 (85.03ms, 10.3MB)
# 테스트 6 〉	통과 (30.97ms, 10.1MB)
# 테스트 7 〉	통과 (72.41ms, 10.2MB)
# 테스트 8 〉	통과 (3.30ms, 10.4MB)
# 테스트 9 〉	통과 (3.05ms, 10.2MB)
# 테스트 10 〉	통과 (214.58ms, 10.3MB)
# 테스트 11 〉	통과 (184.43ms, 10.3MB)
# 테스트 12 〉	통과 (145.88ms, 10.3MB)
# 테스트 13 〉	통과 (262.68ms, 10.3MB)
# 테스트 14 〉	통과 (554.72ms, 10.2MB)
# 테스트 15 〉	통과 (5.91ms, 10.3MB)

from collections import deque

def solution(people, limit):
    answer = 0
    l = len(people)
    p = deque(sorted(people))

    while l > 0:
        answer += 1
        print(f"p :: {p}")
        p1 = p.popleft()
        print(f"p1 :: {p1}")
        l -= 1

        enable = list(filter(lambda x: x + p1 <= limit, p))
        print(f"## enable :: {enable}")

        if len(enable) > 0:
            idx = p.index(enable[-1])
            p.rotate(-idx)
            print(f"#### p :: {p}")
            p.popleft()
            l -= 1
            p.rotate(idx)
            print(f"#### p :: {p}")
        print()

    return answer

print(solution([70, 50, 80, 50], 100))
print(solution([70, 50, 40, 80, 60], 100))

# def solution(people, limit):
#     answer = 0
#     people.sort()
#
#     a = 0
#     b = len(people) - 1
#
#     while a < b:
#         if people[a] + people[b] <= limit:
#             a += 1
#             answer += 1
#         b -= 1
#
#     return len(people) - answer

# 위의 풀이로 했을 때 테스트 결과...
# 정확성  테스트
# 테스트 1 〉	통과 (1.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.95ms, 10.3MB)
# 테스트 3 〉	통과 (0.94ms, 10.2MB)
# 테스트 4 〉	통과 (0.85ms, 10.2MB)
# 테스트 5 〉	통과 (0.45ms, 10.2MB)
# 테스트 6 〉	통과 (0.26ms, 10.1MB)
# 테스트 7 〉	통과 (0.40ms, 10.1MB)
# 테스트 8 〉	통과 (0.04ms, 10.2MB)
# 테스트 9 〉	통과 (0.07ms, 10.2MB)
# 테스트 10 〉	통과 (0.81ms, 10.4MB)
# 테스트 11 〉	통과 (0.71ms, 10.2MB)
# 테스트 12 〉	통과 (0.67ms, 10.2MB)
# 테스트 13 〉	통과 (0.83ms, 10.2MB)
# 테스트 14 〉	통과 (0.98ms, 10.1MB)
# 테스트 15 〉	통과 (0.09ms, 10.2MB)
# 효율성  테스트
# 테스트 1 〉	통과 (7.94ms, 10.6MB)
# 테스트 2 〉	통과 (20.63ms, 10.7MB)
# 테스트 3 〉	통과 (8.13ms, 10.6MB)
# 테스트 4 〉	통과 (7.96ms, 10.7MB)
# 테스트 5 〉	통과 (7.86ms, 10.5MB)