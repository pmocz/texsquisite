from texsquisite import run
import io
import sys


def test_texsquisite():

    # Create a StringIO object
    buffer = io.StringIO()

    # Redirect stdout to the buffer
    original_stdout = sys.stdout
    sys.stdout = buffer

    # Run texsquite
    run(argv=["texsquisite.py", "check"])
    captured_output = buffer.getvalue()

    with open("tests/output.txt", "r") as file:
        expected_output = file.read()

    assert captured_output == expected_output
