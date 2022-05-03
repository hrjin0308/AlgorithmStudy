//
//  MakeOne.swift
//  DynamicProgramming
//
//  Created by 진혜림 on 2022/05/03.
//

import Foundation

class MakeOne {
  func solution() {
    let target = Int(readLine()!)!
    var dp = Array(repeating: 0, count: 2)

    if target < 2 {
      print("0")
    } else {
      for i in 2 ... target {
        dp.append(dp[i - 1] + 1)
        if i % 2 == 0 {
          dp[i] = min(dp[i], dp[i / 2] + 1)
        }
        if i % 3 == 0 {
          dp[i] = min(dp[i], dp[i / 3] + 1)
        }
      }
      print(dp[target])
    }
  }
}
