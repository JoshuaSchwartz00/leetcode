class Solution:   
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        rev = s[::-1]
        s_new = s + "#" + rev
        n_new = len(s_new)
        f = [0] * n_new
        for i in range(1, n_new):
            t = f[i-1]
            while(t > 0 and s_new[i] != s_new[t]):
                t = f[t-1]
            if s_new[i] == s_new[t]:
                t += 1
            f[i] = t
            
        return rev[0:n-f[n_new-1]] + s