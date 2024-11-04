from otter.test_files import test_case

OK_FORMAT = False

name = "q3"
points = None

@test_case(points=None, hidden=False)
def test1_getbookspricebonus(getbookspricebonus):
    import numpy as np
    from numpy.testing import assert_array_equal
    
    q3CORRECT_ANS = np.loadtxt('solutionq3.txt')
    q3STUDENT_ANS = getbookspricebonus()
    
    assert type(q3STUDENT_ANS) is np.ndarray, f"Error: Your solution returned a {type(q3STUDENT_ANS)}, while it should return a numpy Array"
    assert_array_equal(q3STUDENT_ANS, q3CORRECT_ANS)

