// 광고 삽입

// [입출력 예]
// play_time    adv_time    logs    result
// "02:03:55"    "00:14:15"    ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]    "01:30:59"
// "99:59:59"    "25:00:00"    ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]    "01:00:00"
// "50:00:00"    "50:00:00"    ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]    "00:00:00"

// 풀이
// 각 재생시간의 시작시간, 끝 시간을 for문으로 돌면서
// 해당 시간에 광고를 할 때 포함되는 숫자가 제일 높은 구간과 그 때 시청한 사람들의 수를 저장
// 시청할 수 있는 사람들의 수가 같을 땐 더 빠른 시작시간으로 업데이트

import Foundation

func solution(_ play_time:String, _ adv_time:String, _ logs:[String]) -> String {
    // 영상 시간과 광고 시간이 같은 경우 예외처리
    guard play_time != adv_time else {
        return "00:00:00"
    }
    
    let adTimeSec = formattedStrToSec(adv_time)
    // 시청시간 목록과 광고를 넣을 수 있는 시간대 구하기
    var viewerTimes: [ClosedRange<Int>] = []
    var startTimes: [Int] = []
    logs.forEach { log in
        let times = log
            .split(separator: "-")
            .map { formattedStrToSec(String($0)) }
        viewerTimes.append(times[0] ... times[1])
        startTimes.append(times[0])
    }
    
    var bestStartTime: Int = Int.max    // 광고를 넣을 제일 빠른 시간 (초단위)
    var maxViewersNum: Int = 0          // 광고를 볼 수 있는 최대 사람 수
    startTimes.forEach { startTime in
        let adRange = startTime ... startTime + adTimeSec
        let count = viewerTimes
            .filter{ range in
                // 시작 시간에 재생중인 인원 수 || 광고 재생 도중 재생 시작하는 인원 수
                return range.contains(startTime) || adRange.contains(range.first!)
            }
            .count
        
        if maxViewersNum < count {
            maxViewersNum = count
            bestStartTime = startTime
        }
        else if maxViewersNum == count {
            guard bestStartTime > startTime else { return }
            
            bestStartTime = startTime
        }
    }
    
    return secToForamttedStr(bestStartTime)
}

func formattedStrToSec(_ str: String) -> Int {
    let timeStrs = str.split(separator: ":")
    return (Int(timeStrs[0])! * 60 * 60) + (Int(timeStrs[1])! * 60) + Int(timeStrs[2])!
}

func secToForamttedStr(_ sec: Int) -> String {
    var tmpSec = sec
    let hour = Int(tmpSec / (60 * 60))
    tmpSec -= hour * 60 * 60
    let min = Int(tmpSec / 60)
    tmpSec -= min * 60
    return [hour, min, tmpSec]
        .map { String(format: "%02d", $0) }
        .joined(separator: ":")
}

solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"])

