# leetcode-solutions
# 📝 LeetCode Solutions

[![刷题进度](https://img.shields.io/badge/题目总数-1/200-4CAF50?style=flat-square)](#)
![Progress](https://progress-bar.dev/1/?scale=200&title=完成题数&width=500&color=4CAF50)
[![最近更新](https://img.shields.io/badge/最近更新-2025--08--13-blue?style=flat-square)](#)
[![语言](https://img.shields.io/badge/语言-Python%20%7C%20JavaScript-orange?style=flat-square)](#)
[![License](https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square)](#)

记录我的 LeetCode 刷题过程（Python）

---

## 📊 刷题进度
- **题目总数**：0 / 200  
- **最近更新**：2025-08-12  
- **语言**：Python

---

## 📂 题目分类
| 分类 | 已完成 | 链接 |
|------|--------|------|
| 数组 (Array) | 0 | [数组题解](./array) |
| 字符串 (String) | 0 | [字符串题解](./string) |
| 动态规划 (DP) | 0 | [动态规划题解](./dp) |

---

## 🏆 示例题解
以 [LeetCode 1. Two Sum](https://leetcode.com/problems/two-sum/) 为例：

```python
# 题目: Two Sum
# 链接: https://leetcode.com/problems/two-sum/
# 思路: 使用哈希表存储已访问的数字，O(n) 时间复杂度
class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for i, num in enumerate(nums):
            if target - num in hashmap:
                return [hashmap[target - num], i]
            hashmap[num] = i
