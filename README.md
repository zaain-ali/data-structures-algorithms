# Data Structures & Algorithms

A structured, practical guide to learning **Data Structures and Algorithms (DSA)** from fundamentals to advanced problem-solving.

This repository combines **concepts, algorithms, visual explanations, complexity analysis, problem-solving patterns, and LeetCode problems** into one organized learning path.

The goal is to help learners understand **how and why algorithms work**, rather than simply memorizing solutions.

---

## 🎯 What This Repository Covers

The roadmap progresses from fundamental concepts to advanced interview-level topics:

- Algorithmic complexity
- Arrays and strings
- Hashing
- Linked lists
- Stacks and queues
- Recursion
- Trees
- Heaps
- Graphs
- Searching
- Sorting
- Sliding window
- Two pointers
- Prefix sums
- Backtracking
- Greedy algorithms
- Dynamic programming
- Tries
- Bit manipulation
- Advanced data structures and algorithms
- Problem-solving patterns

---



## 🧠 Learning Approach

Each topic is designed around the following learning process:

```text
Concept
   ↓
Algorithm
   ↓
Visual Intuition
   ↓
Example
   ↓
Complexity Analysis
   ↓
Practice Problem
   ↓
Implementation
   ↓
Pattern Recognition
```

The focus is on developing **problem-solving intuition** that can be applied to new problems.

---



## 📚 Roadmap



### 01 — Foundations

- Big-O & Complexity Analysis



### 02 — Arrays

- Array Fundamentals
- Memory & Indexing
- Access, Search, Insert & Delete
- Dynamic Arrays
- Two Pointers
- Fixed Sliding Window
- Variable Sliding Window
- Prefix Sum



### 03 — Hashing

- Hash Tables
- Hash Maps
- Hash Sets
- Frequency Counting
- Lookup Patterns



### 04 — Strings

- String Fundamentals
- Character Frequency
- String Manipulation
- Two Pointers
- Sliding Window



### 05 — Linked Lists

- Singly Linked Lists
- Doubly Linked Lists
- Fast & Slow Pointers
- Reversal
- Cycle Detection
- Merging Lists



### 06 — Stack

- Stack Fundamentals
- Monotonic Stack
- Expression Problems
- Parentheses Problems



### 07 — Queue & Deque

- Queue Fundamentals
- Circular Queue
- Deque
- Monotonic Queue



### 08 — Recursion

- Recursion Fundamentals
- Call Stack
- Base Cases
- Recursive Problem Solving



### 09 — Trees

- Binary Trees
- Tree Traversals
- DFS
- BFS
- Binary Search Trees
- Tree Recursion



### 10 — Heaps

- Heap Fundamentals
- Min Heap
- Max Heap
- Priority Queue
- Top-K Problems



### 11 — Graphs

- Graph Representation
- BFS
- DFS
- Connected Components
- Cycle Detection
- Topological Sort
- Shortest Paths
- Minimum Spanning Tree



### 12 — Searching

- Linear Search
- Binary Search
- Binary Search on Answer
- Search Patterns



### 13 — Sorting

- Selection Sort
- Bubble Sort
- Insertion Sort
- Merge Sort
- Quick Sort
- Heap Sort
- Sorting Patterns



### 14 — Backtracking

- Backtracking Fundamentals
- Permutations
- Combinations
- Subsets
- Constraint-Based Search



### 15 — Greedy Algorithms

- Greedy Fundamentals
- Interval Problems
- Scheduling
- Optimization Patterns



### 16 — Dynamic Programming

- DP Fundamentals
- Memoization
- Tabulation
- 1D DP
- 2D DP
- Knapsack Patterns
- Advanced DP



### 17 — Tries

- Trie Fundamentals
- Prefix Search
- Word Search
- String-Based Problems



### 18 — Bit Manipulation

- Bitwise Operators
- Bit Masks
- XOR Patterns
- Bit Manipulation Problems



### 19 — Advanced Data Structures

- Segment Trees
- Fenwick Trees
- Disjoint Set Union
- Advanced Graph Structures



### 20 — Interview Problem Solving

- Problem Classification
- Pattern Recognition
- Brute Force → Optimization
- Complexity Trade-offs
- Edge Cases
- Interview Strategies

---



## 📂 Repository Structure

