import re
str="HELLO PYTHON PROGRAMMING"
print(re.search("LL",str))
print(re.match("PY",str))
#return none if no match found
#only applies from starting
#returns match if match found

import re
str="HELLO"
t=re.search("LL",str)
print(t.string)

t=re.sub("PYTHON","PYTHONNNNN",str)
print(t)

#t=re.search("LL",str)
#print(t.start())
#starting index