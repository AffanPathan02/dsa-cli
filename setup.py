import subprocess


def setup_engine(setup_env):
    if setup_env == "c":
        subprocess.run(['sh', './scripts/install-c.sh'])
    elif setup_env == "java":
        subprocess.run(['sh', './scripts/install-java.sh'])
