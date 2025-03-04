from texsquisite import run
import io
import sys


def test_texsquisite_check():
    # Create a StringIO object
    buffer = io.StringIO()

    # Redirect stdout to the buffer
    # original_stdout = sys.stdout
    sys.stdout = buffer

    # Run texsquisite check
    run(argv=["texsquisite.py", "check"])
    captured_output = buffer.getvalue()

    with open("tests/output.txt", "r") as file:
        expected_output = file.read()

    assert captured_output == expected_output


def test_texsquisite_check_fix():
    # Run texsquisite check --fix
    run(argv=["texsquisite.py", "check", "--fix"])

    with open("tests/file1.tex", "r") as file:
        output = file.read()

    with open("tests/file1_fixed.tex", "r") as file:
        expected_output = file.read()

    assert output == expected_output
