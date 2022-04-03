# задание 1

a = list(input("chislo: "))

chet = 0
nechet = 0
sum = 0

for i in range(0, len(a)):
    if i % 2 == 0:
        chet += 1
    else:
        nechet +=1
print(chet, nechet)
if chet > nechet:
    for i in range(0, len(a)):
        sum += 1
    print("s:", sum)
else:
    print(a[0] * a[2] * a[5])

# задание 2

word = input("Word: ")
vowel = 0
consonant = 0
vowels = 'aeiouy'

for i in word:
    if i.isalpha():
        if i.lower() in vowels:
            vowel += 1
        else:
            consonant += 1
print(vowel)
print(consonant)
i = 0
if vowel == consonant:
    while i != len(word):
        if word[i].lower() in vowels:
            print(word[i], end=' ')
        i += 1

# задание 3
import random
num1 = int(input("Число1: "))
num2 = int(input("Число2: "))
cor1 = num1 + num2
sum1 = 0

for i in range(7):
    num3 = random.randint(1, 20)
    num4 = random.randint(1, 20)
    print(num3, num4)
    if cor1 > (num3 + num4):
        sum1 += 1
print("Количество: ", sum1)


# задание 4
import random
a = int(input("Количество чисел: "))
num1 = int(input("Искомая цифра: "))
count = 0
for i in range(a):
    b = random.randint(1, 100)
    print(b)
    while b > 0:
        if b % 10 == num1:
            count += 1
        b = b // 10
print(count)


# задание 5

a = input("Введите строку: ")
element = list(a)
for i in element:
    if i.isdigit():
        print(i, end=" ")


# задание 6

string1 = "HHjjSkkiSS"
para_upper = 0
para_lower = 0
for i in range(1, len(string1)):
    print(string1[i - 1], string1[i])
    if string1[i - 1].isupper() and string1[i].isupper():
        para_upper += 1
    if string1[i - 1].islower() and string1[i].islower():
        para_lower += 1
print(para_upper)
print(para_lower)

