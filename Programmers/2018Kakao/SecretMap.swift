// 비밀지도
// 시작시간 21.08.28 17:20
// 제출시간 21.08.28 18.14

// 와 이걸 한줄로 짠사람이있네
//import Foundation
//
//func solution(_ n:Int, _ arr1:[Int], _ arr2:[Int]) -> [String] {
//    func binStr(with decNum: Int) -> String {
//        var bin = String(decNum, radix: 2)
//        while bin.count < n {
//            bin.insert("0", at: bin.startIndex)
//        }
//        return bin
//    }
//
//    let binStrArray1 = arr1.map { binStr(with: $0) }
//    let binStrArray2 = arr2.map { binStr(with: $0) }
//
//    var result: [String] = []
//    for i in 0 ..< n {
//        var mapRow: String = ""
//        let str1 = binStrArray1[i]
//        let str2 = binStrArray2[i]
//        for j in 0 ..< n {
//            let char1 = str1[str1.index(str1.startIndex, offsetBy: j)]
//            let char2 = str2[str2.index(str2.startIndex, offsetBy: j)]
//            if char1 == "1" || char2 == "1" {
//                mapRow += "#"
//            }
//            else {
//                mapRow += " "
//            }
//        }
//        result.append(mapRow)
//    }
//
//    return result
//}

func solution(_ n:Int, _ arr1:[Int], _ arr2:[Int]) -> [String] {
    return (0 ..< n)
        .map {
            let bin = String((arr1[$0] | arr2[$0]), radix: 2)
            return (String(repeating: "0", count: n - bin.count) + bin)
                .reduce("") { $0 + ($1 == "1" ? "#" : " ") }
        }
}

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))
