# 유클리드 호제법
#   두 자연수 A, B에 대하여 (A > B) A를 B로 나눈 나머지를 R
#   이 때 A와 B의 최대 공약수는 B와 R의 최대 공약수와 같다

# 재귀함수로 구현한 유클리드 호제법
def myGCD(num1, num2):
    if num1 < num2:
        tmp = num1
        num1 = num2
        num2 = tmp

    if num1 % num2 == 0:
        return num2
    else:
        return myGCD(num2, num1 % num2)

print(myGCD(192, 162))