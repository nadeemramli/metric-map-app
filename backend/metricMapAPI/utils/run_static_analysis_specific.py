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
    output_file = "static_analysis_results_specific.md"

    # Commands to run
    commands = {
        "pylint": f"pylint metrics/computations",
        "flake8": f"flake8 metrics/computations",
        "mypy": f"mypy metrics/computations",
        "bandit": f"bandit -r metrics/computations",
        "black": f"black --check metrics/computations",
        "isort": f"isort --check-only metrics/computations",
        "pylint": f"pylint metrics/computations",
        "flake8": f"flake8 metrics/computations",
        "mypy": f"mypy metrics/computations",
        "bandit": f"bandit -r metrics/computations",
        "black": f"black --check metrics/computations",
        "isort": f"isort --check-only metrics/computations"
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
