import os
import json

# This is the file where we will save your projects
DATA_FILE = "projects.json"

# This is the text for the shame letter. 
SHAME_LETTER_PROMPT = """
I am ashamed that even I started this project I am incapable of finishing it. 
even though humans can do anything if they really want to...
(Type the rest of your letter below. Be honest. It must be at least 500 characters long to count.)
"""

def load_projects():
    """Loads the list of projects from the file. If the file doesn't exist, returns an empty list."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

def save_projects(projects):
    """Saves the current list of projects to the file."""
    with open(DATA_FILE, "w") as file:
        json.dump(projects, file, indent=4)

def add_project(projects):
    """Asks the user for a new project and adds it to the list."""
    new_project = input("What new project have you started today? ")
    projects.append({"name": new_project, "status": "In Progress"})
    save_projects(projects)
    print(f"Added '{new_project}' to your list. Don't quit this one!")

def shame_and_remove(projects):
    """Shows the list, asks which to remove, and forces a shame letter."""
    if not projects:
        print("You have no projects to remove. Start something first!")
        return

    print("\n--- Your Unfinished Business ---")
    for index, project in enumerate(projects):
        print(f"{index + 1}. {project['name']}")

    try:
        choice = int(input("\nEnter the number of the project you want to remove: ")) - 1
        if 0 <= choice < len(projects):
            project_to_remove = projects[choice]['name']
            print(f"\nYou are trying to remove: '{project_to_remove}'")
            print("\nThis is shameful to leave a project undone. Therefore, you have to write a shame letter.")
            print(SHAME_LETTER_PROMPT)
            
            shame_text = input("> ")
            
            if len(shame_text) < 500:
                print(f"\nYour letter is only {len(shame_text)} characters long. That's not a page. Try again.")
            else:
                print("\n...You have shamed yourself. The project has been removed.")
                projects.pop(choice)
                save_projects(projects)
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """The main loop of the program."""
    print("Welcome to Unfinished Business.")
    projects = load_projects()

    while True:
        # Display the current list of projects
        print("\n--- Your Current Unfinished Business ---")
        if not projects:
            print("(Your list is empty. Shameful. Start something!)")
        else:
            for index, project in enumerate(projects):
                print(f"{index + 1}. {project['name']}")

        print("\n--- Main Menu ---")
        print("1. Add a new project")
        print("2. Review/Remove a project (Shame Letter required)")
        print("3. Exit")
        
        choice = input("What do you want to do? ")

        if choice == "1":
            add_project(projects)
        elif choice == "2":
            shame_and_remove(projects)
        elif choice == "3":
            print("Go finish your projects.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
