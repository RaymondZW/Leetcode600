from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #

        # Find strictly decreasing head
        if not nums: return None
        n = len(nums)
        if n == 1: return nums

        head = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                head = i

        # if already largest possible, return early
        if head == -1:
            return sorted(nums)

        # Find strictly greater num after head
        for i in range(n - 1, head, -1):
            if nums[i] > nums[head]:
                nums[i], nums[head] = nums[head], nums[i]
                break

        # reverse every num after head
        nums[head + 1:] = nums[head + 1:][::-1]
        return


sol = Solution()
nums = [1,2,3]
sol.nextPermutation(nums)
print(nums)

