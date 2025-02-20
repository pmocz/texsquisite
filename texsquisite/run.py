import sys
import os
import toml

from .rules import LatexRules


class Checker:
    def __init__(self, file_name, rules):
        self.file_name = file_name
        self.fixable_errors = []
        self.unfixable_errors = []
        self.rules = rules

    def check(self, fix):
        corrected_tex = []
        # check for errors line-by-line, and apply fix when possible, if requested
        with open(self.file_name, "r") as file:
            for line_number, line in enumerate(file, 1):
                for rule in self.rules:
                    if rule.matches(line):
                        if rule.fixable:
                            self.fixable_errors.append((line_number, rule.id, line))
                            if fix:
                                line = rule.fix(line)
                        else:
                            self.unfixable_errors.append((line_number, rule.id, line))
                if fix:
                    corrected_tex.append(line)
        if fix:
            with open(self.file_name, "w") as file:
                file.writelines(corrected_tex)
        return len(self.fixable_errors), len(self.unfixable_errors)

    def print_errors(self):
        # remove current working directory from file name
        file = self.file_name.replace(os.getcwd(), "").strip("/")
        if self.fixable_errors:
            print(f"Fixable errors in {file}:")
            for line_number, id, line in self.fixable_errors:
                print(f"  line {line_number}: [{id}] - {self.rules[id].description}")
                print(f"    {line}".strip("\n"))
            print()
        if self.unfixable_errors:
            print(f"Other errors in {file}:")
            for line_number, id, line in self.unfixable_errors:
                print(f"  line {line_number}: [{id}] - {self.rules[id].description}")
                print(f"    {line}".strip("\n"))
            print()


def print_explanation(rules, id=None):
    if id:
        rules[id].print()
    else:
        for rule in rules:
            rules[rule.id].print()


def print_help():
    print("A LaTex linter written in Python")
    print()
    print("texsquisite <COMMAND> [option]")
    print()
    print("Commands:")
    print("  check           Perform static analysis on files and report issues")
    print(
        "  check --fix     Perform static analysis on files and apply fixable changes"
    )
    print("  help            Print this help message")
    print("  explain         Get descriptions of each linting rule")
    print("  explain [id]    Get description of a particular linting rule")
    print()
    print("Configurations may be set in a texsquisite.toml file in the root directory.")


def run(argv=sys.argv):
    """Command line interface"""

    rules = LatexRules()
    fix = False

    # Process arguments
    if len(argv) == 2:
        if argv[1] in ["help", "-h", "--help"]:
            print_help()
            return 0
        elif argv[1] == "check":
            pass
        elif argv[1] == "explain":
            print_explanation(rules)
            return 0
        else:
            print(f"Input argument '{argv[1]}' not recognized!\n")
            print_help()
            return -1
    elif len(argv) == 3:
        if argv[1] == "check" and argv[2] == "--fix":
            fix = True
            pass
        elif argv[1] == "explain":
            id = argv[2]
            if id in rules:
                print_explanation(rules, id)
                return 0
            else:
                print(f"{id} is not a valid rule id!")
                return -1
        else:
            print(f"Input argument '{argv[1]} {argv[2]}' not recognized!\n")
            print_help()
            return -1
    else:
        print_help()
        return 0

    # Default behavior
    extensions = ["tex"]
    ignore = []
    exclude = []

    # Read configuration file (if it exists)
    if os.path.exists("texsquisite.toml"):
        with open("texsquisite.toml", "r") as file:
            config = toml.load(file)["check"]
            if "file-extensions" in config:
                extensions = config["file-extensions"]
            if "ignore" in config:
                ignore = config["ignore"]
            if "exclude" in config:
                exclude = config["exclude"]

    # Collect all *.tex files in the current directory and its subdirectories
    tex_files = []
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            for ext in extensions:
                if file.endswith("." + ext):
                    tex_files.append(os.path.join(root, file))

    # Remove ignored files and directories
    for i in range(len(tex_files) - 1, -1, -1):
        file = tex_files[i].replace(os.getcwd(), "").strip("/")
        file_name = file.split("/")[-1]
        file_dirs = file.split("/")[:-1]
        if file_name in exclude:
            tex_files.pop(i)
        else:
            for dir in exclude:
                if dir in file_dirs:
                    tex_files.pop(i)

    # Check each file for errors
    num_errors = 0
    num_fixable = 0
    for tex_file in tex_files:
        checker = Checker(tex_file, rules)
        fixable, unfixable = checker.check(fix)
        num_errors += fixable + unfixable
        num_fixable += fixable
        checker.print_errors()

    # Print summary
    print(f"texsquisite: {len(tex_files)} files scanned.")
    if num_errors:
        print(
            f"{num_errors} error(s) found, {num_fixable} of which are fixable with '--fix'."
        )
        if fix:
            print(f"{num_fixable} error(s) were fixed!")
    else:
        print("All checks passed!")
    print()
    return num_errors
