def findNumber(str, k):
    if len(str) == k:
        return ""

    # 1. 0 ~ k의 범위에서 첫번째 숫자(a) 찾기
    print(f"str: {str}, k: {k}, str[:k + 1]: {str[:k + 1]}")
    bigIdx = 0
    big = "0"
    for idx, value in enumerate(str[:k + 1]):
        print(f"idx: {idx}, value: {value}")
        if value == 9:
            bigIdx = idx
            big = value
            break

        if value > big:
            bigIdx = idx
            big = value

    print(f"bigIdx: {bigIdx}, big: {big}")

    # 2. a의 앞자리 수 만큼 k에서 빼주기.
    k -= bigIdx

    if k <= 0:
        print(f"Recursive End")
        return str[bigIdx:]
    else:
        print(f"Recursive")
        # 2에서 얻은 문자열로 재귀
        return big + findNumber(str[bigIdx + 1:], k)


def solution(number, k):
    return findNumber(number, k)


print(solution("1924", 2))
print()
print()
print()
print(solution("1231234", 3))
print()
print()
print()
print(solution("4177252841", 4))
print()
print()
print()
print(solution("4177252841", 9))

