//
//  CuttingLanLine.swift
//  BinarySearchBOJ
//
//  Created by 진혜림 on 2022/04/13.
//

import Foundation

class CuttingLanLine {
  func solution() {
    let input = readLine()!.split(separator: " ").map { Int(String($0))! }
    var lines = [Int]()

    for _ in 0 ..< input[0] {
      lines.append(Int(readLine()!)!)
    }

    let end = lines.sorted().last!
    var maxLength = 0

    binarySearch(lines, input[1], &maxLength, 1, end)
    print(maxLength)
  }
  
  func binarySearch(_ array: [Int], _ target: Int, _ maxLength: inout Int, _ start: Int, _ end: Int) {
    guard start <= end else {
      return
    }
    
    let mid = (start + end) / 2
    let sliced = array
      .map { $0 / mid }
      .reduce(0, +)
    
    if sliced >= target {
      maxLength = mid
      binarySearch(array, target, &maxLength, mid + 1, end)
    } else {
      binarySearch(array, target, &maxLength, start, mid - 1)
    }
  }
}
