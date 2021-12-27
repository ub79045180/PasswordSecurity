# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 11:58:02 2021

@author: Bundu1628235
"""

import requests
import hashlib
import sys
import random
import string

#Define API function
def request_api_data (query_char):
	url = 'https://api.pwnedpasswords.com/range/' + query_char
	res = requests.get(url)
	if res.status_code != 200:
		raise RuntimeError(f'Error fetching: {res.status_code}, check the API and try again')
	return res

#Define password leakage count function
def get_password_leaks_count (hashes, hash_to_check):
	hashes = (line.split(':') for line in hashes.text.splitlines())
	for h, count in hashes:
		if h == hash_to_check:
			return count
	return 0
		 	
#Define password hashing function	
def pwned_api_check (password):
	# check password if its exists in API response
	sha1password =hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
	first5_char, tail = sha1password[:5], sha1password[5:]
	response = request_api_data(first5_char)
	return get_password_leaks_count(response, tail)

#Define main function
def main(args):
    for password in args:
        count = pwned_api_check(password)
        message_1 = f'Your password "{password}" has been hacked {count} times...Consider changing your password'
        message_2 = f'Your password "{password}" has NOT been hacked. Continue using it!'
        if count:
            return message_1
        else:
            return message_2
    return 'Please enter your password'
#................. Password Generator ..................
uppercases = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
             'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lowercases = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
             'n','o','p','q','r','s','t','u','v','w','x','y','z']

adjectives6 = ['sleepy', 'slowly', 'smelly','orange', 'yellow','purple','fluffy']
adjectives5 = ['wetty', 'fatty', 'reddy', 'green', 'bluey', 'white', 'proud', 'brave']
adjectives4 = ['rich', 'grey', '', 'last', 'same', 'next', 'high', 'long']
adjectives3 = ['est', 'coy', 'sad', 'mad', 'shy', 'fun', 'mid', 'apt']
adjectives2 = ['im', 'pi', 'os', 'gr', 'am', 'cd', 'gv', 'pr']

nouns6 = ['toaste', 'dragon', 'hammer', 'chance', 'answer','source','status','league']
nouns5 = ['apple', 'panda', 'price', 'staff', 'river', 'chair', 'style', 'press']
nouns4 = ['ball', 'goat', 'duck', 'film', 'lady', 'task', 'turn', 'pass','loss']
nouns3 = ['cat', 'bag', 'map', 'pub', 'tea', 'aid', 'dog', 'bed','gun','lad']
nouns2 = ['we', 'xi', 'sd', 'cr', 'au', 'ko', 'lu', 'zx','zm','yt']

special_char = random.choice(string.punctuation)
special_char_1 = random.choice(string.punctuation)
special_chars = string.punctuation
number_1 = random.randrange(0, 9)
number_2 = random.randrange(10, 99)
number_3 = random.randrange(100, 999)

lowercase = random.choice(lowercases)
uppercase = random.choice(uppercases)
lowercase1 = random.choice(lowercases)
uppercase1 = random.choice(uppercases)

adjective6 = random.choice(adjectives6)
adjective5 = random.choice(adjectives5)
adjective4 = random.choice(adjectives4)
adjective3 = random.choice(adjectives3)
adjective2 = random.choice(adjectives2)

noun6 = random.choice(nouns6)
noun5 = random.choice(nouns5)
noun4 = random.choice(nouns4)
noun3 = random.choice(nouns3)
noun2 = random.choice(nouns2)

letters_12 = adjective6.capitalize() + special_char_1 + noun6
letters_10 = adjective5.capitalize() + special_char_1 + noun5
letters_8 = adjective4.capitalize() + special_char_1 + noun4
letters_6 = adjective3.capitalize() + special_char_1 + noun3
letters_4 = adjective2.capitalize() + special_char_1 + noun2

_letters_12 = adjective6.capitalize() + noun6
_letters_10 = adjective5.capitalize() + noun5
_letters_8 = adjective4.capitalize() + noun4
_letters_6 = adjective3.capitalize() + noun3
_letters_4 = adjective2.capitalize() + noun2

fn = str(100000000000000)
sn = str(999999999999999)

# Password with numbers and special characters
def numSchar(l):   
    for i in range(1,16):
        if l < 5 or l > 15:
            return 'Password must be at least 5 characters and at most 15 characters long'
        elif i == l:
            result = random.randrange(int(fn[:l-2]), int(sn[:l-2]))
            password = str(result)[:3] + special_char + str(result)[3:] + special_char_1
            return password  
# Password with special Characters only function 
def sChar(l):
    for i in range(1,16):
        if l < 5 or l > 15:
            return 'Password must be at least 5 characters and at most 15 characters long'
        elif i == l:
            password = random.choices(special_chars, k=l)
            result = ''.join([str(s) for s in password])
            return result
# Password with letters only function
def letters(l):
    for i in range(1,16):
        if l < 5 or l > 15:
            return 'Password must be at least 5 characters and at most 15 characters long'
        elif i == l:
            password = random.choices(lowercases, k=l)
            result = ''.join([str(s) for s in password])
            return result.capitalize()
# Password with numbers only function
def numbers(l):
    for i in range(1,16):
        if l < 5 or l > 15:
            return 'Password must be at least 5 characters and at most 15 characters long'
        elif i == l:
            password = random.randrange(int(fn[:l]), int(sn[:l]))
            return password
# Password with numbers, letters and special characters function
def generateAll(l): 
    if l < 5 or l > 15:
        return 'Password must be at least 5 characters and at most 15 characters long'
    elif l == 15:
        password = letters_12 + str(number_1) + special_char
        return password
    elif l == 14:
        password = letters_10 + str(number_2) + special_char
        return password
    elif l == 13:
        password = letters_8 + str(number_3) + special_char
        return password
    elif l == 12:
        password = letters_8 + str(number_2) + special_char
        return password
    elif l == 11:
       password = letters_6 + str(number_3) + special_char
       return password
    elif l == 10:
        password = letters_6 + str(number_2) + special_char
        return password
    elif l == 9:
        password = letters_4 + str(number_3) + special_char
        return password
    elif l == 8:
        password = letters_4 + str(number_2) + special_char
        return password
    elif l == 7:
        password = letters_4 + str(number_1) + special_char
        return password
    elif l == 6:
        password = letters_4 + str(number_1) 
        return password
    elif l == 5:
        password = adjective2.capitalize() + special_char_1 + lowercase + str(number_1) 
        return password
# Password with numbers and letters function
def numLetters(l):  
    if l < 5 or l > 15:
        return 'Password must be at least 5 characters and at most 15 characters long'
    elif l == 15:
        password = _letters_12 + str(number_3) 
        return password
    elif l == 14:
        password = _letters_12 + str(number_2) 
        return password
    elif l == 13:
        password = _letters_10 + str(number_3) 
        return password
    elif l == 12:
        password = _letters_10 + str(number_2) 
        return password
    elif l == 11:
       password = _letters_8 + str(number_3) 
       return password
    elif l == 10:
        password = _letters_8 + str(number_2) 
        return password
    elif l == 9:
        password = _letters_6 + str(number_3) 
        return password
    elif l == 8:
        password = _letters_6 + str(number_2) 
        return password
    elif l == 7:
        password = _letters_4 + str(number_3)
        return password
    elif l == 6:
        password = _letters_4 + str(number_2) 
        return password
    elif l == 5:
        password = uppercase + lowercase1 + lowercase + str(number_2) 
        return password
  
# Password with letters and Special characters
def letterSchar(l):   
    if l < 5 or l > 15:
        return 'Password must be at least 5 characters and at most 15 characters long'
    elif l == 15:
        password = _letters_12 + special_char_1 + lowercase + special_char
        return password
    elif l == 14:
        password = _letters_12 + special_char_1 + special_char
        return password
    elif l == 13:
        password = _letters_10 + special_char_1 + lowercase + special_char
        return password
    elif l == 12:
        password = _letters_10 + special_char_1 + special_char
        return password
    elif l == 11:
       password = _letters_8 + special_char_1 + lowercase + special_char
       return password
    elif l == 10:
        password = _letters_8 + special_char_1 + special_char
        return password
    elif l == 9:
        password = _letters_6 + special_char_1 + lowercase + special_char
        return password
    elif l == 8:
        password = _letters_6 + special_char_1 + special_char
        return password
    elif l == 7:
        password = _letters_4 + special_char_1 + lowercase + special_char
        return password
    elif l == 6:
        password = _letters_4 + special_char_1 + special_char 
        return password
    elif l == 5:
        password = adjective2.capitalize() + special_char_1 + lowercase + special_char 
        return password


if __name__ == '__main__':
    #args = input().split()
    #print(main(args))
    sys.exit(main(sys.argv[1:]))