#!/usr/bin/env python3
#Author ID: nnimalan

mylist = [ 100, 200, 300, 'six hundred' ]

def give_list():
    return mylist[0:4]
    print(give_list())
    # Returns all of items in the global object my_list unchanged

def give_first_item():
    return str(mylist[0])
    print(give_first_item())
    # Returns the first item in the global object my_list as a string

def give_first_and_last_item():
    # Does not accept any arguments
    return mylist[::len(mylist)-1]
    print(give_first_and_last_item())
    # Returns a list that includes the first and last items in the global object my_list

def give_second_and_third_item():
    # Does not accept any arguments
    return mylist[1:3]
    print(give_second_and_third_item())
    # Returns a list that includes the second and third items in the global object my_list

if __name__ == '__main__':   # This section also referred to as a "main block"
    print(give_list())
    print(give_first_item())
    print(give_first_and_last_item())
    print(give_second_and_third_item())