# 1
def card_hide(card):
    return '*' * len(card[:-4]) + card[-4:]

print(card_hide("1234567890123456"))

# 2

def palindrome(data):
    data = data.replace(' ','').lower()
    return 'Палиндром' if data == data[::-1] else 'Не палиндром'
print(palindrome(""))