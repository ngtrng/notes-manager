import subprocess

def main():
    # Define commit message
    commit_message = "These notes have been added:\n"

    print("This program adds notes to README.md file.")
    more, n = "yes", 0
    while more == "yes" or more == "y":
        note = input("Enter a note: ")
        with open("README.md", "a") as outfile:
            outfile.write("- " + note + "\n")
        print("Note added.")
        n += 1
        commit_message += f"{n}. {note}\n"
        more = input("Do you want to add another note? (yes/no): ").lower()
    print("Notes have been written to README.md")

    # Write the commit message to a temporary file
    with open("commit_message.txt", "w") as commit_file:
        commit_file.write(commit_message)

    # Define the Git commands
    commands = [
        'git add README.md',
        'git commit -F commit_message.txt',
        'git push origin main'
    ]

    # Run the Git commands
    for command in commands:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        print(stdout.decode('utf-8'))
        if stderr:
            print(stderr.decode('utf-8'))

if __name__ == '__main__':
    main()