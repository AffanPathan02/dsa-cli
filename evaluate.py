import os
import subprocess


def evaluate_engine(problems, expected_output):
    os.system("gcc sample.c")
    command = "./a.out"
    result = subprocess.check_output(command, shell=True, text=True)
    if problems[0][expected_output] == result:
        return "Answer is Correct"
    else:
        return "solution is wrong"
