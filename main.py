
import sys
import subprocess

if __name__ == "__main__":
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
    command = f'youtube-dl {sys.argv[1]}'
    subprocess.call(command, shell=True)