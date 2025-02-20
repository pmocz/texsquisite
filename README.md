

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
XXX
```

To fix _fixable_ errors automatically, do:
```sh
texsquisite check --fix
```

