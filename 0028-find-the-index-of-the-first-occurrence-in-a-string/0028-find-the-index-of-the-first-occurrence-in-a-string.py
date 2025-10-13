class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle =="":
           return 0
        m,n = len(haystack),len(needle)
        for i in range(m-n+1):
          if haystack[i:i+n] == needle:
              return i
        return -1
        