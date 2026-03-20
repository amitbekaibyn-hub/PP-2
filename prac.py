import re 
a='abbabbbb  abbbbbb ab as ad addd'

product=re.findall(r"\ba|b\b",a)
print(product)