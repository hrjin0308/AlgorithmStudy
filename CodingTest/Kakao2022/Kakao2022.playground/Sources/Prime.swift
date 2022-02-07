import Foundation

public class Prime {
  public static func solution(_ n:Int, _ k:Int) -> Int {
    return String(n, radix: k)
      .components(separatedBy: "0")
      .filter {
        guard let decimal = Int($0, radix: 10) else { return false }
        return isPrime(decimal)
      }
      .count
  }
  
  private static func isPrime(_ number: Int) -> Bool {
    if number == 1 {
      return false
    }
    else if number < 4 {
      return true
    }
    else {
      for i in 2 ... Int(sqrt(Double(number))) {
        if number % i == 0 {
          return false
        }
      }
    }
    return true
  }
}
