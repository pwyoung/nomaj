#!/usr/bin/env python3

# TODO: replace this with a proper PyTest 

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from lib.shellcmd import run_command

debug = True

class TestIt:
    def __init__(self):
        foo = 'bar'

    def test_long_running_success(self):
        cmd = "for i in $(seq 1 3); do echo $i; sleep 0.2; done"
        print("Test Success: long running: {}".format(
            run_command(cmd)))

    def test_streaming_quickly(self):
        cmd = "timeout 0.5 find /"
        print("Test Success: stream quickly: {}".format(
            run_command(cmd)))

    def test_success(self):
        cmd = "ls -ld /tmp"
        print("Test Success quick: {}".format(
            run_command(cmd)))

    def test_failure(self):
        cmd = "/bin/false"
        print("Test Failure quick: {}".format(
            run_command(cmd)))

    def test_long_running_failure(self):
        cmd = "timeout 0.5 find / &>/dev/null && /bin/false"
        print("Test Success: long running: {}".format(
            run_command(cmd)))


def main(argv):
    app = TestIt()
    app.test_long_running_success()
    # Works. Too verbose to run all the time
    # app.test_streaming_quickly()
    app.test_success()
    app.test_failure()
    app.test_long_running_failure()


if __name__ == "__main__":
    main(sys.argv[1:])

