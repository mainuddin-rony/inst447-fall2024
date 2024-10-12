from otter.test_files import test_case

OK_FORMAT = False

name = "q1"
points = None

@test_case(points=None, hidden=False)
def test1_find_by_name(find_by_name):
    import json
    players = '[{"name":"Gazinsky","team":"Russia"},{"name":"Dzyuba","team":"Russia"},{"name":"Lukaku","team":"Belgium"}]'
    stadium_data = '{"stadiums":[{"name": "Ekaterinburg Arena","city": "Ekaterinburg"},{"name": "Luzhniki Stadium","city": "Moscow"},{"name": "Nizhny Novgorod Stadium","city": "Nizhny Novgorod"}]}'
    
    q1STUDENT_ANS_1 = find_by_name(players, "Gazinsky")
    q1CORRECT_ANS_1 = "Russia"
    assert q1STUDENT_ANS_1 == q1CORRECT_ANS_1, f"Error: Your solution returned {q1STUDENT_ANS_1!r}. Correct answer: {q1CORRECT_ANS_1!r}"

    q1STUDENT_ANS_2 = find_by_name(stadium_data, "Luzhniki Stadium", key="stadiums")
    q1CORRECT_ANS_2 = "Moscow"
    assert q1STUDENT_ANS_2 == q1CORRECT_ANS_2, f"Error: Your solution returned {q1STUDENT_ANS_2!r}. Correct answer: {q1CORRECT_ANS_2!r}"

    q1STUDENT_ANS_3 = find_by_name(players, "Lukaku")
    q1CORRECT_ANS_3 = "Belgium"
    assert q1STUDENT_ANS_3 == q1CORRECT_ANS_3, f"Error: Your solution returned {q1STUDENT_ANS_3!r}. Correct answer: {q1CORRECT_ANS_3!r}"

    q1STUDENT_ANS_4 = find_by_name(stadium_data, "Ekaterinburg Arena", key="stadiums")
    q1CORRECT_ANS_4 = "Ekaterinburg"
    assert q1STUDENT_ANS_4 == q1CORRECT_ANS_4, f"Error: Your solution returned {q1STUDENT_ANS_4!r}. Correct answer: {q1CORRECT_ANS_4!r}"
    
