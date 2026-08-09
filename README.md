# 🎓 Student Management System

A light, menu-driven Python application designed to handle student record management. It provides a simple command-line interface to perform CRUD (Create, Read, Update, Delete) operations with automatic JSON data persistence.

---

## 🚀 Features

* ➕ *Add Student:* Record new student profiles with a name, roll number, and marks.
* 📋 *View Records:* Display all currently registered students in a formatted list.
* 🔍 *Search Student:* Quick lookup by unique roll number.
* ✏️ *Update Student:* Edit existing student names or marks, with option to keep current values.
* 🗑️ *Delete Student:* Permanently remove student entries.
* 💾 *Data Persistence:* Automatically creates and updates students.json to keep data safe between program runs.

---

## 📁 File Structure

```text
├── main.py          # Handles user interactions and application logic
├── database.py      # Manages storage operations (if split)
└── students.json    # Created automatically to store student records
