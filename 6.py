class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        partitions = [""] * numRows
        idx = 0
        forward = True
        
        for i in range(len(s)):
            partitions[idx] += s[i]
            
            if forward:
                idx += 1
                if idx == len(partitions)-1:
                    forward = False
            elif not forward:
                idx -= 1
                if idx == 0:
                    forward = True
                
        final_string = ""
        
        for p in partitions:
            final_string += p
            
        return final_string