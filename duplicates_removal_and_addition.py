# -*- coding: utf-8 -*-
"""duplicates removal and addition.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WZclAfLeOAa3kkTHLPJDHhqhqE9gU8Hn
"""

first_number=int(input("Enter first number: "))
second_number=int(input("Enter second number: "))
third_number=int(input("Enter third number: "))

sum= first_number + second_number + third_number

print("The tota1 sum is ",sum)

if first_number==second_number:
  print("Duplicates removed, the sum is ",third_number)
elif(second_number==third_number):
  print("Duplicates removed, the sum is ",first_number)
elif(third_number==first_number):
  print("Duplicates removed, the sum is ",second_number)
else:
  print("All the inputs are duplicates and the sum is ZERO")