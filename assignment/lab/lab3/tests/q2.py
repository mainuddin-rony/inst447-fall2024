from otter.test_files import test_case

OK_FORMAT = False

name = "q2"
points = None

@test_case(points=None, hidden=False)
def test1_standardizebymon(standardizebymon):
    from numpy.testing import assert_array_equal

    import pandas as pd
    q2df = pd.read_csv('WeatherTrips.csv')

    q2STUDENT_ANS = standardizebymon(q2df)
    q2CORRECT_ANS = pd.read_csv('autograder2.csv')

    assert_array_equal(q2STUDENT_ANS, q2CORRECT_ANS, "Error: the transformed data frame is not correct.", verbose=False)
    
