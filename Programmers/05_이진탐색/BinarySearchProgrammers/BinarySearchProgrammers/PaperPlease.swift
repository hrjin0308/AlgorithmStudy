//
//  PaperPlease.swift
//  BinarySearchProgrammers
//
//  Created by 진혜림 on 2022/04/15.
//

import Foundation

class PaperPlease {
  func solution(_ n:Int, _ times:[Int]) -> Int64 {
    var start =  1
    var end = n * times[times.count - 1]
    var min = end
    
    while start <= end {
      let mid = (start + end) / 2
      let count = times
        .map { mid / $0 }
        .reduce(0, +)
      
      if count >= n {
        min = mid
        end = mid - 1
      } else {
        start = mid + 1
      }
    }
    
    return Int64(min)
  }
}
