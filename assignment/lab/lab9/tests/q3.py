from otter.test_files import test_case

OK_FORMAT = False

name = "q3"
points = None

@test_case(points=None, hidden=False)
def test1_viewsofmanypages(viewsofmanypages):
    from pandas.testing import assert_frame_equal
    import pandas as pd
    article_titles = ['Dog', 'Cat', 'Parrot', 'Rabbit']
    q3STUDENT_ANSWER = viewsofmanypages(article_titles)
    q3CORRECT_ANSWER = pd.read_csv('solutionq3.csv', index_col=0, parse_dates=['timestamp'], date_format='%Y-%m-%d')
    try:
        assert_frame_equal(q3STUDENT_ANSWER, q3CORRECT_ANSWER)
    except AssertionError:
        idx = q3STUDENT_ANSWER != q3CORRECT_ANSWER
        correct = q3CORRECT_ANSWER[idx].dropna().to_string()
        incorrect = q3STUDENT_ANSWER[idx].dropna().to_string()
        raise AssertionError(f"Returned dataframe doesn't match. Mismatches are: \n ===== Correct ===== \n {correct} \n\n ===== Incorrect ===== \n {incorrect}")

