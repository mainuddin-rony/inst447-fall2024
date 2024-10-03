from otter.test_files import test_case

OK_FORMAT = False

name = "q4"
points = None

@test_case(points=None, hidden=False)
def test1_single_item_organic(single_item_organic):
    import pandas as pd
    from pandas.testing import assert_frame_equal
    from io import StringIO
    q4CORRECT_ANSWER = """,aisle_id,num_items,aisle
40,44,1,eye ear care
77,87,1,more household
113,124,1,spirits"""
    q4CORRECT_ANSWER = pd.read_csv(StringIO(q4CORRECT_ANSWER), index_col=0)
    q4STUDENT_ANSWER = single_item_organic()
    
    assert type(q4STUDENT_ANSWER) is pd.DataFrame, f"Error: expected DataFrame, got {type(q4STUDENT_ANSWER)} instead."
    try:
        assert_frame_equal(q4STUDENT_ANSWER, q4CORRECT_ANSWER)
    except AssertionError:
        idx = q4STUDENT_ANSWER != q4CORRECT_ANSWER
        correct = q4CORRECT_ANSWER[idx].dropna().to_string()
        incorrect = q4STUDENT_ANSWER[idx].dropna().to_string()
        raise AssertionError(f"Returned dataframe doesn't match. Mismatches are: \n ===== Correct ===== \n {correct} \n\n ===== Incorrect ===== \n {incorrect}")
        
