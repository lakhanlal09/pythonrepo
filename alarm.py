import threading
import time
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
import winsound


class AlarmClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Clock")
        self.root.geometry("420x260")
        self.root.resizable(False, False)
        self.root.config(bg="#111827")

        self.alarm_time = tk.StringVar(value="07:00")
        self.current_time = tk.StringVar()
        self.status_text = tk.StringVar(value="Alarm not set")
        self.alarm_on = False
        self.ringing = False
        self.stop_ringing = False

        title = tk.Label(
            root,
            text="Alarm Clock",
            font=("Arial", 28, "bold"),
            fg="white",
            bg="#111827",
        )
        title.pack(pady=(20, 10))

        time_label = tk.Label(
            root,
            textvariable=self.current_time,
            font=("Arial", 42, "bold"),
            fg="#38bdf8",
            bg="#111827",
        )
        time_label.pack(pady=10)

        alarm_frame = tk.Frame(root, bg="#111827")
        alarm_frame.pack(pady=10)

        tk.Label(
            alarm_frame,
            text="Set alarm time (HH:MM):",
            font=("Arial", 14),
            fg="white",
            bg="#111827",
        ).pack(side="left", padx=(0, 10))

        entry = tk.Entry(
            alarm_frame,
            textvariable=self.alarm_time,
            width=8,
            font=("Arial", 18),
            justify="center",
        )
        entry.pack(side="left")

        set_button = tk.Button(
            root,
            text="Set Alarm",
            command=self.set_alarm,
            font=("Arial", 12, "bold"),
            bg="#22c55e",
            fg="white",
            width=12,
            height=2,
        )
        set_button.pack(pady=8)

        stop_button = tk.Button(
            root,
            text="Stop Alarm",
            command=self.stop_alarm,
            font=("Arial", 12, "bold"),
            bg="#ef4444",
            fg="white",
            width=12,
            height=2,
        )
        stop_button.pack(pady=5)

        status = tk.Label(
            root,
            textvariable=self.status_text,
            font=("Arial", 12),
            fg="#fbbf24",
            bg="#111827",
            wraplength=350,
        )
        status.pack(pady=(10, 20))

        self.update_clock()

    def update_clock(self):
        now = datetime.now().strftime("%H:%M:%S")
        self.current_time.set(now)

        if self.alarm_on and not self.ringing:
            current_time = datetime.now().strftime("%H:%M")
            if current_time == self.alarm_time.get():
                self.ringing = True
                self.status_text.set("Wake up! Alarm is ringing...")
                threading.Thread(target=self.play_alarm, daemon=True).start()

        self.root.after(1000, self.update_clock)

    def set_alarm(self):
        entered_time = self.alarm_time.get().strip()
        try:
            datetime.strptime(entered_time, "%H:%M")
            self.alarm_on = True
            self.ringing = False
            self.stop_ringing = False
            self.status_text.set(f"Alarm set for {entered_time}")
        except ValueError:
            messagebox.showerror("Invalid time", "Please enter time in HH:MM format, for example 07:30")

    def play_alarm(self):
        while self.ringing and not self.stop_ringing:
            winsound.Beep(1000, 500)
            time.sleep(0.5)

    def stop_alarm(self):
        self.stop_ringing = True
        self.ringing = False
        self.alarm_on = False
        self.status_text.set("Alarm stopped")


if __name__ == "__main__":
    root = tk.Tk()
    app = AlarmClockApp(root)
    root.mainloop()
