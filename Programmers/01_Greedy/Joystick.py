
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
      startIdx = name.find("A")
      endIdx = name.find("A", startIdx + 1)
      while True:
        if endIdx == startIdx + 1 and endIdx != len(name) - 1:
          # 연속될 때
          for char in name[endIdx + 1:]:
            if char == "A":
              endIdx += 1
              continue
            else:
              break
          break
        else:
          # 연속이 아닐 때
          if endIdx == -1:
            break
          startIdx = int(endIdx)
          endIdx = name.find("A", endIdx + 1)

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