# 다이나믹 프로그래밍

## 다이나믹 프로그래밍( == 동적 계획법)
* 메모리를 적절히 사용하여 수행 시간 효율성을 비약적으로 향상시키는 방법
* 이미 계산된 결과(작은 문제)는 별도의 메모리 영역에 저장하여 나중에 필요할 때 다시 계산하지 않고 메모리에서 꺼내 쓰도록 함  
   ->  한 번 계산해서 해결한 문제는 다시 해결하지 않도록 한다.
* 완전 탐색의 문제라 하더라도 다이나믹 프로그래밍으로 보다 효과적인 알고리즘을 만들 수 있음
* 탑다운, 보텀업

> ### [참고] 일반적인 프로그래밍 분야에서의 동적(Dynamic)의 의미
> * 자료구조에서 동적 할당(Dynamic Alloctaion)은 '**프로그램이 실행 되는 도중에 실행에 필요한 메모리를 할당하는 기법**'
> * 다이나믹 프로그래밍에서의 '다이나믹(동적)'은 **별 의미 없다...**

* 문제가 다음의 조건을 만족할 때 사용  
  * **최적 부분 구조 (Optimal Substructure)**
     * 큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아서 큰 문제를 해결 
     * Divide and conquer...랑 비슷?
  * **중복되는 부분 문제 (Overlapping Subproblem)**
     * 동일한 작은 문제를 반복적으로 해결

## 메모이제이션 (Memoization)
* 다이나믹 프로그래밍을 구현하는 방법 중 하나(탑다운)
* 한 번 게산한 결과를 메모리 공간에 메모하는 기법
   * 같은 문제를 다시 호출하면 메모했던 결과를 그대로 가져옴
   * 별도의 테이블(or 배열)에 값을 기록해 놓는다는 점에서 캐싱(Caching)이라고도 함
      * 실제로 코드 구현시 해당 배열의 변수명을 caching, memo, table, dp, d 등을 사용

## 탑다운 VS 보텀업
* 탑다운(메모이제이션) == 하향식
* 보텀업 == 상향식
* 다이나믹 프로그래밍의 전형적인 형태는 보텀업 방식
   * DP 테이블: 결과 저장용 리스트 
* 엄밀히 말하면 메모이제이션은 **이전에 계산된 결과를 일시적으로 기록해 놓는 넓은 개념을 의미** 
  * == 메모이제이션이 다이나믹 프로그래밍에 국한된 개념이 아니다
  * 한 번 계산된 결과를 담아 놓기만 하고 다이나믹 프로그래밍을 위해 활용하지 않을 수도 있음.


## [예시] 피보나치 수열
`1, 1, 2, 3, 5, 8, 13....  `  

* 점화식(인접한 항들 사이의 관계식)을 이용  
* ((((첫번째 + 두번째) + 세번째) + 네번째 + 다섯번째)... + N번째)  
* 프로그래밍에서 이런 수열을 표현하기 위해선 배열이나 리스트를 이용해 표현
* 단순 재귀를 이용한 코드  

```python
def fibo(x):
	if x == 1 or x == 2:
		return 1
	return fibo(x - 1) + fibo(x - 2)

print(fibo(4))		# 실행결과: 3
```

###피보나치 수열의 시간 복잡도 분석
* 단순 재귀 함수로 피보나치 수열을 해결하면 지수 시간 복잡도
* 중복되는 부분이 여러번 호출되면서 불필요한 계산 *(f(2)가 매우 여러번 호출)*
* 빅오 표기법 기준 O(2^N)
  * f(30)을 계산하기 위해 약 10억가량의 연산 수행 

### 피보나치 수열의 효율적인 해법
* 다이나믹 프로그래밍의 사용 조건 확인
   *  최적 부분 구조
   *  중복되는 부분 문제
* 위의 사용 조건에 만족  
* [피보나치 수열: 탑다운 다이나믹 프로그래밍 소스 코드](https://github.com/hrjin0308/PythonStudy/blob/master/%EC%9D%B4%EC%BD%94%ED%85%8C2021/06_%EB%8B%A4%EC%9D%B4%EB%82%98%EB%AF%B9_%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D/Fibo_TopDown.ipynb)  

```python
# 한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
d = [0] * 100

# 피보나치 함수를 재귀 함수로 구현
def fibo(x):
    if x == 1 or x == 2:
        return 1
    # 이미 계산된 적이 있다면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]
    
print(fibo(99))		# 218922995834555169026
```

* [피보나치 수열: 보텀업 다이나믹 프로그래밍 소스 코드](https://github.com/hrjin0308/PythonStudy/blob/master/%EC%9D%B4%EC%BD%94%ED%85%8C2021/06_%EB%8B%A4%EC%9D%B4%EB%82%98%EB%AF%B9_%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D/Fibo_BottomUp.ipynb)

```python
# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 첫 번째 피보나치 수, 두 번째 피보나치 수를 1로 초기화
d[1] = 1
d[2] = 1
n = 99

# 피보나치 함수를 반복문으로 구현(바텀업)
for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])		# 218922995834555169026
```

* 피보나치 수열에 메모이제이션을 적용하면 함수의 시간 복잡도는 O(N) 기대 가능

##다이나믹 프로그래밍 VS 분할 정복
* 다이나믹 프로그래밍과 분할 정복은 모두 **최적 부분 구조**를 가질 때 사용
   * 큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아서 큰 문제를 해결할 수 있는 상황
* 차이점은 부분 문제의 중복
   * 다이나믹 프로그래밍: 각 부분 문제들이 서로 영향을 미치며 부분 문제가 중복
   * 분할 정복 문제: 동일한 부분 문제가 반복적으로 계산 X
   * ex> 퀵 정렬
   
## 다이나믹 프로그래밍 문제에 접근하는 방법
* ***주어진 문제가 다이나믹 프로그래밍 유형임을 파악***
* 가장 먼저 그리디, 구현, 완전 탐색 등의 아이디어로 문제를 해결할 수 있는지 검토
   * 다른 알고리즘으로 풀이 방법이 떠오르지 않으면 다이나믹 프로그래밍을 고려 
* 재귀 함수로 비효율적인 완전 탐색 프로그램을 작성한 뒤 (탑다운) 작은 문제에서 구한 답이 큰 문제에서 그대로 사용도리 수 있으면, 코드를 개선하는 방법 사용
* _일반적인 코딩 테스트 수준에서는 기본 유형의 다이나믹 프로그래밍 문제가 출제_


## LIS(Longest Increased Subsequence)
* 최장 증가 수열
* 원소 중 몇가지를 빼서 증가수열을 만들 때 가장 원소를 많이 가지면서 만들 수 있도록 하는 알고리즘
* 이중포문을 사용한 경우
   * 시간복잡도: O(N^2) 

```python
d = [0] * n

for i in range(1, n):
    for j in range(i):
        if atks[j] > atks[i]:
            d[i] = max(d[i], d[j] + 1)
``` 

* 이분탐색을 사용한 경우 **(코드 추가 필요)**
    * 시간복잡도: O(NLogN) 