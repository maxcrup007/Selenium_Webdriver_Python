import os
import unittest
from POM_test.TestCase.Planting.TC_001 import *
from POM_test.TestCase.Planting.TC_002 import *
from POM_test.TestCase.Planting.TC_003 import *
from POM_test.TestCase.Planting.TC_004 import *
from POM_test.TestCase.Planting.TC_005 import *
from POM_test.TestCase.Planting.TC_006 import *
from POM_test.TestCase.Planting.TC_007 import *
from POM_test.TestCase.Planting.TC_008 import *
from POM_test.TestCase.Planting.TC_009 import *
from POM_test.TestCase.Planting.TC_010 import *
from POM_test.TestCase.Planting.TC_011 import *
from POM_test.TestCase.Planting.TC_012 import *
from POM_test.TestCase.Planting.TC_013 import *
from POM_test.TestCase.Planting.TC_014 import *
from POM_test.TestCase.Planting.TC_015 import *
from POM_test.TestCase.Planting.TC_016 import *
from POM_test.TestCase.Planting.TC_017 import *
from POM_test.TestCase.Planting.TC_018 import *
from POM_test.TestCase.Planting.TC_019 import *
from POM_test.TestCase.Planting.TC_020 import *
from POM_test.TestCase.Planting.TC_021 import *
from POM_test.TestCase.Planting.TC_022 import *
from POM_test.TestCase.Planting.TC_023 import *
from POM_test.TestCase.Planting.TC_024 import *
from POM_test.TestCase.Planting.TC_025 import *
from POM_test.TestCase.Planting.TC_026 import *
from POM_test.TestCase.Planting.TC_027 import *

#     ทดสอบการเข้าใช้งานของ "ปลูก"

def Totally_test_Planting():

    test_case_to_run = [TestPlanting_1, TestPlanting_2, TestPlanting_3, TestPlanting_4, TestPlanting_5, TestPlanting_6, TestPlanting_7,
                        TestPlanting_8, TestPlanting_9, TestPlanting_10, TestPlanting_11, TestPlanting_12, TestPlanting_13, TestPlanting_14,
                        TestPlanting_15,TestPlanting_16, TestPlanting_17, TestPlanting_18, TestPlanting_19, TestPlanting_20, TestPlanting_21,
                        TestPlanting_22, TestPlanting_23, TestPlanting_24, TestPlanting_25, TestPlanting_26, TestPlanting_27]

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
    Totally_test_Planting()



