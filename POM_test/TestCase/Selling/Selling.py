import os
import unittest
from POM_test.TestCase.Selling.TC_001 import *
from POM_test.TestCase.Selling.TC_002 import *
from POM_test.TestCase.Selling.TC_003 import *
from POM_test.TestCase.Selling.TC_004 import *
from POM_test.TestCase.Selling.TC_005 import *
from POM_test.TestCase.Selling.TC_006 import *
from POM_test.TestCase.Selling.TC_007 import *
from POM_test.TestCase.Selling.TC_008 import *
from POM_test.TestCase.Selling.TC_009 import *
from POM_test.TestCase.Selling.TC_010 import *
from POM_test.TestCase.Selling.TC_011 import *
from POM_test.TestCase.Selling.TC_012 import *
from POM_test.TestCase.Selling.TC_013 import *
from POM_test.TestCase.Selling.TC_014 import *
from POM_test.TestCase.Selling.TC_015 import *
from POM_test.TestCase.Selling.TC_016 import *
from POM_test.TestCase.Selling.TC_017 import *
from POM_test.TestCase.Selling.TC_018 import *
from POM_test.TestCase.Selling.TC_019 import *
from POM_test.TestCase.Selling.TC_020 import *


def Totally_test_Selling():

    test_case_to_run = [TestSelling_1, TestSelling_2, TestSelling_3, TestSelling_4, TestSelling_5,
                        TestSelling_6, TestSelling_7, TestSelling_8, TestSelling_9, TestSelling_10,
                        TestSelling_11, TestSelling_12, TestSelling_13, TestSelling_14, TestSelling_15,
                        TestSelling_16, TestSelling_17, TestSelling_18, TestSelling_19, TestSelling_20]

    loader = unittest.TestLoader()

    suites_list = []
    for test_case in test_case_to_run:
        suite = loader.loadTestsFromTestCase(test_case)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)

    runner = unittest.TextTestRunner()
    results = runner.run(big_suite)

    # ...


if __name__ == '__main__':
    Totally_test_Selling()