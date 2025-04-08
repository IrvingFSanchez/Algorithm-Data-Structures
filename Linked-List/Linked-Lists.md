# 🔗 **Singly-Linked List vs. Doubly-Linked List**

## 🧩 **Singly-Linked List**

Each node contains:

- **Data**
- A **pointer to the next node**

```plaintext
[Data|Next] -> [Data|Next] -> [Data|Next] -> None
```

### ✅ Pros

- Simple and uses **less memory** (only one pointer per node)
- Easy to implement
- Great for **forward-only** traversals or **stack-like** behavior (e.g., pushing/popping from the front)

### ❌ Cons

- **No backward traversal**
- To delete a node or access the end, you must **traverse from the head** (O(n) time)

---

### 🔁 **Doubly-Linked List**

Each node contains:

- **Data**
- A **pointer to the next node**
- A **pointer to the previous node**

```plaintext
None <- [Prev|Data|Next] <-> [Prev|Data|Next] <-> [Prev|Data|Next] -> None
```

#### ✅ Advantages

- You can traverse in **both directions**
- Deletion of a known node is **easier and faster** (especially if you’re in the middle of the list)
- Better suited for things like **browser history**, **undo/redo**, or **deques**

#### ❌ Drawbacks

- Uses **more memory** (two pointers per node)
- Slightly more complex to implement and maintain pointer integrity

---

## ⏱️ **Big-O Complexity: What It Means for Each List**

| Operation             | Singly-Linked List | Doubly-Linked List | Notes |
|----------------------|--------------------|--------------------|-------|
| `add_first()`        | O(1)               | O(1)               | Just update head (and possibly tail if list was empty) |
| `add_last()`         | O(n)* or O(1)**    | O(1)               | *O(n) if no tail pointer; **O(1) with tail |
| `remove_first()`     | O(1)               | O(1)               | Just update head |
| `remove_last()`      | O(n)               | O(1)               | Singly needs to traverse; doubly has `tail.prev` |
| `delete(data)`       | O(n)               | O(n)               | Both require search by value unless node ref is given |
| `search(data)`       | O(n)               | O(n)               | Linear scan from head in both |
| `traverse` (forward) | O(n)               | O(n)               | Simple loop |
| `traverse` (backward)| ❌ Not Possible     | O(n)               | Only possible in doubly due to `prev` pointers |

---

### 🧠 Final Thought

- If you **only need to traverse forward** and memory is a concern → **Singly-linked list** is ideal.
- If you need **bidirectional movement** or frequent deletion in the middle → **Doubly-linked list** gives you more power.
