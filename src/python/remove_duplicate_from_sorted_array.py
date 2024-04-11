class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        length = len(nums) -1
        while length >= index:
            if nums[index-1] == nums[index]:
                nums.remove(nums[index-1])
            else:
                index += 1
            length = len(nums)-1
        return len(nums)