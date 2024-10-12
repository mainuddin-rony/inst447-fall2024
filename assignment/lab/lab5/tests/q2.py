from otter.test_files import test_case

OK_FORMAT = False

name = "q2"
points = None

@test_case(points=None, hidden=False)
def test1_teams_by_continent(teams_by_continent):
    import pandas as pd
    import json
    from pandas.testing import assert_frame_equal
    from io import StringIO
    
    q2CORRECT_ANSWER = """continent,num_teams
Africa,5
Asia,2
Central America,2
Europe,14
Middle East,2
North America,1
Pacific,1
South America,5"""
    q2CORRECT_ANSWER = pd.read_csv(StringIO(q2CORRECT_ANSWER), index_col=0)
    q2STUDENT_ANSWER = teams_by_continent('worldcup.teams.json')
    
    assert type(q2STUDENT_ANSWER) is pd.DataFrame, f"Error: expected DataFrame, got {type(q2STUDENT_ANSWER)} instead."
    
    try:
        assert_frame_equal(q2STUDENT_ANSWER, q2CORRECT_ANSWER)
    except AssertionError:
        idx = q2STUDENT_ANSWER != q2CORRECT_ANSWER
        correct = q2CORRECT_ANSWER[idx].dropna().to_string()
        incorrect = q2STUDENT_ANSWER[idx].dropna().to_string()
        raise AssertionError(f"Returned dataframe doesn't match. Mismatches are: \n ===== Correct ===== \n {correct} \n\n ===== Incorrect ===== \n {incorrect}")

