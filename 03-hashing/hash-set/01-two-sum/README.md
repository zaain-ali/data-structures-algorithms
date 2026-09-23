# 1. Two Sum

## Difficulty

Easy

## Topics

- Array
- Hash Table

## Problem

Given an integer array `nums` and an integer `target`, return the indexes of two numbers whose sum equals `target`.

You may assume:

- Every input has exactly one valid answer.
- The same array element cannot be used twice.
- The indexes may be returned in any order.

## Examples

### Example 1

```text
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
```

Because:

```text
nums[0] + nums[1] = 2 + 7 = 9
```

### Example 2

```text
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]
```

### Example 3

```text
Input: nums = [3, 3], target = 6
Output: [0, 1]
```

## Constraints

```text
2 <= nums.length <= 10,000
-1,000,000,000 <= nums[i] <= 1,000,000,000
-1,000,000,000 <= target <= 1,000,000,000
```

Only one valid answer exists.

## Follow-up

Can you design an algorithm with a time complexity better than `O(n²)`?

## LeetCode

[1. Two Sum](https://leetcode.com/problems/two-sum/)
