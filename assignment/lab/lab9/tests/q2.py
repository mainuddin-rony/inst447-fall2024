from otter.test_files import test_case

OK_FORMAT = False

name = "q2"
points = None

@test_case(points=None, hidden=False)
def test1_viewsofpage(viewsofpage):
    import pandas as pd
    from pandas.testing import assert_frame_equal
    dtype_dict = {'timestamp': object}
    article_name = 'Dog'
    q2STUDENT_ANSWER = viewsofpage(article_name)
    q2CORRECT_ANSWER = pd.read_csv('solutionq2.csv', dtype=dtype_dict)
    try:
        assert_frame_equal(q2STUDENT_ANSWER, q2CORRECT_ANSWER)
    except AssertionError:
        idx = q2STUDENT_ANSWER != q2CORRECT_ANSWER
        correct = q2CORRECT_ANSWER[idx].dropna().to_string()
        incorrect = q2STUDENT_ANSWER[idx].dropna().to_string()
        raise AssertionError(f"Returned dataframe doesn't match. Mismatches are: \n ===== Correct ===== \n {correct} \n\n ===== Incorrect ===== \n {incorrect}")

