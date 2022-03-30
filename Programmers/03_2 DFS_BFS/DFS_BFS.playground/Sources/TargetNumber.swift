import Foundation

//[1, 1, 1, 1, 1]  3  5
//[4, 1, 2, 1]  4  2

class TargetNumber {
  func solution(_ numbers:[Int], _ target:Int) -> Int {
    var count = 0
    
    func dfs(_ numbers:[Int], _ result: Int) {
      print(numbers, result)
      guard numbers.count > 0 else {
        if result == target {
          count += 1
        }
        return
      }
      
      var tmpNumbers = numbers
      let first = tmpNumbers.removeFirst()
      dfs(tmpNumbers, result + first)
      dfs(tmpNumbers, result - first)
    }
    
    dfs(numbers, 0)
    
    return count
  }
}
