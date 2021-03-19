import os
import unittest
from POM_test.TestCase.Detail_Garden.TC_001 import *
from POM_test.TestCase.Detail_Garden.TC_002 import *
from POM_test.TestCase.Detail_Garden.TC_003 import *
from POM_test.TestCase.Detail_Garden.TC_004 import *
from POM_test.TestCase.Detail_Garden.TC_005 import *
from POM_test.TestCase.Detail_Garden.TC_006 import *
from POM_test.TestCase.Detail_Garden.TC_007 import *
from POM_test.TestCase.Detail_Garden.TC_008 import *
from POM_test.TestCase.Detail_Garden.TC_009 import *
from POM_test.TestCase.Detail_Garden.TC_010 import *
from POM_test.TestCase.Detail_Garden.TC_011 import *
from POM_test.TestCase.Detail_Garden.TC_012 import *
from POM_test.TestCase.Detail_Garden.TC_013 import *
from POM_test.TestCase.Detail_Garden.TC_014 import *
from POM_test.TestCase.Detail_Garden.TC_015 import *
from POM_test.TestCase.Detail_Garden.TC_016 import *
from POM_test.TestCase.Detail_Garden.TC_017 import *
from POM_test.TestCase.Detail_Garden.TC_018 import *
from POM_test.TestCase.Detail_Garden.TC_019 import *
from POM_test.TestCase.Detail_Garden.TC_020 import *
from POM_test.TestCase.Detail_Garden.TC_021 import *
from POM_test.TestCase.Detail_Garden.TC_022 import *
from POM_test.TestCase.Detail_Garden.TC_023 import *
from POM_test.TestCase.Detail_Garden.TC_024 import *
from POM_test.TestCase.Detail_Garden.TC_025 import *
from POM_test.TestCase.Detail_Garden.TC_026 import *
from POM_test.TestCase.Detail_Garden.TC_027 import *
from POM_test.TestCase.Detail_Garden.TC_028 import *
from POM_test.TestCase.Detail_Garden.TC_029 import *
from POM_test.TestCase.Detail_Garden.TC_030 import *
from POM_test.TestCase.Detail_Garden.TC_031 import *
from POM_test.TestCase.Detail_Garden.TC_032 import *
from POM_test.TestCase.Detail_Garden.TC_033 import *
from POM_test.TestCase.Detail_Garden.TC_034 import *
from POM_test.TestCase.Detail_Garden.TC_035 import *

#         ทดสอบการเข้าเพิ่มข้อมูลของ "แปลง"

def Totally_test_Gardens():

    test_case_to_run = [TestGarden_1, TestGarden_2, TestGarden_3, TestGarden_4, TestGarden_5,
                        TestGarden_6, TestGarden_7, TestGarden_8, TestGarden_9, TestGarden_10,
                        TestGarden_11, TestGarden_12, TestGarden_13, TestGarden_14, TestGarden_15,
                        TestGarden_16, TestGarden_17, TestGarden_18, TestGarden_19, TestGarden_20,
                        TestGarden_21, TestGarden_22, TestGarden_23, TestGarden_24, TestGarden_25,
                        TestGarden_26, TestGarden_27, TestGarden_28, TestGarden_29, TestGarden_30,
                        TestGarden_31, TestGarden_32, TestGarden_33, TestGarden_34, TestGarden_35]

    loader = unittest.TestLoader()

    suites_list = []
    for test_case in test_case_to_run:
        suite = loader.loadTestsFromTestCase(test_case)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)

    runner = unittest.TextTestRunner()
    results = runner.run(big_suite)


if __name__ == '__main__':
    Totally_test_Gardens()