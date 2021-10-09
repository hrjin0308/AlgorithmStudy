// 다트 게임
// 시작시간 21.08.28 22:17
// 제출시간 21.08.28 23:36
import Foundation

func solution(_ dartResult:String) -> Int {
    enum Bonus: String {
        case single = "S"
        case double = "D"
        case triple = "T"
        
        var multiple: Int {
            switch self {
            case .single:   return 1
            case .double:   return 2
            case .triple:   return 3
            }
        }
    }
    
    enum Option: String {
        case star = "*"
        case minus = "#"
    }
    
    var scores: [Int] = []
    var tmpResults = dartResult
    
    while tmpResults.count > 0 {
        let str = String(tmpResults.removeFirst())
        
        if let score = Int(str) {
            // 10점 예외처리
            if score == 1,
               tmpResults.hasPrefix("0") {
                tmpResults.removeFirst()
                scores.append(10)
            }
            else {
                scores.append(score)
            }
            continue
        }
        
        let index = scores.endIndex - 1
        if let bonus = Bonus(rawValue: str) {
            scores[index] = Int(pow(Double(scores[index]), Double(bonus.multiple)))
            continue
        }
        
        if let option = Option(rawValue: str) {
            if option == .star {
                if scores.count > 1 {
                    scores[index] *= 2
                    scores[index - 1] *= 2
                }
                else {
                    scores[index] *= 2
                }
            }
            else {      // .minus
                scores[index] *= -1
            }
        }
    }
    
    return scores.reduce(0, +)
}

solution("1S2D*3T")
