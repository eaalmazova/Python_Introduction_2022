#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
text = ''


# In[2]:


def textwork():
    global text
    print('Please, enter the number of abstracts:')
    abstract = int(input())
    for i in range(abstract):
        print('Please, enter the {} abstract of the text:'.format(i+1))
        text += input()


# In[3]:


def filework():
    global text
    print('Please, enter the name of the txt file from the program folder:')
    filename = input()
    if filename.count('.txt') == 0:
        filename=filename+'.txt'
    with open(filename) as f:
        text = f.read()


# In[4]:


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ''
    for char in plaintext:
        if ord(char)>=65 and ord(char)<=90:
            over = bool((ord(char)+shift)//91)
            ciphertext+=chr(ord(char)+shift-(90-65+1)*int(over))
        elif ord(char)>=97 and ord(char)<=122:
            over = bool((ord(char)+shift)//123)
            ciphertext+=chr(ord(char)+shift-(122-97+1)*int(over))
        else:
            ciphertext+=char
    return ciphertext


# In[5]:


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ''
    for char in ciphertext:
        if ord(char)>=65 and ord(char)<=90:
            over = not bool((ord(char)-shift)//65)
            plaintext+=chr(ord(char)-shift+(90-65+1)*int(over))
        elif ord(char)>=97 and ord(char)<=122:
            over = not bool((ord(char)-shift)//97)
            plaintext+=chr(ord(char)-shift+(122-97+1)*int(over))
        else:
            plaintext+=char
    return plaintext


# In[6]:


def output(t):
    out = ''
    while out != 'n' or out != 'y':
        print('Do you want to write the resulting text in a file? y/n')
        out = input()
        if out == 'n':
            outputtext(t)
            return
        elif out == 'y':
            print('Please, input the name of the txt file')
            filename = input()
            if filename.count('.txt') == 0:
                filename=filename+'.txt'
            with open(filename,'w') as f:
                f.write(t)
            return
        else:
            print('Please, try again.')


# In[7]:


def outputtext(t):
    if ans[0]=='e':
        print('Encrypted text:\n{}'.format(t))
    else:
        print('Decrypted text:\n{}'.format(t))


# In[ ]:


choice = False
while not choice:
    ans = ''
    print('Do you want to encrypt or decrypt? e/d')
    ans+=input()
    print('Do you want to open a file or work with a text? f/t')
    ans+=input()
    if ans=='ef':
        filework()
        output(encrypt_caesar(text))
        choice = True
    elif ans=='et':
        textwork()
        output(encrypt_caesar(text))
        choice = True
    elif ans=='df':
        filework()
        output(decrypt_caesar(text))
        choice = True
    elif ans=='dt':
        textwork()
        output(decrypt_caesar(text))
        choice = True
    else:
        print('Please, try again.')


# In[ ]:




