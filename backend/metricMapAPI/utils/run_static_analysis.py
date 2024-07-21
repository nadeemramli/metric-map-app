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
    project = "metricMapAPI"
    app = "metrics"
    output_file = "static_analysis_results.md"

    # Commands to run
    commands = {
        "pylint": f"pylint {project}",
        "flake8": f"flake8 {project}",
        "mypy": f"mypy {project}",
        "bandit": f"bandit -r {project}",
        "black": f"black --check {project}",
        "isort": f"isort --check-only {project}",
        "pylint": f"pylint {app}",
        "flake8": f"flake8 {app}",
        "mypy": f"mypy {app}",
        "bandit": f"bandit -r {app}",
        "black": f"black --check {app}",
        "isort": f"isort --check-only {app}"
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
