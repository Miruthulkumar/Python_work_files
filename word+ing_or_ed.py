# -*- coding: utf-8 -*-
"""word+ing or ed.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1F4D5nLekhdSdytjDmUuZa3be7BvnqjfU
"""

def apple():
  name=str(input("Enter a word: "))
  if len(name)<3:
    print("The string is less than 3 letters")
  else:
    if (name[-3:]=='ing'):
      print(name[:-3] + 'ed')
    else:
      print(name + 'ing')

apple()