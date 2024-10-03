from otter.test_files import test_case

OK_FORMAT = False

name = "q3"
points = None

@test_case(points=None, hidden=False)
def test1_avg_orders_by_dow(avg_orders_by_dow):
    import pandas as pd
    from pandas.testing import assert_frame_equal
    from io import StringIO
    q3CORRECT_ANSWER = """order_dow,avg_orders
0,11.15
1,10.39
2,9.47
3,9.21
4,9.58
5,9.66
6,11.25"""
    q3CORRECT_ANSWER = pd.read_csv(StringIO(q3CORRECT_ANSWER), index_col=0)
    q3STUDENT_ANSWER = avg_orders_by_dow()
    
    assert type(q3STUDENT_ANSWER) is pd.DataFrame, f"Error: expected DataFrame, got {type(q3STUDENT_ANSWER)} instead."
    try:
        assert_frame_equal(q3STUDENT_ANSWER, q3CORRECT_ANSWER)
    except AssertionError:
        idx = q3STUDENT_ANSWER != q3CORRECT_ANSWER
        correct = q3CORRECT_ANSWER[idx].dropna().to_string()
        incorrect = q3STUDENT_ANSWER[idx].dropna().to_string()
        raise AssertionError(f"Returned dataframe doesn't match. Mismatches are: \n ===== Correct ===== \n {correct} \n\n ===== Incorrect ===== \n {incorrect}")

