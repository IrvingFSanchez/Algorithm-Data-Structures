# 📚 Algorithm & Data Structures 🚀

Welcome to the **Algorithm-Data-Structures** repository! This is a collection of Python projects exploring core concepts in **data structures** and **algorithmic problem-solving**. Each project tackles a unique challenge, from **directory traversal** to **memory management simulations**, with a mix of efficiency, creativity, and a bit of personal flair.

---

## 📌 Projects Overview

### 🔗 **Linked List Implementations** (`singlylinked.py`, `doublylinked.py`)

- **Singly Linked List** with O(1) `add_first`/`add_last` operations
  - Tail pointer optimization for efficient appends
  - Full suite of operations: insert/delete/search
- **Doubly Linked List** with bidirectional traversal
  - O(1) operations at both ends
  - Real-world applications (browser history, undo systems)
- Includes:
  - Big-O complexity analysis
  - Edge case handling
  - Interactive test cases

📌 **Concepts applied**: **Pointer Manipulation**, **Time Complexity**, **Bidirectional Traversal**, **Memory Efficiency**

---

## 🚀 Key Features of Linked List Project

| Feature          | Singly-Linked | Doubly-Linked |
|------------------|---------------|---------------|
| **Insert at Head** | ✅ O(1)       | ✅ O(1)       |
| **Insert at Tail** | ✅ O(1)       | ✅ O(1)       |
| **Delete Middle**  | ⚠️ O(n)      | ⚠️ O(n)      |
| **Traversal**      | → Only        | ↔ Bidirectional |

**Real-World Use Cases**:

- Music playlists (singly-linked)
- Browser history (doubly-linked)
- Undo/redo systems

---

### 🎥 **Movie Recommendation & Directory Traversal** (`main.py`)

- Implements **recursive directory traversal** to locate and load **movie data** from text files.
- Uses a **Deque (double-ended queue)** for **movie storage and recommendations**.
- Features a **speakeasy-style UI**, inspired by 1920s slang, for a fun **interactive menu system**.
- Offers:
  - **Movie listing & searching with autocomplete**
  - **Personalized recommendations**
  - **Top-rated movie selections**
- Libraries used: `os`, `pyfiglet`, `colorama`

📌 **Concepts applied**: **Recursion**, **Deque ADT**, **File I/O**, **Error Handling**, **Sorting Algorithms**

---

### 💧 **Health Tracker** (`health_tracker.py`)

- A simple **daily health logger** to track:
  - 💦 **Water intake** (goal: 64 oz/day)
  - 🏃 **Activity minutes** (goal: 30 min/day)
- **User-friendly CLI menu** for logging data.
- **Encouraging messages** based on progress.
- **Data reset feature** to start fresh every day.
- **Error handling** to prevent invalid inputs.

📌 **Concepts applied**: **User Input Handling**, **Looping Constructs**, **Conditionals**, **Global Variables & Constants**

---

### 📂 **Directory Tree Traversal** (`directory_traverse.py`)

- **Recursive function** to traverse **file directories**.
- **Indentation formatting** for a **tree-like output**.
- **Error handling** for permission and path issues.
- **Latin-inspired variable names** for a touch of creativity.

📌 **Concepts applied**: **Recursion**, **Tree Representation**, **Error Handling**, **Python Generators**

---

### 🔑 **School Locker System (Dynamic Array Simulation)** (`school_locker.py`)

- **Mimics low-level memory management** like **C-based array handling**.
- **Dynamic resizing** for efficient memory allocation.
- Features:
  - **Locker Addition & Insertion**
  - **Locker Removal**
  - **Locker Search**
  - **Dynamic Expansion**
- Uses **ctypes** for raw memory allocation.

📌 **Concepts applied**: **Dynamic Arrays**, **Memory Allocation**, **Custom Data Structures**

---

## 🚀 **Getting Started**

### 🛠 Prerequisites

Ensure you have Python **3.x** installed. Some projects require:

```bash
pip install pyfiglet colorama
```

### ▶ **Running a Project**

To execute a project, simply run:

```bash
python filename.py
```

For example:

```bash
python main.py
```

---

## 🤓 **Why This Repo?**

This repository is a hands-on **exploration of data structures** through practical applications. Instead of just theory, each project **applies ADTs in creative ways** to solve real-world problems.

**Stay tuned for more projects & optimizations!** ✨

---

🎯 **Built with Python** | 🧠 **By Irving F. Sanchez** | 🏛 **Lewis University, CPSC-34000-002**

---
