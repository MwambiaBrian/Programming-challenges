# Sliding Window Algorithms

This repository provides efficient Python implementations for solving common substring problems using the **sliding window technique**. These solutions are designed to handle varying constraints, such as unique characters, a fixed number of distinct characters, or a dynamic limit of distinct characters.

---

## **Algorithms Included**

### 1. **Longest Substring Without Repeating Characters**

Finds the length of the longest substring where all characters are unique.  
**Key Features:**

- Uses a `set` to maintain the unique characters in the current window.
- Adjusts the window dynamically by moving the `left` pointer when duplicates are encountered.

**Function:**

```python
def length_of_longest_substring(s: str) -> int:
    char_set = set()  # Set of unique characters
    left = 0
    max_length = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length
```

#### **Example Usage**"

```python
print(length_of_longest_substring(s))  # Output: 3
```

### **2. Longest Substring With At Most Two Distinct Characters**

Finds the length of the longest substring that contains at most two distinct characters.
**Key Features:**

- Uses a `dictionary` to count the frequency of characters in the current window.
- Shrinks the window when more than two distinct characters are present.
  **Function:**

```python
Copy code
def length_of_longest_substring_two_distinct(s: str) -> int:
    char_count = {}  # Dictionary to store character counts
    left = 0
    max_length = 0
    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        while len(char_count) > 2:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        max_length = max(max_length, right - left + 1)
    return max_length
```

**Example Usage:**

```python
Copy code
s = "eceba"
print(length_of_longest_substring_two_distinct(s))  # Output: 3
```

### **3. Longest Substring With At Most K Distinct Characters**

Finds the length of the longest substring containing at most k distinct characters.
**Key Features:**

- Generalized solution using a `dictionary` to track character frequencies.
- Handles varying values of k efficiently.
  **Function:**

```python
Copy code
def length_of_longest_substring_k_distinct(s: str, k: int) -> int:
    if k == 0 or not s:
        return 0
    char_count = {}  # Dictionary to store character counts
    left = 0
    max_length = 0
    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        max_length = max(max_length, right - left + 1)
    return max_length
```

**Example Usage:**

```python
Copy code
s = "eceba"
k = 3
print(length_of_longest_substring_k_distinct(s, k))  # Output: 5
```

### **How It Works**

**Sliding Window Approach**

- Start with two pointers (left and right) to define the current window.
- Expand the window by moving right and include the current character in the window.
- If the window becomes invalid (e.g., exceeds constraints on distinct characters), move left to shrink the window.
- Update the maximum length after each iteration.
  **Performance**

- Time Complexity:
  𝑂(𝑛)
  O(n) for all functions, where n is the length of the input string.
- Space Complexity:
  𝑂(𝑘)
  O(k), where k is the number of distinct characters in the substring.