```text
dsa-roadmap/
│
├── README.md
│
├── 01-foundations/
│   └── big-o/
│
├── 02-arrays/
│   ├── fundamentals/
│   ├── two-pointers/
│   ├── sliding-window/
│   │   ├── fixed/
│   │   └── variable/
│   └── prefix-sum/
│
├── 03-hashing/
├── 04-strings/
├── 05-linked-lists/
├── 06-stack/
├── 07-queue/
├── 08-recursion/
├── 09-trees/
├── 10-heaps/
├── 11-graphs/
├── 12-searching/
├── 13-sorting/
├── 14-backtracking/
├── 15-greedy/
├── 16-dynamic-programming/
├── 17-trie/
├── 18-bit-manipulation/
├── 19-advanced-data-structures/
│
└── 20-interview-problem-solving/
```

---



## 🧩 Topic Structure

Each topic contains explanations and practical problems.

For example:

```text
sliding-window/
│
├── fixed/
│   ├── README.md
│   ├── 643-maximum-average-subarray-i.py
│   └── 1456-maximum-number-of-vowels.py
│
└── variable/
    ├── README.md
    └── 209-minimum-size-subarray-sum.py
```

Topic documentation focuses on:

- What the concept is
- When to use it
- How the algorithm works
- Visual intuition
- Step-by-step examples
- Time complexity
- Space complexity
- Common mistakes
- Related problems

---



## 💻 Problem-Solving Philosophy

A problem should not be approached by immediately searching for a solution.

Instead:

```text
Understand the Problem
        ↓
Understand the Constraints
        ↓
Think of a Brute-Force Solution
        ↓
Analyze Its Complexity
        ↓
Identify a Pattern
        ↓
Optimize the Approach
        ↓
Implement
        ↓
Test Edge Cases
        ↓
Analyze Complexity Again
```

This approach helps develop the ability to solve **unfamiliar problems**, rather than only problems that have been seen before.

---



## ⏱️ Complexity Analysis

Every algorithm should be evaluated in terms of:

### Time Complexity

How the execution time grows as the input size increases.

Common complexities include:

```text
O(1)
O(log n)
O(n)
O(n log n)
O(n²)
O(2ⁿ)
O(n!)
```



### Space Complexity

How much additional memory an algorithm requires.

Understanding the trade-off between time and space is an important part of algorithm design.

---



## 🧪 Practice Problems

The repository includes problems from platforms such as **LeetCode** and other algorithmic problem-solving platforms.

Problems are organized by the underlying concept or pattern rather than simply by difficulty.

For example:

```text
Sliding Window
├── Fixed Window
│   ├── Problem A
│   └── Problem B
│
└── Variable Window
    ├── Problem C
    └── Problem D
```

This makes it easier to recognize when the same technique can be applied to a different problem.

---



## 📝 Solution Format

Solutions should remain readable and focused on the underlying algorithm.

Example:

```python
"""
Problem: Minimum Size Subarray Sum

Pattern:
Variable Sliding Window

Time: O(n)
Space: O(1)
"""
```

The objective is to make each solution useful for both **practice and future revision**.

---



## 🔍 Common Problem-Solving Patterns

A major goal of this repository is learning reusable patterns.

Some important patterns include:

- Two Pointers
- Sliding Window
- Prefix Sum
- Hash Map / Hash Set
- Fast & Slow Pointers
- Binary Search
- Stack / Monotonic Stack
- BFS / DFS
- Backtracking
- Heap / Priority Queue
- Greedy
- Dynamic Programming
- Union Find
- Topological Sort

Instead of asking:

> "Have I seen this exact problem before?"

the goal is to learn to ask:

> "What pattern does this problem resemble?"

---



## 🎓 Who Is This For?

This repository is designed for anyone who wants to learn or strengthen their DSA skills, including:

- Beginners learning DSA for the first time
- Computer science students
- Software engineering students
- Developers preparing for technical interviews
- Developers improving algorithmic thinking
- Anyone practicing competitive programming

The roadmap can be followed sequentially or used as a reference for individual topics.

---



## ⭐ Learning Principle

> **Don't memorize solutions. Understand the pattern.**

A good DSA solution is not just code that passes the test cases.

You should be able to explain:

- Why the algorithm works
- Why it is correct
- When the pattern can be used
- What its complexity is
- What its limitations are
- How it could be adapted to another problem

---



## 🤝 Contributions

Suggestions, improvements, corrections, and additional learning resources are welcome.

If you find an error or have a better explanation or implementation, feel free to open an issue or submit a pull request.

---



## 📖 License

This repository is intended for educational purposes. LeetCode problem statements and other third-party content remain the property of their respective owners.

Solutions and original explanations in this repository are provided for learning and educational use.
