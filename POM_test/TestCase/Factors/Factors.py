import os
import unittest
from POM_test.TestCase.Factors.TC_001 import *
from POM_test.TestCase.Factors.TC_002 import *
from POM_test.TestCase.Factors.TC_003 import *
from POM_test.TestCase.Factors.TC_004 import *
from POM_test.TestCase.Factors.TC_005 import *
from POM_test.TestCase.Factors.TC_006 import *
from POM_test.TestCase.Factors.TC_007 import *
from POM_test.TestCase.Factors.TC_008 import *
from POM_test.TestCase.Factors.TC_009 import *
from POM_test.TestCase.Factors.TC_010 import *
from POM_test.TestCase.Factors.TC_011 import *
from POM_test.TestCase.Factors.TC_012 import *
from POM_test.TestCase.Factors.TC_013 import *
from POM_test.TestCase.Factors.TC_014 import *
from POM_test.TestCase.Factors.TC_015 import *
from POM_test.TestCase.Factors.TC_016 import *
from POM_test.TestCase.Factors.TC_017 import *

#     ทดสอบการเข้าใช้งานของ "ปัจจัย"


def Totally_test_Factors():

    test_case_to_run = [TestFactor_1, TestFactor_2, TestFactor_3, TestFactor_4, TestFactor_5,
                        TestFactor_6, TestFactor_7, TestFactor_8, TestFactor_9, TestFactor_10,
                        TestFactor_11, TestFactor_12, TestFactor_13, TestFactor_14, TestFactor_15,
                        TestFactor_16, TestFactor_17]

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
    Totally_test_Factors()