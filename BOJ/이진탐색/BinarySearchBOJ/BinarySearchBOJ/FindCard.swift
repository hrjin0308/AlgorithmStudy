//
//  FindCard.swift
//  BinarySearchBOJ
//
//  Created by 진혜림 on 2022/04/13.
//

import Foundation

class FindCard {
  func solution() {
    let count = Int(readLine()!)!
    let myCards = readLine()!.split(separator: " ").map { Int(String($0))! }
    let targetCount = Int(readLine()!)!
    let targetCards = readLine()!.split(separator: " ").map { Int(String($0))! }

    var dict: [Int: Int] = [:]

    myCards.forEach {
      if let count = dict[$0] {
        dict[$0] = count + 1
      } else {
        dict[$0] = 1
      }
    }

    let result = targetCards
      .map { card -> String in
        if let count = dict[card] {
          return String(count)
        } else {
          return "0"
        }
      }
      .joined(separator: " ")

    print(result)
  }
}
