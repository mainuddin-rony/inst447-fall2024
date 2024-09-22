from otter.test_files import test_case

OK_FORMAT = False

name = "q1"
points = None

@test_case(points=None, hidden=False)
def test1_tripspermonth(tripspermonth):
    
    from numpy.testing import assert_array_equal
    import pandas as pd
    
    q1df = pd.read_csv('WeatherTrips.csv')

    q1STUDENT_ANS = tripspermonth(q1df)
    q1CORRECT_ANS = pd.read_csv('autograder1.csv')

    assert_array_equal(q1STUDENT_ANS, q1CORRECT_ANS, "Error: the aggregated data frame is not correct.", verbose=False)

