'''
Created on Sep 15, 2013

@author: ezulkosk
'''
from common import Z3Instance, Options




def run():
    '''
    Runs the Z3-translator on each pair (file, numInstances) in tests, 
    and ensures that the number of generated models equals numInstances.
    '''
    if Options.TEST_SET == Options.MY_TESTS:
        tests = Options.my_tests
    elif Options.TEST_SET == Options.POSITIVE_TESTS:
        tests = Options.positive_tests
    
    count = 0
    for t in tests:
        count = count+1
        (file, expected_model_count) = t
        module = file.getModule()
        print("Attempting: " + str(file))
        z3 = Z3Instance.Z3Instance(module)
        actual_model_count = z3.run()
        
        if(expected_model_count == actual_model_count):
            print("PASSED: " + str(file))
        else:
            print("FAILED: " + str(file) + " " + str(expected_model_count) + " " + str(actual_model_count))