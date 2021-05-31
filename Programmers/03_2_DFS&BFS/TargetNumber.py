# 타겟 넘버
# 문제 설명
# n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다.
# 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.
#
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
# 사용할 수 있는 숫자가 담긴 배열 numbers,
# 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# 주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
# 각 숫자는 1 이상 50 이하인 자연수입니다.
# 타겟 넘버는 1 이상 1000 이하인 자연수입니다.
# 입출력 예
# numbers	            target	    return
# [1, 1, 1, 1, 1]	    3	        5

def solution(numbers, target):
    answer = 0
    # numbers[0] 과 -1 * numbers[0]으로 시작하는 dfs 구해서 결과값 리턴

    # nums: sum해야되는 숫자들
    def dfs(nums, idx, v):
        answer = 0
        # list 크기가 numbers의 크기와 같으면 타깃넘버 비교.
        # 타깃 넘버 비교 후 같으면 answer에 1을 더하기위해 1을 return
        print()
        print(nums)
        if idx == len(numbers) - 1:
            if sum(nums) == target:
                print("return 1")
                return 1
            else:
                print("return 0")
                return 0

        # list에 v 숫자 * 1 or v 숫자 * -1 넣기
        for mult in [-1, 1]:
            newList = list(nums)
            newList.append(v)
            answer += dfs(newList, idx + 1, mult * numbers[idx + 1])
            print(f"answer: {answer}")

        print(f"total answer: {answer}")

        return answer

    answer += dfs([], 0, numbers[0])
    # answer += dfs([], -numbers[0])

    return answer

solution([1, 1, 1, 1, 1], 3)