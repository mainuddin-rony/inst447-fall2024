OK_FORMAT = True

test = {   'name': 'q1',
    'points': None,
    'suites': [   {   'cases': [   {   'code': ">>> assert type(yearofdate('12/12/2012')) == int, 'For input 12/12/2012, the function should return an integer, but found ' + "
                                               "str(type(yearofdate('12/12/2012')))\n",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> assert yearofdate('12/12/2012') == 2012, 'For input 12/12/2012, the function should return 2012, but found ' + str(yearofdate('12/12/2012'))\n",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> assert yearofdate('03/03/2024') == 2024, 'For input 03/03/2024, the function should return 2024, but found ' + str(yearofdate('03/03/2024'))\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
