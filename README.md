# Notes Management - Powered by GitHub

---

## Introduction

Welcome to the Notes Management - Powered by **GitHub** ! This simple yet powerful script allows you to seamlessly add notes to your `README.md` file and automatically commit and push those changes to your GitHub repository. Say goodbye to manual note-taking and version control hassles!

## How to Use

### 0. **Setup Repository**:

- Clone this repository to your local machine using the following command:
  ```bash
  git clone https://github.com/ngtrng/notes-management.git
  ```
- Navigate to the project directory:
  ```bash
    cd notes-management
  ```

### 1. **Run the Script**:

- Execute the script using Python: `python addnote.py`.

### 2. **Enter Your Note**:

- You will be prompted to enter your note: `(✏️) Enter your note:`.
- Type your note and press Enter.

### 3. **Confirmation**:

- After adding the note, you'll see a confirmation message: `(⭐) Note added.`.
- The script will ask if you want to add another note: `(❓) Do you want to add another note? (y/n):`.
- Enter `yes` or `y` to add another note, or `no` or `n` to finish.

### 4. **Automatic Git Operations**:

- Once you finish adding notes, the script will automatically:
- Add the `README.md` file to the Git staging area.
- Commit the changes with a commit message listing all the added notes.
- Push the changes to the `main` branch of your GitHub repository.

### 5. **Success Message**:

- After the Git operations are completed, you'll see a success message: `(✅) Your notes have been added successfully!`.

### Example:

```bash
python addnote.py
(🔄) Pulling the latest changes from the remote repository...
(✏️) Enter your note: Complete the project documentation.
(⭐) Note added.
(❓) Do you want to add another note? (y/n): y
(✏️) Enter your note: Schedule the team meeting.
(⭐) Note added.
(❓) Do you want to add another note? (y/n): n
(🚀) Waiting for Git to save your notes...
(✅) Your notes have been added successfully!
```

---

### **Notes**
