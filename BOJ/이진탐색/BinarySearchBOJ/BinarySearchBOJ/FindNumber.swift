//
//  FindNumber.swift
//  BinarySearchBOJ
//
//  Created by 진혜림 on 2022/04/12.
//

import Foundation

class FindNumber {
  static func solution() {
    let count = Int(readLine()!)!
    let numbers = readLine()!
      .split(separator: " ")
      .map { Int(String($0))! }
      .sorted()
    let _ = Int(readLine()!)!
    let targetNumbers = readLine()!
      .split(separator: " ")
      .map { Int(String($0))! }

    targetNumbers.forEach {
      print(binarySearch(numbers, $0, 0, count - 1))
    }
  }
  
  private static func binarySearch(_ array: [Int], _ target: Int, _ start: Int, _ end: Int) -> Int {
    guard start <= end else {
      return 0
    }
    
    let mid = (start + end) / 2
    if array[mid] > target {
      return binarySearch(array, target, start, mid - 1)
    } else if array[mid] < target {
      return binarySearch(array, target, mid + 1, end)
    } else {
      return 1
    }
  }
}
