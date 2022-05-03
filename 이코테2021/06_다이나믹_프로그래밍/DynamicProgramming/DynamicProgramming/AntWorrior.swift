//
//  AntWorrior.swift
//  DynamicProgramming
//
//  Created by 진혜림 on 2022/05/03.
//

import Foundation

class AntWorrior {
  /*
   입력값
   4
   1 3 1 5
   기댓값
   8
   */
  func solution() {
    let houseCount = Int(readLine()!)!
    let foodList = readLine()!.split(separator: " ").map{ Int($0)! }

    var dp = [Int]()
    dp.append(foodList[0])
    dp.append(max(foodList[0], foodList[1]))

    for i in 2 ..< foodList.count {
      dp.append(max(dp[i - 1], dp[i - 2] + foodList[i]))
    }

    print(dp.last!)
  }
}
