# 📚 Algorithm & Data Structures 🚀

Welcome to the **Algorithm-Data-Structures** repository! This is a collection of Python projects exploring core concepts in **data structures** and **algorithmic problem-solving**. Each project tackles a unique challenge, from **directory traversal** to **memory management simulations**, with a mix of efficiency, creativity, and a bit of personal flair.

---

## 📌 Projects Overview

### ⏱️ **Sorting Algorithm Benchmark** (`sorting-benchmark.py`)

- **Compares performance** of Bubble Sort vs Quick Sort on real-world datasets:
  - Pokémon stats (~1,000 entries)
  - MTG tokens (~5,000 entries)
  - Video games (~10,000 entries)
- **Interactive menu system** for dataset/field selection
- **Configurable data preparation**:
  - 🎲 Fully randomized order
  - 🔄 Almost-sorted (95% sorted, 5% swapped)
- **Benchmarking features**:
  - 5 timed runs per algorithm
  - Auto-generated performance graphs
  - Option to save sorted results (e.g., `Pokemon_Name_sorted_data.txt`)
- **Visualization**:
  - 🟥 Bubble Sort vs 🟩 Quick Sort timing comparison
  - Average performance lines
  - Annotated millisecond values

---

### 🧠 Brain Filing System: Custom Hash Table ADT

- A metaphorical hash table designed as a **Brain Filing System**, where:
  - Keys are *thoughts* 🧠
  - Values are *memories* 📦
  - Drawers represent slots in the internal fixed-size list
- Implements core hash table operations:
  - `store_memory()` → insert/update (put)
  - `recall_memory()` → retrieve (get)
  - `forget_memory()` → delete (remove)
- Uses **Python's built-in `hash()` function** and modulo operation
- Collision handling with **separate chaining (list-based)**
- Features two simulation runs:
  - **Standard Brain** with 10 drawers
  - **Tiny Brain** with 2 drawers (forces collisions)
- Includes structured comment blocks

📌 **Concepts applied**: **Abstract Data Types**, **Hashing**, **Collision Handling**, **Chaining**, **Python Lists**, **Modular Arithmetic**

🧾 **Final Reflection & Write-Up:** [Located in the Hash Table README](./Hash-Table/README.md), including project insight, hash behavior analysis, and chaining validation.

---

### 🌳 **Tree ADT Implementation** (`forest_manager.py`)

- **General tree structure** with botanical naming conventions (nodes as trees, children as branches)
- **Three traversal methods**:
  - 🌱 Preorder (Root → Children)
  - 🍂 Postorder (Children → Root)
  - 🌍 Breadth-First (Level Order)
- **Clear visual representation** using Mermaid diagrams
- **Practical applications**:
  - File system navigation
  - Organization charts
  - Decision tree algorithms
- Includes:
  - Recursive traversal implementations
  - Queue-based breadth-first search
  - Comprehensive test cases
  
```mermaid
flowchart TD
    A --> B --> E
    B --> F
    A --> C
    A --> D --> G --> H
    G --> I
    G --> J
```

---

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
