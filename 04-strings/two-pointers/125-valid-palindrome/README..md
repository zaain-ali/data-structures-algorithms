# 125. Valid Palindrome

## Difficulty

Easy

## Topics

- String
- Two Pointers

## Problem

A phrase is a palindrome if, after converting uppercase letters to lowercase and removing all non-alphanumeric characters, it reads the same forward and backward.

Given a string `s`, return `True` if it is a palindrome. Otherwise, return `False`.

Alphanumeric characters include letters and numbers.

## Examples

### Example 1

```text
Input: s = "A man, a plan, a canal: Panama"
Output: true
```

After normalization:

```text
amanaplanacanalpanama
```

### Example 2

```text
Input: s = "race a car"
Output: false
```

After normalization:

```text
raceacar
```

### Example 3

```text
Input: s = " "
Output: true
```

After removing non-alphanumeric characters, the string is empty. An empty string is a palindrome.

## Constraints

```text
1 <= s.length <= 200,000
s contains only printable ASCII characters
```

## LeetCode

[125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
