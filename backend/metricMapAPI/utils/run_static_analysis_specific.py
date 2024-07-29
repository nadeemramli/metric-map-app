import os
import subprocess

def run_command(command):
    """Run a shell command and return its output."""
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode('utf-8'), result.stderr.decode('utf-8')

def save_to_markdown(results, filename):
    """Save the results dictionary to a markdown file."""
    with open(filename, 'w') as f:
        f.write("# Static Analysis Results\n")
        for tool, output in results.items():
            f.write(f"## {tool}\n")
            f.write("```\n")
            f.write(output)
            f.write("\n```\n")

def main():
    # Get the absolute path to the permanent_computations.py file
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    target_file = os.path.join(base_dir,"metricMapAPI", "metrics", "computations", "permanent_computations.py")
    
    if not os.path.exists(target_file):
        print(f"Error: The file {target_file} does not exist.")
        return

    output_file = "static_analysis_results_specific.md"

    # Commands to run
    commands = {
        "pylint": f"pylint {target_file}",
        "flake8": f"flake8 {target_file}",
        "mypy": f"mypy {target_file}",
        "bandit": f"bandit -r {target_file}",
        "black": f"black --check {target_file}",
        "isort": f"isort --check-only {target_file}"
    }

    # Run each command and collect the output
    results = {}
    for tool, command in commands.items():
        print(f"Running {tool}...")
        stdout, stderr = run_command(command)
        results[tool] = stdout + stderr

    # Save results to markdown file
    save_to_markdown(results, output_file)
    print(f"Static analysis results saved to {output_file}")

if __name__ == "__main__":
    main()