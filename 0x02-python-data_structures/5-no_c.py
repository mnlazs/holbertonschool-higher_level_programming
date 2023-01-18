#!/usr/bin/python3
#def no_c(my_string):
#"""Function that removes all c and C characters from a string"""   
#    new_string = ""
#    for i in range(len(my_string)):
#        if my_string[i] != 'c' and my_string[i] != 'C':
#            new_string += my_string[i]
#    return new_string
#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for c in my_string:
        if c not in "Cc":
            new_string += c
    return new_string
