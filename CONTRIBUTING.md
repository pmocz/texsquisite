
# Contributing to **`texsquisite`**

Thank you for taking the time to contribute! All types of contributions are welcome.

- [Report a bug](#report-a-bug)
- [Suggest an enhancement](#suggest-an-enhancement)
- [Add a feature](#add-a-feature)

And if you don't have time to contribute but like the project, star it and share with your friends/colleagues.

## Report a bug

If you spot a bug, raise an Issue on GitHub. Make sure you are using the latest version of the code,
and provide enough information so that the bug can be reproduced easily.

## Suggest an enhancement

Wishing a certain capability existed but is not there? Raise an issue on GitHub and tag it as an enhancement.

## Add a feature

Fork this repository, add your feature, and submit a PR for review. If you are adding new linter rules, please add them in `rules.py` and add an example of a bad LaTeX line that the rule should catch in `tests/file1.tex`.
Run
```sh
python texsquisite.py check
```
in the project directory and update `tests/output.txt` with its output, which is used for testing.
To make sure the code passes testing, do a:
```sh
pip install .
pytest
```
