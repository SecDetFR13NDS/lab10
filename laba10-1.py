s = open("sentences.txt")
a = len([i for i in s.split('.')])
print("Кількість розповідних речень в тексті ", a)
b = len([i for i in s.split('! ')])
print("Кількість окличних речень в тексті ", b)
с = len([i for i in s.split('? ')])
print("Кількість питальних речень в тексті ", с)
d = len([i for i in s.split(' ')])
print("Кількість слів в тексті ", d)
