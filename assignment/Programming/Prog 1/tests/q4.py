from otter.test_files import test_case

OK_FORMAT = False

name = "q4"
points = None

@test_case(points=None, hidden=False)
def test1_clean_ward(clean_ward):
    import pandas as pd
    from pandas.api.types import is_numeric_dtype
    from numpy.testing import assert_array_equal

    if clean_ward is None:
        raise AssertionError("No student function found for this problem.")
    
    q4df = pd.read_csv('311_City_Service_Requests_in_2014.csv')
    q4df = clean_ward(q4df)
    
    # 1) Test that the WARD column has the correct dtype
    assert is_numeric_dtype(q4df['WARD'].dtype), "Error: the WARD column is not a numeric dtype."
    
    q4CORRECT_ANS = pd.read_csv('autograder4.csv')['WARD']
    q4STUDENT_ANS = q4df['WARD']
    assert_array_equal(q4STUDENT_ANS, q4CORRECT_ANS, "Error: the value of the WARD column is not correct.", verbose=False)



