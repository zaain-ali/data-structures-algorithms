class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for index, num in enumerate(nums):
            needed = target - num

            if num in seen:
                return [seen[num], index]
            
            seen[needed] = index

solution = Solution()
print(solution.twoSum([2,7,11,15], 9))
