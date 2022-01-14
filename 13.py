class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        total = 0
        if len(s) == 0:
            return total
        
        for i in range(0, len(s)-1):
            if(dic[s[i]] < dic[s[i+1]]):
                total -= dic[s[i]]
            else:
                total += dic[s[i]]
        total += dic[s[len(s)-1]]
        return total