import tkinter as tk
from tkinter import messagebox
import random

def accept_love():
    messagebox.showinfo("Yay! ✨", "I knew you would say yes! I love you! 💖")
    root.destroy()

def move_button(event):
    # Generates random coordinates so the 'No' button skips away when hovered
    x = random.randint(50, 350)
    y = random.randint(50, 350)
    no_btn.place(x=x, y=y)

# Window Setup
root = tk.Tk()
root.title("A Very Important Question 💖")
root.geometry("450x450")
root.configure(bg="#ffe6ec")

label = tk.Label(root, text="Will you be my Valentine / Date forever?", 
                 font=("Helvetica", 14, "bold"), bg="#ffe6ec", fg="#d90429")
label.pack(pady=50)

# Yes Button
yes_btn = tk.Button(root, text="Yes, absolutely! 😍", font=("Helvetica", 12), 
                    bg="#ff4d6d", fg="white", command=accept_love)
yes_btn.pack(pady=20)

# No Button (Hovering over it triggers move_button)
no_btn = tk.Button(root, text="No 💔", font=("Helvetica", 12), bg="#adb5bd", fg="white")
no_btn.pack(pady=20)
no_btn.bind("<Enter>", move_button)

root.mainloop()
