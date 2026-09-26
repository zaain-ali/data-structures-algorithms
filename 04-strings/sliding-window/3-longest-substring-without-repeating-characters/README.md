# 3. Longest Substring Without Repeating Characters

## Difficulty

Medium

## Topics

- String
- Hash Table
- Sliding Window

## Problem

Given a string `s`, return the length of its longest substring containing no repeated characters.

A substring must contain consecutive characters from the original string.

## Examples

### Example 1

```text
Input: s = "abcabcbb"
Output: 3
```

Possible longest substrings include:

```text
"abc"
"bca"
"cab"
```

### Example 2

```text
Input: s = "bbbbb"
Output: 1
```

The longest substring without repetition is:

```text
"b"
```

### Example 3

```text
Input: s = "pwwkew"
Output: 3
```

One valid longest substring is:

```text
"wke"
```

`"pwke"` is not valid because it is a subsequence rather than a continuous substring.

## Constraints

```text
0 <= s.length <= 100,000
s contains English letters, digits, symbols, and spaces
```

## LeetCode

[3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
