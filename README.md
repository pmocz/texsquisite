

# texsquisite

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
