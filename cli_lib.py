import threading
import time
from evaluate import evaluate_engine
import sys


def display_content(problems):
    def format_problem(problem):
        content = f"Title: {problem['title']}\n"
        content += f"ID: {problem['id']}\n"
        content += f"Description: {problem['description']}\n"
        content += f"Topics: {', '.join(problem['topics'])}\n"
        content += f"Expected Output: {problem['expected_output']}\n"
        return content

    def timer_thread():
        nonlocal timer_running
        countdown = 5
        while countdown > 0 and timer_running:
            min, sec = divmod(countdown, 60)
            timer = "{:02d}:{:02d}".format(min, sec)
            print(timer, flush=True, end="\r")
            time.sleep(1)
            countdown -= 1
        if timer_running:
            print("Time's Up!")
            timer_running = False
            print("Evaluation Result: Time's Up!")
            exit()

    def user_input_thread():
        nonlocal timer_running
        while True:
            command = input(
                "Enter 'start' to begin the timer or 'submit' to submit (only valid after starting): ").strip().lower()
            if command == 'start':
                if timer_running:
                    print("Timer is already running.")
                else:
                    print("Timer started!")
                    timer_running = True
                    # Start the timer in a new thread
                    threading.Thread(target=timer_thread).start()
            elif command == 'submit':
                if timer_running:
                    timer_running = False
                    result = evaluate_engine(problems, 'expected_output')
                    print(f"Evaluation Result: {result}")
                    break
                else:
                    print(
                        "Timer has expired or not started. No further submissions allowed.")
            elif command == 'exit':
                break
                exit()
            else:
                print("Invalid command. Please enter 'start' or 'submit'.")

    # Display the problems
    for problem in problems:
        print(format_problem(problem))
        print("-" * 40)

    # Initialize variables
    timer_running = False

    # Start user input process
    user_input_thread()
