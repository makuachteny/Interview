from collections import deque

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        wordset = set(wordDict)
        queue = deque([0])
        visited = set()

        while queue:
            start = queue.popleft()
            if start == n:
                return True
            if start in visited:
                continue
            visited.add(start)
            for end in range(start + 1, n + 1):
                if s[start:end] in wordset:
                    queue.append(end)
        return False
