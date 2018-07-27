class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle is None or needle is None:
            return -1
        len_h = len(haystack)
        len_n = len(needle)
        i = 0
        for i in range(len_h-len_n+1):
            j = 0
            while(j < len_n):
                if(haystack[i+j] != needle[j]):
                    break
                    return -1
                j += 1
            if(j == len_n):
                return i
        return -1       