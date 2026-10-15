import os
import json

DATA_FILE = "projects.json"

SHAME_LETTER_PROMPT = """
I am ashamed that even I started this project I am incapable of finishing it. 
even though humans can do anything if they really want to...
(Type the rest of your letter below. Be honest. It must be at least 500 characters long to count.)
"""

def load_data():
    """Loads both unfinished and finished projects. Returns them as a dictionary."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            # Handle the old format (just a list) by upgrading it
            if isinstance(data, list):
                return {"unfinished": data, "finished": []}
            return data
    return {"unfinished": [], "finished": []}

def save_data(data):
    """Saves both lists to the file."""
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def add_project(data):
    """Asks the user for a new project and adds it to the unfinished list."""
    new_project = input("What new project have you started today? ")
    data["unfinished"].append({"name": new_project, "status": "In Progress"})
    save_data(data)
    print(f"Added '{new_project}' to your list. Don't quit this one!")

def shame_and_remove(data):
    """Removes a project but forces a shame letter first."""
    unfinished = data["unfinished"]
    if not unfinished:
        print("You have no projects to remove. Start something first!")
        return

    print("\n--- Your Unfinished Business ---")
    for index, project in enumerate(unfinished):
        print(f"{index + 1}. {project['name']}")

    try:
        choice = int(input("\nEnter the number of the project you want to remove: ")) - 1
        if 0 <= choice < len(unfinished):
            project_to_remove = unfinished[choice]['name']
            print(f"\nYou are trying to remove: '{project_to_remove}'")
            print("\nThis is shameful to leave a project undone. Therefore, you have to write a shame letter.")
            print(SHAME_LETTER_PROMPT)
            
            shame_text = input("> ")
            
            if len(shame_text) < 500:
                print(f"\nYour letter is only {len(shame_text)} characters long. That's not a page. Try again.")
            else:
                print("\n...You have shamed yourself. The project has been removed.")
                unfinished.pop(choice)
                save_data(data)
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def complete_project(data):
    """Moves a project to the finished list and congratulates the user."""
    unfinished = data["unfinished"]
    if not unfinished:
        print("You have no projects to complete. Start something first!")
        return

    print("\n--- Your Unfinished Business ---")
    for index, project in enumerate(unfinished):
        print(f"{index + 1}. {project['name']}")

    try:
        choice = int(input("\nWhich project did you finally finish? ")) - 1
        if 0 <= choice < len(unfinished):
            finished_project = unfinished[choice]['name']
            print(f"\n🎉 You finished: '{finished_project}'! 🎉")
            print("\nThe world you see today is made by some dedicated and")
            print("determined souls like you. Finishing a project is a brick")
            print("laid perfectly in the castle of your dreams.")
            print("\nWell done. Truly.")
            
            # Move it from unfinished to finished (don't delete it!)
            data["finished"].append({"name": finished_project})
            unfinished.pop(choice)
            save_data(data)
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """The main loop of the program."""
    print("Welcome to Unfinished Business.")
    data = load_data()

    while True:
        # Display the current list of projects
        unfinished_count = len(data["unfinished"])
        finished_count = len(data["finished"])
        
        print(f"\n--- Your Current Unfinished Business ({unfinished_count} projects) ---")
        if not data["unfinished"]:
            print("(Your list is empty. Shameful. Start something!)")
        else:
            for index, project in enumerate(data["unfinished"]):
                print(f"{index + 1}. {project['name']}")

        # Display the proud/firm message based on finished count
        print()
        if finished_count == 0:
            print("I see you couldn't manage to finish any projects yet.")
            print("Roll up your sleeves, get things done. I'm ready to celebrate")
            print("your success with you.")
        else:
            print(f"I proudly announce that you have finished {finished_count} successful")
            print("project(s) with us. So proud of you.")

        print("\n--- Main Menu ---")
        print("1. Add a new project")
        print("2. Review/Remove a project (Shame Letter required)")
        print("3. Mark a project as FINISHED (Celebration!)")
        print("4. Exit")
        
        choice = input("What do you want to do? ")

        if choice == "1":
            add_project(data)
        elif choice == "2":
            shame_and_remove(data)
        elif choice == "3":
            complete_project(data)
        elif choice == "4":
            print("Go finish your projects.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
