//기능개발

import Foundation

public class Progress {
    public static func solution(_ progresses:[Int], _ speeds:[Int]) -> [Int] {
        var result = [Int]()
        var qProgress = progresses
        var qSpeeds = speeds
        var days: Double = 0.0
        var count = 0
        
        repeat {
            guard
                let p = qProgress.first,
                let s = qSpeeds.first
            else {
                break
            }
            
            let dP = Double(p)
            let dS = Double(s)
            if dP + (dS * days) < 100.0 {
                if count > 0 {
                    result.append(count)
                }
                
                days = ceil((100.0 - dP) / dS)
                count = 1
            }
            else {
                count += 1
            }
            
            qProgress.removeFirst()
            qSpeeds.removeFirst()
        } while qProgress.count > 0
        
        if count > 0 {
            result.append(count)
        }
        
        return result
    }
}
