import re
import numpy as np

text = "Сегодня Вера красивая. Веру ты просто огонь. Вера как ты можешь быть такой"
if re.search("Вера", text):
    print('о даа')
else:
    print("блин")
x = re.split('\.', text)
y = ['bogdan'] * 3

# print(x)
# print(y)
# print(x + y)


z = re.findall('а', text)
print(z)
b = re.findall('[авВ]', text)
print(b)

с = re.findall("ера|еру", text)
print(с)

d = re.findall("[^Вера]", text)
print(d)

grades = 'ААрам АААвроамм Армин ААААекс'
print(re.findall("А{2,10}",grades))
print(re.findall("А{1,1}А{1,1}",grades))
