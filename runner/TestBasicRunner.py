import os
import sys
import re
from case.TestHelloword import TestHelloword
from case.TestHelloword2 import TestHelloword2
sys.path.append("../../")
from test_runner import TestRunner

class TestBasicRunner(TestRunner):
    def __init__(self):
        self.case_list = []
        case = TestHelloword()
        self.case_list.append(case)
        case = TestHelloword2()
        self.case_list.append(case)
