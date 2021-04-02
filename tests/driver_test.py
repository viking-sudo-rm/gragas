from unittest import TestCase
from gragas.driver import Driver
import argparse


class TestExperiment(TestCase):

    def test_make_driver(self):
        Experiment = Driver.new("Experiment", flag="exp")
        assert isinstance(Experiment, type)
        assert hasattr(Experiment, "flag_str")
        assert Experiment.flag_str == "exp"
    
    def test_run(self):
        self.ran = False

        @Driver.register()
        def main(args):
            self.ran = True
        
        args = argparse.Namespace(driver="main")
        Driver.run(args)
        assert self.ran == True

    def test_run_subclass(self):
        self.ran_sub = False
        SubDriver = Driver.new("SubDriver")

        @SubDriver.register()
        def main(args):
            self.ran_sub = True
        
        args = argparse.Namespace(driver="main")
        SubDriver.run(args)
        assert self.ran_sub == True
