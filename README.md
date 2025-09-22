# FAR's Project Template

This is a Python package
[cookiecutter](https://cookiecutter.readthedocs.io/en/latest/README.html) template
for developing utility libraries at FAR using our standard tool chain:

- [`uv`](https://docs.astral.sh/uv/) as the main package management tool.
- [`ruff`](https://docs.astral.sh/ruff/) for auto-formatting and linting code.
- [`mypy`](https://mypy-lang.org/) for type-enforcement
- [`pytest`](https://docs.pytest.org/en/stable/) for building and running test-suites.
- [`mkdocs`](https://www.mkdocs.org/) and [mkdocs Material](https://squidfunk.github.io/mkdocs-material/)
  for writing and building documentation.
- [`CircleCI`](https://circleci.com/docs/) for continuous integration.
- [`pre-commit`](https://pre-commit.com/) for automatically running the tool-chain
  before submitting changes to git.

## Features

#### Automatic updates to the projects generated from this cookiecutter

* Powered by [cruft](https://cruft.github.io/cruft/)
* Keeps downstream projects up-to-date with best practices as they evolve.

#### Continuous integration

* Powered by [`CircleCI`](https://circleci.com/docs/).
* This allows for all sorts of automation, including testing, building docs, automated code review, and many other things.

#### Documentation

* Powered by [mkdocs-material](https://github.com/squidfunk/mkdocs-material)
* Auto-generated API documentation from docstrings via [mkdocstrings](https://github.com/mkdocstrings/mkdocstrings)
* See the extensive list of [MkDocs plugins](https://github.com/mkdocs/mkdocs/wiki/MkDocs-Plugins) which can help you
 to tune the documentation to fit your project's needs

#### Automated releases

TODO: Set up an internal PyPI server and allow for an automated release process.

#### Changelog management

* Gently enforced: [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
* GitHub releases get their description automatically populated based on the changelog content
* The _Unreleased_ section is automatically updated when a release is done
* Changelog is embedded in the documentation

#### Automation

TODO: Add CircleCI workflows to keep downstream repositories in line with template updates.

## Usage

Make sure you have [`cruft`](https://github.com/cruft/cruft#installation) installed. Alternatively, you can use
 [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/installation.html) if you are not interested in
  getting updates to the project "boilerplate" in the future.

Create a new project:

```sh
cruft create https://github.com/AlignmentResearch/far-project-template
```

The CLI interface will ask some basic questions, such the name of the project, and then
generate all the goodies automatically.

After that you can make it a proper git repo:

```sh
cd <your-project-slug>
git init
git add .
git commit -m "Initial project structure from Python Package cookiecutter"
```

We update this cookiecutter template regularly to keep it up-to-date with the best
practices of the Python world. You can get the updates into your project with:

```sh
cruft update
```

### Configure secrets

TODO: Figure out what secrets we need to make automation work and write instructions for their generation and use.
