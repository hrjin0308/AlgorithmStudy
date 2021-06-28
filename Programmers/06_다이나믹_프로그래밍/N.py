# N으로 표현
# 문제 설명
# 아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.
#
# 12 = 5 + 5 + (5 / 5) + (5 / 5)
# 12 = 55 / 5 + 5 / 5
# 12 = (55 + 5) / 5
#
# 5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.
# 이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.
#
# 제한사항
# N은 1 이상 9 이하입니다.
# number는 1 이상 32,000 이하입니다.
# 수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
# 최솟값이 8보다 크면 -1을 return 합니다.
#
# 입출력 예
# N	    number	    return
# 5	    12	        4
# 2	    11	        3
#
# 입출력 예 설명
# 예제 #1
# 문제에 나온 예와 같습니다.
#
# 예제 #2
# 11 = 22 / 2와 같이 2를 3번만 사용하여 표현할 수 있습니다.

# @see https://velog.io/@j_user0719/N%EC%9C%BC%EB%A1%9C-%ED%91%9C%ED%98%84-PYTHON

# 쥰내 모르겟네
# 일단 답코드...
# def solution(N, number):
#     answer = -1
#     dp = []
#
#     for i in range(1, 9):
#         # i = N의 개수
#         all_case = set()
#         check_number = int(str(N) * i)
#         # {N}, {NN} , {NNN}...
#         all_case.add(check_number)
#
#         for j in range(0, i - 1):
#             // j
#             개를
#             사용해서
#             만든
#             값들
#         for op1 in dp[j]:
#             for op2 in dp[-j - 1]:
#                 all_case.add(op1 - op2)
#                 all_case.add(op1 + op2)
#                 all_case.add(op1 * op2)
#                 if op2 != 0:
#                     all_case.add(op1 // op2)
#
#     if number in all_case:
#         answer = i
#         break
#
#     dp.append(all_case)
#
#
# return answer

def solution(N, number):
    answer = 0

    d = [set()] * 8
    return answer
