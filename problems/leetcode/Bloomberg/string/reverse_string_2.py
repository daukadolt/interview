class Solution:
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        counter = len(str)
        index = len(str)-1
        length = len(str)
        while(counter != 0):
            if str[index] == " ":
                # print(str[-(length - index)+1:])
                str = str[:index] + [" "] + str[-(length - index)+1:]
            index -= 1
            counter -= 1

if __name__ == "__main__":
    sol = Solution()
    inp = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
    sol.reverseWords(inp)
    print(inp)