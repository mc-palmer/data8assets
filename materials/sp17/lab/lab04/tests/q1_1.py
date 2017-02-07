test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Make sure you are examining the values in the column, not the column itself
          >>> import numpy
          >>> total_pay_type != numpy.ndarray
          True

          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> total_pay_type == str
          True

          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Make sure to call the type function a value in the column
          >>> total_pay_type != int
          True

          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}