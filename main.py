import tkinter as tk

# Create the main window
root = tk.Tk()

# Window title
root.title("AI Virtual Assistant")

# Window size
root.geometry("900x600")

# Background color
root.configure(bg="#1E1E1E")

# Heading
title = tk.Label(
    root,
    text="🤖 AI Virtual Assistant",
    font=("Arial", 24, "bold"),
    fg="cyan",
    bg="#1E1E1E"
)
title.pack(pady=20)

# Status
status = tk.Label(
    root,
    text="Status: Ready",
    font=("Arial", 14),
    fg="white",
    bg="#1E1E1E"
)
status.pack(pady=10)

# Run the app
root.mainloop()
