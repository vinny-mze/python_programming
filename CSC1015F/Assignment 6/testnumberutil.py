"""
>>> import numberutil

>>> numberutil.aswords(0)
'zero'

>>> numberutil.aswords(18)
'eighteen'

>>> numberutil.aswords(30)
'thirty'

>>> numberutil.aswords(45)
'forty five'

>>> numberutil.aswords(200)
'two hundred'

>>> numberutil.aswords(208)
'two hundred and eight'

>>> numberutil.aswords(330)
'three hundred and thirty'

>>> numberutil.aswords(455)
'four hundred and fifty five'

"""
import doctest
doctest.testmod(verbose=True)


# 1. hundreds=0 and remainder=0
# 2. hundreds=0 and remainder>0 and remainder<21
# 3. hundreds=0 and remainder>0 and remainder>=21 and units=0
# 4. hundreds=0 and remainder>0 and remainder>=21 and units>0
# 5. hundreds>0 and remainder=0
# 6. hundreds>0 and remainder>0 and remainder<21
# 7. hundreds>0 and remainder>0 and remainder>=21 and units=0
# 8. hundreds>0 and remainder>0 and remainder>=21 and units>0