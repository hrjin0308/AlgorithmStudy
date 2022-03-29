import Foundation

public class JoyStick {
  public static func solution(_ name:String) -> Int {
    // 상/하 키로 각 알파벳을 얻을 수 있는 수 얻기
    let udCount = name
      .utf16
      .map { min(($0 - "A".utf16.first!), ("Z".utf16.first! - $0) + 1) }
      .reduce(0, +)
    // 좌/우 키로 이동한 수 얻기
    // 1. 한 방향으로만 쭉 갔을 경우
    var lrCount = name.count - 1
    // 2. 중간에 A가 중첩되어 왔다가 돌아가는 게 더 빠른 경우 체크
    var index = 0
    while index < name.count {
      var nextIndex = index + 1
      while nextIndex < name.count && name[name.index(name.startIndex, offsetBy: nextIndex)] == "A" {
        nextIndex += 1
      }
      lrCount = min(
        (index * 2) + (name.count - nextIndex),
        index + ((name.count - nextIndex) * 2),
        lrCount
      )
      index = nextIndex
    }
    
    return Int(udCount) + lrCount
  }
}
