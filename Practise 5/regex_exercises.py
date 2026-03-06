import re

# 1
pattern = r'ab*'

text = ["a", "ab", "abb", "ac"]

for t in text:
    if re.fullmatch(pattern, t):
        print(t, "match")

# 2
pattern = r'ab{2,3}'

words = ["abb", "abbb", "abbbb"]

for w in words:
    if re.fullmatch(pattern, w):
        print(w)

# 3
text = "hello_world test_value myVariable"

result = re.findall(r'[a-z]+_[a-z]+', text)

print(result)

# 4
text = "Hello world MyName Test"

result = re.findall(r'[A-Z][a-z]+', text)

print(result)

# 5
pattern = r'a.*b'

text = ["ab", "acb", "axxxb", "a123b"]

for t in text:
    if re.fullmatch(pattern, t):
        print(t)

# 6
text = "Hello, world. Python regex"

result = re.sub(r'[ ,.]', ':', text)

print(result)

# 7 snake → camel
def snake_to_camel(text):
    return re.sub(r'_([a-z])', lambda x: x.group(1).upper(), text)

print(snake_to_camel("hello_world_python"))

# 8 split uppercase
import re

text = "HelloWorldTest"

result = re.split(r'(?=[A-Z])', text)

print(result)

# 9 insert spaces
text = "HelloWorldPython"

result = re.sub(r'(?<!^)([A-Z])', r' \1', text)

print(result)

# 10 camel → snake
ptext = "HelloWorldPython"

result = re.sub(r'(?<!^)([A-Z])', r'_\1', text).lower()

print(result)