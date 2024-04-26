 
# test_my_code.py
 
# I only want the import!!! Not to run the code
# done! (we are careful on my_code.py 
# to make a distinction between imports and calls)
from my_code import factorial_iterative, factorial_recursive
 
# tests with pytest
# happens BEFORE a test (for all tests)
def setup_function(p_some_test_function):
    # will be called BEFORE any and all test functions
    msg = f"Will now call the test function "+\
    f"{p_some_test_function.__name__}"
    print(msg)
# def setup_function
 
# happens AFTER a test (for all tests)
def teardown_function(p_some_test_function):
    # will be called AFTER any test
    msg = f"I just ended calling test function "+\
    f"{p_some_test_function.__name__}"
    print(msg)
 
# def teardown_function
 
# this testing file provides a single test
# tests are functions whose name begins with "test"
TEST_THIS = 33
def test_our_only_test():
    fr = factorial_iterative(TEST_THIS)
    fi = factorial_recursive(TEST_THIS)
 
    # our test is checking if the recursive factorial
    # matches the iterative factorial
    try:
        assert(fr==fi)
        print("Tests passed")
        return True
    except Exception as e:
        print("Test failed")
        return False
    # try-except
# def test_our_only_test
 
REAL_VALUE_FOR_2 = 2
def test_second_test():
    # 2! = 2*1 = 2
    try:
        assert(
            factorial_iterative(2)==REAL_VALUE_FOR_2 
            and
            factorial_recurive(2)==REAL_VALUE_FOR_2
        )
 
        print("Test passed")
        return True
    except Exception as e:
        print("Test NOT passed")
        return False
    # try-except
# def test_second_test