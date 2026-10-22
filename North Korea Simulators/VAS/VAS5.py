import tkinter as tk
import random

# ---------------- MAIN APP ----------------

root = tk.Tk()
root.title("Visa Approval Simulator - GUI Edition")
root.geometry("500x400")

loyalty = 50

# ---------------- SCREENS ----------------

def clear():
    for widget in root.winfo_children():
        widget.destroy()

# ---------- LOADING SCREEN ----------

def loading_screen(next_screen):
    clear()
    label = tk.Label(root, text="Processing request...", font=("Arial", 16))
    label.pack(pady=30)

    dots = tk.Label(root, text="", font=("Arial", 20))
    dots.pack()

    def animate(i=0):
        dots.config(text="." * (i % 4))
        if i < 12:
            root.after(300, animate, i + 1)
        else:
            next_screen()

    animate()

# ---------- INTRO / MENU ----------

def main_menu():
    clear()

    title = tk.Label(root, text="VISA APPROVAL SYSTEM", font=("Arial", 18))
    title.pack(pady=20)

    subtitle = tk.Label(root, text="GUI Edition", font=("Arial", 12))
    subtitle.pack(pady=5)

    tk.Button(root, text="Start Evaluation", command=questions_screen).pack(pady=10)
    tk.Button(root, text="System Info", command=info_screen).pack(pady=10)
    tk.Button(root, text="Exit", command=root.destroy).pack(pady=10)

# ---------- INFO SCREEN ----------

def info_screen():
    clear()

    tk.Label(root, text="SYSTEM INFO", font=("Arial", 16)).pack(pady=20)

    info = [
        "Version: GUI Edition 1.0",
        "Approval Rate: 100% (official data)",
        "Status: Stable",
        "All decisions are final"
    ]

    for line in info:
        tk.Label(root, text=line).pack()

    tk.Button(root, text="Back", command=main_menu).pack(pady=20)

# ---------- QUESTIONS ----------

def questions_screen():
    clear()

    global loyalty
    loyalty = 50

    tk.Label(root, text="Loyalty Evaluation", font=("Arial", 16)).pack(pady=10)

    def q1():
        global loyalty
        if var1.get() == "yes":
            loyalty += 30
        else:
            loyalty -= 20
        q2()

    def q2():
        global loyalty
        if var2.get() == "yes":
            loyalty += 20
        else:
            loyalty -= 10
        q3()

    def q3():
        global loyalty
        if var3.get() == "yes":
            loyalty += 15
        else:
            loyalty -= 15
        loading_screen(result_screen)

    var1 = tk.StringVar(value="yes")
    var2 = tk.StringVar(value="yes")
    var3 = tk.StringVar(value="yes")

    tk.Label(root, text="Do you trust the system?").pack()
    tk.Entry(root, textvariable=var1).pack()

    tk.Label(root, text="Do you enjoy national celebrations?").pack()
    tk.Entry(root, textvariable=var2).pack()

    tk.Label(root, text="Is obedience important?").pack()
    tk.Entry(root, textvariable=var3).pack()

    tk.Button(root, text="Submit", command=q1).pack(pady=20)

# ---------- RESULT SCREEN ----------

def result_screen():
    clear()

    global loyalty

    tk.Label(root, text="RESULT", font=("Arial", 18)).pack(pady=10)

    tk.Label(root, text=f"Loyalty Score: {loyalty}%").pack(pady=10)

    if loyalty >= 90:
        text = "ULTRA LOYAL ENDING\nYou are promoted to Supreme Officer."
    elif loyalty >= 70:
        text = "APPROVED ENDING\nVisa granted. One-way to North Korea."
    elif loyalty >= 40:
        text = "PROBATION ENDING\nApplication delayed."
    else:
        text = "DENIED ENDING\nInsufficient ideological alignment."

    tk.Label(root, text=text).pack(pady=20)

    tk.Button(root, text="Back to Menu", command=main_menu).pack(pady=10)
    tk.Button(root, text="Exit", command=root.destroy).pack()

# ---------------- START ----------------

main_menu()
root.mainloop()