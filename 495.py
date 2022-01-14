class Solution:
    def findPoisonedDuration(self, timeSeries: list, duration: int) -> int:
        if(len(timeSeries) == 0 or duration == 0):
            return 0
        total = 0
        
        for i in range(len(timeSeries)-1):
            total += min(timeSeries[i+1] - timeSeries[i], duration)
        total += duration
                
        return total