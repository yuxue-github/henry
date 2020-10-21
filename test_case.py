import os
import sys

class TestCase(object):
    def __init__(self):
        print "do some init"
        self.run_bare = 1

    def set_up(self):
        print "setup start"

    def run_bare(self, run_bare):
        print "run bare start"
        self.run_bare = run_bare

    def test(self):
        print "test start"

    def tear_down(self):
        print "tear down start"

    def run(self):
        print "run start"
        for i in range(self.run_bare):
            self.set_up()
            result = self.test()
            self.tear_down()
            if result:
                break
