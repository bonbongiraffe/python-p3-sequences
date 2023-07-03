#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci = [0,1]
    if length == 0:
        print ([])
    elif length == 1:
        print ([0])
    elif length == 2:
        print ([0,1])
    # why doesn't this work?
    # if (length >= 1) and (length <= 2):
    #     for i in range (length):
    #         print (fibonacci[0:length][i])
    else:
        for i in range (length-2):
            fibonacci.append(fibonacci[i] + fibonacci[i+1])
        print (fibonacci)
