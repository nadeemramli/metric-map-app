import os
import subprocess

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output.decode('utf-8'), error.decode('utf-8')

def run_pylint(file_path):
    print(f"Running Pylint on {file_path}")
    output, error = run_command(f"pylint {file_path}")
    print(output)
    if error:
        print(f"Pylint Error: {error}")

def run_mypy(file_path):
    print(f"Running Mypy on {file_path}")
    output, error = run_command(f"mypy {file_path}")
    print(output)
    if error:
        print(f"Mypy Error: {error}")

def main():
    # Specify the directory containing your Python files
    directory = "path/to/your/project"
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                run_pylint(file_path)
                run_mypy(file_path)

if __name__ == "__main__":
    main()