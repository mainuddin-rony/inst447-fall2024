OK_FORMAT = True

test = {   'name': 'q4',
    'points': None,
    'suites': [   {   'cases': [   {   'code': ">>> assert ssnredacter('111-11-1111') == '***-**-1111', 'For input 111-11-1111, the function should return ***-**-1111, but found ' + "
                                               "str(ssnredacter('111-11-1111'))\n",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> assert ssnredacter('999-19-1919') == '***-**-1919', 'For input 999-19-1919, the function should return ***-**-1919, but found ' + "
                                               "str(ssnredacter('999-19-1919'))\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
