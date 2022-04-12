//
//  Tteokbokki.swift
//  BInarySearch
//
//  Created by 진혜림 on 2022/04/12.
//

import Foundation

class Tteokbokki {
  static func solution() {
    // 떡의 갯수와 원하는 길이 얻기
    let info = readLine()!.components(separatedBy: " ").map({ Int($0)! })
    let lengths = readLine()!.components(separatedBy: " ").map({ Int($0)! })
    var result = 0
    
    // 절단기 높이 배열
    let maxLength = lengths.sorted(by: >).first!
    binarySearch(array: lengths, target: info[1], result: &result, start: 0, end: maxLength)
    
    print(result)
  }
  
  private static func binarySearch(array: [Int], target: Int, result: inout Int, start: Int, end: Int) {
    guard start <= end else {
      return
    }
    let mid = (start + end) / 2
    let sliced = array
      .map {
        $0 <= mid ? 0 : $0 - mid
      }
    if sliced.reduce(0, +) >= target {
      if mid > result {
        result = mid
      }
      binarySearch(array: array, target: target, result: &result, start: mid + 1, end: end)
    } else {
      binarySearch(array: array, target: target, result: &result, start: start, end: mid - 1)
    }
  }
}
