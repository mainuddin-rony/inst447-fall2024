OK_FORMAT = True

test = {   'name': 'q3',
    'points': None,
    'suites': [   {   'cases': [   {   'code': ">>> assert emailuppercase('gciampag@umd.edu') == 'gciampag@UMD.EDU', 'For input gciampag@umd.edu, the function should return gciampag@UMD.EDU, but "
                                               "found ' + str(emailuppercase('gciampag@umd.edu'))\n",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> assert emailuppercase('student1@terpmail.umd.edu') == 'student1@TERPMAIL.UMD.EDU', 'For input student1@terpmail.umd.edu, the function should "
                                               "return student1@TERPMAIL.UMD.EDU, but found ' + str(emailuppercase('student1@terpmail.umd.edu'))\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
