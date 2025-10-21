class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = set() # Initialzie the set to iterate
        left = 0  # move pointer to the right
        max_len = 0 # initalize max len(last elt)

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_len = max(max_len, right - left+1)

        return  max_len