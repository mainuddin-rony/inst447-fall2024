from otter.test_files import test_case

OK_FORMAT = False

name = "q2"
points = None

@test_case(points=None, hidden=False)
def test1_getbooksprice(getbooksprice):
    assert type(getbooksprice()) is list, "Error: Your solution should return a list, while it found a " + str(type(getbooksprice()))
    assert getbooksprice() == [51.77, 53.74, 50.1, 47.82, 54.23, 22.65, 33.34, 17.93, 22.6, 52.15, 13.99, 20.66, 17.46, 52.29, 35.02, 57.25, 23.88, 37.59, 51.33, 45.17], "Error: Your solution return [51.77, 53.74, 50.1, 47.82, 54.23, 22.65, 33.34, 17.93, 22.6, 52.15, 13.99, 20.66, 17.46, 52.29, 35.02, 57.25, 23.88, 37.59, 51.33, 45.17], but found " + str(getbooksprice())

