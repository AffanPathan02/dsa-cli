import os
import subprocess


def setup_engine(setup_env):
    if setup_env == "c":
        #        os.system("./scripts/install-c.sh")
        subprocess.run(['sh', './scripts/install-c.sh'])
    elif setup_env == "java":
        #        os.system("./scripts/install-java.sh")
        subprocess.run(['sh', './scripts/install-java.sh'])
