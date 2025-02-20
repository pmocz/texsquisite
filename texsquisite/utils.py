# Parsing utility functions


def strip_comments(line):
    # remove comments from line (anything after %, but not \%)
    result = []
    in_comment = False
    escape = False
    for char in line:
        if char == "%" and not escape:
            in_comment = True
        if char == "\\" and not escape:
            escape = True
        else:
            escape = False
        if not in_comment:
            result.append(char)
        else:
            break
    return "".join(result)
