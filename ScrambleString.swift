class Solution {
    var memo = [String: Bool]()
    
    func isScramble(_ s1: String, _ s2: String) -> Bool {
        if s1 == s2 { return true }
        if s1.count != s2.count { return false }
        
        let key = "\(s1)-\(s2)"
        if let cached = memo[key] {
            return cached
        }
        
        if Array(s1).sorted() != Array(s2).sorted() {
            memo[key] = false
            return false
        }
        
        let n = s1.count
        let s1Array = Array(s1)
        let s2Array = Array(s2)
        
        for i in 1..<n {
            let left1 = String(s1Array[0..<i])
            let right1 = String(s1Array[i..<n])
            
            let left2a = String(s2Array[0..<i])
            let right2a = String(s2Array[i..<n])
            
            let left2b = String(s2Array[0..<(n - i)])
            let right2b = String(s2Array[(n - i)..<n])
            
            if (isScramble(left1, left2a) && isScramble(right1, right2a)) ||
               (isScramble(left1, right2b) && isScramble(right1, left2b)) {
                memo[key] = true
                return true
            }
        }
        
        memo[key] = false
        return false
    }
}
