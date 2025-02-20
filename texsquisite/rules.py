from .utils import strip_comments


class Rule:
    def __init__(self):
        self.name = None
        self.id = None
        self.description = None
        self.fixable = False

    def print(self):
        print(f"[{self.id}] {self.name}" + ["", " (fixable)"][self.fixable])
        print("    " + self.description + "\n")

    def matches(self, line):
        raise NotImplementedError

    def fix(self, line):
        raise NotImplementedError


class Rules:
    def __init__(self):
        self.rules = {}

    def add(self, rule):
        self.rules[rule.id] = rule

    def __iter__(self):
        return iter(self.rules.values())

    def __contains__(self, item):
        return item in self.rules

    def __getitem__(self, item):
        return self.rules[item]


class LatexRules(Rules):
    def __init__(self):
        super().__init__()
        self.add(TrailingWhitespace())
        self.add(Quotation())
        self.add(MissingTilde())
        self.add(ExtraWhitespace())
        self.add(DoubleSpace())
        self.add(MathPunctuation())


class TrailingWhitespace(Rule):
    def __init__(self):
        super().__init__()
        self.name = "Trailing Whitespace"
        self.id = "S001"
        self.description = r"line should not end with trailing whitespace"
        self.fixable = True

    def matches(self, line):
        return line.endswith(" \n") or line.endswith("\t\n")

    def fix(self, line):
        return line.rstrip() + "\n"


class Quotation(Rule):
    def __init__(self):
        super().__init__()
        self.name = "Quotation"
        self.id = "S002"
        self.description = r"quotation should look like `this' or ``this''"
        self.fixable = True

    def matches(self, line):
        # TODO:
        pass

    def fix(self, line):
        # TODO:
        return line


class MissingTilde(Rule):
    def __init__(self):
        super().__init__()
        self.name = "Missing Tilde"
        self.id = "S003"
        self.description = r"\ref should have ~ before it"
        self.fixable = True

    def matches(self, line):
        # TODO:
        pass

    def fix(self, line):
        # TODO:
        return line


class ExtraWhitespace(Rule):
    def __init__(self):
        super().__init__()
        self.name = "Extra Whitespace"
        self.id = "S004"
        self.description = r"\footnote should not have space before it"
        self.fixable = True

    def matches(self, line):
        # if line contains \footnote, check if there is a space before it
        return r" \footnote" in strip_comments(line)

    def fix(self, line):
        # TODO:
        return line


class DoubleSpace(Rule):
    def __init__(self):
        super().__init__()
        self.name = "Double Whitespace"
        self.id = "S005"
        self.description = r"~ should not have space before/after"
        self.fixable = True

    def matches(self, line):
        # TODO:
        pass

    def fix(self, line):
        # TODO:
        return line


class MathPunctuation(Rule):
    def __init__(self):
        super().__init__()
        self.name = "Math Punctuation"
        self.id = "S006"
        self.description = (
            r"punctuations {.,} should be inside \[math.\] and outside $math$."
        )
        self.fixable = True

    def matches(self, line):
        # TODO:
        pass

    def fix(self, line):
        # TODO:
        return line
