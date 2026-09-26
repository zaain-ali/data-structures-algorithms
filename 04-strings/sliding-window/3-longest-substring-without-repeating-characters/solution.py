class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        maximum = 0
        window = set()

        for ind, char in enumerate(s):

            while char in window:
                window.remove(s[left])

                left += 1
            
            window.add(s[ind])
            length = ind - left + 1
            maximum = max(maximum, length)
        return maximum
        
sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))