import tkinter as tk
from tkinter import messagebox
from evaluate import evaluate_engine
import time


def display_content(problems):
    def format_problem(problem):
        content = f"Title: {problem['title']}\n"
        content += f"ID: {problem['id']}\n"
        content += f"Description: {problem['description']}\n"
        content += f"Topics: {', '.join(problem['topics'])}\n"
        content += f"Expected Output: {problem['expected_output']}\n"
        return content

    def start_timer():
        countdown = 5
        while countdown > 0:
            timer_label.config(text=str(countdown))
            root.update()
            time.sleep(1)
            countdown -= 1

        timer_label.pack_forget()
        messagebox.showinfo("Times Ups!!!!", "Time is over")
        root.destroy()

    root = tk.Tk()
    root.title("DSA cli window")
    root.geometry("600x400")

    content_frame = tk.Frame(root)
    content_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

    timer_frame = tk.Frame(root)
    timer_frame.pack(side=tk.BOTTOM, pady=20)

    content_label = tk.Label(content_frame, text="\n\n".join(
        [format_problem(problem) for problem in problems]), justify=tk.LEFT, anchor="w")
    content_label.pack(expand=True, fill=tk.BOTH)

    timer_label = tk.Label(timer_frame, text="10", font=("Helvetica", 48))
    timer_label.pack()

    submit_button = tk.Button(root, text="Submit", command=lambda: evaluate_engine(
        problems[0]['expected_output']), anchor="center")
    submit_button.pack(side=tk.BOTTOM, pady=30)

    root.after(1000, start_timer)

    root.mainloop()
