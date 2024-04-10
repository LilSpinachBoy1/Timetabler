# Timetabler
The ultimate timetabling app! Idea is to create an app for distribution, which is actually practical and useful for A-Levels.

## Features
The app should have the following features...
1. The ability to create new timetables (stored as JSON files in a dedicated folder)
2. A feature to populate the timetables, such as asking the number of sessions and then prompting the user to enter the subject/activity, before saving the file
3. A feature to edit timetables
4. Timetable viewer, which presents the entire timetable in an easy to read format, while also presenting the relevant info for the current day
5. NOT IN V1: A timer feature (similar to that of the clock app) to provide a visual countdown on revision sessions

## File structure
Similar to Dom's NEA, menus can be run from seperate files, which will be in the `SCRIPTS` folder of the project.
Any images used or sprites will be in the `ASSETS` folder, along with fonts and any other files that need to be imported.
Notes or further code explanations that are too complex for comments will be stored in `Notes.txt`.
Timetables themselves will be stored in `TIMETABLES`, allowing for a directory to search through when looking for timetables.

Finally, the program's menu and any initial boot code will lie within `main.py` in the root directory.

## Development notes
The app will be developed with pygame, both as practice for the NEA and as it is a reliable and useful graphics library. Other libraries will likely be used, like the json library for storing timetables. The app can be packaged as an msi installer and distributed as such.
