#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys

abc = {}
abcsorted = {}
charnum = 0
lines = 0


# In[2]:


def filework():
    global charnum
    global lines
    print('Please, enter the name of the txt file from the program folder:')
    filename = input()
    if filename.count('.txt') == 0:
        filename=filename+'.txt'
    with open(filename) as f:
        lines = f.read().count('?')
        f.seek(0)
        lines += f.read().count('!')
        f.seek(0)
        lines += f.read().count('.')-2*f.read().count('...')
        if lines == 0:
            print('File is empty.')
            sys.exit()
        for key in range(32,127):
            f.seek(0)
            abc[key]=f.read().count(chr(key))
            charnum+=abc[key]


# In[3]:


def textwork():
    global charnum
    global lines
    text = ''
    print('Please, enter the number of abstracts:')
    abstract = int(input())
    for i in range(abstract):
        print('Please, enter the {} abstract of the text:'.format(i+1))
        text += input()
        print('\n')
    lines = text.count('?')
    lines += text.count('!')
    lines += text.count('.')-2*text.count('...')
    if lines == 0:
        print('File is empty.')
        sys.exit()
    for key in range(32,127):
        abc[key]=text.count(chr(key))
        charnum+=abc[key]


# In[4]:


def longoutput():
    print('Total: {} symbol(s)'.format(charnum))
    abcsorted = dict(sorted(abc.items(),key = lambda i: i[1], reverse=True))
    for key in abcsorted.keys():
        print("Symbol '{}' arose {} time(s), in average {} time(s) in a sentence".format(chr(key),abc[key], abc[key]//lines))


# In[5]:


def shortoutput():
    print('Total: {} symbol(s)'.format(charnum))
    abcsorted = dict(sorted(abc.items(),key = lambda i: i[1], reverse=True))
    for key in abcsorted.keys():
        if abc[key] != 0:
            print("Symbol '{}' arose {} time(s), in average {} time(s) in a sentence".format(chr(key),abc[key], abc[key]//lines))


# In[6]:


choice = False

print('Do you want to open a file or work with a text? f/t')
while not choice:
    answer = input()
    if answer == 'file' or answer == 'File' or answer == 'file.' or answer == 'File.' or answer == 'f':
        choice = True
        filework()
    elif answer == 'text' or answer == 'Text' or answer == 'text.' or answer == 'Text.' or answer == 't':
        choice = True
        textwork()
    else:
        print('Please, choose again')
    
choice = False

print('Do you want a short or long output? s/l')
while not choice:
    answer = input()
    if answer == 'short' or answer == 'Short' or answer == 'short.' or answer == 'Short.' or answer == 's':
        choice = True
        shortoutput()
    elif answer == 'long' or answer == 'Long' or answer == 'long.' or answer == 'Long.' or answer == 'l':
        choice = True
        longoutput()
    else:
        print('Please, choose again')


# In[ ]:




