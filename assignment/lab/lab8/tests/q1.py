from otter.test_files import test_case

OK_FORMAT = False

name = "q1"
points = None

@test_case(points=None, hidden=False)
def test1_gettextbytag(gettextbytag):
    assert gettextbytag("q1file.html", "h1") == ["This is a Heading"], "For the file 'q1file.html1', and the tag 'h1', the fuction should return ['This is a Heading'], but found " + str(gettextbytag("q1file.html", "h1"))
    assert gettextbytag("q1file.html", "p") == ['This is first paragraph.', 'This is second paragraph.', 'This is third paragraph.'], "For the file 'q1file.html', and the tag 'p', the fuction should return ['This is first paragraph.', 'This is second paragraph.', 'This is third paragraph.'], but found " + str(gettextbytag("q1file.html", "p"))
    assert gettextbytag("q1file.html", "a") == [], "For the file 'q1file.html1', and the tag 'a', the fuction should return an empty list, but found " + str(gettextbytag("q1file.html", "a"))

