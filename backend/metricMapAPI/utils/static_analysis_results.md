# Static Analysis Results
## pylint
```
************* Module metrics
metrics:1:0: F0001: No module named metrics (fatal)

```
## flake8
```
metrics:0:1: E902 FileNotFoundError: [Errno 2] No such file or directory: 'metrics'

```
## mypy
```
mypy: can't read file 'metrics': No such file or directory

```
## bandit
```
Run started:2024-07-24 13:16:23.613058

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 0
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
	Total issues (by confidence):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
Files skipped (1):
	./metrics (No such file or directory)
[main]	INFO	profile include tests: None
[main]	INFO	profile exclude tests: None
[main]	INFO	cli include tests: None
[main]	INFO	cli exclude tests: None
[main]	INFO	running on Python 3.10.7

```
## black
```
Usage: black [OPTIONS] SRC ...
Try 'black -h' for help.

Error: Invalid value for 'SRC ...': Path 'metrics' does not exist.

```
## isort
```
Broken 1 paths

```
