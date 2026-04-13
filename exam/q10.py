a = "2.0"
b = float(a)
print(b, type(b))
# Output: 2.0 <class 'float'>

a = "this is a string"
b = float(a)
"""
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[5], line 2
      1 a = "1.2345"
----> 2 b = int(a)
      3 print(b, type(b))

ValueError: invalid literal for int() with base 10: '1.2345'
"""
b = float(a)
print(b, type(b))
"""
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[5], line 2
      1 a = "1.2345"
----> 2 b = int(a)
      3 print(b, type(b))

ValueError: invalid literal for int() with base 10: '1.2345'
"""
b = float(a)
print(b, type(b))
# Output: 1.2345 <class 'float'>
