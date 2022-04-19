//
//  Progress.swift
//  StackQueue
//
//  Created by 진혜림 on 2022/04/19.
//

import Foundation

class Progress {
  func solution(_ progresses:[Int], _ speeds:[Int]) -> [Int] {
    var result = [Int]()
    var count = 0
    var day = 1
    
    for i in 0 ..< progresses.count {
      let progress = progresses[i]
      let speed = speeds[i]
      if progress + (day * speed) < 100 {
        if count > 0 {
          result.append(count)
        }
        day = Int(ceil(Double((100 - progress)) / Double(speed)))
      }
      count += 1
    }
    
    if count > 0 {
      result.append(count)
    }
    
    return result
  }
}
