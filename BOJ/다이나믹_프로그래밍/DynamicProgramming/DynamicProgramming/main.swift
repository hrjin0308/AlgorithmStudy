//
//  main.swift
//  DynamicProgramming
//
//  Created by 진혜림 on 2022/05/03.
//

import Foundation

let count = Int(readLine()!)!
let numberList = readLine()!.split(separator: " ").map { Int($0)! }

var dp = Array(repeating: 0, count: count)
dp[0] = numberList[0]
var max = dp[0]

for i in 1 ..< count {
  guard dp[i - 1] > 0 else {
    dp[i] = numberList[i]
    continue
  }
  
  let sum = dp[i - 1] + numberList[i]
  dp[i] = sum
  
  if max < sum {
    max = sum
  }
}

print(max)
