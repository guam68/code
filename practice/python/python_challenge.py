import sys
import string
import re
import requests
import urllib

# Scripts for solving puzzles on pythonchallenge.com

def rot2():
    message = sys.argv[1]
    alpha = string.ascii_lowercase
    decrypted = ''

    for char in message:
        if char not in alpha:
            decrypted += char
            continue

        i = alpha.index(char)
        
        if i + 2 > 25:
            decrypted += alpha[i + 2 - 26]
        else:
            decrypted += alpha[i + 2]

    print(decrypted)


def rare_char(text):
    # file_name = sys.argv[1]
    chars = {}

    # with open(file_name, encoding='utf-8') as file:
    #     text = file.read()

    for char in text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    print(chars)


def find_letter():
    file_name = sys.argv[1]

    with open(file_name, encoding='utf-8') as file:
        text = file.read()

    alpha = string.ascii_lowercase + string.ascii_uppercase

    txt = ''
    for char in text:
        if char in alpha:
            txt += char
    
    text = txt
    test = ''
    test2 = ''

    for i in range(3, len(text) - 3):
        
        pre = ''.join(text[i-3:i])
        post = ''.join(text[i+1:i+4])

        if pre.isupper() and post.isupper():
            if text[i].islower() and text[i-4].islower() and text[i+4].islower():
                print(text[i-4] + ' ' + pre + text[i] + post + ' ' + text[i+5])
                test += text[i]
                test2 += pre + text[i] + post

    print(rare_char(test))
    print(test)
    print(test2)
    

def linked_list():
    # url = sys.argv[1]
    next_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
    url = next_url + str(93781)
    regex = r'\d+'

    for i in range(1000):
        response = requests.get(url).text
        num = re.search(regex, response)
        print(response)
        url = next_url + num[0]


def pkill():
    file_name = sys.argv[1]
    regex = r'lp\d+'
    with open(file_name, encoding='utf-8') as file:
        text = file.read()

    alpha = string.ascii_lowercase + string.ascii_uppercase + '()!@#$%^&*.' + '0123456789'

    txt = ''
    for char in text:
        if char in alpha:
            txt += char

    text = re.findall(regex, txt)
    regex = r'lp'
    text = re.sub(regex, '', ''.join(text))
    # text = ''.join(text)
    print(text)


pkill()