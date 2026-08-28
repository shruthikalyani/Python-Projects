import tkinter as tk
import random

# COLORS


BG = "#0F1117"
CARD = "#181B24"
TEXT = "#F5F5F5"
MUTED = "#8B91A1"
ACCENT = "#A78BFA"
SUCCESS = "#C084FC"



# WINDOW


window = tk.Tk()
window.title("Tasks")
window.geometry("520x650")
window.configure(bg=BG)



# HEADER


header = tk.Frame(window, bg=BG)
header.pack(fill="x", padx=35, pady=(35, 10))

greeting = tk.Label(
header,
text="GOOD EVENING ✨",
font=("Arial", 11, "bold"),
fg=ACCENT,
bg=BG
)
greeting.pack(anchor="w")

title = tk.Label(
header,
text="Let's get things done.",
font=("Arial", 26, "bold"),
fg=TEXT,
bg=BG
)
title.pack(anchor="w", pady=(5, 0))

subtitle = tk.Label(
header,
text="Small steps. Big progress.",
font=("Arial", 12),
fg=MUTED,
bg=BG
)
subtitle.pack(anchor="w", pady=(4, 0))



# INPUT CARD

input_card = tk.Frame(
window,
bg=CARD
)
input_card.pack(
fill="x",
padx=35,
pady=25
)

task_entry = tk.Entry(
input_card,
font=("Arial", 14),
bg=CARD,
fg=TEXT,
insertbackground=TEXT,
bd=0
)

task_entry.pack(
side="left",
fill="x",
expand=True,
padx=18,
pady=18
)

# TASK AREA


task_area = tk.Frame(
window,
bg=BG
)

task_area.pack(
fill="both",
expand=True,
padx=35
)


# SPARKLE EFFECT


def sparkle_effect(card):
    """
    Creates a small burst of sparkles on the completed task.
    """

    sparkle_canvas = tk.Canvas(
        card,
        bg=CARD,
        highlightthickness=0
    )

    sparkle_canvas.place(
        relx=0,
        rely=0,
        relwidth=1,
        relheight=1
    )

    sparkles = []

    
    for _ in range(18):

        x = random.randint(80, 420)
        y = random.randint(10, 50)

        size = random.choice([2, 3, 4])

        sparkle = sparkle_canvas.create_text(
            x,
            y,
            text=random.choice(["✦", "✧", "·", "⋆"]),
            fill=random.choice([
                "#A78BFA",
                "#C084FC",
                "#E9D5FF",
                "#FFFFFF"
            ]),
            font=("Arial", size + 7, "bold")
        )

        dx = random.uniform(-2, 2)
        dy = random.uniform(-1.5, -0.3)

        sparkles.append(
            (sparkle, dx, dy)
        )

    def animate(step=0):

        if step >= 20:
            sparkle_canvas.destroy()
            return

        for sparkle, dx, dy in sparkles:

            sparkle_canvas.move(
                sparkle,
                dx,
                dy
            )

        window.after(
            40,
            lambda: animate(step + 1)
        )

    animate()


# COMPLETE TASK


def complete_task(card, checkbox, label):

    # Change checkbox

    checkbox.config(
        text="✓",
        fg=TEXT,
        bg=ACCENT
    )

    # Cross out task
    label.config(
        fg=MUTED,
        font=("Arial", 13, "overstrike")
    )

    
    sparkle_effect(card)



# ADD TASK


def add_task():

    task = task_entry.get().strip()

    if task == "":
        return

    # Task card
    task_card = tk.Frame(
        task_area,
        bg=CARD,
        height=65
    )

    task_card.pack(
        fill="x",
        pady=6
    )

    task_card.pack_propagate(False)

  
    checkbox = tk.Button(
        task_card,
        text="○",
        font=("Arial", 20),
        fg=ACCENT,
        bg=CARD,
        activebackground=CARD,
        activeforeground=ACCENT,
        bd=0,
        relief="flat"
    )

    checkbox.pack(
        side="left",
        padx=(12, 8)
    )

    # Task text
    task_label = tk.Label(
        task_card,
        text=task,
        font=("Arial", 13),
        fg=TEXT,
        bg=CARD
    )

    task_label.pack(
        side="left",
        fill="x",
        expand=True,
        anchor="w"
    )

    # Delete button
    delete_button = tk.Button(
        task_card,
        text="×",
        font=("Arial", 18),
        fg=MUTED,
        bg=CARD,
        activebackground=CARD,
        activeforeground=TEXT,
        bd=0,
        relief="flat",
        command=task_card.destroy
    )

    delete_button.pack(
        side="right",
        padx=15
    )

    # Connect checkbox to completion
    checkbox.config(
        command=lambda: complete_task(
            task_card,
            checkbox,
            task_label
        )
    )

    # Clear input
    task_entry.delete(
        0,
        tk.END
    )



# ADD BUTTON


add_button = tk.Button(
input_card,
text="+",
font=("Arial", 20, "bold"),
fg=TEXT,
bg=ACCENT,
activebackground="#B69AF5",
activeforeground=TEXT,
bd=0,
width=3,
command=add_task
)

add_button.pack(
side="right",
padx=8,
pady=8
)



# ENTER KEY


task_entry.bind(
"<Return>",
lambda event: add_task()
)


# =========================================================
# START APP
# =========================================================

window.mainloop()