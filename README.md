 
# 📚 Student Information Management System (SIMS)

## 📌 Project Overview

The **Student Information Management System (SIMS)** is a simple Python-based mini project that allows users to manage student records efficiently using a **JSON file** for data storage.

This system is designed for learning purposes and demonstrates basic concepts of:

* File handling
* JSON data storage
* CRUD operations
* Menu-driven programs

---

## 🚀 Features

* ➕ Add new student records
* 📄 View all students
* 🔍 Search students by name
* ✏️ Update student information
* ❌ Delete student records
* 💾 Persistent storage using JSON file

---

## 🛠️ Technologies Used

* **Programming Language:** Python 3
* **Data Storage:** JSON file (`students.json`)
* **Libraries Used:**

  * `json` (for data handling)
  * `os` (for file checking)

---

## 📂 Project Structure

```
SIMS/
│
├── src/main.py       # Main Python program
├── students.json     # Data storage file (auto-created)
└── README.md         # Project documentation
```

---

## ⚙️ How It Works

* The system stores student data in a **JSON file**.
* Each student record includes:

  * ID
  * Name
  * Age
  * Department
  * CGPA
* The program provides a **menu-driven interface** for user interaction.

---

## ▶️ How to Run the Project

1. Install Python (if not already installed)
2. Clone or download this project
3. Open terminal/command prompt
4. Navigate to the project folder
5. Run the program:

```bash
python sims.py
```

---

## 🧪 Example Menu

```
===== Student Information Management System =====
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
```

---

## 💡 Example JSON Data

```json
[
    {
        "id": 1,
        "name": "Abebe Alemayew",
        "age": "21",
        "department": "Computer Engineering",
        "cgpa": "3.8"
    }
]
```

---

## 📈 Future Improvements

This project can be extended with:

* GUI (Tkinter / PyQt)
* Database integration (MySQL, SQLite)
* User authentication (login system)
* Input validation
* Export data to Excel/CSV
* Web version using Flask/Django

---

## 🎯 Learning Objectives

This project helps you understand:

* Python file handling
* JSON data structures
* Building CLI applications
* Structuring small software projects

---
 
