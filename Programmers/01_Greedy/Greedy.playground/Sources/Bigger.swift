import Foundation

/*
 테스트 1 〉  통과 (0.13ms, 16.4MB)
 테스트 2 〉  통과 (0.14ms, 16.5MB)
 테스트 3 〉  통과 (0.16ms, 16.7MB)
 테스트 4 〉  통과 (0.41ms, 16.5MB)
 테스트 5 〉  통과 (0.92ms, 16.7MB)
 테스트 6 〉  통과 (167.34ms, 16.4MB)
 테스트 7 〉  통과 (871.41ms, 16.7MB)
 테스트 8 〉  통과 (5617.14ms, 18MB)
 테스트 9 〉  통과 (241.82ms, 25.1MB)
 테스트 10 〉  실패 (시간 초과)
 테스트 11 〉  통과 (0.08ms, 16.4MB)
 테스트 12 〉  통과 (0.05ms, 16.3MB)
 
 하단에 참고용 답 코드 추가..
 */

public class Bigger {
  public static func solution(_ number:String, _ k:Int) -> String {
    guard number.count > k else {
      return number
    }
    
    let chars = number.map { $0 }
    var tmpK = k
    var answers: [Character] = []
    var cursor = 0
    
    while tmpK > 0 {
      var maxNum = -1
      var maxCursor = 0
      for i in cursor ..< cursor + tmpK + 1 {
        let num = Int(String(chars[i]))!
        guard num != 9 else {
          maxNum = 9
          maxCursor = i
          break
        }
        if num > maxNum {
          maxNum = num
          maxCursor = i
        }
      }
      answers.append(String(maxNum).first!)
      tmpK -= maxCursor - cursor
      if answers.count == number.count - k {
        break
      }
      
      cursor = maxCursor + 1
    }
    
    if answers.count + k < number.count {
      answers.append(contentsOf: chars[cursor...])
    }
    return String(answers)
  }
}


/*
 import Foundation

 func solution(_ number:String, _ k:Int) -> String {
     let numbers = number.compactMap{ Int(String($0))}

     var sub: [Int] = []

     var k = k

     for (i,e) in numbers.enumerated() {
         while k>0, sub.isEmpty == false, sub.last! < e {
             k-=1
             sub.removeLast()
         }

         if k == 0 {
             sub.append(contentsOf: numbers[i...])
             break
         } else {
             sub.append(e)
         }
     }

     return sub[..<(sub.count-k)].map {String($0)}.joined()
 }
 */
