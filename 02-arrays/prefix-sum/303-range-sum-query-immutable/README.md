# 303. Range Sum Query — Immutable

## Difficulty

Easy

## Topics

- Array
- Prefix Sum
- Design

## Problem

Given an integer array `nums`, handle multiple queries that ask for the sum of elements between two indexes.

Implement the `NumArray` class:

- `NumArray(nums)` initializes the object with the integer array `nums`.
- `sumRange(left, right)` returns the sum of the elements from index `left` to index `right`, inclusive.

## Example

```text
Input:
["NumArray", "sumRange", "sumRange", "sumRange"]

[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]

Output:
[null, 1, -1, -3]
```

### Explanation

```text
NumArray([-2, 0, 3, -5, 2, -1])

sumRange(0, 2) returns 1
sumRange(2, 5) returns -1
sumRange(0, 5) returns -3
```

## Constraints

```text
1 <= nums.length <= 10,000
-100,000 <= nums[i] <= 100,000
0 <= left <= right < nums.length
At most 10,000 calls will be made to sumRange.
```

## Goal

Answer every range-sum query correctly and efficiently.

## LeetCode

[303. Range Sum Query — Immutable](https://leetcode.com/problems/range-sum-query-immutable/)