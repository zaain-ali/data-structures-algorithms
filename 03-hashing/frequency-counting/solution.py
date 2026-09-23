class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        frequency = {}
        threshold = len(nums) // 2

        for num in nums:

            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
            
            if frequency[num] > threshold:
                return num

solution = Solution()
print(solution.majorityElement([3,2,3]))