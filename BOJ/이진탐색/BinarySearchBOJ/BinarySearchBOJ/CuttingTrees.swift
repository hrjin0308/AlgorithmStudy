//
//  CuttingTrees.swift
//  BinarySearchBOJ
//
//  Created by 진혜림 on 2022/04/13.
//

import Foundation

func CuttingTrees {
  func solution() {
    let input = readLine()!.split(separator: " ").map { Int(String($0))! }
    let trees = readLine()!.split(separator: " ").map { Int(String($0))! }
    var maxHeight = 0
    let end = trees.sorted().last!

    binarySearch(trees, input[1], &maxHeight, 0, end)
    print(maxHeight)
  }
  
  func binarySearch(_ array: [Int], _ target: Int, _ maxHeight: inout Int, _ start: Int, _ end: Int) {
    guard start <= end else {
      return
    }
    let mid = (start + end) / 2
    let sum = array
      .map { $0 <= mid ? 0 : $0 - mid }
      .reduce(0, +)
    if sum >= target {
      if mid > maxHeight {
        maxHeight = mid
      }
      binarySearch(array, target, &maxHeight, mid + 1, end)
    } else {
      binarySearch(array, target, &maxHeight, start, mid - 1)
    }
  }
}
