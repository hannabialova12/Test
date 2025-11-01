from random import choice, shuffle
import string

letters_upper = string.ascii_uppercase
letters_lower = string.ascii_lowercase
digits = string.digits
symbols = '!@#$%&*'

def password(length,isdigit,issymb,isupper):
    char = letters_lower
    psw = [choice(letters_lower)]

    if isdigit.lower()=='yes':
        char += digits
        psw.append(choice(digits))
    if issymb.lower()=='yes':
        char += symbols
        psw.append(choice(symbols))
    if isupper.lower()=='yes':
        char += letters_upper
        psw.append(choice(letters_upper))
    while len(psw)<length:
        psw.append(choice(char))
    shuffle(psw)
    return psw


def check(p,isdigit,issymb,isupper):
    flag = True
    if isdigit.lower()=='yes':
        flag = any(map(lambda x: x.isdigit(),p))
        if flag == False:
            return False
    if issymb.lower()=='yes':
        flag = any(map(lambda x: x in symbols,p))
        if flag == False:
            return False
    if isupper.lower()=='yes':
        flag = any(map(lambda x: x.isupper(),p))
        if flag == False:
            return False
    return flag




print('Hi! I want to help you with your password! I can generate unic password for you. Do you want that i do it for you?')
answ = (input('Enter your answer: '))
while answ.lower() == 'yes':
    length = int((input('How many symbols should your password have? ')))
    isdigit = (input('Do you want that your password contain numbers?'))
    issymb = (input('Do you want that your password contain simbols?'))
    isupper = (input('Do you want that your password contain uppercase letters?'))
    min_length = 1+(isdigit.lower()=='yes')+(issymb.lower()=='yes')+(isupper.lower()=='yes')
    if min_length>length:
        print('Please enter another length or other parametrs')
        answ = 'yes'
        continue
    psw = password(length,isdigit,issymb,isupper)

    while check(psw,isdigit,issymb,isupper) != True:
        psw = password(length,isdigit,issymb,isupper)

    print(''.join(psw))
    answ = input('Do you need one more password?')

print('See you!')

