#!/usr/bin/env python
# coding: utf-8

# In[10]:


import sys
text = ''
key = ''
stop = False


# In[19]:


def textwork():
    global text
    global key
    print('Please, enter the number of abstracts of the text:')
    abstract = int(input())
    for i in range(abstract):
        print('Please, enter the {} abstract of the text:'.format(i+1))
        text += input()
    print('Please, enter the number of abstracts of the key text:')
    abstract = int(input())
    for i in range(abstract):
        print('Please, enter the {} abstract of the key text:'.format(i+1))
        key += input()


# In[20]:


def filework():
    global text
    global key
    print('Please, enter the name of the txt file from the program folder:')
    filename = input()
    if filename.count('.txt') == 0:
        filename=filename+'.txt'
    print('Please, enter the number of abstracts of the text:')
    abstract = int(input())
    with open(filename) as f:
        for i in range(abstract):
            text += f.readline()
        key = f.read()


# In[21]:


def check():
    global key
    if key == 'a' or key == 'A':
        check = True
    if len(key)<len(text):
        add = len(text)-len(key*(len(text)//len(key)))
        key=key*(len(text)//len(key))+key[:add]
    key=key.lower()


# In[22]:


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ''
    check()
    if stop:
        return plaintext
    for i in range(len(plaintext)):
        if ord(plaintext[i])>=65 and ord(plaintext[i])<=90:
            over = bool((ord(plaintext[i])+(ord(key[i])-97))//91)
            ciphertext+=chr(ord(plaintext[i])+(ord(key[i])-97)-(90-65+1)*int(over))
        elif ord(plaintext[i])>=97 and ord(plaintext[i])<=122:
            over = bool((ord(plaintext[i])+(ord(key[i])-97))//123)
            ciphertext+=chr(ord(plaintext[i])+(ord(key[i])-97)-(122-97+1)*int(over))
        else:
            ciphertext+=plaintext[i]
    return ciphertext


# In[23]:


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ''
    check()
    if stop:
        return ciphertext
    for i in range(len(ciphertext)):
        if ord(ciphertext[i])>=65 and ord(ciphertext[i])<=90:
            over = not bool((ord(ciphertext[i])-(ord(key[i])-97))//65)
            plaintext+=chr(ord(ciphertext[i])-(ord(key[i])-97)+(90-65+1)*int(over))
        elif ord(ciphertext[i])>=97 and ord(ciphertext[i])<=122:
            over = not bool((ord(ciphertext[i])-(ord(key[i])-97))//97)
            plaintext+=chr(ord(ciphertext[i])-(ord(key[i])-97)+(122-97+1)*int(over))
        else:
            plaintext+=ciphertext[i]
    return plaintext


# In[24]:


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


# In[25]:


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
        output(encrypt_vigenere(text,key))
        choice = True
    elif ans=='et':
        textwork()
        output(encrypt_vigenere(text,key))
        choice = True
    elif ans=='df':
        filework()
        output(decrypt_vigenere(text,key))
        choice = True
    elif ans=='dt':
        textwork()
        output(decrypt_vigenere(text,key))
        choice = True
    else:
        print('Please, try again.')


# In[ ]:




