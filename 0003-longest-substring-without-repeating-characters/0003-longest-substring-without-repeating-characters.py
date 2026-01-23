class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        lastSeen = [-1]* 256
        start,maxLen,next = 0,0,0
        while next < n:
            nextChar = ord(s[next])
            if lastSeen[nextChar] >= start:
                maxLen = max(maxLen,next-start)
                start = lastSeen[nextChar]+1
            
            lastSeen[nextChar] = next
            next += 1
        
        maxLen = max(maxLen,next-start)
        return maxLen