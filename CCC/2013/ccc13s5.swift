import Foundation

let N = Int(readLine()!)!
var cost = 0
var n = N
while n > 1 {
    let r = Int(sqrt(Double(n))) + 1
    var f = 2
    while f <= r && n % f != 0 {
        f += 1
    }
    if f < n && n % f == 0 {
        let x = n / f
        n -= x
        cost += n / x
    } else {
        n -= 1
        cost += n
    }
}
print(cost)