import subprocess
from datetime import datetime

def main():
    # Define commit message
    commit_message, more, n = "Tap to view what changed!\n", "y", 0

    # Pulling the latest changes from the remote repository
    print("[🔄] Pulling the latest changes from the remote repository...")
    pulling_cmd = subprocess.Popen("git pull origin main", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    pulling_cmd.communicate()

    # Add notes
    while more == "yes" or more == "y":
        note = input("[✏️] Enter your note: ")
        current_time = datetime.now().strftime("%d/%m/%Y %H:%M")
        with open("README.md", "a") as outfile:
            outfile.write(f"- {note} ~ `{current_time}`\n")
        print("[💾] Your note has been added.")
        n += 1
        commit_message += f"{n}. {note}\n"
        more = input("[❓] Do you want to add another note? (y/n): ").lower()
    print("[🚀] Waiting for Git to save your notes...")

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

    # Get the remote URL
    get_remote_url = subprocess.Popen("git remote get-url origin", shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    stdout, stderr = get_remote_url.communicate()
    if get_remote_url.returncode == 0:
        remote_url = stdout.decode("utf-8").strip()
        hyperlink = "\033]8;;{url}\033\\{text}\033]8;;\033\\".format(url=remote_url, text="repository")
        print(f"[✅] Your notes have been saved to your {hyperlink}.")
    else:
        print("[❌] An error occurred while getting the remote URL.")

if __name__ == '__main__':
    main()