# ✨ To-Do List.exe

> because apparently my brain needed a GUI to remember what it was supposed to do.

A tiny, slightly dramatic, ✨ aesthetic ✨ To-Do List built with Python + Tkinter.

No fancy frameworks.
No database.
Just Python, buttons, and questionable amounts of purple.

---

## 🧠 What does this thing do?

```python
if task == "important":
    add_task()

elif task == "done":
    sparkle()

elif task == "oops":
    delete_task()
Basically:

✍️ Type a task
       ↓
➕ Add it
       ↓
📋 See it
       ↓
✓ Finish it
       ↓
✨ GET SPARKLES
🎨 The vibe

┌─────────────────────────────────────┐
│                                     │
│       GOOD EVENING ✨               │
│       Let's get things done.        │
│                                     │
│  ┌───────────────────────────────┐  │
│  │ What needs to be done?      + │  │
│  └───────────────────────────────┘  │
│                                     │
│  ○ Finish Python project          × │
│  ○ Study                           × │
│  ✓ Touch grass                   ✨ │
│                                     │
└─────────────────────────────────────┘
✨ Features

features = [
    "➕ Add tasks",
    "↵ Press Enter to add",
    "✓ Complete tasks",
    "✨ Sparkle when completed",
    "× Delete tasks",
    "🌙 Dark mode",
    "🎨 Custom UI"
]
🛠️ Built with

import tkinter
import random
That’s it.

Well…

A lot more code happened after that.

🧩 How it works

The app is basically a tiny ecosystem:

                 ┌──────────────┐
                 │    WINDOW    │
                 └──────┬───────┘
                        │
          ┌─────────────┴─────────────┐
          ↓                           ↓
     INPUT AREA                   TASK AREA
          │                           │
          ↓                           ↓
      add_task()              ┌─────────────┐
          │                    │  Task Card  │
          │                    └──────┬──────┘
          │                           │
          │                    ┌──────┴──────┐
          │                    ↓             ↓
          │               Complete        Delete
          │                    │
          │                    ↓
          │             sparkle_effect()
          │                    │
          └────────────────────┤
                               ↓
                              ✨
🚀 Run it

Clone the repository:

git clone YOUR_REPOSITORY_LINK
Enter the folder:

cd To-Do-List
Run:

python todo_gui.py
And boom.

You now have a To-Do List.

Hopefully you actually use it.

📁 Files

To-Do-List/
│
├── 🐍 todo_gui.py
│
└── 📖 README.md
🧠 Things I learned

things_i_learned = {
    "GUI": "Tkinter",
    "layout": "Frames + pack()",
    "interaction": "Button commands",
    "input": "Entry widgets",
    "events": "bind()",
    "functions": "def",
    "animation": "Canvas + after()",
    "sparkles": "random ✨"
}
The biggest thing I learned?

A program becomes a lot more interesting when you stop thinking
about individual lines and start thinking about how they interact.

✨ The Sparkle™

When a task is completed:

○  Finish project

        ↓ click

✓ ̶F̶i̶n̶i̶s̶h̶ ̶p̶r̶o̶j̶e̶c̶t̶

       ✦  ·  ✧
    ⋆    ✨    ⋆
       ·  ✦
The sparkles are generated using Tkinter’s Canvas
and random positions.

Because checking off a task deserves a tiny celebration.

🔮 What’s next?

CURRENT
   │
   ├── ✓ Add tasks
   ├── ✓ Complete tasks
   ├── ✓ Delete tasks
   └── ✓ Sparkle effect
          │
          ↓
COMING SOON
   │
   ├── ☐ Save tasks
   ├── ☐ Due dates
   ├── ☐ Categories
   ├── ☐ Progress bar
   ├── ☐ Task editing
   └── ☐ Even more ✨
🏆 Project #04

This is Project #04 in my journey of learning Python
by actually building things.

01  Hello World             ✓
02  Simple Calculator       ✓
03  Number Guessing Game   ✓
04  To-Do List             ← YOU ARE HERE
05  Alarm Clock             → next
The goal:

Python
   ↓
AI
   ↓
Computer Vision
   ↓
Robotics
   ↓
????
Let’s see where this goes.

👩‍💻 Made by Shruthi

Built with Python, curiosity,
and probably too much time spent choosing purple.

One project at a time. 🚀