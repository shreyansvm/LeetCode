# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        final_nums = []
        solution_found = 0
        i = 0
        for num in nums:
            num_1_index = i
            i += 1
            for next_num in range(i, len(nums)):
                num_2_index = next_num
                local_target = num + nums[next_num]
                if local_target == target:
                    final_nums.append(num_1_index)
                    final_nums.append(num_2_index)
                    solution_found = 1
                    break
            if solution_found:
                break
        return final_nums

        # --- OR --- method 2 :
        # for num in nums:
        #     num_1_index = i
        #     i += 1
        #     for next_num in range(i, len(nums)):
        #         num_2_index = next_num
        #         local_target = num + nums[next_num]
        #         if local_target == target:
        #             return [num_1_index, num_2_index]


a = Solution()
nums = [2, 7, 11, 15]
target = 9
print(a.twoSum(nums, target))