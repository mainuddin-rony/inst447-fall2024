from otter.test_files import test_case

OK_FORMAT = False

name = "q1"
points = None

@test_case(points=None, hidden=False)
def test1_busiest_dow(busiest_dow):
    import pandas as pd
    q1file = 'orders.csv'
    q1CORRECT_ANS = 0
    q1STUDENT_ANS = busiest_dow(q1file)

    assert type(q1STUDENT_ANS) == int, f"Error: Your solution returned a {type(q1STUDENT_ANS)} while it should return an int"
    assert q1STUDENT_ANS == q1CORRECT_ANS, f"Error: Your solution returned {q1STUDENT_ANS}. Correct answer: {q1CORRECT_ANS}"

@test_case(points=None, hidden=False)
def test2_busiest_dow(busiest_dow):
    import pandas as pd
    q2file = 'q1_test.csv'
    q2CORRECT_ANS = 1
    q2STUDENT_ANS = busiest_dow(q2file)

    assert type(q2STUDENT_ANS) == int, f"Error: Your solution returned a {type(q2STUDENT_ANS)} while it should return an int"
    assert q2STUDENT_ANS == q2CORRECT_ANS, f"Error: Your solution returned {q2STUDENT_ANS}. Correct answer: {q2CORRECT_ANS}"

