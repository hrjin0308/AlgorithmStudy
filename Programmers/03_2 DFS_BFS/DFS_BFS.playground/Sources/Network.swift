import Foundation

func solution(_ n:Int, _ computers:[[Int]]) -> Int {
  var count = 0
  var tmpComputers = computers
  for i in 0 ..< n {
    for j in 0 ..< n {
      if tmpComputers[i][j] == 1 {
        count += 1
        dfs(j, &tmpComputers)
      }
    }
  }
  return count
}

func dfs(_ index: Int, _ computers: inout [[Int]]) {
  computers[index][index] = 0
  for (i, value) in computers[index].enumerated() {
    if value == 1 {
      computers[i][index] = 0
      computers[index][i] = 0
      dfs(i, &computers)
    }
  }
}
