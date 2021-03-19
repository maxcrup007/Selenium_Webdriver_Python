import os
import unittest
from POM_test.TestCase.Harvest.TC_001 import *
from POM_test.TestCase.Harvest.TC_002 import *
from POM_test.TestCase.Harvest.TC_003 import *
from POM_test.TestCase.Harvest.TC_004 import *
from POM_test.TestCase.Harvest.TC_005 import *
from POM_test.TestCase.Harvest.TC_006 import *
from POM_test.TestCase.Harvest.TC_007 import *
from POM_test.TestCase.Harvest.TC_008 import *
from POM_test.TestCase.Harvest.TC_009 import *
from POM_test.TestCase.Harvest.TC_010 import *
from POM_test.TestCase.Harvest.TC_011 import *
from POM_test.TestCase.Harvest.TC_012 import *
from POM_test.TestCase.Harvest.TC_013 import *
from POM_test.TestCase.Harvest.TC_014 import *
from POM_test.TestCase.Harvest.TC_015 import *
from POM_test.TestCase.Harvest.TC_016 import *
from POM_test.TestCase.Harvest.TC_017 import *
from POM_test.TestCase.Harvest.TC_018 import *

def Totally_test_Harvest():

    test_case_to_run = [TestHarvest_1, TestHarvest_2, TestHarvest_3, TestHarvest_4, TestHarvest_5,
                        TestHarvest_6, TestHarvest_7, TestHarvest_8, TestHarvest_9, TestHarvest_10,
                        TestHarvest_11, TestHarvest_12, TestHarvest_13, TestHarvest_14, TestHarvest_15,
                        TestHarvest_16, TestHarvest_17, TestHarvest_18]

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
    Totally_test_Harvest()