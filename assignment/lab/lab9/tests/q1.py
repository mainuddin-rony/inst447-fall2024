from otter.test_files import test_case

OK_FORMAT = False

name = "q1"
points = None

@test_case(points=None, hidden=False)
def test1_dogrevisions(dogrevisions):
    import pandas as pd
    from pandas.testing import assert_frame_equal
    revisions = [
    '1183754588',
    '1183750837',
    '1183617457',
    '1183413301',
    '1182612592',
    '1182593497',
    '1181852947',
    '1180839131',
    '1179700159',
    '1179559162'
]
    q1STUDENT_ANSWER = dogrevisions(revisions)
    q1CORRECT_ANSWER = pd.read_csv('solutionq1.csv', keep_default_na=False)
    try:
        assert_frame_equal(q1STUDENT_ANSWER, q1CORRECT_ANSWER)
    except AssertionError:
        idx = q1STUDENT_ANSWER != q1CORRECT_ANSWER
        correct = q1CORRECT_ANSWER[idx].dropna().to_string()
        incorrect = q1STUDENT_ANSWER[idx].dropna().to_string()
        raise AssertionError(f"Returned dataframe doesn't match. Mismatches are: \n ===== Correct ===== \n {correct} \n\n ===== Incorrect ===== \n {incorrect}")
    
