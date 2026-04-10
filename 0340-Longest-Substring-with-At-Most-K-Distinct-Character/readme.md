
# Longest Substring with At Most K Distinct Characters

## 📌 Problem (LeetCode 340)

Given a string `s` and an integer `k`, return the length of the longest substring of `s` that contains **at most `k` distinct characters**.

---

## 🧾 Description

A substring is a contiguous non-empty sequence of characters within a string.

You need to find the longest possible substring such that the number of **distinct characters** in that substring is less than or equal to `k`.

---

## 📥 Input

- A string `s`
- An integer `k`

---

## 📤 Output

- An integer representing the length of the longest valid substring

---

## 📌 Constraints

- `1 <= s.length <= 10^5`
- `0 <= k <= 26` (or up to number of unique characters in input)
- `s` consists of lowercase English letters

---

## 🧪 Example 1

### Input:
```

s = "eceba"
k = 2

```

### Output:
```

3

```

### Explanation:
The longest substring with at most 2 distinct characters is `"ece"`.

---

## 🧪 Example 2

### Input:
```

s = "aa"
k = 1

```

### Output:
```

2

```

### Explanation:
The entire string has only one distinct character.

---

## 💡 Note

- You must consider **contiguous substrings only**
- The result is the **maximum length possible**
- Each substring must contain **at most k distinct characters**

---
```

---

