# Morgan Hale, mah7ks

class Solution(object):

    def twoSum(self, nums, target):
        solution = []
        for i in nums:
            for j in nums:
                if (i + j == target) and (i != j):
                    solution.append(nums.index(i))
                    break;
        return solution;

    



        