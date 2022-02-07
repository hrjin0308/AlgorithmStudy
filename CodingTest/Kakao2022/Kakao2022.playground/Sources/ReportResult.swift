import Foundation

public class ReportResult {
  public static func solution(_ id_list:[String], _ report:[String], _ k:Int) -> [Int] {
    var reportDict: [String: Set<String>] = [:]
    for reportContent in report {
      let array = reportContent.components(separatedBy: " ")
      if let _ = reportDict[array[1]] {
        reportDict[array[1]]!.insert(array[0])
      }
      else {
        reportDict[array[1]] = [array[0]]
      }
    }
    return id_list.map({ id in
      reportDict
        .filter { $0.value.count >= k }
        .filter { $0.value.contains(id) }
        .count
    })
  }
}
