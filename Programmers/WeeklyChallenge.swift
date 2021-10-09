// 직업군 추천하기

import Foundation

func solution(_ table:[String], _ languages:[String], _ preference:[Int]) -> String {
    struct Work {
        let name: String!
        let langArray: [String]!
        
        func score(_ language: String) -> Int {
            guard
                let langArray = langArray,
                let index = langArray.firstIndex(of: language)
            else {
                return 0
            }
            
            return langArray.count - index
        }
    }
    
    // Work 만들기
    var works = table
        .map { str -> Work in
            var array = str.components(separatedBy: " ")
            return Work(name: array[0], langArray: Array(array[1 ... (array.count - 1)]))
        }
    
    var maxScore = 0
    var maxScoreName = ""
    works.forEach { work in
        var total = 0
        for (i, lang) in languages.enumerated() {
            total += preference[i] * work.score(lang)
        }
        
        print("")
        print("work name: \(work.name)")
        print("work score: \(total)")
        print("")
        
        if total > maxScore {
            maxScore = total
            maxScoreName = work.name
        }
        else if total == maxScore {
            maxScoreName = min(maxScoreName, work.name)
        }
    }
    
    return maxScoreName
}