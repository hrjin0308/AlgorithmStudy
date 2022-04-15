//
//  SteppingStone.swift
//  BinarySearchProgrammers
//
//  Created by 진혜림 on 2022/04/15.
//

import Foundation

class SteppingStone {
  func solution(_ distance:Int, _ rocks:[Int], _ n:Int) -> Int {
    let sorted = rocks.sorted()
    
    var rockDistances = [sorted.first!]
    for i in 1 ..< sorted.count {
      rockDistances.append(sorted[i] - sorted[i - 1])
    }
    rockDistances.append(distance - sorted.last!)

    var start = 1
    var end = distance
    var maxValue = 0
    
    while start <= end {
      var tmpRockDistances = rockDistances
      var removedCount = 0
      let mid = (start + end) / 2
      var pos = 0
      
      while pos < tmpRockDistances.count {
        let distance = tmpRockDistances[pos]
        if distance < mid {
          removedCount += 1
          tmpRockDistances.remove(at: pos)
          
          if pos == tmpRockDistances.count {
            tmpRockDistances[pos - 1] += distance
          } else {
            tmpRockDistances[pos] += distance
          }
        } else {
          pos += 1
        }
      }
      
      if removedCount > n {
        end = mid - 1
      } else {
        if mid > maxValue {
          maxValue = mid
        }
        start = mid + 1
      }
    }
    
    return maxValue
  }
}
