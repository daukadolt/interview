class Solution:
    def firstUniqChar(self, s):
        """
        :type s: s
        :rtype: int
        """
        _dict = {}
        for i in range(len(s)):
            if _dict.get(s[i]) == None:
                _dict[s[i]] = [i]
            else:
                _dict[s[i]].append(i)
        returnVal = None
        for i in _dict:
            if len(_dict[i]) == 1:
                if returnVal == None:
                    returnVal = _dict[i][0]
                elif _dict[i][0]<returnVal:
                    returnVal = _dict[i][0]
        return returnVal

if __name__ == "__main__":
    testcases = ["leetcode", "loveleetcode"]
    a = Solution()
    print(a.firstUniqChar(testcases[0]))
    # for i in testcases:
    #     print(Solution(s=i))