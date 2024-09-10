from otter.test_files import test_case

OK_FORMAT = False

name = "q5"
points = None

@test_case(points=None, hidden=False)
def test1_missing_ward(missing_ward):
    import pandas as pd
    
    if missing_ward is None:
        raise AssertionError("No student function found for this problem.")
        
    q5CORRECT_ANS = 4
    q5df = pd.read_csv('311_City_Service_Requests_in_2014.csv')
    q5STUDENT_ANS = missing_ward(q5df) 
    
    assert q5STUDENT_ANS == q5CORRECT_ANS, f"Error: wrong answer! Expecting: {q5CORRECT_ANS}. Your answer: {q5STUDENT_ANS}."

