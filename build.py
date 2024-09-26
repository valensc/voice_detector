import os
import subprocess
import sys
import venv

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    if process.returncode != 0:
        print(f"Error executing command: {command}")
        print(error.decode('utf-8'))
        sys.exit(1)
    return output.decode('utf-8')

def main():
    # Create and activate virtual environment
    venv_dir = 'venv'
    venv.create(venv_dir, with_pip=True)
    
    if sys.platform == 'win32':
        activate_script = os.path.join(venv_dir, 'Scripts', 'activate.bat')
        python_executable = os.path.join(venv_dir, 'Scripts', 'python.exe')
    else:
        activate_script = os.path.join(venv_dir, 'bin', 'activate')
        python_executable = os.path.join(venv_dir, 'bin', 'python')

    # Install required packages
    print("Installing required packages...")
    run_command(f"{python_executable} -m pip install -r requirements.txt")

    # Install PyInstaller
    print("Installing PyInstaller...")
    run_command(f"{python_executable} -m pip install pyinstaller")

    # Build the executable
    print("Building the executable...")
    if sys.platform == 'darwin':  # macOS
        run_command(f"{python_executable} -m PyInstaller --onefile --windowed --add-data 'src:src' --name 'VoiceDetector' src/main.py")
    else:
        run_command(f"{python_executable} -m PyInstaller --onefile --windowed src/main.py")

    if sys.platform == 'darwin':
        print("Creating macOS application bundle...")
        run_command("mkdir -p dist/VoiceDetector.app/Contents/MacOS")
        run_command("mv dist/VoiceDetector dist/VoiceDetector.app/Contents/MacOS/")
        run_command("cp Info.plist dist/VoiceDetector.app/Contents/")

    print("Build complete. The executable can be found in the 'dist' directory.")

if __name__ == "__main__":
    main()