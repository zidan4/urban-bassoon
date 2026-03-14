import re

#finding all python errors
for i in dir(__builtins__):
  if re.match(r'^[A-Z]', i):
    print i
