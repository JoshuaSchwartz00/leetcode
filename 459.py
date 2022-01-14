class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        sub = ""
        works = False
        for i in range(1, len(s)):
            temp = s
            sub = s[0:i]
            while len(temp) != 0:
                if sub == temp[0:len(sub)]:
                    temp = temp[len(sub):len(temp)]
                else:
                    break
            
            if len(temp) == 0:
                works = True
        
        return works