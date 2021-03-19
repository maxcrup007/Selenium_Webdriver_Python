import os
import unittest

from POM_test.TestCase.Detail_crops.TC_001 import *
from POM_test.TestCase.Detail_crops.TC_002 import *
from POM_test.TestCase.Detail_crops.TC_003 import *
from POM_test.TestCase.Detail_crops.TC_004 import *
from POM_test.TestCase.Detail_crops.TC_005 import *
from POM_test.TestCase.Detail_crops.TC_006 import *
from POM_test.TestCase.Detail_crops.TC_007 import *
from POM_test.TestCase.Detail_crops.TC_008 import *


def Totally_test_Detail_crops():

    test_case_to_run = [TestGarden_1, TestGarden_2, TestGarden_3, TestGarden_4,
                        TestGarden_5, TestGarden_6, TestGarden_7, TestGarden_8]

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
    Totally_test_Detail_crops()
