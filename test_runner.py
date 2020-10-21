import os
import sys

class TestRunner(object):
    def __init__(self):
        print "do some init"
        self.case_list = []

    def run(self):
        for case in self.case_list:
            case.run()