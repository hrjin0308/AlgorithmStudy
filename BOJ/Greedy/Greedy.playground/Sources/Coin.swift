import Foundation

let inputStr = readLine()!
let input = inputStr
  .split(separator: " ")
  .map{ Int(String($0))! }
var coins = [Int]()
var money = input[1]

for _ in 0 ..< input[0] {
  coins.append(Int(readLine()!)!)
}

coins.sort(by: >)
var count = 0
for coin in coins {
  guard coin <= money else {
    continue
  }
  let share = money / coin
  count += share
  money -= (coin * share)
  if money == 0 {
    break
  }
}

print(count)


