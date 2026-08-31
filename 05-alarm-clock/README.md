⏰ Alarm Clock

A small desktop alarm clock built with Python's built-in Tkinter GUI toolkit. Shows a live clock and date, and lets you set a one-shot alarm that pops up a notification when it goes off.

Features
Live time (12-hour, with AM/PM) and date display, updated every second
Set a one-shot alarm in 24-hour HH:MM format
Cancel a pending alarm at any time
Input validation — rejects invalid times with a clear error message
Placeholder text and Enter-to-submit on the time field
Dark, card-style UI with hover effects on buttons
Requirements
Python 3.7+
Tkinter (bundled with most Python installs)
Windows / macOS: included by default.
Linux (Debian/Ubuntu): if import tkinter fails, install it with:
bash
    sudo apt install python3-tk

No third-party packages are required.

Usage
bash
python3 alarm_clock.py
Type a time in 24-hour format (e.g. 07:30 or 18:45) in the input box.
Click 🔔 Set (or press Enter) to arm the alarm.
Click ✕ Cancel at any time to clear it.
When the alarm time is reached, a popup and a system beep will notify you.
Project Structure
.
├── alarm_clock.py   # Application entry point
├── README.md
└── .gitignore
License

Feel free to use, modify, and share this project for any purpose.