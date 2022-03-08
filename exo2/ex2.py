import re

p = re.compile('(.* = .*\n)*')
test = p.findall("main : {"
    "test = 42"
    "test2 = test"
    "test3 = 42.42"
"}")

x = re.sub(test)

for i in x:
    print(i, end='')
