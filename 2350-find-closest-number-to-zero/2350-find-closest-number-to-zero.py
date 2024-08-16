class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        d = []
        c_no = []
        
        for i in range(len(nums)):
            d.append(abs(nums[i]))
        
        for i in range(len(d)):
            if d[i] == min(d):
                c_no.append(nums[i])

        return max(c_no)


        