// 괄호 변환
import Foundation

func solution(_ p:String) -> String {
//    print("p: \(p)")
    // 빈 문자열 예외처리
    guard !p.isEmpty else {
        return p
    }
    
    // u 찾기
    var u = ""
    for char in p {
        u += String(char)
        if u.filter({ $0 == "(" }).count == u.filter({ $0 == ")" }).count {
            break
        }
    }
    
    // v 초기화
    let v = String(p.suffix(p.count - u.count))
//    print("u: \(u)", "v: \(v)")
    
    // 올바른 괄호 문자열 확인
    var tmpU = u
    while tmpU.contains("()") {
        tmpU = tmpU.replacingOccurrences(of: "()", with: "")
    }
    
    if tmpU.count == 0 {
        // 올바른 괄호 문자열
        return u + solution(v)
    }
    else {
        let newU = u.count <= 2 ? "" : u[u.index(u.startIndex, offsetBy: 1) ... u.index(u.endIndex, offsetBy: -2)]
            .replacingOccurrences(of: "(", with: "|")
            .replacingOccurrences(of: ")", with: "(")
            .replacingOccurrences(of: "|", with: ")")
//        print("newU: \(newU)")
        return "(\(solution(v)))\(newU)"
    }
}

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
