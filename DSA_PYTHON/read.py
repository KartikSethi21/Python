# Here's a complete guide to hashing in Python, from the basics all the way through maps and collision handling.


## What is Hashing?

# Hashing is a two-step technique:
# 1. **Pre-storing** — scan your data once and store useful info (like frequencies) in a structure
# 2. **Fetching** — look up answers in O(1) instead of re-scanning the data

# Without hashing, answering Q queries over N elements costs **O(Q × N)**. With hashing, it drops to **O(N + Q)**.

# Let me show how this works visually, then walk through all the code.---

## 1. Number Hashing — Array-based (small numbers only)

# When the values fit in a small range, you can use a Python list as your hash array. Each index represents a value; the stored number is its frequency.

# Number hashing using a list (only works when max element is small)

def number_hashing_array():
    arr = list(map(int, input().split()))

    # Step 1: Pre-store — build frequency table
    max_val = 12  # assume max element ≤ 12
    hash_table = [0] * (max_val + 1)  # index = element value

    for num in arr:
        hash_table[num] += 1  # increment frequency

    # Step 2: Fetch — answer queries in O(1)
    q = int(input())
    for _ in range(q):
        number = int(input())
        if number <= max_val:
            print(hash_table[number])
        else:
            print(0)

# Sample run (no input needed):
arr = [1, 3, 2, 1, 3]
hash_table = [0] * 13

for num in arr:
    hash_table[num] += 1

# hash_table is now: [0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]

queries = [1, 4, 2, 3, 12]
for q in queries:
    print(f"count of {q}: {hash_table[q]}")

# Output:
# count of 1: 2
# count of 4: 0
# count of 2: 1
# count of 3: 2
# count of 12: 0

# **Why the list approach has limits:** If values go up to 10⁹, you'd need a list of a billion elements — that's ~4 GB of memory and completely impractical.


## 2. Character Hashing — Three Cases

### Case 1: Lowercase letters only (map to 0–25)

s = "abcdabefc"

# Pre-store: map 'a'→0, 'b'→1, ..., 'z'→25
hash_char = [0] * 26

for ch in s:
    hash_char[ord(ch) - ord('a')] += 1
    # ord('f') - ord('a') = 102 - 97 = 5  → hash_char[5] += 1

# Fetch
queries = ['a', 'c', 'z']
for ch in queries:
    print(f"count of '{ch}': {hash_char[ord(ch) - ord('a')]}")

# Output:
# count of 'a': 2
# count of 'c': 1
# count of 'z': 0

### Case 2: Uppercase letters only (map to 0–25)

s = "HELLO"
hash_char = [0] * 26

for ch in s:
    hash_char[ord(ch) - ord('A')] += 1  # 'A'→0, 'B'→1, ...

# Fetch
print(hash_char[ord('L') - ord('A')])  # Output: 2

### Case 3: Mixed uppercase + lowercase (use full 256 ASCII)

s = "Hello World"
hash_char = [0] * 256

for ch in s:
    hash_char[ord(ch)] += 1  # use raw ASCII — no subtraction needed

# Fetch
print(hash_char[ord('l')])  # Output: 3
print(hash_char[ord('H')])  # Output: 1
print(hash_char[ord(' ')])  # Output: 1

## 3. Hashing Large Numbers — Python `dict` (your real workhorse)

# This is the Python equivalent of C++'s `unordered_map`. It handles any key — including numbers as large as 10⁹ or higher — without any size restrictions.

arr = [1, 2, 3, 1, 3, 2, 12]

# Step 1: Pre-store using a dict
freq = {}
for num in arr:
    freq[num] = freq.get(num, 0) + 1
    # OR: use collections.Counter (even simpler — shown below)

# freq is now: {1: 2, 2: 2, 3: 2, 12: 1}

# Step 2: Fetch
queries = [1, 2, 3, 4, 12]
for q in queries:
    print(f"count of {q}: {freq.get(q, 0)}")
    # .get(key, 0) returns 0 if the key doesn't exist — just like C++ map behavior

# Output:
# count of 1: 2
# count of 2: 2
# count of 3: 2
# count of 4: 0
# count of 12: 1

### The Pythonic shortcut: `collections.Counter`


from collections import Counter

arr = [1, 2, 3, 1, 3, 2, 12]
freq = Counter(arr)
# Counter({1: 2, 2: 2, 3: 2, 12: 1})

