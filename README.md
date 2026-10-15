# Unfinished-Business 

A Python command-line tool designed to stop me from abandoning my projects. 

It tracks my unfinished business (books, gym plans, skills) and forces me to write a page-long letter of shame before I'm allowed to delete a project from the list. 

### Current Status
- [x] Version 1.0: Command-line interface with file storage and the "Shame Letter" feature.
- [ ] Version 2.0: Random desktop notifications.
- [ ] Version 3.0: Detect when the screen is on and trigger reminders.

### How to Run It

You need Python 3 installed on your machine.

1. Clone this repository or download the `Unfinished-Business.py` file.
2. Open your terminal in the folder containing the file.
3. Run the following command:

```
 python3 Unfinished-Business.py
```

### How It Works

- The app starts by showing you a list of all your unfinished projects.
- You can add new projects, review existing ones, or mark a project as finished from the main menu.
- **The Shame Letter:** If you try to *remove* an abandoned project, the app will force you to write a 500-character letter of shame first. This is a feature, not a bug.
- **The Celebration:** If you *finish* a project, the app will congratulate you. Because finishing things matters.

### Built With

- Python 3
- Standard library only (`json`, `os`)
