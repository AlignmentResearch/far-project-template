import functools
import sys
from pathlib import Path

from git.repo import Repo

from {{ cookiecutter.project_name }}.utils.utils import ask_for_confirmation


@functools.cache
def git_latest_commit() -> str:
    """Gets the latest commit hash."""
    repo = Repo(".", search_parent_directories=True)
    commit_hash = str(repo.head.object.hexsha)
    return commit_hash


@functools.cache
def get_repo_root() -> Path:
    """Get the root directory of the git repository."""
    repo = git.Repo(".", search_parent_directories=True)
    working_dir = repo.working_tree_dir
    if working_dir is None:
        raise RuntimeError("Could not find git repository root")
    return Path(working_dir)


def validate_git_repo() -> None:
    """Validates the git repo before running a batch job."""
    repo = Repo(".", search_parent_directories=True)

    # Push to git as we want to run the code with the current commit.
    repo.remote("origin").push(repo.active_branch.name).raise_if_error()

    # Check if repo is dirty.
    if repo.is_dirty(untracked_files=True):
        should_continue = ask_for_confirmation(
            "Git repo is dirty. Are you sure you want to continue?"
        )
        if not should_continue:
            print("Aborting")
            sys.exit(1)
