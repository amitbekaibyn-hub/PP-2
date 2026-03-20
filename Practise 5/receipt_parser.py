import re
import json

with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

products = re.findall(r'\d+\.\n(.+)', text)

prices = re.findall(r'\d+\s\d{3},\d{2}|\d+,\d{2}', text)

date = re.search(r'\d{2}\.\d{2}\.\d{4}', text)

time = re.search(r'\d{2}:\d{2}:\d{2}', text)

payment = re.search(r'Банковская карта', text)

print("Products:")
for p in products:
    print("-", p)

print("\nPrices:", prices)

print("\nDate:", date.group() if date else None)
print("Time:", time.group() if time else None)

if payment:
    print("Payment: Bank Card")


a='cat dog catdog'

product=re.findall(r'cat|dog')