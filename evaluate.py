import os
import subprocess
def evaluate_engine(expected_output):
    os.system(f"gcc sample.c")
    command="./a.out"
    result=subprocess.check_output(command,shell=True, text=True)
    if expected_output == result:
        print("answer is corrected")
    else:
        print("solution is wrong")


    
