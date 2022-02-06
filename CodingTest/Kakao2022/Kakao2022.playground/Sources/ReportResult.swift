import Foundation

public class ReportResult {
  public static func solution(_ id_list:[String], _ report:[String], _ k:Int) -> [Int] {
    var reportDict: [String: Set<String>] = [:]
    report.forEach {
      let array = $0.components(separatedBy: " ")
      if let _ = reportDict[array[1]] {
        reportDict[array[1]]!.insert(array[0])
      }
      else {
        reportDict[array[1]] = Set([array[0]])
      }
    }
    return id_list.map({ id in
      reportDict
        .filter { $0.value.count >= 2 }
        .filter { $0.value.contains(id) }
        .count
    })
  }
}
