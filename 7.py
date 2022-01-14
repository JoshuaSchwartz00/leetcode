class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if(x < 0):
            neg = True
        x = abs(x)
        reversex = 0
        i = 10**(len(str(x))-1)
        while(x > 0):
            reversex += x % 10 * i
            print(reversex)
            x = x // 10
            i /= 10
        reversex = int(reversex)
        if(neg):
            reversex *= -1
        if(reversex < (-2)**31 or reversex > 2**31-1):
            return 0
        return reversex