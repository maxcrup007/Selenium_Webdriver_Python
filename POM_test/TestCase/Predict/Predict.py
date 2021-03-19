import os
import unittest
from POM_test.TestCase.Predict.TC_001 import *
from POM_test.TestCase.Predict.TC_002 import *
from POM_test.TestCase.Predict.TC_003 import *
from POM_test.TestCase.Predict.TC_004 import *
from POM_test.TestCase.Predict.TC_005 import *
from POM_test.TestCase.Predict.TC_006 import *
from POM_test.TestCase.Predict.TC_007 import *
from POM_test.TestCase.Predict.TC_008 import *
from POM_test.TestCase.Predict.TC_009 import *
from POM_test.TestCase.Predict.TC_010 import *

def Totally_test_Predict():

    test_case_to_run = [TestPredict_1, TestPredict_2, TestPredict_3, TestPredict_4, TestPredict_5,
                        TestPredict_6, TestPredict_7, TestPredict_8, TestPredict_9, TestPredict_10]

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
    Totally_test_Predict()