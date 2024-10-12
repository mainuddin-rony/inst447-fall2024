from otter.test_files import test_case

OK_FORMAT = False

name = "q3"
points = None

@test_case(points=None, hidden=False)
def test1_tied_matches(tied_matches):
    import pandas as pd
    from pandas.testing import assert_frame_equal
    from io import StringIO
    
    q4CORRECT_ANSWER = """,team1.name,team2.name
2,Portugal,Spain
6,Argentina,Iceland
8,Brazil,Switzerland
21,Denmark,Australia
31,Japan,Senegal
34,Iran,Portugal
35,Spain,Morocco
36,Denmark,France
41,Switzerland,Costa Rica
50,Spain,Russia
51,Croatia,Denmark
55,Colombia,England
58,Russia,Croatia
61,Croatia,England"""
    q4CORRECT_ANSWER = pd.read_csv(StringIO(q4CORRECT_ANSWER), index_col=0)
    q4STUDENT_ANSWER = tied_matches('worldcup2018.sqlite')
    assert type(q4STUDENT_ANSWER) is pd.DataFrame, f"Error: expected DataFrame, got {type(q4STUDENT_ANSWER)} instead."
    
    try:
        assert_frame_equal(q4STUDENT_ANSWER, q4CORRECT_ANSWER)
    except AssertionError:
        idx = q4STUDENT_ANSWER != q4CORRECT_ANSWER
        correct = q4CORRECT_ANSWER[idx].dropna().to_string()
        incorrect = q4STUDENT_ANSWER[idx].dropna().to_string()
        raise AssertionError(f"Returned dataframe doesn't match. Mismatches are: \n ===== Correct ===== \n {correct} \n\n ===== Incorrect ===== \n {incorrect}")

