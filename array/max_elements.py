class Solution:
    def findMax(self, nums):
        max_num = nums[0]

        for num in nums:
            if num > max_num:
                max_num = num

        return max_num


# Example usage
nums = [12, 45, 7, 89, 23, 56]

solution = Solution()
print("Maximum element:", solution.findMax(nums))