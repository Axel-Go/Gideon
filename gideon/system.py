from pathlib import Path
import platform
import subprocess


def get_project_name() -> str:
    """Return the current project's folder name."""
    return Path.cwd().name


def get_python_version() -> str:
    """Return the current Python version."""
    return platform.python_version()

def get_git_branch() -> str:
    """Return the current Git branch."""

    result = subprocess.run(
        ["git", "branch", "--show-current"],
        capture_output=True,
        text=True,
    )

    return result.stdout.strip()