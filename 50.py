class Solution:
    def pow_log(self, x: float, n: int):
        store = 1
        
        while(n > 1):
            if n % 2 == 0:
                x *= x
                n //= 2
            elif n % 2 == 1:
                store *= x
                n -= 1
                x *= x
                n //= 2
            print(x, n)

        x *= store
            
        return x
    
    def myPow(self, x: float, n: int) -> float:
        # x**n = (x**2)^(n/2)
        if n > 0:
            x = self.pow_log(x, n)
        elif n < 0:
            x = self.pow_log(1/x, -n)
        elif n == 0:
            x = 1.

        return x