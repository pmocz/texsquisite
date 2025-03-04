# Parsing utility functions


def strip_comment(line):
    # remove comment from line (anything after %, but not \%)
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


def remove_all_spaces_before(pattern, line):
    while " " + pattern in line:
        line = line.replace(" " + pattern, pattern)
    while "~" + pattern in line:
        line = line.replace("~" + pattern, pattern)
    return line


def prepend(prepend_str, pattern, line):
    return line.replace(pattern, prepend_str + pattern)
