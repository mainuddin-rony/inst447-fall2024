from otter.test_files import test_case

OK_FORMAT = False

name = "q6"
points = None

@test_case(points=None, hidden=False)
def test1_ward_stats(ward_stats):
    import pandas as pd
    
    if ward_stats is None:
        raise AssertionError("No student function found for this problem.")
        
    q6CORRECT_ANS = {'avg_reqs': 40371.75, 'ward_most': 2.0, 'ward_least': 8.0}
    q6df = pd.read_csv('autograder4.csv')
    q6STUDENT_ANS = ward_stats(q6df) 
    
    assert q6STUDENT_ANS == q6CORRECT_ANS, f"Error: wrong answer! Expecting: {q6CORRECT_ANS}. Your answer: {q6STUDENT_ANS}."

