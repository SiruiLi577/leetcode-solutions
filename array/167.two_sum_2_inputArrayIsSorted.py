"""
题目: Two Sum 2 input array is sorted
链接: https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/
难度: Medium
标签: array
"""

# 思路:
# 双指针，利用题目已经对数组排序并且有唯一解

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        while True: #sorted/exactly one solu
            s = numbers[left] + numbers[right]
            if s == target:
                return [left + 1, right + 1]
            if s < target:
                left += 1
            else:
                right -= 1
            
        
