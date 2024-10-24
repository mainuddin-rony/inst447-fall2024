OK_FORMAT = True

test = {   'name': 'q2',
    'points': None,
    'suites': [   {   'cases': [   {   'code': ">>> assert type(monthofdate('March 8, 2017')) == int, 'For input March 8, 2017, the function should return an integer, but found ' + "
                                               "str(type(monthofdate('March 8, 2017')))\n",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> assert monthofdate('March 8, 2017') == 3, 'For input March 8, 2017, the function should return 3, but found ' + str(monthofdate('March 8, "
                                               "2017'))\n",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> assert monthofdate('May 3, 2019') == 5, 'For input May 3, 2019, the function should return 5, but found ' + str(monthofdate('May 3, 2019'))\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
