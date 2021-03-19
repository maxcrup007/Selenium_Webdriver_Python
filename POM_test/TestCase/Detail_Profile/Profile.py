import os
import unittest
from POM_test.TestCase.Detail_Profile.TC_001 import *
from POM_test.TestCase.Detail_Profile.TC_002 import *
from POM_test.TestCase.Detail_Profile.TC_003 import *
from POM_test.TestCase.Detail_Profile.TC_004 import *
from POM_test.TestCase.Detail_Profile.TC_005 import *
from POM_test.TestCase.Detail_Profile.TC_006 import *
from POM_test.TestCase.Detail_Profile.TC_007 import *
from POM_test.TestCase.Detail_Profile.TC_008 import *

#     ทดสอบการเข้าใช้งานของ "ปัจจัย"

def Totally_test_Factors():

    test_case_to_run = [TestProfile_1, TestProfile_2, TestProfile_3, TestProfile_4,
                        TestProfile_5, TestProfile_6, TestProfile_7, TestProfile_8, ]

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