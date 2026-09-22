class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:

        left = 0
        window_sum = 0
        length = float("inf")

        for right in range(len(nums)):
            # Move right
            window_sum += nums[right]
            
            # Check the  window_sum >= target
            while window_sum >= target:
                # Record a length
                length = min(length, right - left + 1)

                # Remove the left element
                window_sum -= nums[left]

                # Increase one left
                left += 1

        if length == float("inf"):
            return 0

        return length

solution = Solution()
print(solution.minSubArrayLen(15, [5,1,3,5,10,7,4,9,2,8]))
