class Solution:
    def establishMaximums(self, maximums, nums):
        while(len(nums) != 0 or len(maximums) < 3):
            maximums.append(nums.pop(0))
    
    def swap(self, array, indexA, indexB):
        temp = array[indexA]
        array[indexA] = array[indexB]
        array[indexB] = temp

    def pushToMaxs(self, number, maximums):
        maximums[0] = number
        for i in range(1, len(maximums)):
            if maximums[i]<maximums[i-1]:
                self.swap(maximums, i, i-1)
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximums = []
        self.establishMaximums(maximums, nums)
        print(maximums)
        for index in range(0, len(nums)):
            print(maximums)
            if nums[index] > maximums[0]:
                self.pushToMaxs(nums[index], maximums)
        return maximums
                
if __name__ == "__main__":
    array = [2, 2, 3, 1]
    solution = Solution()
    print(solution.thirdMax(array))