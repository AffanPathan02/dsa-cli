import json
import os
import threading
# from window_lib import display_content
from cli_lib import display_content
import simpy
import texteditor


def solve_engine(arg):
    data = json_parser("problems/problems.json", arg)


def json_parser(filename, arg):
    # Change this to match the question id
    solution = "sample"
    # Add support for multiple languages
    os.system(f"touch {solution}.c")
    editor_thread = threading.Thread(
        target=texteditor.open, kwargs={'filename': 'sample.c'})

    with open(filename, 'r') as f:
        data = json.load(f)
        if arg in ['easy', 'medium', 'hard']:
            question_thread = threading.Thread(
                target=display_content, args=(data[arg],))
            question_thread.start()
        else:
            print("Invalid argument. Please provide one of 'easy', 'medium', or 'hard'.")

    editor_thread.start()
    editor_thread.join()
    if 'question_thread' in locals():
        question_thread.join()
