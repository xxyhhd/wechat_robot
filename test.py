import re

if re.match(r'翻译：', '翻译：who are you: i am your father'):
    print(True)
else:
    print(False)

# a = '翻译：who are 翻译：you: i am 翻译： your father'
# a = a.lstrip('翻译：')
# print(a)