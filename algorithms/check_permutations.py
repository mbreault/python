## given two strings check if one is a permutation of the other

## method 1 using built-in python list methods

def sorted_chars(s):
    
    ## sort characters in a string
    return sorted(set(s))

def check_permutation(a,b):

    if a == b:
        return True
    elif len(a) != len(b):
        return False
    else:
        return sorted_chars(a) == sorted_chars(b)
    
print(check_permutation('x','y')) ## False
print(check_permutation('xx','y')) ## False
print(check_permutation('radar','radar')) ## True
print(check_permutation('abcdefgh','xyzzy')) ## False
print(check_permutation('sent','nest')) ## True

