"""Constants for the {{ cookiecutter.project_name }} package."""

PROJECT_NAME = "{{ cookiecutter.project_name }}"
PROJECT_SHORT = "{{ cookiecutter.project_name.split('_') | map('first') | join('') }}"
WANDB_ENTITY = "farai"
WANDB_PROJECT = "{{ cookiecutter.project_name }}"
