import subprocess
import os

def run_git(args):
    try:
        result = subprocess.run(['git'] + args, capture_output=True, text=True)
        print(f"STDOUT:\n{result.stdout}")
        print(f"STDERR:\n{result.stderr}")
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    print("Running git status:")
    run_git(['status'])
    print("\nRunning git ls-files --stage:")
    run_git(['ls-files', '--stage'])
