//
//  SugarDelivery.swift
//  DynamicProgramming
//
//  Created by 진혜림 on 2022/05/03.
//

import Foundation

class SugarDelivery {
  func solution() {
    let num = Int(readLine()!)!
    var dp = Array(repeating: -1, count: 5001)
    dp[3] = 1
    dp[5] = 1

    if num <= 5 {
      print(dp[num])
    } else {
      for i in 6 ... num {
        if dp[i - 3] != -1 && dp[i - 5] != -1 {
          dp[i] = min(dp[i - 3] + 1, dp[i - 5] + 1)
        } else {
          if dp[i - 3] != -1 {
            dp[i] = dp[i - 3] + 1
          } else if dp[i - 5] != -1 {
            dp[i] = dp[i - 5] + 1
          }
        }
      }
      
      print(dp[num])
    }
  }
}
