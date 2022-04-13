//
//  Router.swift
//  BinarySearchBOJ
//
//  Created by 진혜림 on 2022/04/14.
//

import Foundation

class Router {
  func solution() {
    let input = readLine()!.split(separator: " ").map { Int(String($0))! }
    var distance = [Int]()
    for _ in 0 ..< input[0] {
      distance.append(Int(readLine()!)!)
    }
    distance.sort()

    let end = (distance.last! - distance.first!)
    var max = 0
    binarySearch(distance, input[1], &max, 1, end)
    print(max)
  }
  
  func binarySearch(_ array: [Int], _ num: Int, _ max: inout Int, _ start: Int, _ end: Int) {
    guard start <= end else {
      return
    }
    
    let mid = (start + end) / 2
    var count = 1
    var lastAddr = array[0]
    for i in 1 ..< array.count {
      let addr = array[i]
      if addr - lastAddr >= mid {
        count += 1
        lastAddr = addr
        
        if count >= num {
          if mid > max {
            max = mid
          }
          binarySearch(array, num, &max, mid + 1, end)
          return
        }
      }
    }
    binarySearch(array, num, &max, start, mid - 1)
  }
}
