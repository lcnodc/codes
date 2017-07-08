#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Exercise 13:  Fibonacci
 
Write a program that asks the user how many Fibonnaci numbers to
generate and then generates them. Take this opportunity to think about
how you can use functions. Make sure to ask the user to enter the number
of numbers in the sequence to generate.(Hint: The Fibonnaci sequence
is a sequence of numbers where the next number in the sequence is the
sum of the previous two numbers in the sequence. The sequence looks like
this: 1, 1, 2, 3, 5, 8, 13, …)
"""

def fibonaccis(x: int) ->list:
    l = []

    for i in range(0, x):
        l.append(l[-1] + l[-2]) if i > 1 else l.append(1)
    return l


number = int(input("Enter with a number: "))

print(fibonaccis2(number))
