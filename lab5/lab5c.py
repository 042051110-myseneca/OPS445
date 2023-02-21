#!/usr/bin/env python3
# Author ID: nnimalan

def add(number1, number2):
    try:
        return(int(number1)+int(number2))
    except:
        return('error: could not add numbers')
# Add two numbers together, return the result, if error return string 'error: could not add numbers'

def read_file(filename):
    try:
         f = open(filename, 'r')
         files = f.readlines()
         f.close()
         return(files)
    except FileNotFoundError:
         return('error: could not read file')
# Read a file, return a list of all lines, if error return string 'error: could not read file'        

if __name__ == '__main__':
    print(add(10,5))                        # works
    print(add('10',5))                      # works
    print(add('abc',5))                     # exception
    print(read_file('seneca2.txt'))         # works
    print(read_file('file10000.txt'))       # exception
    print(read_file('file10000.txt'))       # exception