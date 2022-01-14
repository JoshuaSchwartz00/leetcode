class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        ans_dict = {}
        ans = []
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in ans_dict.keys():
                ans = [ans_dict[diff], i]
            else:
                ans_dict[nums[i]] = i
        
        return ans