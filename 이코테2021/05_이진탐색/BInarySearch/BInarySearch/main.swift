//
//  main.swift
//  BInarySearch
//
//  Created by 진혜림 on 2022/04/12.
//

import Foundation

// recursive

func binarySearchRecrsive(array: [Int], target: Int, start: Int, end: Int) -> Int {
  guard start <= end else {
    return -1
  }
  
  let mid = (start + end) / 2
  if array[mid] > target {
    return binarySearchRecrsive(
      array: array,
      target: target,
      start: start,
      end: mid - 1
    )
  } else if array[mid] < target {
    return binarySearchRecrsive(
      array: array,
      target: target,
      start: mid + 1,
      end: end
    )
  } else {
    return mid
  }
}

// while
func binarySearchWhile(array: [Int], target: Int) -> Int {
  var start = 0
  var end = array.count - 1
  
  repeat {
    let mid = (start + end) / 2
    if array[mid] > target {
      end = mid - 1
    } else if array[mid] < target {
      start = mid + 1
    } else {
      return mid
    }
  } while start <= end
  
  return -1
}

let array = [1, 3, 5, 7, 7, 9, 11, 13, 15, 17, 19]
//binarySearchRecrsive(array: array, target: 7, start: 0, end: array.count - 1)
//binarySearchWhile(array: array, target: 7)

Tteokbokki.solution()
