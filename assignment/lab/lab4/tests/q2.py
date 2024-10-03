from otter.test_files import test_case

OK_FORMAT = False

name = "q2"
points = None

@test_case(points=None, hidden=False)
def test1_items_per_order(items_per_order):
    import pandas as pd
    from pandas.testing import assert_frame_equal
    q2CORRECT_ANSWER = pd.read_csv("solutionq2.csv", index_col=0)
    q2STUDENT_ANSWER = items_per_order()
    
    assert type(q2STUDENT_ANSWER) is pd.DataFrame, f"Error: expected DataFrame, got {type(q2STUDENT_ANSWER)} instead."
    try:
        assert_frame_equal(q2STUDENT_ANSWER, q2CORRECT_ANSWER)
    except AssertionError:
        idx = q2STUDENT_ANSWER != q2CORRECT_ANSWER
        correct = q2CORRECT_ANSWER[idx].dropna().to_string()
        incorrect = q2STUDENT_ANSWER[idx].dropna().to_string()
        raise AssertionError(f"Returned dataframe doesn't match. Mismatches are: \n ===== Correct ===== \n {correct} \n\n ===== Incorrect ===== \n {incorrect}")

