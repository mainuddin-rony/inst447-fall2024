from otter.test_files import test_case

OK_FORMAT = False

name = "q7"
points = None

@test_case(points=None, hidden=False)
def test1_sort_servicecode(sort_servicecode):
    import pandas as pd
    
    if sort_servicecode is None:
        raise AssertionError("No student function found for this problem.")
        
    
    q7df = pd.read_csv('311_City_Service_Requests_in_2014.csv')
    q7CORRECT_ANS = sorted(q7df['SERVICECODEDESCRIPTION'].unique())
    q7STUDENT_ANS = sort_servicecode(q7df)

    assert type(q7STUDENT_ANS) == type(q7CORRECT_ANS), "Expecting the return type should be a list"
    
    assert q7STUDENT_ANS == q7CORRECT_ANS, f"Error: wrong answer! Expecting: {q7CORRECT_ANS}. Your answer: {q7STUDENT_ANS}."

