# ▲ - 다음 알파벳
# ▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
# ◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
# ▶ - 커서를 오른쪽으로 이동

# 예를 들어 아래의 방법으로 "JAZ"를 만들 수 있습니다.

# - 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
# - 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
# - 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
# 따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.

#   name	  return
# "JEROEN"	  56
# "JAN"	      23

def solution(name):
    cursorCount = 0
    countList = list(
      map(
        lambda x: 
        # 주어진 철자의 int값에서 A의 int값을 뺀 값과
        # Z의 int값에서 주어진 철자의 int값 중 min값
        # ABCDEFGHIJKLMNOPQRSTUVWXYZ
        min(
          abs(ord(x) - ord("A")), 
          abs(ord("Z") - ord(x)) + 1
        ), 
        list(name)
      )
    )

    # cursorCount 계산(좌/우 한방향)
    tmpCountListR = list(countList) # 오른쪽으로 간 경우
    tmpCountListL = list(countList) # 왼쪽으로 간 경우
    for i in range(len(countList)):
      tmpCountListR[i] = 0
      tmpCountListL[-i] = 0

      if len(list(filter(lambda x: x != 0, tmpCountListR))) == 0\
        or len(list(filter(lambda x: x != 0, tmpCountListL))) == 0\
        or i == len(countList) - 1:
        cursorCount += i     # i만큼 커서 이동
        break

    # cursorCount 계산(오른쪽으로 갔다가 돌아오는 경우)
    if name.find("A") != -1 and name.count("A") > 1:
      # preIdx = name.find("A")
      # nextIdx = name.find("A", preIdx + 1)
      # while nextIdx != -1:
      #   print(f"preIdx: {preIdx}, nextIdx: {nextIdx}")
      #   aLength = nextIdx - preIdx + 1
      #   if name[preIdx:nextIdx + 1] == "A" * aLength:
      #     # break 안걸고 길이 비교해서 제일 긴걸로 하도록 해야될거 같긴 한데...귀찮다...
      #     print("if?")
      #     frontCount = 2 * (len(name[:preIdx]) - 1)
      #     backCount = len(name[nextIdx:]) - 1
      #     cursorCount = min(cursorCount, frontCount + backCount)
      #     break
      #   else:
      #     print("else?")
      #     preIdx = int(nextIdx)
      #     nextIdx = name.find("A", preIdx + 1)
      startIdx = name.find("A")
      
      while :
        endIdx = int(startIdx) + 1  #init
        if endIdx == startIdx + 1:
          # 연속될 때
          print("if")
          endIdx = name.find("A", endIdx + 1)
          for char in rnage(endIdx):
            if char == "A":

        else:
          # 연속이 아닐 때
          print("else")
          if endIdx == -1:
            break
          startIdx = int(endIdx)
          endIdx = name.find("A", endIdx + 1)

      print(f"startIdx: {startIdx}")
      print(f"endIdx: {endIdx}")
      print(f"name[startIdx:endIdx + 1]: {name[startIdx:endIdx + 1]}")
      
      if endIdx != -1:
        frontCount = 2 * (len(name[:startIdx]) - 1)
        backCount = len(name[endIdx:]) - 1
        cursorCount = min(cursorCount, frontCount + backCount)

    return cursorCount + sum(countList)


print(solution("JAZ"))
print(solution("JEROEN"))
print(solution("JAN"))
print(solution("BBBAAAB"))
print(solution("ABABAAAAABA"))