print(freq[4])   # Output: 0  (Counter returns 0 for missing keys automatically)
print(freq[1])   # Output: 2


# Counter` is built on `dict` internally but gives you frequency counting for free. Use it whenever you're counting occurrences.

### Character hashing with `dict`


s = "abcdabefc"
char_freq = {}

for ch in s:
    char_freq[ch] = char_freq.get(ch, 0) + 1

# char_freq: {'a': 2, 'b': 2, 'c': 2, 'd': 1, 'e': 1, 'f': 1}

# Fetch
queries = ['a', 'c', 'z']
for ch in queries:
    print(f"count of '{ch}': {char_freq.get(ch, 0)}")

# Output:
# count of 'a': 2
# count of 'c': 1
# count of 'z': 0


## 4. Understanding Collision (Division Method Explained in Python)

# Here's Python code that simulates the division method and chaining — this is what Python's `dict` handles internally for you:

# python
# Simulating the division method manually (for understanding only)
# In practice, just use Python's dict!

class ManualHashTable:
    def __init__(self, size=10):
        self.size = size
        # Each slot holds a list (chain) of (key, value) pairs
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return key % self.size  # Division method

    def insert(self, key):
        bucket = self._hash(key)
        # Check if key already exists in the chain
        for pair in self.table[bucket]:
            if pair[0] == key:
                pair[1] += 1
                return
        self.table[bucket].append([key, 1])  # New key

    def fetch(self, key):
        bucket = self._hash(key)
        for pair in self.table[bucket]:
            if pair[0] == key:
                return pair[1]
        return 0  # Not found

# Demo
arr = [2, 5, 16, 28, 139, 38, 48, 28, 18]
ht = ManualHashTable(size=10)

for num in arr:
    ht.insert(num)

# 28, 38, 48, 18 all map to bucket 8 → collision! → chained together
print("Bucket 8:", ht.table[8])
# Output: Bucket 8: [[28, 2], [38, 1], [48, 1], [18, 1]]

print("Freq of 28:", ht.fetch(28))  # Output: 2
print("Freq of 38:", ht.fetch(38))  # Output: 1
print("Freq of 99:", ht.fetch(99))  # Output: 0


## 5. Complexity Summary

# Now let's visualize how the different approaches compare:---

## 6. Complete Python Summary — All Patterns Side by Side

from collections import Counter, defaultdict

# ── Pattern 1: List-based (small integer keys only) ─────────────────
arr = [1, 2, 1, 3, 2]
hash_list = [0] * 13        # size = max_element + 1
for x in arr:
    hash_list[x] += 1
print(hash_list[1])          # 2

# ── Pattern 2: dict (any key — numbers, strings, tuples) ────────────
freq = {}
for x in arr:
    freq[x] = freq.get(x, 0) + 1
print(freq.get(5, 0))        # 0 — missing key returns 0

# ── Pattern 3: defaultdict (cleaner syntax) ──────────────────────────
freq2 = defaultdict(int)     # default value = 0
for x in arr:
    freq2[x] += 1            # no need for .get()
print(freq2[99])             # 0 — auto-initialized

# ── Pattern 4: Counter (most Pythonic for frequency problems) ────────
freq3 = Counter(arr)
print(freq3[1])              # 2
print(freq3[99])             # 0

# ── Pattern 5: Character hashing with dict ───────────────────────────
s = "abcdabefc"
char_freq = Counter(s)       # or build manually with dict
print(char_freq['a'])        # 2
print(char_freq['z'])        # 0

## Key Takeaways

# Python makes hashing much simpler than C++ because:

# - **`dict`** is Python's built-in hash map — it works like `unordered_map` in C++, giving O(1) average insert and lookup with no size limits.
# - **`Counter`** from `collections` is a `dict` subclass tailor-made for frequency counting — it returns 0 for missing keys automatically and can be built from any iterable in one line.
# - **`defaultdict(int)`** is another great option — any missing key auto-initializes to 0, so you never need to check if a key exists before incrementing.
# - Use a plain **`list`** only when your keys are small non-negative integers (like character ASCII values or small array values).
# - **Collision** is real but almost never a problem in practice — Python's dict uses a very robust hashing algorithm internally, and worst-case O(N) behavior is extremely rare.