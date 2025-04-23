# 🛍️ Project Timeline: Building the Brain Filing System 🧠

---

## First and Foremost 🤓☝️

Before diving into the technical journey, it’s important to share the intention behind how I approach coding projects like this one.

I write code as if I’m teaching it to someone who has little to no experience with programming — not because I assume they can’t understand it, but because I believe most confusion in math, science, and computer science stems from unnecessary overcomplication. My goal is to make concepts like hash tables approachable, relatable, and maybe even a little fun.

Every line I write is an opportunity to build a bridge — not just between variables and functions, but between learners and ideas. I want my code to do more than just earn a grade. I want it to be something that could help someone — maybe a high school student exploring engineering, maybe a curious adult learning to code for the first time — feel like this world is accessible to them too.

This has always been a part of my mission aparatus, ever since I learned about my complications in a learning environment.

---

### 🧹 **Step 1: Defining the Goal**

**🗓️ Timeline:** Part 1  
**💭 Mindset:** Curious, open to exploring beyond textbook programming  
I started by reviewing the assignment objective: build a hash table from scratch using Python. Instead of jumping into raw code, the goal was to reimagine it through a metaphor that could help non-programmers and myself understand abstract concepts. Furthermore, documenting the way this code is developed is actually really satisfying to me because I am huge into being able to replicate one's work through pre-lab and a historical timeline--this probably came from my many times writing up lab reports during my time in Physics and Chemistry.

```python
class BrainFilingSystem:
    def __init__(self, capacity=10):
        self.drawer_count = capacity
        self.memory_drawers = [None] * self.drawer_count
```

---

### 🧠 **Step 2: Brainstorming Metaphors**

**🗓️ Timeline:** Part 2  
**🛠️ Thought Process:** “How can we *humanize* this structure?”  
Several metaphors came to mind and were proposed — libraries, treasure chests, post offices, backpacks — but the “Brain Filing System” stood out--especially since I'm sure in some way shape or form this simple yet important concept could revolve around a field I'm passionate about: AI, neuroscience, education, and machine learning. It framed the concept in a way that felt intuitive: thoughts being stored and retrieved from memory drawers.

---

### 🔧 **Step 3: Building the Core Class**

**🗓️ Timeline:** Part 3  
**🧠 Decision Making:**  

- The class was named `BrainFilingSystem` instead of `HashTable`  
- Hash function was described as the brain's internal logic for organizing thoughts  
- Collision handling became “storing multiple memories in one drawer”  

```python
def hash(self, thought):
    return abs(hash(thought)) % self.drawer_count
```

This stage emphasized clarity over complexity — using readable comments and metaphors throughout the method names (`store_memory`, `recall_memory`, `forget_memory`).

---

### 📃️ **Step 4: Implementing Collision Handling**

**🗓️ Timeline:** Part 4  
**🧹 Technical Insight:** I chose **chaining**, implemented as lists inside drawers.  
I commented this visually as “multiple memories under the same thought category.” This was a great teaching point to discuss how the brain handles multiple memories tied to similar triggers.

```python
if self.memory_drawers[drawer_idx] is None:
    self.memory_drawers[drawer_idx] = [(thought, memory)]
else:
    for i, (existing_thought, _) in enumerate(self.memory_drawers[drawer_idx]):
        if existing_thought == thought:
            self.memory_drawers[drawer_idx][i] = (thought, memory)
            return
    self.memory_drawers[drawer_idx].append((thought, memory))
```

---

### 🎨 **Step 5: Annotating with Blocks & Commentary**

**🗓️ Timeline:** Part 5  
**✍️ Writing Style:** Inspired by previous codebase aesthetics  
I wrapped each method with labeled comment blocks (e.g., `/*---+---+---+--Start of store_memory Function Block---+---+---+--*/`) to maintain consistency with my style. This also made it easy to read like chapters in a mental user's manual.

---

### 📚 **Step 6: Final Metaphorical Framing**

**🗓️ Timeline:** Part 6  
**📖 Output Summary:** The `__str__()` method gives a printable catalog of what’s in each drawer — simulating a mental map of remembered or forgotten thoughts.

```python
def __str__(self):
    summary = "\n Brain Memory Drawers (Hash Table):\n"
    for idx, drawer in enumerate(self.memory_drawers):
        ... # Shows which drawer holds what
    return summary
```

---

### 🏛️ Interpreting Output: Drawer Capacity & Collision Impact

When running the program with the default capacity (10 drawers), most thoughts are distributed across different drawers. This shows a relatively clean layout:

```python
Drawer 0: 'vacation' -> Sunburns and ice cream
Drawer 4: 'childhood dog' -> Barked loudly at the mailman
Drawer 9: 'first bike ride' -> Wobbly but thrilling
```

When switching to a brain with only 2 drawers, we dramatically increase the likelihood of collisions. The output looks like this:

```python
Drawer 0: 'childhood fear' -> Afraid of thunder | 'deep conversation' -> Felt seen for the first time
Drawer 1: 'sunset memory' -> The sky turned gold at the beach | 'favorite snack' -> Hot Cheetos during cartoons
```

This confirms that multiple (key, value) pairs can be stored in the same slot, thanks to the chaining mechanism.

---

## 💡 Mindset Throughout the Project

- **Creative Framing**: The goal wasn’t just to *build* a hash table, but to tell a story that makes its inner workings feel personal and intuitive.
- **Simplicity & Clarity**: Every method has human-readable names and comments to support comprehension over cleverness.
- **Empathy for Beginners**: By designing for the curious beginner, we made something that even a non-coder could explain.
- **Playful but Purposeful**: Humor and metaphor served to demystify a data structure that can feel intimidating.

---

## ✍🏻 Final Reflection

Initially if you run this program multiple times, you might notice that the same thoughts (like "vacation" or "childhood dog") get stored in different drawers each time. At first, this might
seem like an error--but it's actually an expected behavior. In Python, the built-in hash() function is intentionally designed to produce different results ever time the program runs--which
I didn't know myself. I dug a tiny bit further into this and found out this is a security feature known as hash randomization. Essentially, it helps protect Python programs from certain type of
attacks but also means that the internal hash values are not consistent between sessions. Because I use the hash value to determine where to store a thought (using hash(thought) % drawer_count),
even though the same though is added every time, it might land in a different drawer on each run. For this project, I intentionally kept Python's built-in hash() per requirement--and this
behavior is part of how real-world hashing can work unpredictably depending on the language or environment. With that being said, initially this confused me because initially I thought
every thought was going to be set in an organized manner but then realized this was done by complete randomization--chaos always trips me up but a learning experience nonetheless.

Furthermore, to demonstrate that my implementation correctly handles collisions using chaining, I created a new BrainFilingSystem with only two drawers. This dramatically increases the chances
that multiple thoughts will be stored in the same drawer. When I printed the brain's content, I observed that multiple distinct thoughts were indeed chained together inside a single drawer--confirming
the success of my collision handling. This result can still be seen with 10 drawers as well but won't occur as often as it would within a two drawer system.
