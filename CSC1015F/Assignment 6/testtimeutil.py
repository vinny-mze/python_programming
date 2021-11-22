"""
>>> import timeutil

>>> timeutil.validate("1 1 a.m.")
False

>>> timeutil.validate("111:50 a.m.")
False

>>> timeutil.validate("0:17 p.m.")
False

>>> timeutil.validate("00:63 a.m.")
False

>>> timeutil.validate("12:13 ")
False

>>> timeutil.validate("11:111 p.m.")
False

"""
import doctest
doctest.testmod(verbose=True)
