import tkinter as tk
from time import strftime


def main():
    root = tk.Tk()
    root.title("Digital Clock")
    root.geometry("420x180")
    root.resizable(False, False)
    root.config(bg="black")

    time_label = tk.Label(
        root,
        font=("Arial", 48, "bold"),
        fg="cyan",
        bg="black",
        padx=20,
        pady=10,
    )
    time_label.pack(anchor="center")

    date_label = tk.Label(
        root,
        font=("Arial", 18),
        fg="white",
        bg="black",
        pady=10,
    )
    date_label.pack(anchor="center")

    def update_clock():
        time_label.config(text=strftime("%H:%M:%S"))
        date_label.config(text=strftime("%A, %d %B %Y"))
        root.after(1000, update_clock)

    update_clock()
    root.mainloop()


if __name__ == "__main__":
    main()

