from otter.test_files import test_case

OK_FORMAT = False

name = "q10"
points = None

@test_case(points=None, hidden=False)
def test1_most_common_reqs(most_common_reqs):
    import pandas as pd
    
    if most_common_reqs is None:
        raise AssertionError("No student function found for this problem.")
        
    q10CORRECT_ANS = {'Parking Meter Repair': 92571,
 'Bulk Collection': 43097,
 'Parking Enforcement': 26714,
 'CONTAINER REMOVAL': 24634,
 'Pothole': 11348}
    q10df = pd.read_csv('autograder10.csv')
    print(q10df.columns)
    q10STUDENT_ANS = most_common_reqs(q10df) 
    
    assert q10STUDENT_ANS == q10CORRECT_ANS, f"Error: wrong answer! Expecting: {q10CORRECT_ANS}. Your answer: {q10STUDENT_ANS}."

