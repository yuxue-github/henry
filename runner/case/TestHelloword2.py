import os
import sys
import re
sys.path.append("../../../")
from test_case import TestCase

class TestHelloword2(TestCase):
    def set_up(self):
        print "TestHelloword2 set up"

    def test(self):
        print "Hello world2"
        return True

    def tear_down(self):
        print "TestHelloword2 tear down"