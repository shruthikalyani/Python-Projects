"""
Alarm Clock — a small Tkinter desktop app.
 
Shows a live clock and date, and lets the user set (or cancel) a
one-shot alarm in 24-hour HH:MM format.
"""
 
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
 
# ---------------------------------------------------------------------------
# Theme
# ---------------------------------------------------------------------------
 
COLORS = {
    "bg": "#0f172a",
    "card": "#1e293b",
    "card_border": "#334155",
    "title": "#e879f9",
    "subtitle": "#94a3b8",
    "time": "#a78bfa",
    "date": "#cbd5e1",
    "label": "#ffffff",
    "placeholder": "#64748b",
    "input_text": "#ffffff",
    "primary": "#8b5cf6",
    "primary_hover": "#a855f7",
    "secondary": "#334155",
    "secondary_hover": "#475569",
    "success": "#4ade80",
    "muted": "#64748b",
}
 
FONT = "Helvetica"
PLACEHOLDER = "HH:MM"
WINDOW_SIZE = (420, 660)
 
 
class AlarmClockApp:
    """A live clock with a simple one-shot alarm."""
 
    def __init__(self, root: tk.Tk):
        self.root = root
        self.alarm_time = tk.StringVar()
        self.alarm_active = False
 
        self._configure_window()
        self._build_ui()
        self._center_window()
        self.update_clock()
 
    # ---- setup ---------------------------------------------------------
 
    def _configure_window(self):
        self.root.title("⏰ Alarm Clock")
        self.root.resizable(False, False)
        self.root.configure(bg=COLORS["bg"])
 
    def _center_window(self):
        self.root.update_idletasks()
        w, h = WINDOW_SIZE
        x = (self.root.winfo_screenwidth() - w) // 2
        y = (self.root.winfo_screenheight() - h) // 2
        self.root.geometry(f"{w}x{h}+{x}+{y}")
 
    def _build_ui(self):
        tk.Label(
            self.root, text="⏰ Alarm Clock", font=(FONT, 28, "bold"),
            bg=COLORS["bg"], fg=COLORS["title"],
        ).pack(pady=(36, 6))
 
        tk.Label(
            self.root, text="Never miss an important moment ♥", font=(FONT, 12),
            bg=COLORS["bg"], fg=COLORS["subtitle"],
        ).pack()
 
        self.time_label = tk.Label(
            self.root, text="--:--:-- --", font=(FONT, 42, "bold"),
            bg=COLORS["bg"], fg=COLORS["time"],
        )
        self.time_label.pack(pady=(44, 4))
 
        self.date_label = tk.Label(
            self.root, text="", font=(FONT, 14),
            bg=COLORS["bg"], fg=COLORS["date"],
        )
        self.date_label.pack()
 
        card = tk.Frame(
            self.root, bg=COLORS["card"],
            highlightthickness=1, highlightbackground=COLORS["card_border"],
        )
        card.pack(pady=(40, 0), padx=36, fill="x")
 
        tk.Label(
            card, text="SET ALARM  ·  24-HOUR FORMAT", font=(FONT, 11, "bold"),
            bg=COLORS["card"], fg=COLORS["label"],
        ).pack(pady=(20, 12))
 
        self.alarm_entry = tk.Entry(
            card, font=(FONT, 20), justify="center",
            bg="#0f172a", fg=COLORS["placeholder"],
            insertbackground="white", relief="flat",
        )
        self.alarm_entry.pack(padx=24, fill="x", ipady=10)
        self.alarm_entry.insert(0, PLACEHOLDER)
        self.alarm_entry.bind("<FocusIn>", self._clear_placeholder)
        self.alarm_entry.bind("<FocusOut>", self._restore_placeholder)
        self.alarm_entry.bind("<Return>", lambda _e: self.set_alarm())
 
        vcmd = (self.root.register(self._validate_entry), "%P")
        self.alarm_entry.config(validate="key", validatecommand=vcmd)
 
        button_row = tk.Frame(card, bg=COLORS["card"])
        button_row.pack(pady=18, padx=24, fill="x")
 
        self.set_button = tk.Button(
            button_row, text="🔔 Set", font=(FONT, 13, "bold"),
            bg=COLORS["primary"], fg="white",
            activebackground=COLORS["primary_hover"], activeforeground="white",
            relief="flat", cursor="hand2", command=self.set_alarm,
        )
        self.set_button.pack(side="left", expand=True, fill="x", ipady=9, padx=(0, 6))
        self._add_hover(self.set_button, COLORS["primary"], COLORS["primary_hover"])
 
        self.cancel_button = tk.Button(
            button_row, text="✕ Cancel", font=(FONT, 13, "bold"),
            bg=COLORS["secondary"], fg="white",
            activebackground=COLORS["secondary_hover"], activeforeground="white",
            relief="flat", cursor="hand2", command=self.cancel_alarm,
        )
        self.cancel_button.pack(side="left", expand=True, fill="x", ipady=9, padx=(6, 0))
        self._add_hover(self.cancel_button, COLORS["secondary"], COLORS["secondary_hover"])
 
        self.status_label = tk.Label(
            card, text="No alarm set", font=(FONT, 12),
            bg=COLORS["card"], fg=COLORS["muted"],
        )
        self.status_label.pack(pady=(0, 20))
 
        tk.Label(
            self.root, text="Made with ♥ using Python & Tkinter", font=(FONT, 10),
            bg=COLORS["bg"], fg=COLORS["muted"],
        ).pack(side="bottom", pady=20)
 
    # ---- placeholder / validation helpers ------------------------------
 
    def _clear_placeholder(self, _event=None):
        if self.alarm_entry.get() == PLACEHOLDER:
            self.alarm_entry.delete(0, tk.END)
            self.alarm_entry.config(fg=COLORS["input_text"])
 
    def _restore_placeholder(self, _event=None):
        if not self.alarm_entry.get().strip():
            self.alarm_entry.insert(0, PLACEHOLDER)
            self.alarm_entry.config(fg=COLORS["placeholder"])
 
    def _validate_entry(self, proposed: str) -> bool:
        # Allow only digits/colon while typing; real format check happens
        # on submit via datetime.strptime.
        if proposed == "":
            return True
        if len(proposed) > 5:
            return False
        return all(ch.isdigit() or ch == ":" for ch in proposed)
 
    def _add_hover(self, widget, normal, hover):
        widget.bind("<Enter>", lambda _e: widget.config(bg=hover))
        widget.bind("<Leave>", lambda _e: widget.config(bg=normal))
 
    # ---- alarm logic -----------------------------------------------------
 
    def set_alarm(self):
        value = self.alarm_entry.get().strip()
        if not value or value == PLACEHOLDER:
            messagebox.showerror("No Time Entered", "Please enter a time first, e.g. 07:30.")
            return
 
        try:
            datetime.strptime(value, "%H:%M")
        except ValueError:
            messagebox.showerror(
                "Invalid Time",
                "Please enter the time in 24-hour HH:MM format,\ne.g. 07:30 or 18:45.",
            )
            return
 
        self.alarm_time.set(value)
        self.alarm_active = True
        self.status_label.config(text=f"✓ Alarm set for {value}", fg=COLORS["success"])
 
        self.alarm_entry.delete(0, tk.END)
        self._restore_placeholder()
 
    def cancel_alarm(self):
        self.alarm_active = False
        self.alarm_time.set("")
        self.status_label.config(text="No alarm set", fg=COLORS["muted"])
 
    def update_clock(self):
        # Reschedule immediately so the clock keeps ticking even while a
        # modal alarm dialog is open (previously the display froze until
        # the popup was dismissed).
        self.root.after(1000, self.update_clock)
 
        now = datetime.now()
        self.time_label.config(text=now.strftime("%I:%M:%S %p"))
        self.date_label.config(text=now.strftime("%A, %d %B %Y"))
 
        if self.alarm_active and self.alarm_time.get() == now.strftime("%H:%M"):
            self._ring_alarm()
 
    def _ring_alarm(self):
        self.alarm_active = False
        self.alarm_time.set("")
        self.status_label.config(text="No alarm set", fg=COLORS["muted"])
        self.root.bell()
        messagebox.showinfo("⏰ Wake Up!", "It's time! Your alarm is ringing! 🎉")
 
 
if __name__ == "__main__":
    root = tk.Tk()
    app = AlarmClockApp(root)
    root.mainloop()
 