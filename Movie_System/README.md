# 🎬 Movie Recommendation System

Welcome to the **Movie Recommendation System**! This Python project allows you to explore a directory of movie data files, load the data into memory, and interact with it using a menu-driven system. The program features an intuitive interface, autocomplete search, and recommendations based on a **Deque (Double-Ended Queue)** data structure.

---

## ✨ Features

- **📂 Recursive Directory Traversal:** Scan a directory and load movie data from `.txt` files.
- **🍿 Movie Recommendations:** Recommend movies based on **a Deque (Double-Ended Queue) data structure.**.
- **🔍 Autocomplete Search:** Search for movies by title with autocomplete suggestions.
- **🏆 Top 3 Movies:** Recommend the top 3 movies by rating, with the option to view the next 3.

---

## 🛠️ Prerequisites

Before running the program, ensure you have the following installed:

- **Python 3.8 or higher**
- **Git** (optional, for cloning the repository)

---

## 🚀 Setup Instructions

Follow these steps to set up and run the project on your local machine.

### 1. Clone the Repository

If you have Git installed, clone the repository to your local machine:

```bash
git clone 
cd Movie_System
```

If you don't have Git, you can download the repository as a ZIP file and extract it.

---

### 2. Set Up a Virtual Environment

To isolate the project's dependencies, create and activate a virtual environment.

#### 🪟 On Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### 🍎 On macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

Once activated, your terminal prompt will show `(venv)` at the beginning.

---

### 3. Install Dependencies

Install the required Python packages using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

---

### 4. Run the Program

Start the Movie Recommendation System by running the `main.py` file:

```bash
python main.py
```

---

## 🎮 Usage

Once the program starts, follow the on-screen instructions:

1. **📁 Enter the Directory Path:**
   - Provide the path to the directory containing your movie data files (e.g., `Movie_List`).

2. **📋 Main Menu:**
   - Choose from the following options:
     - **1. List all movies:** Display all loaded movies.
     - **2. Recommend a movie:** Get a movie recommendation based on FIFO rules.
     - **3. Search for a movie by title:** Search for a movie with autocomplete suggestions.
     - **4. Recommend Top 3 movies by rating:** View the top 3 movies, with the option to see the next 3.
     - **5. Exit:** Exit the program.

---

## 🗂️ Project Structure

The project directory is organized as follows:

```bash
Movie_System/
├── venv/                   # Virtual environment (ignored by Git)
├── main.py                 # Main program
├── movie.py                # Movie class
├── deque.py                # Deque implementation
├── requirements.txt        # Dependencies file
├── README.md               # This file
├── .gitignore              # Git ignore file
└── Movie_List/             # Folder containing movie data files
```

---

## 📝 Example Movie Data Format

Each movie data file (e.g., `avatar.txt`) should have the following format:

```bash
Title: Avatar
Year: 2009
Genre: Science Fiction
Rating: 7.8
```

---

## 🤝 Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Please ensure your code follows the project's style and includes appropriate documentation.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **pyfiglet:** For creating the ASCII art title banner.
- **Python Standard Library:** For providing the tools to build this project.
- **Visual Studio Code:** For providing the IDE environment to develop this program
- **Notepad++:** For assisting in developing the Movie_System program

---

Enjoy exploring the Movie Recommendation System! 🎥🍿

---
