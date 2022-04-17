//
//  N.swift
//  DynamicProgramming
//
//  Created by 진혜림 on 2022/04/17.
//

import Foundation

// TODO: dfs로 풀어보기
class N {
  func solution(_ N:Int, _ number:Int) -> Int {
    guard N != number else {
      return 1
    }
    
    var array: [Set<Int>] = [[N]]
    
    while true {
      let count = array.count
      var results = Set<Int>()
      if count < 2 {
        results = [N + N, N - N, N / N, N * N]
      } else {
        for i in 0 ..< count / 2 {
          array[i].forEach { num1 in
            array[count - 1 - i].forEach { num2 in
              results.insert(num1 + num2)
              results.insert(num1 - num2)
              results.insert(num2 - num1)
              results.insert(num1 * num2)
              if num1 != 0 {
                results.insert(num2 / num1)
              }
              if num2 != 0 {
                results.insert(num1 / num2)
              }
            }
          }
        }
      }
      
      let decimalPow = Array(repeating: String(N), count: count + 1)
        .joined(separator: "")
      results.insert(Int(decimalPow)!)
      
      if results.contains(number) {
        return array.count + 1
      } else {
        array.append(results)
        
        guard array.count < 8 else {
          return -1
        }
      }
    }
  }
}
