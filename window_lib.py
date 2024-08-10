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
        nonlocal timer_running
        countdown = 5
        timer_running = True
        while countdown > 0 and timer_running:
            timer_label.config(text=str(countdown))
            root.update()
            time.sleep(1)
            countdown -= 1

        if timer_running:  # Timer finished without being stopped
            timer_label.pack_forget()
            show_result_dialog("Time's Up!", None)

    def show_result_dialog(title, result):
        def on_next_button_click(problems):
            display_content(problems)

        def on_exit_button_click():
            result_dialog.destroy()
            root.destroy()

        result_dialog = tk.Toplevel(root)
        result_dialog.title(title)

        if result is not None:
            result_label = tk.Label(result_dialog, text=f"Evaluation Result: {
                                    result}", font=("Helvetica", 16))
            result_label.pack(pady=20, padx=20)
        else:
            result_label = tk.Label(
                result_dialog, text="Time's Up!", font=("Helvetica", 16))
            result_label.pack(pady=20, padx=20)

        next_button = tk.Button(
            result_dialog, text="Next", command=lambda: (on_next_button_click(problems)))
        next_button.pack(pady=10)

        exit_button = tk.Button(
            result_dialog, text="Exit", command=on_exit_button_click)
        exit_button.pack(pady=20)

    def on_start_button_click():
        start_button.config(state=tk.DISABLED)  # Disable the start button
        submit_button.config(state=tk.NORMAL)    # Enable the submit button
        # Start the timer after 1 second delay
        root.after(1000, start_timer)

    def on_submit_button_click(problems):
        result = evaluate_engine(problems, 'expected_output')
        show_result_dialog("Evaluation Result", result)

    root = tk.Tk()
    root.title("DSA CLI Window")

    content_frame = tk.Frame(root)
    content_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

    timer_frame = tk.Frame(root)
    timer_frame.pack(side=tk.BOTTOM, pady=20)

    content_label = tk.Label(content_frame, text="\n\n".join(
        [format_problem(problem) for problem in problems]), justify=tk.LEFT, anchor="w")
    content_label.pack(expand=True, fill=tk.BOTH)

    timer_label = tk.Label(timer_frame, text="10", font=("Helvetica", 48))
    timer_label.pack()

    submit_button = tk.Button(root, text="Submit", command=lambda: on_submit_button_click(
        problems), state=tk.DISABLED)
    submit_button.pack(side=tk.BOTTOM, pady=30)

    start_button = tk.Button(root, text="Start", command=on_start_button_click)
    start_button.pack(side=tk.BOTTOM, pady=10)

    root.update_idletasks()
    content_width = content_frame.winfo_reqwidth()
    content_height = content_frame.winfo_reqheight()
    timer_width = timer_frame.winfo_reqwidth()
    timer_height = timer_frame.winfo_reqheight()

    root.geometry(f"{content_width}x{content_height + timer_height +
                  submit_button.winfo_height() + start_button.winfo_height()}")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = root.winfo_width()
    window_height = root.winfo_height()

    x = screen_width - window_width
    y = screen_height - window_height

    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Variable to track if the timer is running
    timer_running = False

    root.mainloop()
