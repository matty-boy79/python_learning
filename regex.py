"""
https://www.w3schools.com/python/python_regex.asp
"""

import re

txt = "The rain in Spain"
x = re.search("Sp[a-z]in", txt)
if x:
    print("Yes")
else:
    print("No")

print(x.start())
print(x.end())
