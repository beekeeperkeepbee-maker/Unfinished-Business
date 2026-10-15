# Unfinished-Business 

A Python command-line tool designed to stop me from abandoning my projects. 

It tracks my unfinished business (books, gym plans, skills) and forces me to write a page-long letter of shame before I'm allowed to delete a project from the list. 

### Current Status
- [x] Version 1.0: Command-line interface with file storage and the "Shame Letter" feature.
- [x] Version 1.1: Finished project tracking with proud/encouraging dashboard messages.
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

- The app opens with a dashboard showing your unfinished projects and a proud/encouraging message based on how many you've finished.
- **Add:** Start tracking a new project.
- **Finish:** Mark a project as complete — you'll be congratulated, and it moves to your finished list.
- **Delete:** Try to abandon a project, and the app forces you to write a 500-character letter of shame first. This is a feature, not a bug.
- **The Dashboard:** If you haven't finished anything yet, the app gives you a firm push. If you have, it proudly announces your success. Either way, it's watching.

### Built With

- Python 3
- Standard library only (`json`, `os`)
