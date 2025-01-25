import subprocess

def main():
    # Define commit message
    commit_message = "👉 Tap to View\n"
    more, n = "yes", 0
    while more == "yes" or more == "y":
        note = input("(?) Enter your note: ")
        with open("README.md", "a") as outfile:
            outfile.write("- " + note + "\n")
        print("(+) Note added.")
        n += 1
        commit_message += f"{n}. {note}\n"
        more = input("(?) Do you want to add another note? (yes/no): ").lower()
    print("(*) Waiting for Git commands to execute...")

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
        stdout, stderr = process.communicate()
    
    # Reset temporary files to empty
    with open("commit_message.txt", "w") as commit_file:
        commit_file.write("")
    
    # Print success message
    print("\n(!) Notes have been saved and added to README.md")

if __name__ == '__main__':
    main()