from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_index = 0
        right_index = len(nums) - 1
        while left_index <= right_index:
            mid_index = (left_index + right_index) // 2
            mid_number = nums[mid_index]
            if target == mid_number:
                return mid_index
            elif target < mid_number:
                right_index = mid_index - 1
            else:
                left_index = mid_index + 1
        return -1
