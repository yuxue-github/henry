import os
import sys, getopt
import re
from test_case import TestCase

def usage():
    print "usage: python henry.py -r test_runner -c test_case"

if __name__ == '__main__':
    print "start henry..."
    opts, args = getopt.getopt(sys.argv[1:], "hr:c:")
    usage = False
    runner = None
    case = None
    for op, value in opts:
        if op == "-r":
            runner = value
            usage = True
        elif op == "-c":
            case = value
            usage = True
        elif op == "-h":
            usage()
            sys.exit()
    if not usage:
        usage()
        sys.exit()

    if runner:
        if case:
            file_name = 'test.runner.case.' + case
            module = __import__(file_name, fromlist=True)
            test_class = getattr(module, case)
            test_case = test_class()
            test_case.run()
        else:
            file_name = 'test.runner.' + runner
            module = __import__(file_name, fromlist=True)
            runner_class = getattr(module, runner)
            test_runner = runner_class()
            test_runner.run()

