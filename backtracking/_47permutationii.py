from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # Sort nums
        # Use an extra array to keep track of usage
        res = []
        if not nums:
            return res

        nums.sort()
        used = [False for i in range(len(nums))]

        self.bt(nums, res, used, [])
        return res

    def bt(self, nums, res, used, li):
        if len(li) == len(nums):
            res.append(li.copy())
            return

        for i in range(len(nums)):
            if used[i]: continue
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]: continue

            li.append(nums[i])
            used[i] = True
            self.bt(nums, res, used, li)
            li.pop()
            used[i] = False


sol = Solution()
res = sol.permuteUnique([1,1,2])
print(res)
