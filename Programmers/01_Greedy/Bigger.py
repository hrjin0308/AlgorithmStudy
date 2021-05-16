
def solution(number, k):
    length = len(number)
    if length == k:
        return number

    a = 0
    result = ""
    while k > 0:
        big = (0, "")  # 큰 수의 인덱스 정보와 값

        # 1. a ~ k의 범위에서 첫번째 숫자(big) 찾기
        print(f"찾으려는 범위 :: {number[a:a+k+1]}")
        for i in range(a, a + k + 1):
            num = number[i]
            if num == "9":
                big = (i, num)
                break

            if big[1] < number[i]:
                big = (i, number[i])

        print(f"big :: {big}")

        # 2-1. result에 big 업데이트
        result += big[1]
        # 2-2. k 초기화
        k -= big[0] - a
        print(f"k :: {k}, a:: {a}")

        # 3. result의 길이가 length - k면 break
        if len(result) == length - k:
            break

        # 4. a초기화
        a = big[0] + 1

    if len(result) != length - k:
        result += number[big[0] + 1:]

    return result


