# MLSmellHound

MLSmellHound is a tool that provides context-aware linting. It is based on Pylint, a popular linter for Python projects that is highly configurable but that does not consider context.

## Dependencies

* Bash
* Python3
* pylint 2.11.1 (pip install pylint)

## Usage

```
# Lint all Python files in example-src (edit script to run on your own project)
./mlsh
```

The script will analyse all Python files in the project directory then write the audit report to `outputs/<datetime>/lint-context.txt`
