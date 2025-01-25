# Notes Management - Powered by GitHub

---

## Introduction

Welcome to the Notes Management - Powered by **GitHub** ! This simple yet powerful script allows you to seamlessly add notes to your `README.md` file and automatically commit and push those changes to your GitHub repository. Say goodbye to manual note-taking and version control hassles! _Jump to your notes list by clicking **[here](#notes)**._

## How to Use

### 0. **Setup Repository**:

- Click on the `Use this template` button to create a new repository from this template.
- Clone the repository you created to your local machine using Git.
- Navigate to the repository directory in your terminal.

### 1. **Run the Script**:

- Execute the script using Python: `python addnote.py`.

### 2. **Enter Your Note**:

- You will be prompted to enter your note: `[✏️] Enter your note:`.
- Type your note and press Enter.

### 3. **Confirmation**:

- After adding the note, you'll see a confirmation message: `[⭐] Note added.`.
- The script will ask if you want to add another note: `[❓] Do you want to add another note? (y/n):`.
- Enter `yes` or `y` to add another note, or `no` or `n` to finish.

### 4. **Automatic Git Operations**:

- Once you finish adding notes, the script will automatically:
- Add the `README.md` file to the Git staging area.
- Commit the changes with a commit message listing all the added notes.
- Push the changes to the `main` branch of your GitHub repository.

### 5. **Success Message**:

- After the Git operations are completed, you'll see a success message: `[✅] Your notes have been added successfully!`.

### Example:

```
python addnote.py
[🔄] Pulling the latest changes from the remote repository...
[✏️] Enter your note: Complete the project documentation.
[⭐] Note added.
[❓] Do you want to add another note? (y/n): y
[✏️] Enter your note: Schedule the team meeting.
[⭐] Note added.
[❓] Do you want to add another note? (y/n): n
[🚀] Waiting for Git to save your notes...
[✅] Your notes have been added successfully!
```

---

## **Notes**
- First day on Python. It is a bit hard, but I'm gonna learn this quick! ~ `25/01/2025 20:53`
- Moving to something new, soon. ~ `25/01/2025 21:12`
- I'm gonna sleep, next day I'll make a showcase video. ~ `25/01/2025 21:21`
