from otter.test_files import test_case

OK_FORMAT = False

name = "q2"
points = None

@test_case(points=None, hidden=False)
def test1_col_dist(col_dist):
    import pandas as pd
    from pandas.testing import assert_series_equal
    
    q1df = pd.read_csv('311_City_Service_Requests_in_2014.csv')
    expected = q1df['WARD'].value_counts()

    if col_dist is None:
        raise AssertionError("No student function found for this problem.")
    answer = col_dist(q1df)
    assert type(answer) == pd.core.series.Series, "The function should return a Pandas Series"
    
    try:
        assert_series_equal(expected, answer)
    except AssertionError as e:
        raise AssertionError(f"Your solution returned:\n{answer}\n\n\nWhile it should have returned:\n{expected}") from e

