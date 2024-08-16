class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ans = False
        i = 0
        if len(s) == 0:
            return True
        while i <= (len(s)-1):
            for j in range(len(t)):
                if s[i] == t[j]:
                    i += 1
                    if i == len(s):
                        ans = True
                        return ans
            break
        return ans
        

        