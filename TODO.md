# Todos

- [x] Set up CircleCI for the template
- [x] Work through updates to template implementation to use uv & circle ci
- [ ] Set up an internal PyPI server and allow for an automated release process (update README when done)
- [ ] Add CircleCI workflows to keep downstream repositories in line with template updates (update README when done)
- [ ] Figure out what secrets we need to make automation work and write instructions for their generation and use (update README when done)
- [ ] Pull request template: ask to link Linear issue or GH issue
- [ ] Prune .gitignore, 
- [ ] Remove example starter code and remove their libraries from pyproject.toml
- [ ] Add Makefile
- [ ] Pyright config in pyproject.toml: probably can remove the options, since we'll just uv run pyright in the Makefile
- [ ] Add top-level tests for whether pre-commit works, make commands work, etc.
- [ ] Other things to copy/merge from project_template: `Dockerfile`, `experiments`, `k8s`, `main.py`, `README.md` 
- [ ] Update top-level README