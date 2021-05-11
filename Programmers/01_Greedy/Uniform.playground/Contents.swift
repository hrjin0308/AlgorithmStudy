/*
 체육복
 greedy
 */

import Foundation

func solution(_ n:Int, _ lost:[Int], _ reserve:[Int]) -> Int {
    var changedLost = lost.filter({ !reserve.contains($0) })
    var changedReserve = reserve.filter({ !lost.contains($0) })
    
    changedLost.forEach { (student) in
        let lostStudentIndex = changedLost.firstIndex(of: student)!
        var reserveStudentIndex: Int?
        
        if changedReserve.contains(student) {
            reserveStudentIndex = changedReserve.firstIndex(of: student)!
        }
        else if changedReserve.contains(student - 1) {
            reserveStudentIndex = changedReserve.firstIndex(of: student - 1)!
        }
        else if changedReserve.contains(student + 1) {
            reserveStudentIndex = changedReserve.firstIndex(of: student + 1)!
        }
        
        if let theIndex = reserveStudentIndex {
            changedLost.remove(at: lostStudentIndex)
            changedReserve.remove(at: theIndex)
        }
    }
    
    return (n - changedLost.count)
}

solution(5, [2, 4], [1, 3, 5])
solution(5, [2, 4], [3])
solution(3, [3], [1])
