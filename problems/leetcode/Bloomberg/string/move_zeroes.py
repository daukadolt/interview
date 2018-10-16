class Solution:
    def swap(self, array, indexA, indexB):
        temp = array[indexA]
        array[indexA] = array[indexB]
        array[indexB] = temp

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        numOfZeroes = 0
        index = 0
        while(index != len(nums)):
            if nums[index] == 0:
                numOfZeroes += 1
                nums.pop(index)
            else:
                index += 1
        for _ in range(numOfZeroes):
            nums.append(0)
                
if __name__ == "__main__":
    solution = Solution()
    array = [0,1,0,3,12]
    solution.moveZeroes(array)
    print(array)