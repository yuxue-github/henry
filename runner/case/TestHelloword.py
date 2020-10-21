import os
import sys
import re
sys.path.append("../../../")
from test_case import TestCase

class TestHelloword(TestCase):
    def set_up(self):
        print "TestHelloword set up"

    def test(self):
        print "Hello world"
        return True

    def tear_down(self):
        print "TestHelloword tear down"