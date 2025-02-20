# texsquisite

[![Repo Status][status-badge]][status-link]
[![PyPI Version Status][pypi-badge]][pypi-link]
[![Test Status][workflow-test-badge]][workflow-test-link]
[![Readthedocs Status][docs-badge]][docs-link]
[![License][license-badge]][license-link]

[status-link]:         https://www.repostatus.org/#active
[status-badge]:        https://www.repostatus.org/badges/latest/active.svg
[pypi-link]:           https://pypi.org/project/texsquisite
[pypi-badge]:          https://img.shields.io/pypi/v/texsquisite?label=PyPI&logo=pypi
[workflow-test-link]:  https://github.com/texsquisiteProject/texsquisite/actions/workflows/test-package.yml
[workflow-test-badge]: https://github.com/texsquisiteProject/texsquisite/actions/workflows/test-package.yml/badge.svg?event=push
[docs-link]:           https://texsquisite.readthedocs.io
[docs-badge]:          https://readthedocs.org/projects/texsquisite/badge
[license-link]:        https://opensource.org/licenses/MIT
[license-badge]:       https://img.shields.io/badge/MIT-blue.svg

**`texsquisite`** is an linter for LaTeX that auto-formats code and fixes common typesetting mistakes.

## Install 

```sh
pip install texsquisite
```

## How to Use

Run **`texsquisite`** in the command-line in your working directory:
```sh
texsquisite check
```

It will automatically detect all `*.tex` files and print errors.
For example, it may output something like:
```console
Fixable errors in tests/file1.tex:
  line 3: [S001] - line should not end with trailing whitespace
    hello world              % trailing whitespace  
  line 11: [S004] - \footnote should not have space before it
    hello \footnote{world}   % whitespace before footnote

Fixable errors in tests/dir2/file2.tex:
  line 3: [S001] - line should not end with trailing whitespace
    hello world              % trailing whitespace  

texsquisite: 2 files scanned.
3 error(s) found, 3 of which are fixable with '--fix'.
```

To auto-fix _fixable_ errors, do:
```sh
texsquisite check --fix
```

Include a [`texsquisite.toml`](texsquisite.toml) file in your working directory to add configurable options.

For more info, check out the [docs](https://texsquisite.readthedocs.io).

## Contribute

**`texsquisite`** is open-source and just getting started!
Fork the code and submit a PR to add your own features.

- [X] publish on PyPI
- [ ] use a LaTeX lexer/parser to catch more types of errors
- [ ] spot and fix common text/math-mode mix-ups
- [ ] ambitious: check units in equations
- [ ] add more rules (this will never end)

For more info, check out the [Contributing Guide](CONTRIBUTING.md)

## License

This work is distributed under the MIT License. See [LICENSE](LICENSE) for more information.

## Support

:star: Star this repository, share with friends/colleagues, or donate to become a supporter of the project.
