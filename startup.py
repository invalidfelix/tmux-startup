import os
import time


print("\nDeleting old tmux sessions...")
os.system("tmux kill-server")
print("Starting new tmux sessions...")
print("------------------------------------")
time.sleep(5)


def run(path):
    name = path.split('/')[-1]
    
    os.system(f"tmux new -d -s '{name}'")
    os.system(f"tmux send-keys -t 'cd {path}' C-m")
    result = os.system(f"tmux send-keys 'python3 main.py' C-m")
    
    if result == 0:
        print(f"Started {path} successfully")
    else:
        print(f"Failed to start {path}")
    
    
home = "../home/"


for dir1 in os.listdir(home):
    if "main.py" not in os.listdir(home + dir1):
        print(f"Detected {dir1} as a subfolder")
        for dir2 in os.listdir(home + dir1): # iterate through all subdirectories
            if "main.py" not in os.listdir(home + dir1 + "/" + dir2):
                print(f"Warning: Detected empty subfolder {dir1}/{dir2}")
            else:
                run(dir1 + "/" + dir2)
    else:
        run(dir1)