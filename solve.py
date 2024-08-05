import json
import os
from window_lib import display_content

def solve_engine(arg):
    json_parser("problems/problems.json", arg)

def json_parser(filename, arg):
    solution="sample"                               #change is later to match the question id
    os.system(f"touch {solution}.c")                #add support multiple language
    with open(filename, 'r') as f:
        data = json.load(f)
        if arg in ['easy', 'medium', 'hard']:
            display_content(data[arg])
        else:
            print("Invalid argument. Please provide one of 'easy', 'medium', or 'hard'.")
