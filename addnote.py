import subprocess
from datetime import datetime

def main():
    # Define commit message
    commit_message = "👉 Tap to View\n"
    more, n = "yes", 0

    # Pulling the latest changes from the remote repository
    print("(🔄) Pulling the latest changes from the remote repository...")
    pulling_cmd = subprocess.Popen("git pull origin main", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    pulling_cmd.communicate()

    # Add notes
    while more == "yes" or more == "y":
        note = input("(✏️) Enter your note: ")
        current_time = datetime.now().strftime("%d/%m/%Y %H:%M")
        with open("README.md", "a") as outfile:
            outfile.write(f"- {note} ~ `{current_time}`\n")
        print("(⭐) Note added.")
        n += 1
        commit_message += f"{n}. {note}\n"
        more = input("(❓) Do you want to add another note? (y/n): ").lower()
    print("(🚀) Waiting for Git to save your notes...")

    # Write the commit message to a temporary file
    with open("commit_message.txt", "w", encoding="utf-8") as commit_file:
        commit_file.write(commit_message)

    # Define the Git commands
    commands = [
        'git add README.md',
        'git commit -F commit_message.txt',
        'git push origin main'
    ]

    # Run the Git commands
    for command in commands:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        process.communicate()
    
    # Reset temporary files to empty
    with open("commit_message.txt", "w") as commit_file:
        commit_file.write("")
    
    # Print success message
    print("(✅) Your notes have been added successfully!")

if __name__ == '__main__':
    main()