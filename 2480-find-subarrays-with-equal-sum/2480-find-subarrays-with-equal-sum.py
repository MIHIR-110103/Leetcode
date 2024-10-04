class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        arr = []

        for i in range(len(nums)-1):
            x = sum(nums[i : i+2] )
            print(x)
            arr.append(x)
            print(arr)
        
        return sorted(set(arr)) != sorted(arr)
        